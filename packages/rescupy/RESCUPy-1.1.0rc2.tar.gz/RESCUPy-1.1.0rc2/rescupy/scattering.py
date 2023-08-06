"""
scattering states calculator
"""
from pathlib import Path
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.system import plot_isosurfaces as plot_isosurfaces_system
from rescupy.totalenergy import TotalEnergy
from rescupy.twoprobe import TwoProbe, get_transport_dir
from rescupy.utils import dict_converter, read_field
import attr
import copy
import h5py
import numpy as np
import os


@attr.s
class Scattering(Base):
    """Scattering class.
    Attributes:
        dos: density of states
        transport_axis
        left_equal_right: boolean variable indicating whether the two lead structures are identical.
    """

    center: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )

    left: TotalEnergy = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda d: dict_converter(d, TotalEnergy)),
        validator=attr.validators.optional(attr.validators.instance_of(TotalEnergy)),
    )

    right: TotalEnergy = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda d: dict_converter(d, TotalEnergy)),
        validator=attr.validators.optional(attr.validators.instance_of(TotalEnergy)),
    )
    left_equal_right: bool = attr.ib(default=False)  # are lead structures identical?

    transport_axis: int = attr.ib(
        default=-1, validator=attr.validators.in_([-1, 0, 1, 2])
    )

    energy: Quantity = attr.ib(
        default=np.array([0.0]) * ureg.eV,
        converter=lambda x: to_quantity(x, "eV", shape=(-1)),
        validator=attr.validators.instance_of(Quantity),
    )

    def __attrs_post_init__(self):
        if self.transport_axis < 0:
            self.transport_axis = get_transport_dir(self.center.system.cell.boundary)
        if self.transport_axis not in [0, 1, 2]:
            raise Exception("transport direction not specified.")
        self.center = copy.deepcopy(self.center)
        if self.left is None:
            self.left = copy.deepcopy(self.center)
        else:
            self.left = copy.deepcopy(self.left)

        if self.right is None:
            self.left_equal_right = True
        if self.left_equal_right:
            print("Left and right lead structures are same.")
            self.right = copy.deepcopy(self.left)
        else:
            self.right = copy.deepcopy(self.right)
        # self.center.solver.restart.densityPath = "center_out.h5"

    @classmethod
    def from_twoprobe(cls, twoprb, **kwargs):
        """initializes instance from TwoProbe object"""
        if not isinstance(twoprb, TwoProbe):
            raise Exception("Reading from not a TwoProbe object.")
        calc = cls(
            center=twoprb.center,
            left=twoprb.left,
            right=twoprb.right,
            transport_axis=twoprb.transport_axis,
            left_equal_right=twoprb.left_equal_right,
            **kwargs,
        )
        return calc

    def get_energies(self):
        return self.energy

    def set_energy(self, energy):
        self.energy = to_quantity(energy, "eV", shape=(-1))

    def solve(self, energy=None, input="nano_scatt_in", output="nano_scatt_out"):
        """Calculates transmission
        This method triggers the nanodcalplus_trsm executable.
        Result is stored in self.dos.transmission

        Args:
            energies (float / iterable): energy grid over which the transmission is to be calculated.
                eg. energies=0.1
                eg. energies=[0.1,0.2,0.3]
        """

        if energy is not None:
            self.set_energy(energy)
        if not (Path(self.center.solver.restart.densityPath).is_file()):
            raise Exception("densityPath file not found for central region.")
        if not (Path(self.left.solver.restart.densityPath).is_file()):
            raise Exception("densityPath file not found for left lead.")
        if not self.left_equal_right:  # if different structure
            if not (Path(self.right.solver.restart.densityPath).is_file()):
                raise Exception("densityPath file not found for right lead.")
        inputname = os.path.splitext(input)[0] + ".json"
        self.left.solver.mpidist = self.center.solver.mpidist
        self.right.solver.mpidist = self.center.solver.mpidist
        self.write(inputname)
        command, binname = self.center.solver.cmd.get_cmd("scatt")
        ret = command(inputname)
        ret.check_returncode()
        # shutil.move("nano_scatt_out.json", output + ".json")
        # self._update(output+".json")
        # self.set_units("si")

    def get_bloch(
        self,
        lead,
        direction,
        k_long_index=None,
        k_trans_index=0,
        energy_index=0,
        spin=1,
    ):
        """get information about certain Bloch-wave in leads.
        Args:
            k_trans_index (int): index of transverse wave vector,
                see system.kpoint.fractional_coordinates
            energy_index (int): index of energy-point
            spin (int): +1/-1   spin-up/down
            k_long_index (int / None): index of the longitudinal wave vector;
                 if None, take all wave vectors.
            lead (str): in which lead, "left" or "right"
            direction (str): "in"coming or "out"going

        Returns:
            dictionary
        """
        ept = energy_index
        kpt = k_trans_index
        if lead != "left" and lead != "right":
            raise ValueError('lead must be "left" or "right".')

        if spin == 1:
            spin_dir = "up"
        if spin == -1:
            spin_dir = "down"
        if self.center.system.hamiltonian.ispin == 4:
            spin_dir = "noncolinear"

        if spin == 1 or self.center.system.hamiltonian.ispin == 4:
            prefix = f"e{ept+1}k{kpt+1}s1/" + lead
        else:
            prefix = f"e{ept+1}k{kpt+1}s2/" + lead

        f = h5py.File("nano_scatt_out.h5", mode="r")
        k_in = f[prefix + "/k_in"][0:].flatten()  # / 2 / np.pi
        k_out = f[prefix + "/k_out"][0:].flatten()  # / 2 / np.pi

        if direction[0] == "i":
            if k_long_index is None:
                k_long_frac = k_in
            else:
                k_long_frac = k_in[k_long_index]
        elif direction[0] == "o":
            if k_long_index is None:
                k_long_frac = k_out
            else:
                k_long_frac = k_out[k_long_index]
        else:
            raise ValueError('direction must be "in" or "out".')

        res = {
            "lead": lead,
            "direction": direction,
            "spin": spin,
            "spin_direction": spin_dir,
            "k_trans_frac": self.center.system.kpoint.fractional_coordinates[kpt, :],
            "k_trans_index": kpt,
            "k_long_index": k_long_index,
            "k_long_frac": k_long_frac,
            "energy": self.energy[ept],
            "energy_index": ept,
        }
        return res

    def get_scatt_wave(
        self, lead, k_long_index, k_trans_index=0, energy_index=0, spin=1, **kwargs
    ):
        """get certain wave-function as 3d-array, given incident wave.
        Args:
            k_trans_index (int): index of transverse wave vector,
                see system.kpoint.fractional_coordinates
            energy_index (int): index of energy-point
            spin (int): +1/-1   spin-up/down
            k_long_index (int): index of the longitudinal wave vector
            lead (str): from which lead, "left" or "right", the incident wave comes
        """

        ept = energy_index
        kpt = k_trans_index
        if lead != "left" and lead != "right":
            raise ValueError('lead must be "left" or "right".')

        if spin == 1:
            att = f"e{ept+1}k{kpt+1}s1/" + lead + "/wavefunction/field"
        else:
            att = f"e{ept+1}k{kpt+1}s2/" + lead + "/wavefunction/field"

        if self.center.system.hamiltonian.ispin == 4:
            if spin == 1:
                att = f"e{ept + 1}k{kpt + 1}s1/" + lead + "/wavefunction/field"
            else:
                att = f"e{ept + 1}k{kpt + 1}s1/" + lead + "/wavefunction_/field"

        field = read_field("nano_scatt_out.h5", att)
        return field[..., k_long_index]

    def plot_isosurfaces(
        self,
        lead,
        k_long_index,
        k_trans_index=0,
        energy_index=0,
        spin=1,
        vals=None,
        **kwargs,
    ):
        """plot isosurface of selected wavefunction at given contour-values
        Args:
            k_trans_index (int): index of transverse wave vector,
                see system.kpoint.fractional_coordinates
            energy_index (int): index of energy-point
            spin (int): +1/-1   spin-up/down
            k_long_index (int): index of the longitudinal wave vector
            lead (str): from which lead, "left" or "right", the incident wave comes
            vals (list of float): contour values
        """
        field = self.get_scatt_wave(
            lead, k_long_index, k_trans_index, energy_index, spin
        )
        plot_isosurfaces_system(self.center.system, field, vals=vals)

    def get_scatter_rate(self, incoming, outgoing):
        """Gets scattering rate from an incoming to an outgoing state.
        Args:
            incoming (dict): see get_bloch
            outgoing (dict): see get_bloch
        """
        if incoming["direction"][0] != "i":
            raise ValueError('incoming["direction"] must be "in".')
        if outgoing["direction"][0] != "o":
            raise ValueError('outgoing["direction"] must be "out".')

        ept = incoming["energy_index"]
        kpt = incoming["k_trans_index"]

        prefix = f"e{ept + 1}k{kpt + 1}s1/"

        f = h5py.File("nano_scatt_out.h5", mode="r")
        mat = np.transpose(f[prefix + "scatt_mat_out_in"][0:])
        mat = mat[::2, :] + 1j * mat[1::2, :]

        num_left_k_in = f[prefix + "left/k_in"][0:].size
        num_left_k_out = f[prefix + "left/k_out"][0:].size

        if incoming["lead"] == "left":
            c = incoming["k_long_index"]
        elif incoming["lead"] == "right":
            c = incoming["k_long_index"] + num_left_k_in
        else:
            raise ValueError('incoming["lead"] must be "left" or "right".')

        if outgoing["lead"] == "left":
            r = outgoing["k_long_index"]
        elif outgoing["lead"] == "right":
            r = outgoing["k_long_index"] + num_left_k_out
        else:
            raise ValueError('incoming["lead"] must be "left" or "right".')

        return mat[r, c]
