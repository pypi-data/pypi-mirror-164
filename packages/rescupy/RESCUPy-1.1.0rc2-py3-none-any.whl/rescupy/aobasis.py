# -*- coding: utf-8 -*-
"""Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from rescupy.base import Base
from rescupy.orb import AoOrb, KbOrb, RadFunc
from rescupy.utils import load_dcal
from typing import Dict, List, Optional, Set
import attr
import numpy as np


@attr.s
class NaoBasis(Base):
    """``naoBasis`` class.

    Attributes:
        orb (AoOrb):
            Atomic orbitals.
        path (str):
            Pseudopotential path.
        symbol (str):
            Element symbol.
        varname (str):
            Variable name in the H5/MAT-file.

    """

    path: str = attr.ib(validator=attr.validators.instance_of(str))
    varname: str = attr.ib(validator=attr.validators.instance_of(str))
    symbol: Optional[str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    numorb: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
    )
    orb: AoOrb = attr.ib(
        default=None,
        # validator=attr.validators.instance_of(AoOrb),
    )

    def __attrs_post_init__(self) -> None:
        """
        :rtype: None
        """
        varname = self.varname
        filename = self.path
        if isinstance(self.orb, list) and "symbol" in self.__dict__.keys():
            norb = len(self.orb)
            self.orb = [AoOrb(**self.orb[i]) for i in range(norb)]
            self.numorb = len(self.orb)
            return
        data, fmt = load_dcal(filename)
        if fmt == "mat":
            norb = len(data[varname][0][0])
        else:
            norb = len(data[varname]["Parameter"])
        self.orb = [AoOrb(filename, varname, index=i) for i in range(norb)]
        self.numorb = len(self.orb)
        for snam, inam in zip(["symbol"], ["symbol"]):
            try:
                if fmt == "mat":
                    tmp = data["atom"][0][0][inam][0][0]
                else:
                    tmp = data["atom"][inam][0:]
                    if inam == "symbol":
                        tmp = "".join(map(chr, tmp.flatten()))
                if isinstance(tmp, np.ndarray):
                    tmp = float(tmp)
                if isinstance(tmp, str):
                    tmp = str(tmp)
                setattr(self, snam, tmp)
            except ValueError:
                raise Exception(
                    "Couldn't find parameter 'atom.%s' in file %s." % (inam, filename)
                )

    """Returns the number of orbitals."""

    def get_number_of_orbitals(self):
        llist = [o.l for o in self.orb]
        return np.sum(2 * np.array(llist, dtype=int) + 1)

    def to_vacuum(self):
        self.path = ""
        # self.varname = "Vnl"
        self.symbol += "_Va"
        for i in range(len(self.orb)):
            self.orb[i].to_vacuum()


@attr.s
class VnlBasis(Base):
    """``vnlBasis`` class.

    Attributes:
        symbol (str):
            Element symbol.
        path (str):
            Pseudopotential path.
        orb (KbOrb):
            Atomic orbitals.

    """

    path: str = attr.ib(validator=attr.validators.instance_of(str))
    varname: str = attr.ib(validator=attr.validators.instance_of(str))
    symbol: Optional[str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )

    numorb: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
    )
    orb = attr.ib(
        default=None,
        # validator=attr.validators.optional(attr.validators.instance_of(KbOrb)),
    )

    def __attrs_post_init__(self):
        varname = self.varname
        filename = self.path
        if isinstance(self.orb, list) and "symbol" in self.__dict__.keys():
            norb = len(self.orb)
            rng = range(0, norb)
            self.orb = [KbOrb(**self.orb[j]) for i, j in zip(rng, range(0, norb))]
            return
        data, fmt = load_dcal(filename)
        norb = 0
        try:
            data[varname]
        except:
            raise Exception(f"Cannot read field {varname} from {filename}.")
        if fmt == "mat" and len(data[varname][0]) > 0:
            norb = len(data[varname][0][0])
        elif data[varname].attrs.get("MATLAB_empty"):
            norb = 0
        elif len(data[varname]["Parameter"]) > 0:
            # find length based on HDF5 object reference
            norb = len(data[varname]["Parameter"])
        if varname == "VnlSO":
            rng = range(1, norb)
        else:
            rng = range(0, norb)
        self.orb = [
            KbOrb(filename, varname, index=i) for i in rng
        ]  # 1st entry is empty
        for snam, inam in zip(["symbol"], ["symbol"]):
            try:
                if fmt == "mat":
                    tmp = data["atom"][0][0][inam][0][0]
                else:
                    tmp = data["atom"][inam][0:]
                    if inam == "symbol":
                        tmp = "".join(map(chr, tmp.flatten()))
                if isinstance(tmp, np.ndarray):
                    tmp = float(tmp)
                if isinstance(tmp, str):
                    tmp = str(tmp)
                setattr(self, snam, tmp)
            except ValueError:
                raise Exception(
                    "Couldn't find parameter 'atom."
                    + inam
                    + " in file "
                    + filename
                    + "."
                )

        self.numorb = len(self.orb)

    def to_vacuum(self):
        self.path = ""
        # self.varname = "Vnl"
        self.symbol += "_Va"
        self.numorb = 0
        self.orb = []
