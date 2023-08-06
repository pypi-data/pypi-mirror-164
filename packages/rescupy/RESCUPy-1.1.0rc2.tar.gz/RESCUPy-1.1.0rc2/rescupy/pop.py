# -*- coding: utf-8 -*-
"""This module defines the ``Pop`` class."""

from attr import field
from nptyping import NDArray
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.utils import is_array_like
import attr
import numpy as np


def validate_type(type):
    assert isinstance(type, str)
    if type not in ["fx", "fd", "ga", "mp", "tm"]:
        raise Exception("Invalid pop.type value: " + type + ".")


def long2short(long):
    if long == "fixed":
        return "fx"
    if long == "fermi-dirac":
        return "fd"
    if long == "gauss":
        return "ga"
    if long == "methfessel-paxton":
        return "mp"
    if long == "tetrahedron":
        return "tm"
    return long


@attr.s
class Pop(Base):
    """``Pop`` class.

    The ``Pop`` class (for population) stores data and parameters related to the Kohn-Sham occupancies.

    Attributes:
        blochl:
            If blochl is True, then Blochl's correction scheme is applied to the `tetrahedron method <https://doi.org/10.1103/PhysRevB.49.16223>`_.
            It is not variational, and hence should not be used in force calculations.

            Examples::

                pop.blochl = 2

        mpn:
            Order of the Methfessel-Paxton smearing.

            Examples::

                pop.mpn = 2
        occ (3D array):
            Occupancies for every Kohn-Sham states. If this attribute is set together with type = "fx",
            then the occupancies are not updated during a ground state calculation.
            Instead, the occupancies are kept fixed to the values given in occ.
        sigma:
            Smearing parameter. If type is "fd" (Fermi-Dirac), then sigma corresponds to kBT.
            If type is "ga" or "mp" (Gaussian or Methfessel-Paxton),
            then sigma corresponds to the half-width of the Gaussian envelope.

            Examples::

                pop.sigma = 0.1
        type:
            Sets the occupation scheme. The allowed values are for:

                * "fd": Fermi-Dirac smearing.
                * "fx": Fixed occupancies.
                * "ga": `Gaussian smearing <https://books.google.ca/books?id=eWQEGwAACAAJ)>`_.
                * "mp": `Methfessel-Paxton smearing <https://doi.org/10.1103/PhysRevB.40.3616>`_.
                * "tm": `tetrahedron method <https://doi.org/10.1103/PhysRevB.49.16223>`_.

            Treating the eigenvalues constituting the eigenspectrum as delta functions generally leads to adverse effects (e.g. bad k-sampling convergence).
            The contribution of each eigenvalue to the band structure can be smoothed by a combination of smearing and interpolation.
            The Fermi-Dirac method populates the states according to the Fermi-Dirac distribution.
            The temperature or smearing width can be set by kpoint.sigma.
            Individual eigenvalues are broaden by adopting the shape of the derivative of the Fermi-Dirac distribution.
            The Gaussian method smears the eigenvalues' DOS using Gaussian functions.
            The states occupation numbers are then attributed using a complementary error function.
            The Methfessel-Paxton combines Hermite polynomials with Gaussian functions to smear the energy levels.
            The tetrahedron method linearly interpolates the bands between the calculated eigenvalues.
            The obtained piecewise linear bands are then treated analytically.

            Examples::

                pop.type = "gauss"
        bias (float):
        voltage (float):
        temperature (float):
        nCircle (int): number of sampling points on the circular part of energy contour.
        nPlat (int): number of sampling points on the flat part of energy contour.
        nPole (int): number of Fermi poles. Used for contour Green function integration.
        nReal (int): number of energy sampling points on real axis. used in nonequilibrium two-probe calculation.
        contour_type (str): "single" (default) or "double". contour type used in nonequilibrium two-probe calculation.
    """

    blochl: bool = attr.ib(
        default=False,
        validator=attr.validators.instance_of(bool),
    )
    mpn: float = attr.ib(
        default=1,
        converter=float,
        validator=attr.validators.instance_of(float),
    )
    occ: NDArray = attr.ib(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    occ_shape: list = attr.ib(
        default=None,
        converter=attr.converters.optional(list),
        validator=attr.validators.optional(attr.validators.instance_of(list)),
    )
    sigma: Quantity = field(
        default=0.1 * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    type: str = attr.ib(
        default="ga",
        validator=attr.validators.instance_of(str),
    )
    bias: Quantity = field(
        default=0.0 * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    voltage: Quantity = field(
        default=0.0 * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    nCircle: int = attr.ib(
        default=20, converter=int, validator=attr.validators.instance_of(int)
    )
    nPlat: int = attr.ib(
        default=10, converter=int, validator=attr.validators.instance_of(int)
    )
    nPole: int = attr.ib(
        default=10, converter=int, validator=attr.validators.instance_of(int)
    )
    nReal: int = attr.ib(
        default=20, converter=int, validator=attr.validators.instance_of(int)
    )
    contour_type: str = attr.ib(
        default="single",
        validator=attr.validators.instance_of(str),
    )
    occ_shape: tuple = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.type = long2short(self.type)
        validate_type(self.type)
        if self.type == "fx":
            self.sigma = 0.0 * ureg.eV
        if not self.type == "mp":
            self.mpn = 0

    def set_sigma(self, sigma):
        """Sets the smearing parameter."""
        self.sigma = to_quantity(sigma, "eV")

    def set_type(self, type):
        """Sets the population scheme."""
        self.type = long2short(type)
        validate_type(self.type)
        self.__attrs_post_init__()

    def _reshape(self):
        if is_array_like(self.occ):
            self.occ = np.reshape(self.occ, self.occ_shape, order="F")
