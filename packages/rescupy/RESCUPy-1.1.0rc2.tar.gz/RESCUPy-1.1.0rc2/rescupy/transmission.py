"""
two-probe transport calculator
"""
from matplotlib import pyplot as plt
from pathlib import Path
from rescupy.base import Base
from rescupy.dos import Dos
from rescupy.totalenergy import TotalEnergy
from rescupy.twoprobe import TwoProbe, get_transport_dir
from rescupy.utils import dict_converter
import attr
import copy
import numpy as np
import os
import shutil


@attr.s
class Transmission(Base):
    """Transmission class.
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

    dos: Dos = attr.ib(
        factory=Dos,
        converter=lambda d: dict_converter(d, Dos),
        validator=attr.validators.instance_of(Dos),
    )
    transport_axis: int = attr.ib(
        default=-1, validator=attr.validators.in_([-1, 0, 1, 2])
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

    def _set_dos_grid(self, energies):
        self.dos.set_energy(energies)

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

    def solve(self, energies=None, input="nano_trsm_in", output="nano_trsm_out"):
        self.calc_transmission(energies=energies, input=input, output=output)

    def calc_transmission(
        self, energies=None, input="nano_trsm_in", output="nano_trsm_out"
    ):
        """Calculates transmission
        This method triggers the nanodcalplus_trsm executable.
        Result is stored in self.dos.transmission

        Args:
            energies (float / iterable): energy grid over which the transmission is to be calculated.
                eg. energies=0.1
                eg. energies=[0.1,0.2,0.3]
            unit (string): energy unit
        """

        if energies is not None:
            self._set_dos_grid(energies)
        if not (Path(self.center.solver.restart.densityPath).is_file()):
            raise Exception("Error in transmission.solve: densityPath file not found.")
        if not (Path(self.left.solver.restart.densityPath).is_file()):
            raise Exception("Error in transmission.solve: densityPath file not found.")
        if not self.left_equal_right:  # if different structure
            if not (Path(self.right.solver.restart.densityPath).is_file()):
                raise Exception(
                    "Error in transmission.solve: densityPath file not found."
                )
        inputname = os.path.splitext(input)[0] + ".json"
        self.left.solver.mpidist = self.center.solver.mpidist
        self.right.solver.mpidist = self.center.solver.mpidist
        self.write(inputname)
        command, binname = self.center.solver.cmd.get_cmd("trsm")
        ret = command(inputname)
        ret.check_returncode()
        shutil.move("nano_trsm_out.json", output + ".json")
        self._update(output + ".json")
        self.set_units("si")
        self._reshape_transmission()

    def _reshape_transmission(self):
        nb = self.dos.energy.size
        nk = self.center.system.kpoint.get_kpoint_num()
        self.dos.transmission = self.dos.transmission.reshape((nb, nk, -1), order="F")

    def get_transmission(self):
        self._reshape_transmission()
        return self.dos.transmission

    def get_energies(self):
        return self.dos.energy

    def plot(self, filename=None, show=True):
        """visualizes the result"""
        self._reshape_transmission()
        sys = self.center.system
        nb = self.dos.energy.size
        nk = sys.kpoint.get_kpoint_num()
        ispin = sys.hamiltonian.ispin
        axes_cross = list(range(3))
        axes_cross.pop(self.transport_axis)
        grid_cross = sys.kpoint.grid.copy()
        grid_cross.pop(self.transport_axis)
        labels_cross = ["kx", "ky", "kz"]
        labels_cross.pop(self.transport_axis)
        if nk == 1:
            x = self.dos.energy.m
            xunit = self.dos.energy.u
            y = self.dos.transmission
            # assert y.shape[2] == sys.hamiltonian.ispin
            el = 0.0 * xunit
            er = el - sys.pop.bias.to(xunit)
            Emin = min(el.m, er.m)
            Emax = max(el.m, er.m)
            fig = plt.figure()
            if ispin == 2:
                plt.plot(x, y[:, 0, 0], "-g", label="spin-up")
                plt.plot(x, y[:, 0, 1], "-r", label="spin-down")
            else:
                plt.plot(x, y[:, 0, 0], "-k")
            if abs(Emax - Emin) < 1.0e-10:
                plt.axvline(x=Emin, color="k", linestyle="--", label="Fermi energy")
            else:
                plt.axvspan(Emin, Emax, facecolor="r", alpha=0.25)
            plt.xlabel(f"Energy ({xunit})")
            plt.ylabel("Transmission")
            plt.legend()
            fig.tight_layout()
        elif sys.kpoint.type == "line" or np.count_nonzero(sys.kpoint.grid == 1) == 2:
            # kpoints are lined up
            raise Exception("We cannot plot this.")
        elif sys.kpoint.type == "full" and nb == 1:
            # plot transmission through the BZ at single energy point
            bvec_cross = sys.kpoint.bvec.m[axes_cross, :]
            bvec_unit = sys.kpoint.bvec.u
            k_coo = sys.kpoint.fractional_coordinates[:, axes_cross]
            ind = np.lexsort((k_coo[:, 0], k_coo[:, 1]))
            k_coo = k_coo[ind, :]
            x_coo = np.reshape(k_coo[:, 0], tuple(grid_cross), order="F")
            y_coo = np.reshape(k_coo[:, 1], tuple(grid_cross), order="F")
            if ispin == 1 or ispin == 4:
                fig, ax0 = plt.subplots()
            else:
                fig, (ax0, ax1) = plt.subplots(ncols=2)
            # spin-maj
            t_max = np.amax(self.dos.transmission)
            t_min = np.amin(self.dos.transmission)
            trans = self.dos.transmission[0, ind, 0]
            trans = np.reshape(trans, tuple(grid_cross), order="F")
            cs = ax0.contourf(
                y_coo[0, :] * np.linalg.norm(bvec_cross[1]),
                x_coo[:, 0] * np.linalg.norm(bvec_cross[0]),
                trans,
                vmin=t_min,
                vmax=t_max,
            )
            ax0.set(
                xlabel=labels_cross[1] + f" ({bvec_unit})",
                ylabel=labels_cross[0] + f" ({bvec_unit})",
            )
            fig.colorbar(cs, ax=ax0)
            # spin-min
            if ispin == 2:
                ax0.set_title("spin-majority")
                trans = self.dos.transmission[0, ind, 1]
                trans = np.reshape(trans, tuple(grid_cross), order="F")
                cs = ax1.contourf(
                    y_coo[0, :] * np.linalg.norm(bvec_cross[1]),
                    x_coo[:, 0] * np.linalg.norm(bvec_cross[0]),
                    trans,
                    vmin=t_min,
                    vmax=t_max,
                )
                ax1.set(
                    xlabel=labels_cross[1] + f" ({bvec_unit})",
                    ylabel=labels_cross[0] + f" ({bvec_unit})",
                )
                ax1.set_title("spin-minority")
                fig.colorbar(cs, ax=ax1)
        else:
            raise Exception("We cannot plot this.")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig
