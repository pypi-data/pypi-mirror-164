# -*- coding: utf-8 -*-
"""
Created on 2020-05-12

@author: Vincent Michaud-Rioux
"""

from nptyping import NDArray
from numpy.polynomial.legendre import leggauss
from rescupy.base import Base
from rescupy.utils import load_dcal, load_dcal_parameter, load_dcal_var
from scipy.special import spherical_jn as jn
import attr
import numpy as np


# TODO: what to do with vfld
@attr.s(auto_detect=True, eq=False)
class RadFunc(Base):
    """
    radFunc class.

    Attributes:

    """

    path: str = attr.ib(validator=attr.validators.instance_of(str))
    varname: str = attr.ib(validator=attr.validators.instance_of(str))
    ecut: float = attr.ib(
        default=36.75, converter=float, validator=attr.validators.instance_of(float)
    )
    index: int = attr.ib(
        default=0,
        converter=int,
        validator=attr.validators.instance_of(int),
    )
    rgrid: NDArray = attr.ib(
        factory=lambda: np.zeros((0)),
        converter=attr.converters.optional(np.array),
        # validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    rwght: NDArray = attr.ib(
        factory=lambda: np.zeros((0)),
        converter=attr.converters.optional(np.array),
        # validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    rvals: NDArray = attr.ib(
        factory=lambda: np.zeros((0)),
        converter=attr.converters.optional(np.array),
        # validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    qgrid: NDArray = attr.ib(
        factory=lambda: np.zeros((0)),
        converter=attr.converters.optional(np.array),
        # validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    qwght: NDArray = attr.ib(
        factory=lambda: np.zeros((0)),
        converter=attr.converters.optional(np.array),
        # validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    qvals: NDArray = attr.ib(
        factory=lambda: np.zeros((0)),
        converter=attr.converters.optional(np.array),
        # validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )

    def __attrs_post_init__(self):
        sizes = [
            getattr(self, a).size
            for a in ["rgrid", "rwght", "rvals", "qgrid", "qwght", "qvals"]
        ]
        if np.alltrue(np.array(sizes) > 0):
            return
        varname = self.varname
        if varname in ["Vna", "Vlocal", "Vnl"]:
            vfld = "vvData"
        if varname in ["VnlSO"]:
            vfld = "vsoData"
        if varname in ["Rna", "Rlocal", "Rpc"]:
            vfld = "rhoData"
        if varname in ["OrbitalSet"]:
            vfld = "frData"

        if varname in ["Vna", "Vlocal", "Rna", "Rlocal", "Rpc"]:
            i = None
        else:
            i = self.index

        data, fmt = load_dcal(self.path, varname)

        if data is None or len(data) == 0:
            self.rgrid = np.linspace(0, 5, 11)
            self.rwght = np.zeros((11))
            self.rvals = np.zeros((11))
            self.qgrid = np.linspace(0, 5, 11)
            self.qwght = np.zeros((11))
            self.qvals = np.zeros((11))
            self.ecut = max(self.qgrid)
            return

        self.rgrid = load_dcal_var(data, "rrData", fmt, i)
        self.rwght = load_dcal_var(data, "drData", fmt, i)
        self.rvals = load_dcal_var(data, vfld, fmt, i)

        try:
            self.qgrid = load_dcal_var(data, "qqData", fmt, i)
            self.qwght = load_dcal_var(data, "qwData", fmt, i)
            self.qvals = load_dcal_var(data, "fqData", fmt, i)
        except:
            # self.qgrid, self.qwght = leggauss(int(ecut*10))
            # self.qgrid = (0 * (1 - self.qgrid) + ecut * (1 + self.qgrid)) / 2
            nq = int(self.ecut * 30)
            if type(self) is RadFunc:
                l = 0
            else:
                l = self.l

            self.qgrid = np.linspace(0, self.ecut, num=nq + 1)
            self.qwght = np.ones((nq + 1)) / nq * self.ecut
            self.qwght[0] *= 0.5
            self.qwght[-1] *= 0.5
            self.qvals = radialFT(self.rgrid, self.rwght, self.rvals, self.qgrid, l)
        self.ecut = max(self.qgrid)

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.path, self.varname, self.ecut, self.index,) == (
            other.path,
            other.varname,
            other.ecut,
            other.index,
        ) and (
            np.allclose(self.rgrid, other.rgrid)
            and np.allclose(self.rwght, other.rwght)
            and np.allclose(self.rvals, other.rvals)
            and np.allclose(self.qgrid, other.qgrid)
            and np.allclose(self.qwght, other.qwght)
            and np.allclose(self.qvals, other.qvals)
        )

    def zero_out(self):
        self.rvals[:] = 0.0
        self.qvals[:] = 0.0


