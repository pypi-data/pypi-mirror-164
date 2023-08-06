# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from nptyping import NDArray
from pathlib import Path
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.ewald import ewaldEnergy, ewaldPotential
from rescupy.geometry import distmatper, wigner_seiz_radius
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
from shutil import copyfile
from subprocess import Popen
import attr
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy


def to_quantity_dict(x, unit):
    for k, v in x.items():
        x[k] = to_quantity(v, unit)
    return x


@attr.s
class Defect(Base):
    """
    Defect project class.

    Attributes:
        charges : NDArray
            List of charged states
        name : string
            Project name (used to make main directory).
        supercell : NDArray
            Supercell transformation.
        unitsys : TotalEnergy
            TotalEnergy object describing the unit cell.
    """

    unitsys: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )
    bandgap: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    charges: NDArray = attr.ib(
        factory=lambda: np.array([0]),
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    chemicalpotentials: dict = attr.ib(
        factory=dict,
        converter=attr.converters.optional(lambda x: to_quantity_dict(x, "eV")),
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
    )
    corrections: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV", shape=(-1))),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    dielectric: NDArray = attr.ib(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    efermi: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    formationenergies: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV", shape=(-1))),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    name: str = attr.ib(
        default="defect",
        converter=str,
        validator=attr.validators.instance_of(str),
    )
    relax: bool = attr.ib(
        default=True,
        validator=attr.validators.instance_of(bool),
    )
    transitionlevels: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV", shape=(-1))),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    site: int = attr.ib(
        default=0,
        converter=int,
        validator=attr.validators.instance_of(int),
    )
    supercell: NDArray = attr.ib(
        factory=lambda: np.array([1, 1, 1]),
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    dielectric_shape: tuple = attr.ib(default=(3, 3))

    def __attrs_post_init__(self):
        self._reshape()
        self.charges[::-1].sort()
        # self.create_directories()

    def get_formation_energies(self, correct=False):
        if self.formationenergies is not None:
            return self.formationenergies
        if self.relax:
            fname = "relax"
        else:
            fname = "scf"
        cwd = os.getcwd()
        os.chdir(self.get_dir("host"))
        if os.path.exists("nano_scf_out.json"):
            rschost = TotalEnergy.read("nano_scf_out.json")
        else:
            raise Warning("Host calculation results not found.")
        os.chdir(cwd)
        site = self.site
        spec = rschost.system.atoms.get_symbol(site)
        n = -1
        self.formationenergies = []
        for i, c in enumerate(self.charges):
            os.chdir(self.get_dir("defect", charge=c))
            if os.path.exists("nano_" + fname + "_out.json"):
                rscdefc = TotalEnergy.read("nano_" + fname + "_out.json")
                self.formationenergies.append(
                    rscdefc.energy.etot
                    - rschost.energy.etot
                    - n * self.chemicalpotentials[spec]
                    + c * self.efermi
                )
            os.chdir(cwd)
        os.chdir(cwd)
        self.formationenergies = Quantity.from_list(self.formationenergies)
        if correct:
            self.get_formation_correction()
            self.formationenergies += self.corrections
        return self.formationenergies

    def get_formation_correction(self, scheme="KO"):
        if self.dielectric is None:
            raise Exception(
                "The dielectric attribute is None. Cannot electrostatic correction."
            )
        if self.relax:
            fname = "relax"
        else:
            fname = "scf"
        site = self.site
        eps = self.dielectric
        cwd = os.getcwd()
        os.chdir(self.get_dir("host"))
        if os.path.exists("nano_scf_out.json"):
            rschost = TotalEnergy.read("nano_scf_out.json")
            if scheme == "KO":
                velhost = -rschost.get_potential("electrostatic", units="atomic")
            asys = rschost.system
            asys.set_units("atomic")
            avec_b = asys.cell.avec.to("bohr").m
            pos_b = asys.atoms.positions.to("bohr").m
            xyz_b = pos_b[site : site + 1, 0::]
            pts_b = asys.cell.get_grids().to("bohr").m
            # x_b, y_b, z_b = asys.cell.get_grids(shape="grid")
        else:
            raise Warning("Host calculation results not found.")
        os.chdir(cwd)
        self.corrections = [0.0 * ureg.eV for i in range(len(self.charges))]
        for i, c in enumerate(self.charges):
            if c == 0:
                continue
            os.chdir(self.get_dir("defect", charge=c))
            if os.path.exists("nano_" + fname + "_out.json"):
                rscdefc = TotalEnergy.read("nano_" + fname + "_out.json")
                if scheme == "KO":
                    veldefc = -rscdefc.get_potential("electrostatic", units="atomic")
                elat = ewaldEnergy(avec_b, eps, xyz_b, c)
                self.corrections[i] += (-elat * ureg.hartree).to("eV")
                if scheme.lower() == "ewald":
                    continue
                vpc_atm, eta = ewaldPotential(avec_b, eps, xyz_b, c, pos_b)
                vmh, eta = ewaldPotential(avec_b, eps, xyz_b, c, pts_b)
                vmh = np.reshape(vmh, asys.cell.grid, order="F")
                vqb = veldefc - velhost
                vqb_atm = interp_periodic(avec_b, vqb, pos_b)
                vsr_atm = vqb_atm - vpc_atm
                r_atm = distmatper(pos_b, xyz_b, avec_b).flatten()
                rws = wigner_seiz_radius(avec_b)
                C1 = np.mean(vsr_atm[r_atm >= rws * 0.9999])
                vsr1 = vqb - vmh - C1
                Esr1 = c * np.mean(vsr1)
                self.corrections[i] += (Esr1 * ureg.hartree).to("eV")
            os.chdir(cwd)
        os.chdir(cwd)
        self.corrections = Quantity.from_list(self.corrections)

    def get_dir(self, name, charge=None):
        cwd = os.getcwd()
        if name == "host":
            natm = np.product(self.supercell) * self.unitsys.get_number_of_atoms()
            ndir = "natm_" + str(natm)
            tmp = "host"
            return os.path.join(cwd, self.name, ndir, tmp)
        if name == "defect":
            natm = np.product(self.supercell) * self.unitsys.get_number_of_atoms()
            ndir = "natm_" + str(natm)
            if charge == 0:
                tmp = "defect_q0"
            if charge > 0:
                tmp = "defect_qp" + str(abs(charge))
            if charge < 0:
                tmp = "defect_qm" + str(abs(charge))
            return os.path.join(cwd, self.name, ndir, tmp)
        return os.path.join(cwd, self.name, name)

    def get_transition_levels(self, correct=False):
        forme = self.get_formation_energies(correct=correct)
        formem = forme.m
        q = self.charges
        tr = np.zeros((len(q) - 1))
        for i in range(len(q)):
            if i > 0:
                p = [q[i] - q[i - 1], formem[i] - formem[i - 1]]
                tr[i - 1] = np.roots(p)
        self.transitionlevels = tr * forme.u

    def plot_transition_level_diagram(self, filename=None, show=True):
        """Generates a plot of the transition level diagram.

        Args:
            filename (str, optional):
                If not None, then the figure is saved to filename.
            show (bool, optional):
                If True block and show figure.
                If False, do not show figure.

        Returns:
            fig (:obj:`matplotlib.figure.Figure`):
                A figure handle.
        """
        if self.transitionlevels is None:
            raise Exception(
                "transitionlevels is None. get_transition_levels must be called before plot_transition_level_diagram."
            )
        c = self.charges
        eunit = self.transitionlevels.u
        fig, ax = plt.subplots()
        x = np.arange(0.0, 1.0, 0.1)
        xs = np.arange(0.15, 0.85, 0.1)
        y1 = 0.0 * np.ones((x.size))
        y2 = -10.0 * np.ones((x.size))
        ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor="gray", interpolate=True)
        if self.bandgap is not None:
            y1 = (self.bandgap.to(eunit) * np.ones((x.size))).m
            y2 = ((20.0 * ureg.eV).to(eunit) * np.ones((x.size))).m
            ax.fill_between(
                x, y1, y2, where=y2 >= y1, facecolor="gray", interpolate=True
            )
            yub = self.bandgap.to(eunit) + (1.0 * ureg.eV).to(eunit)
        else:
            yub = np.max(self.transitionlevels) + (1.0 * ureg.eV).to(eunit)
        for i, t in enumerate(self.transitionlevels):
            y1 = t.m * np.ones((xs.size))
            label = "%+d/%+d" % (c[i], c[i + 1])
            ax.plot(xs, y1, label=label)
        ax.legend()
        plt.ylim((-1.0 * ureg.eV).to(eunit).m, yub.m)
        plt.ylabel(f"Transition levels ({self.transitionlevels.u})")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def solve(self, force=False):
        cwd = Path(os.getcwd())
        root = cwd / self.name
        natm = np.product(self.supercell) * self.unitsys.get_number_of_atoms()
        ndir = "natm_" + str(natm)
        os.chdir(root / ndir / "host")
        print(os.getcwd())
        if self.relax:
            fname = "relax"
        else:
            fname = "scf"
        if force or not os.path.exists("nano_scf_out.json"):
            # https://stackoverflow.com/questions/58268304/kill-program-run-with-execopenfile-read-in-python
            p = Popen(["python3", "scf.py"])
            p.wait()
        for c in self.charges:
            if c == 0:
                dirname = "defect_q0"
            if c > 0:
                dirname = "defect_qp" + str(abs(c))
            if c < 0:
                dirname = "defect_qm" + str(abs(c))
            os.chdir(root / ndir / dirname)
            print(os.getcwd())
            if force or not os.path.exists("nano_" + fname + "_out.json"):
                p = Popen(["python3", fname + ".py"])
                p.wait()
        os.chdir(cwd)

    def create_directories(self):
        cwd = Path(os.getcwd())
        root = cwd / self.name
        os.makedirs(root, exist_ok=True)
        usyspath = root / "nano_scf_ref.json"
        self.unitsys.write(usyspath)
        natm = np.product(self.supercell) * self.unitsys.get_number_of_atoms()
        dtmp = self.get_dir("natm_" + str(natm))
        os.makedirs(dtmp, exist_ok=True)
        dtmp = self.get_dir("host")
        os.makedirs(dtmp, exist_ok=True)
        self._create_template_supercell_host(dest=dtmp)
        for c in self.charges:
            dtmp = self.get_dir("defect", charge=c)
            os.makedirs(dtmp, exist_ok=True)
            self._create_template_supercell_defect(dest=dtmp, charge=c)
            self._create_template_supercell_defect(dest=dtmp, charge=c, relax=True)

    def _create_template_supercell_host(self, dest="./"):
        content = """import numpy as np
from rescupy import TotalEnergy
calc = TotalEnergy.read("../../nano_scf_ref.json")
calc.supercell(T=np.diag([%d,%d,%d]))
calc.solve()
""" % (
            *self.supercell,
        )
        ifile = os.path.join(dest, "scf.py")
        with open(ifile, mode="w") as f:
            f.write(content)

    def _create_template_supercell_defect(self, dest="./", charge=0, relax=False):
        if relax:
            fname = "relax"
        else:
            fname = "scf"
        content = """import numpy as np
from rescupy import TotalEnergy, Relax
calc = TotalEnergy.read("../../nano_scf_ref.json")
calc.supercell(T=np.diag([%d,%d,%d]))
calc.system.vacate(site=%d)
nval = calc.system.atoms.valence_charge
calc.system.set_occ(bands = [nval/2, nval/2 + 2], occ=%f/6.)
""" % (
            *self.supercell,
            self.site,
            2 - charge,
        )
        if relax:
            content += """rlx = Relax.from_totalenergy(calc, fixatoms = [%d])
rlx.solve(output="nano_%s_out.json")
""" % (
                self.site,
                fname,
            )
        else:
            content += "calc.solve()"
        ifile = os.path.join(dest, fname + ".py")
        with open(ifile, mode="w") as f:
            f.write(content)
        content = """from rescupy import TotalEnergy, BandStructure as BS 
ecalc = TotalEnergy.read("nano_scf_out.json")
calc = BS.from_totalenergy(ecalc)
calc.system.set_kpoint_path(special_points=["X","G","M"], grid=50)
calc.solve()
fig = calc.plot_bs(filename="bs.png")
"""
        ifile = os.path.join(dest, "bs.py")
        with open(ifile, mode="w") as f:
            f.write(content)


def copypseudos(sys, dest):
    for s in sys.system.atoms.species:
        path = s.path
        copyfile(path, os.path.join(dest, os.path.split(path)[-1]))


def interp_periodic(avec, farr, pos):
    """
    Interp a periodic function discretized on a 3D regular grid.

    Args:
        avec (NDArray): Lattice vectors (row-vectors).

        farr (NDArray): Function values.

        pos (NDArray): Target positions (Cartesian)

    Return:
        NDArray: Function interpolated at the positions given by pos.
    """

    ng = farr.shape
    u = np.array(np.arange(-2, ng[0] + 4))
    v = np.array(np.arange(-2, ng[1] + 4))
    w = np.array(np.arange(-2, ng[2] + 4))
    f = farr[np.mod(u - 1, ng[0]), :, :]
    f = f[:, np.mod(v - 1, ng[1]), :]
    f = f[:, :, np.mod(w - 1, ng[2])]
    u = u / ng[0]
    v = v / ng[1]
    w = w / ng[2]
    p = np.linalg.solve(avec.T, pos.T).T
    interp = scipy.interpolate.RegularGridInterpolator((u, v, w), f)
    return interp(p)
