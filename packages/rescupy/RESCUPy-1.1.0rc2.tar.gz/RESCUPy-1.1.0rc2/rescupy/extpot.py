# -*- coding: utf-8 -*-
"""
Created on 2020-11-25

__author__ = Vincent Michaud-Rioux
"""

import attr
from typing import List
from rescupy.base import Base
from rescupy.utils import to_quantity, Quantity, ureg


@attr.s
class Region(Base):
    """
    Region class, defines a constant function in a specified region

    Attributes:
        fractional_x_range: used to specify the geometry of the parallelepipedic region, eg. [0.3,0.6]
        val: a voltage value (for gates) or a dielectric constant
    """

    x_range = attr.ib(default=None)
    fractional_x_range: List[float] = attr.ib(factory=lambda: [-1.0, -1.0])
    y_range = attr.ib(default=None)
    fractional_y_range: List[float] = attr.ib(factory=lambda: [-1.0, -1.0])
    z_range = attr.ib(default=None)
    fractional_z_range: List[float] = attr.ib(factory=lambda: [-1.0, -1.0])
    val: Quantity = attr.ib(
        default=0.0 * ureg.eV,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.instance_of(Quantity),
    )

    def __attrs_post_init__(self):
        for key in self.__dict__.keys():
            atr = getattr(self, key)
            if (
                key[-6:] == "_range"
                and (not hasattr(atr, "__iter__"))
                and atr is not None
            ):
                setattr(self, key, [atr, atr])


@attr.s
class Extpot(Base):
    """
    External potential class

    Attributes:
        axis (int):
            Direction (lattice vector) of external potential modulation. ``axis`` is passed to the Fortran code, and hence it ranges from 1 to 3.
        amplitude (float):
            External potential amplitude.
        shape (string):
            External potential shape. Valid shapes are

                * sawtooth
                * zero (default)
    """

    axis: int = attr.ib(
        default=1,
        converter=int,
        validator=attr.validators.instance_of(int),
    )
    amplitude: Quantity = attr.ib(
        default=0.0 * ureg.eV,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.instance_of(Quantity),
    )
    shape: str = attr.ib(
        default="zero",
        converter=str,
        validator=attr.validators.instance_of(str),
    )
    gates: List[Region] = attr.ib(
        factory=list,
        converter=lambda d: [Region(**d[i]) for i in range(len(d))],
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Region),
            iterable_validator=attr.validators.instance_of(list),
        ),
    )
    dielectrics: List[Region] = attr.ib(
        factory=list,
        converter=lambda d: [Region(**d[i]) for i in range(len(d))],
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Region),
            iterable_validator=attr.validators.instance_of(list),
        ),
    )

    def set_units(self, units):
        super().set_units(units=units)
        if self.gates is not None:
            for g in self.gates:
                g.set_units(units)
        # no need to set dielectric units
