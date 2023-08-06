# -*- coding: utf-8 -*-
"""Hamiltonian module"""

from rescupy.extpot import Extpot
from rescupy.utils import dict_converter
import attr
from rescupy.base import Base
import numpy as np


@attr.s
class Hamiltonian(Base):
    """``Hamiltonian`` class.

    Attributes:
        extpot (Extpot):
            Contains the external potential parameters.
        ispin (int):
            Hamiltonian spin-treatment level:

            * 1 : degenerate
            * 2 : collinear
            * 4 : non-collinear

        soc (bool):
            Include spin-orbit coupling if True.

    """

    extpot: Extpot = attr.ib(
        factory=Extpot,
        converter=lambda d: dict_converter(d, Extpot),
        validator=attr.validators.instance_of(Extpot),
    )
    ispin: int = attr.ib(
        default=1, converter=int, validator=attr.validators.instance_of(int)
    )
    soc: bool = attr.ib(
        default=False, converter=bool, validator=attr.validators.instance_of(bool)
    )

    def __attrs_post_init__(self):
        if self.soc:
            self.ispin = 4
        if not self.ispin in [1, 2, 4]:
            raise Exception("Invalid hamiltonian.ispin value: " + self.ispin + ".")

    def get_ispin(self):
        """Returns the spin-treatment level."""
        return self.ispin

    def get_spin_num(self):
        """Returns number of spin channels."""
        ns = self.ispin
        if self.ispin == 4:
            ns = 1
        return ns

    def set_ispin(self, ispin):
        """Sets spin-treatment level.

        One can set ispin either as an int or str. The correspondence is as follows

        - 1 == "degenerate"
        - 2 == "collinear"
        - 4 == "non-collinear"

        Args:

            ispin (int, str): spin-treatment level.

        """
        if isinstance(ispin, str):
            if ispin == "degenerate":
                ispin = 1
            elif ispin == "collinear":
                ispin = 2
            elif ispin == "non-collinear":
                ispin = 4
            else:
                raise Exception("Invalid ispin value: " + ispin + ".")
        elif not isinstance(ispin, int):
            raise Exception("Argument ispin must be an int or a str.")
        if not ispin in [1, 2, 4]:
            raise Exception("Invalid hamiltonian.ispin value: " + ispin + ".")
        self.ispin = ispin

    def set_soc(self, soc):
        """Sets soc switch.

        Args:

            soc (bool): If True then SOC is included and it isn't otherwise.

        """
        if not isinstance(soc, bool):
            raise Exception("Argument soc must be a bool.")
        self.soc = soc
        if self.soc:
            self.set_ispin(4)
