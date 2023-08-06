from attr import define, field, validators
from joblib import Parallel, delayed
from nptyping import NDArray
from pathlib import Path
from rescupy import TotalEnergy, Energy
from rescupy.base import Base, Quantity, to_quantity, ureg
import attr
import json
import numpy as np
import os


@define
class Displacement(Base):
    atom_index: int = field(default=0)
    direction_index: int = field(default=0)
    h_direction: NDArray = field(default=np.array([0, 0, 1]))
    h_magnitude: Quantity = field(
        default=0.0001 * ureg.angstrom,
        converter=lambda x: to_quantity(x, "angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    sign: int = field(default=1, converter=int, validator=validators.instance_of(int))
    energy: Energy = field(default=None)
    free_energy: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    workdir: str = field(default="/")

    def generate_input(self, calc):
        self.workdir.mkdir(parents=True, exist_ok=True)
        etot = self.get_calc(calc)
        path = Path(self.workdir) / "nano_scf_in.json"
        etot.system.atoms.write_xyz(Path(self.workdir) / "Atom.xyz")
        etot.write(path)
        return

    def get_calc(self, calc):
        etot = calc.copy()
        pos = etot.system.atoms.positions
        if self.atom_index != -1:
            h = self.h_magnitude
            pos[self.atom_index, :] += h * self.h_direction * self.sign
            etot.system.set_positions(pos)
        return etot

    def get_h_direction(self):
        return self.h_direction / np.linalg.norm(self.h_direction)

    def get_output_paths(self):
        self.workdir.mkdir(parents=True, exist_ok=True)
        output = Path(self.workdir) / "nano_scf_out.json"
        outhdf = Path(self.workdir) / "nano_scf_out.h5"
        return output, outhdf

    def _get_energy(self):
        if isinstance(self.energy, Energy):
            return self.energy
        output, outhdf = self.get_output_paths()
        if output.exists() and outhdf.exists():
            etot = TotalEnergy.read(output)
            self.energy = etot.energy
            return self.energy
        else:
            raise Exception(f"Output file {output.absolute()} not found.")

    def get_free_energy(self):
        output, outhdf = self.get_output_paths()
        if output.exists() and outhdf.exists():
            with open(output, "r") as f:
                d = json.load(f)
            energy = Energy(**d["energy"])
            energy.set_units("si")
            return energy.efree
            # etot = TotalEnergy.read(output)
            # return etot.energy.efree
        else:
            raise Exception(f"Output file {output.absolute()} not found.")

    def solve(self, calc):
        root = os.getcwd()
        output, outhdf = self.get_output_paths()
        if output.exists() and outhdf.exists():
            etot = TotalEnergy.read(output)
        else:
            etot = self.get_calc(calc)
        if etot.solver.mix.converged:
            print(f"Found converged calculation {output.absolute()}")
        else:
            os.chdir(self.workdir)
            etot.solve(output=output)
        os.chdir(root)


@define
class FDForces(Base):
    displacements = field(default=None)
    fd_scheme: str = field(default="forward")
    forces: NDArray = field(default=None)
    h_cartesian: bool = field(default=True)
    h_magnitude: Quantity = field(
        default=0.0001 * ureg.angstrom,
        converter=lambda x: to_quantity(x, "angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    free_energies = field(default=None)
    total_energy_calc: TotalEnergy = field(default=None)
    workdir: str = field(
        default="./", converter=str, validator=validators.instance_of(str)
    )

    def __attrs_post_init__(self):
        natm = self.total_energy_calc.system.get_number_of_atoms()
        if self.h_cartesian:
            directions = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
        else:
            raise Exception(f"Invalid h_cartesian value {self.h_cartesian}")
        workdir = Path(self.workdir).absolute() / f"etot_center"
        self.displacements = [
            Displacement(
                atom_index=-1,
                h_direction=directions[0],
                h_magnitude=0.0 * ureg.angstrom,
                workdir=workdir,
            )
        ]
        if self.fd_scheme == "central":
            signs = [1, -1]
        else:
            signs = [1]
        for sind, s in enumerate(signs):
            for i in range(natm):
                for d in range(3):
                    workdir = (
                        Path(self.workdir).absolute() / f"etot_atm{i}_dir{d}_sgn_{sind}"
                    )
                    self.displacements.append(
                        Displacement(
                            atom_index=i,
                            direction_index=d,
                            h_direction=directions[d],
                            h_magnitude=self.h_magnitude,
                            sign=s,
                            workdir=workdir,
                        )
                    )
        self.forces = np.empty((natm, 3)) * ureg.eV / ureg.angstrom
        self.free_energies = np.empty(len(self.displacements)) * ureg.eV

    def generate_inputs(self):
        for d in self.displacements:
            d.generate_input(self.total_energy_calc)

    def get_forces(self):
        ftots = self.get_free_energies()
        natm = self.total_energy_calc.get_number_of_atoms()
        for j, disp in enumerate(self.displacements):
            i = disp.atom_index
            if i == -1:
                ftot0 = ftots[j]
                break
        ftotf = np.empty((natm, 3))
        ftotb = np.empty((natm, 3))
        hs = np.empty((natm, 3))
        for j, disp in enumerate(self.displacements):
            i = disp.atom_index
            if i == -1:
                continue
            d = disp.direction_index
            hs[i, d] = disp.h_magnitude.to(ureg.angstrom).m
            s = disp.sign
            if s == 1:
                ftotf[i, d] = ftots[j].to(ureg.eV).m
            else:
                ftotb[i, d] = ftots[j].to(ureg.eV).m
        ftotf *= ureg.eV
        ftotb *= ureg.eV
        hs *= ureg.angstrom
        if self.fd_scheme == "central":
            self.forces = -(ftotf - ftotb) / hs / 2
        else:
            self.forces = -(ftotf - ftot0) / hs
        return self.forces

    def _get_forces(self, name="efree"):
        ftots = self._get_energies()
        allowed = [
            "esr",
            "ebg",
            "ebs",
            "edh",
            "exc",
            "evxc",
            "etot",
            "efree",
            "entropy",
        ]
        if name not in allowed:
            raise Exception(f"Invalid force name {name}.")
        ftots = [getattr(f, name) for f in ftots]
        natm = self.total_energy_calc.get_number_of_atoms()
        for j, disp in enumerate(self.displacements):
            i = disp.atom_index
            if i == -1:
                ftot0 = ftots[j]
                break
        ftotf = np.zeros((natm, 3))
        ftotb = np.zeros((natm, 3))
        hs = np.zeros((natm, 3))
        for j, disp in enumerate(self.displacements):
            i = disp.atom_index
            if i == -1:
                continue
            d = disp.direction_index
            hs[i, d] = disp.h_magnitude
            s = disp.sign
            if s == 1:
                ftotf[i, d] = ftots[j]
            else:
                ftotb[i, d] = ftots[j]
        if self.fd_scheme == "central":
            self.forces = -(ftotf - ftotb) / hs / 2
        else:
            self.forces = -(ftotf - ftot0) / hs
        return self.forces

    def _get_energies(self, n_jobs=1):
        self.energies = []
        Parallel(n_jobs=n_jobs)(
            delayed(self.energies.append)(d._get_energy()) for d in self.displacements
        )
        return self.energies

    # def _get_energies(self):
    #     self.energies = []
    #     for i, d in enumerate(self.displacements):
    #         self.energies.append(d._get_energy())

    def get_free_energies(self):
        for i, d in enumerate(self.displacements):
            self.free_energies[i] = d.get_free_energy()
        return self.free_energies

    def solve(self, n_jobs=1):
        Parallel(n_jobs=n_jobs)(
            delayed(d.solve)(self.total_energy_calc) for d in self.displacements
        )
        # for d in self.displacements:
        #     d.solve(self.total_energy_calc)
