# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from attr.validators import instance_of, optional
from pathlib import Path
import attr
from rescupy.base import Base
from rescupy.system import plot_isosurfaces as plot_isosurfaces_system
import copy
import h5py
import io
import json
import matplotlib.pyplot as plt
from nptyping import NDArray
import numpy as np
import toml

from rescupy.system import System
from rescupy.energy import Energy
from rescupy.io.calculators import read as read_calc, solve_generic
from rescupy.solver import Solver
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import read_field, SpecialCaseEncoder, dict_converter


@attr.s
class Wavefunction(Base):
    """``Wavefunction`` class.

    Examples::

        from rescupy import Wavefunction as WF
        import numpy as np
        calc = WF.from_totalenergy("nano_scf_out.json")
        calc.system.kpoint.set_grid([3,3,3])
        calc.solve()

    Attributes:
        system:
           Object containing system related parameters.
        energy:
           Object containing the total energy and its derivatives (force, stress, etc.).
        solver:
           Object containing solver related parameters.
    """

    # input is dictionary with default constructor
    system: System = attr.ib(
        converter=lambda d: dict_converter(d, System),
        validator=attr.validators.instance_of(System),
    )

    # optional
    energy: Energy = attr.ib(
        factory=Energy,
        converter=lambda d: dict_converter(d, Energy),
        validator=attr.validators.instance_of(Energy),
    )
    solver: Solver = attr.ib(
        factory=Solver,
        converter=lambda d: dict_converter(d, Solver),
        validator=attr.validators.instance_of(Solver),
    )

    def __attrs_post_init__(self):
        self._reshape()

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        sys = totalenergy.system.copy()
        calc = cls(sys, solver=totalenergy.solver, **kwargs)
        calc.energy = totalenergy.energy.copy()
        return calc

    def solve(self, input="nano_wvf_in", output="nano_wvf_out"):
        """Performs a non.self-consistent calculation calling ``rescuplus_wvf``.

        Args:
            filename (str):
                The object is saved to an input file ``filename`` which is read by ``rescuplus_wvf``.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        self._check_wvf()
        output = solve_generic(self, "wvf", input, output)
        self._update(output + ".json")

    def _check_wvf(self):
        return

    def plot_isosurfaces(self, kpt=0, band=0, spin=1, vals=None):
        """plot isosurface of selected wavefunction at given contour-values
        Args:
            kpt  (int): index of k-point, see system.kpoint.fractional_coordinates
            band (int): band index
            spin (int): +1/-1   spin up/down
            vals (list of float): contour values
        """

        if self.system.hamiltonian.ispin == 1:
            att = f"wavefunctions/{kpt + 1}/field"
        else:
            if spin == 1:
                att = f"wavefunctions/spin-up/{kpt + 1}/field"
            else:
                att = f"wavefunctions/spin-down/{kpt + 1}/field"

        field = read_field('nano_wvf_out.h5', att)
        field = field[..., band]
        plot_isosurfaces_system(self.system, field, vals=vals)


