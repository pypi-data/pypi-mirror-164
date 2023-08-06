# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from pathlib import Path
from rescupy.io.calculators import read as read_calc
from rescupy.utils import convert_units, ureg, Quantity, to_quantity, Unit
from rescupy.utils import SpecialCaseEncoder, is_array_like, list_methods
import attr
import copy
import io
import json
import numpy as np


@attr.s
class Base:
    """The ``Base`` class is used to define universal methods and parameters common to `rescupy` classes."""

    # input is dictionary with default constructor
    # attr = attr.ib(default=None)

    # def __attrs_post_init__(self):
    #     return

    @classmethod
    def read(cls, filename, units="si"):
        """Initialize an object from a JSON file."""
        return read_calc(cls, filename, units=units)

    def asdict(self):
        """
        Returns the object as a dictionary.

        Args:

        Returns:

        """
        return attr.asdict(
            self,
            recurse=True,
            filter=lambda attr, value: attr.name != "inpDict",
        )

    def copy(self):
        """Returns a deep copy of the object."""
        return copy.deepcopy(self)

    def set_units(self, units):
        """Converts all units to the prescribed unit system (recursive).

        Args:
            units (str):
                Unit system ('atomic' or 'si')

        """
        set_units_core(self, units)

    def write(self, filename, units="atomic"):
        self.set_units(units)
        adict = self.asdict()
        if isinstance(filename, io.TextIOWrapper):
            path = Path(filename.name)
        else:
            path = Path(filename)
        with path.open(mode="w") as fid:
            json.dump(adict, fid, indent=2, sort_keys=True, cls=SpecialCaseEncoder)

    def _reshape(self):
        reshape_core(self)

    def _update(self, filename):
        tmp = self.__class__.read(filename)
        self.__dict__.update(tmp.__dict__)


def reshape_core(obj):
    """Reshapes all array-like objects recursively."""
    for key in obj.__dict__.keys():
        # call _reshape recursively
        atr = getattr(obj, key)
        object_methods = list_methods(atr)
        if "_reshape" in object_methods:
            atr._reshape()
            setattr(obj, key, atr)
            continue
        # look for xxx_shape
        if len(key) < 6:
            continue
        if key[-6:] != "_shape":
            continue
        # reshape
        atr_key = key[:-6]
        atr = getattr(obj, atr_key)
        if is_array_like(atr):
            shape = getattr(obj, key)
            if not isinstance(atr, Quantity):
                atr = np.array(atr)
            atr = np.reshape(atr, shape, order="F")
            setattr(obj, atr_key, atr)


def set_units_core(self, units):
    """
    Convert all units to the prescribed unit system (recursive).

    Args:
        units (str): Unit system ('atomic' or 'si')

    Returns:

    """
    units = units.lower()
    if not units in ["atomic", "si"]:
        raise Exception("Unit system " + units + " not recognized.")
    for key in self.__dict__.keys():
        atr = getattr(self, key)
        object_methods = list_methods(atr)
        if "set_units" in object_methods:
            atr.set_units(units)
            setattr(self, key, atr)
            continue
        if isinstance(atr, Quantity):
            atr = convert_quantity(atr, units)
            continue
        if len(key) < 6:
            continue
        if key[-6:] != "_units":
            continue
        atr = getattr(self, key[:-6])
        unit = getattr(self, key)
        atr, unit = convert_units(atr, unit, units)
        setattr(self, key[:-6], atr)
        setattr(self, key, unit)


def convert_quantity(atr, unit_system):
    units = atr.to_tuple()[1]
    newunits = [list(u) for u in units]
    for j, u in enumerate(units):
        unit = Unit(u[0])
        if unit_system == "si":
            if unit.is_compatible_with("angstrom"):
                newunits[j][0] = "angstrom"
            if unit.is_compatible_with("eV"):
                newunits[j][0] = "eV"
        if unit_system == "atomic":
            if unit.is_compatible_with("bohr"):
                newunits[j][0] = "bohr"
            if unit.is_compatible_with("hartree"):
                newunits[j][0] = "hartree"
    string = []
    for u in newunits:
        string.append(u[0] + f"**{u[1]}")
    string = "*".join(string)
    atr.ito(string)
