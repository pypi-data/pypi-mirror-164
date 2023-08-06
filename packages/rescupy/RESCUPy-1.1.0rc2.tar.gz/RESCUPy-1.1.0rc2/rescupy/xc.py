# -*- coding: utf-8 -*-
"""This module defines the ``Xc`` class."""

import attr
from rescupy.base import Base
import numpy as np


@attr.s
class Xc(Base):
    """``Xc`` class.

    Attributes:
        functional_id (1D array):
            Functional id (LibXC).

            Examples::

                xc.functional_id = [1, 12] # LDA-PW
        functional_names (list of strings):
            Functional names (LibXC).

            Examples::

                xc.functional_names = ["XC_GGA_X_PBE","XC_GGA_C_PBE"]
    """

    functional_id = attr.ib(default=None)
    functional_names = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.functional_id is None and self.functional_names is None:
            self.functional_id = [1, 12]

        if self.functional_names is not None:
            self.functional_id = [
                name2id(name.lower()) for name in self.functional_names
            ]

        if self.functional_id is not None:
            self.functional_names = [id2name(str(i)) for i in self.functional_id]

    def get_dict_of_functional_names(self):
        """Returns a dict with all functional"""
        from rescupy.data.xc import infoDict

        return infoDict

    def set_functional(self, functional):
        """Sets the functional.

        Allowed values are: 

            - LDA
            - PBE

        """

        if functional == "LDA":
            self.set_functional_names(["XC_LDA_X","XC_LDA_C_PW"])
        elif functional == "PBE":
            self.set_functional_names(["XC_GGA_X_PBE","XC_GGA_C_PBE"])
        else:
            raise Exception(f"Invalid function {functional}.")

    def set_functional_names(self, functional_names):
        """Sets function functional_names.

        The functional_id attribute is updated accordingly.
        """
        if not isinstance(functional_names, list):
            raise Exception("functional_names must be a list.")
        self.functional_names = functional_names
        self.functional_id = [name2id(name.lower()) for name in self.functional_names]


def name2id(name):
    """Converts a functional name into it's integer ID."""
    from rescupy.data.xc import idDict

    return idDict[name]


def id2name(id):
    """Converts an integer ID into a functional name."""
    from rescupy.data.xc import nameDict

    return nameDict[id]
