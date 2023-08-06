# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from rescupy.aobasis import VnlBasis
from rescupy.base import Base
from rescupy.orb import RadFunc
from rescupy.utils import load_dcal
import attr
import numpy as np


@attr.s
class Pspot(Base):
    """
    pspot class.

    Attributes:
        symbol : string
           element symbol
        path : string
           pseudopotential path
        Z: integer
           pseudoion charge
        vlc : radFunc
           local pseudopotential
        rpc : radFunc
           partial core charge
        vnl : kbOrb-array
           KB-orbitals
        vso : kbOrb-array
           SO-orbitals
    """

    path: str = attr.ib(validator=attr.validators.instance_of(str))
    symbol: str = attr.ib(
        default=None,
        converter=attr.converters.optional(str),
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    Z: float = attr.ib(
        default=None,
        converter=attr.converters.optional(float),
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    vlc = attr.ib(default=None)
    rpc = attr.ib(default=None)
    vnl = attr.ib(default=None)
    vso = attr.ib(default=None)

    def __attrs_post_init__(self):
        self._set_vlc()
        self._set_rpc()
        self._set_vnl()
        # self._init_vso()
        # temporarily do not real vso, just fill field with vnl values
        # self.vso = copy.deepcopy(self.vnl)
        # self.vso.orb = self.vso.orb[0:1]
        # self.vso.numorb = 1
        # self.vso = VnlBasis({"symbol":self.symbol, "path":self.path}, 'VnlSO')
        if self.symbol is None or self.Z is None:
            data, fmt = load_dcal(self.path)
            for snam, inam in zip(["Z", "symbol"], ["N", "symbol"]):
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
                        "Couldn't find parameter 'atom.%s' in file %s."
                        % (inam, self.path)
                    )

    def _set_vlc(self):
        if isinstance(self.vlc, dict) and "path" in self.vlc.keys():
            self.vlc = RadFunc(**self.vlc)
        else:
            self.vlc = RadFunc(path=self.path, varname="Vlocal")

    def _set_rpc(self):
        if isinstance(self.rpc, dict) and "path" in self.rpc.keys():
            self.rpc = RadFunc(**self.rpc)
        else:
            self.rpc = RadFunc(path=self.path, varname="Rpc")

    def _set_vnl(self):
        if isinstance(self.vnl, dict) and set(["path", "varname", "symbol"]).issubset(
            set(self.vnl.keys())
        ):
            self.vnl = VnlBasis(**self.vnl)
        else:
            self.vnl = VnlBasis(path=self.path, varname="Vnl", symbol=self.symbol)

    def _init_vso(self):
        if isinstance(self.vso, dict) and set(["path", "varname", "symbol"]).issubset(
            set(self.vso.keys())
        ):
            self.vso = VnlBasis(**self.vso)
        else:
            self.vso = VnlBasis(path=self.path, varname="VnlSO", symbol=self.symbol)

    def _rm_vso(self):
        self.vso = None

    def to_vacuum(self):
        self.path = ""
        self.symbol += "_Va"
        self.Z = 0
        self.vlc.zero_out()
        self.rpc.zero_out()
        self.vnl.to_vacuum()
        self._rm_vso()