@attr.s
class Orb(RadFunc):
    l: int = attr.ib(default=None)
    n: int = attr.ib(default=-1)

    def __attrs_post_init__(self):
        if self.l is None:
            i = self.index
            data, fmt = load_dcal(self.path, self.varname)
            try:
                tmp = load_dcal_parameter(data, "L", fmt, i)
                self.l = int(tmp)
            except ValueError:
                raise Exception(
                    "Couldn't find parameter 'l' in file " + self.path + "."
                )
            try:
                tmp = load_dcal_parameter(data, "N", fmt, i)
                self.n = int(tmp)
            except:
                pass
        super().__attrs_post_init__()


@attr.s
class KbOrb(Orb):
    j: int = attr.ib(default=None)
    energy = attr.ib(default=None)
    kbcos = attr.ib(default=None)
    kbnrg = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.kbnrg is None:
            i = self.index
            data, fmt = load_dcal(self.path, self.varname)
            try:
                tmp = load_dcal_parameter(data, "halfLxEkbso", fmt, i)
                if tmp is None:
                    tmp = load_dcal_parameter(data, "KBenergy", fmt, i)
                else:
                    j = load_dcal_parameter(data, "J", fmt, i)
                    self.j = int(j)
                self.kbnrg = float(tmp)
            except ValueError:
                raise Exception(
                    "Couldn't find parameter 'KBenergy' in file " + self.path + "."
                )
        super().__attrs_post_init__()


@attr.s
class AoOrb(Orb):
    zeta = attr.ib(default=-1)
    energy = attr.ib(default=None)
    coulombU = attr.ib(default=None)
    exchangeJ = attr.ib(default=None)
    population = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.population is None:
            i = self.index
            data, fmt = load_dcal(self.path, self.varname)
            try:
                tmp = load_dcal_parameter(data, "Population", fmt, i)
                self.population = float(tmp)
            except ValueError:
                raise Exception(
                    "Couldn't find parameter 'Population' in file " + self.path + "."
                )

        super().__attrs_post_init__()

    def to_vacuum(self):
        self.path = ""
        self.energy = 0.0
        self.coulombU = 0.0
        self.exchangeJ = 0.0
        self.population = 0.0


def radialFT(r, fr, dr, q, l=0):
    """
    Description
    Computes the radial Fourier transform.

    Args:
        r (1D array):
           Radial grid.
        fr (1D array):
           Radial values.
        dr (1D array):
           Radial integration weights.
        q (1D array):
           Fourier grid.
        l (1D array):
           Principal angular momentum.

    Returns:
        fq (1D array):
            Radial Fourier transform.
    """
    if l < 0:
        l = 0
    fq = r.reshape((-1, 1)) * q.reshape((1, -1))
    fq = jn(l, fq)
    fq = r.reshape((-1, 1)) ** 2 * fr.reshape((-1, 1)) * fq
    fq = np.sqrt(2 / np.pi) * np.matmul(dr.reshape((1, -1)), fq).flatten()
    return fq
    # reference MATLAB code
    # fq = bsxfun(@times,r(:),q(:)');
    # fq = bsxfun(@times,r(:).^2.*fr(:),calcSphericalBessel(l,fq));
    # fq = sqrt(2/pi)*dr*fq;
