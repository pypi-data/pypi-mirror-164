"""
two-probe transport calculator
"""
from attr import field
from pathlib import Path
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.kpoint import Kpoint
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
import attr
import copy
import numpy as np
import os
import scipy
import scipy.signal
import shutil


@attr.s
class TwoProbe(Base):
    """``TwoProbe`` calculator class.

    Attributes:
        transport_axis (int):
            Transport direction.

        left_equal_right (bool):
            Indicates whether the two lead structures are identical.

        bias (float):
            Drain-source bias voltage.

        energy_resolution (float):
            Energy resolution for real-axis integration.
    """

    # must specify at initialization: system, transport_axis
    center: TotalEnergy = field(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )
    left: TotalEnergy = field(
        default=None,
        converter=attr.converters.optional(lambda d: dict_converter(d, TotalEnergy)),
        validator=attr.validators.optional(attr.validators.instance_of(TotalEnergy)),
    )
    right: TotalEnergy = field(
        default=None,
        converter=attr.converters.optional(lambda d: dict_converter(d, TotalEnergy)),
        validator=attr.validators.optional(attr.validators.instance_of(TotalEnergy)),
    )
    transport_axis: int = field(
        default=-1, validator=attr.validators.in_([-1, 0, 1, 2])
    )
    left_equal_right: bool = field(default=False)  # are lead structures identical?

    # drain-source bias
    bias: Quantity = field(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    # resolution on real energy axis for contour integral
    energy_resolution: Quantity = field(
        default=0.01 * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
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

        if self.bias is None:
            self.bias = self.center.system.pop.bias
        self.set_units("si")
        self.set_bias(self.bias)

        grid = self.center.system.kpoint.grid.copy()
        if grid is not None and grid[self.transport_axis] > 1:
            print("k-points to be cut off along transport direction")
            grid[self.transport_axis] = 1
            self.center.system.kpoint = Kpoint(grid=grid)
            self.center.system.kpoint.set_bvec(self.center.system.cell)

        self.center.system.cell.boundary[
            self.transport_axis * 2 : self.transport_axis * 2 + 2
        ] = [1, 1]
        self.center.system.pop.set_type(type="fd")
        self.left.system.pop.set_type(type="fd")
        self.right.system.pop.set_type(type="fd")
        # the scf program will start by looking for these files
        # self.left.solver.restart.densityPath = "left_out.h5"
        # self.right.solver.restart.densityPath = "right_out.h5"

    def set_bias(self, bias, energy_resolution=None):
        """Sets drain-source bias and optionally the energy resolution for real-axis integration.
        Args:
            bias (float): drain-source bias
            energy_resolution (float): energy resolution for real-axis integration
        """
        bias = to_quantity(bias, "eV")
        self.center.system.pop.bias = bias
        self.bias = bias
        if energy_resolution is not None:
            self.energy_resolution = energy_resolution
        self.center.system.pop.nReal = int(
            abs(self.bias / self.energy_resolution).to("dimensionless").m
        )

    def set_cmd(self, mpi):
        """Sets os command to run nanodcalplus_2pb
        eg. mpi="mpiexec -n 16"
        """
        self.left.solver.cmd.mpi = mpi
        self.center.solver.cmd.mpi = mpi
        self.right.solver.cmd.mpi = mpi

    def solve_left(self):
        """self-consistent calculation for lead"""
        if Path("left_out.h5").is_file() and Path("left_out.json").is_file():
            print("calculation seems complete for left lead")
            self.left = TotalEnergy.read("left_out.json")
        else:
            self.left.solve(input="left", output="left_out")

    def solve_right(self):
        """self-consistent calculation for lead"""
        if not self.left_equal_right:  # if different structure
            if Path("right_out.h5").is_file() and Path("right_out.json").is_file():
                print("calculation seems complete for right lead")
                self.right = TotalEnergy.read("right_out.json")
            else:
                self.right.solve(input="right", output="right_out")
        else:
            self.right = copy.deepcopy(self.left)

    def solve(self, input="nano_2prb_in", output="nano_2prb_out"):
        self.solve_left()
        self.solve_right()
        self.left.solver.mpidist = self.center.solver.mpidist
        self.right.solver.mpidist = self.center.solver.mpidist
        self.left.solver.cmd = self.center.solver.cmd
        self.right.solver.cmd = self.center.solver.cmd
        inputname = os.path.splitext(input)[0] + ".json"
        self.write(inputname)
        command, binname = self.center.solver.cmd.get_cmd("2prb")
        ret = command(inputname)
        ret.check_returncode()
        shutil.move("nano_2prb_out.json", output + ".json")
        self._update(output + ".json")

    def smooth_field(self, field, axis, width=2.0, shape="erf", preslice=None):
        """Smooths a field by circular convolution.

        Args:
            field (str):
                str: Path in the HDF5 filed pointed to by self.solver.restart.density. For example, "potential/effective".
            axis (int):
                Axis remaining after averaging. The value should be between 0 and 2.
            width (float):
                Unit system ('atomic' or 'si')
            preslice (lamda):
                Lamda expression that slices the field, for example when we wanna cut out the surrounding vaccum
                preslice=lambda f: f[:,60:90,:]
        """
        if axis != self.transport_axis:
            return self.center.smooth_field(
                field=field, axis=axis, width=width, shape=shape
            )
        axes_cross = list(range(3))
        axes_cross.pop(axis)

        field3 = [self.left.get_field(field), self.center.get_field(field)]
        if self.left_equal_right:
            field3.append(self.left.get_field(field))
        else:
            field3.append(self.right.get_field(field))

        if field.find("potential") != -1:
            field3[0] = field3[0] - self.left.energy.efermi
            field3[2] = field3[2] - self.right.energy.efermi - self.bias

        if preslice is not None:
            for j in range(len(field3)):
                field3[j] = preslice(field3[j])
        for j in range(len(field3)):
            field3[j] = np.mean(field3[j], axis=tuple(axes_cross))
        field3 = np.concatenate(tuple(field3))

        x_l = self.left.system.cell.get_grid(axis=axis)
        x_c = self.center.system.cell.get_grid(axis=axis)
        x_r = self.right.system.cell.get_grid(axis=axis)
        dx = self.center.system.cell.get_dx(axis)
        lx_l = self.left.system.cell.get_length(axis=axis)
        lx_c = self.center.system.cell.get_length(axis=axis)
        lx_r = self.right.system.cell.get_length(axis=axis)
        L = lx_l + lx_c + lx_r

        x_lcr = np.concatenate((x_l - lx_l, x_c, x_r + lx_c)) + lx_l
        x3 = np.concatenate((x_lcr - L, x_lcr, x_lcr + L))
        pulse = 0.5 * (scipy.special.erf((x3 - width / 2.0)) + 1.0) - 0.5 * (
            scipy.special.erf((x3 + width / 2.0)) + 1.0
        )
        pulse = pulse / np.sum(pulse) / dx
        for i in np.arange(2):
            field3 = scipy.signal.convolve(np.tile(field3, 3), pulse, mode="full") * dx
            field3 = field3[2 * x_lcr.size : 3 * x_lcr.size]
        return field3[x_l.size : x_l.size + x_c.size]

    @classmethod
    def read3(cls, file_center, file_left=None, file_right=None, units="si"):
        """initialize TwoProbe object from json files.
        Args:
            file_center (string)
            file_left (string/None)
            file_right (string/None)
            units (string): unit system.
            eg. file_center="center_out.json"
                file_left="left_out.json"
                file_right="right_out.json"
        """
        inpDict = {}
        inpDict["center"] = TotalEnergy.read(file_center, units)
        if file_left is not None:
            inpDict["left"] = TotalEnergy.read(file_left, units)
        if file_right is not None:
            inpDict["right"] = TotalEnergy.read(file_right, units)
        ins = cls(**inpDict)
        return ins


def get_transport_dir(bd):
    assert len(bd) == 6
    nz = np.flatnonzero(np.array(bd) == 1)[0]
    td = np.int(np.floor(nz / 2))
    if td not in [0, 1, 2]:
        td = -1
        # raise Exception('fail to identify transport direction from the given boundary condition.')
    return td
