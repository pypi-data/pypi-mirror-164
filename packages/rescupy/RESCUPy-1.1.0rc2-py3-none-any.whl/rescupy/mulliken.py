# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from attr.validators import instance_of, optional
from pathlib import Path
import attr
from rescupy.base import Base
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
class MullikenData(Base):
    """``Mulliken`` class' data holder.

    Args:

    Returns:

    """

    atom_populations: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    atom_populations_shape: list = attr.ib(
        default=None,
        converter=attr.converters.optional(list),
        validator=attr.validators.optional(attr.validators.instance_of(list)),
    )
    orbital_populations: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    orbital_populations_shape: list = attr.ib(
        default=None,
        converter=attr.converters.optional(list),
        validator=attr.validators.optional(attr.validators.instance_of(list)),
    )
    orbital_atom: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    orbital_index: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    orbital_l: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    orbital_m: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    orbital_species: NDArray = attr.ib(
        default=[],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )


@attr.s
class Mulliken(Base):
    """``Mulliken`` class.

    Examples::

        from rescupy import Mulliken
        import numpy as np
        calc = Mulliken.from_totalenergy("nano_scf_out.json")
        calc.solve()

    Attributes:
        system:
           Object containing system related parameters.
        energy:
           Object containing the total energy and its derivatives (force, stress, etc.).
        mulliken:
           Object containing the Mulliken population data.
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
    mulliken: MullikenData = attr.ib(
        factory=MullikenData,
        converter=lambda d: dict_converter(d, MullikenData),
        validator=attr.validators.instance_of(MullikenData),
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

    def solve(self, input="nano_mul_in", output="nano_mul_out"):
        """Performs a non.self-consistent calculation calling ``rescuplus_mul``.

        Args:
            filename (str):
                The object is saved to an input file ``filename`` which is read by ``rescuplus_mul``.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        self._check_mul()
        output = solve_generic(self, "mul", input, output)
        self._update(output + ".json")

    def _check_mul(self):
        return
