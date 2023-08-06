# -*- coding: utf-8 -*-
"""This module defines the ``Kpoint`` class."""

from attr import field
from rescupy.cell import Cell
from rescupy.data.kpoint import (
    defaultSymmetryKPoints,
    kValue2kSymbol,
    kSymbol2kValue,
    is_row_vector,
)
from nptyping import NDArray
from rescupy.base import Base
from rescupy.utils import to_quantity, Quantity, ureg
import attr
import numpy as np


def to_quantity_bvec(x):
    shape = (3, 3)
    return to_quantity(x, "1 / angstrom", allow_none=True, shape=shape)
    # if x is None or isinstance(x, Quantity):
    #     return x
    # if isinstance(x, tuple):
    #     unit = x[1]
    #     x = np.array(x[0], dtype=float).reshape(shape, order="F")
    #     return to_quantity(x, unit)
    # else:
    #     x = np.array(x, dtype=float).reshape(shape, order="F")
    #     return to_quantity(x, "1 / angstrom")


@attr.s
class Kpoint(Base):
    """``Kpoint`` class.

    The ``Kpoint`` class defines parameters related to k-sampling.

    Attributes:
        bvec (2D array):
            Array of row-reciprocal-vectors.
        special_points (list of strings):
            special_points specifies k-points (typically high-symmetry k-points)
            defining the line which samples the Brillouin zone. A line going through
            all such k-points is generated and discretized using ``system.kpoint.
            grid`` points or a resolution of 0.015 $\mathring{\text{A}}^{-1}$ is
            used. This keyword can be a list of labels, ``['L','G','X']``, a list of
            lists (or array), ``[[.5, .5, .5], [.0, .0, .0], [.5, .0, .5]]``, or a
            mix of the two.

            Examples::

                kpoint.special_points = ['L','G','X']

        gamma_centered (bool):
            gamma_centered equal True induces a shift of the Monkhorst-Pack mesh such
            that a point lies at $\Gamma$.

            Examples::

                kpoint.gamma_centered = True

        grid (1D array):
            ``grid`` is a size-3 array giving the number of points along each direction
            in the Brillouin zone discretization. The `Monkhorst-Pack scheme <https://
            doi.org/10.1103/PhysRevB.13.5188>`_ is used . In linear band structure
            calculations, ``grid`` is a size-1 array giving the total number of
            points. The points are distributed as uniformly as possible.
            Note that a line such as ["L", "G", "X", "W"]
            is always decomposed into segments [["L", "G"], ["G", "X"], ["X", "W"]]. Since
            "G" and "X" are duplicated, if grid is set to 20, internal quantities like
            ``kpoint.fractional_coordinates`` will have size 22 in the k-point axis.
            Examples::

                kpoint.grid = [4 4 4]

        fractional_coordinates (2D array):
            fractional_coordinates contains row-vectors giving the fractional
            coordinates of the k-points. ``fractional_coordinates`` has precedence
            over Monkhors-Pack mesh generation and linear k-point sampling.

            Examples::

                kpoint.fractional_coordinates = [0.25,0.25,0.25,0.25,0.25,-0.25]

        kwght (1D array):
            weight of each k-point.

            Examples::

                kpoint.kwght = [6;2]

        type (string):
            type equal "full" will sample the entire Brillouin zone (most
            calculations use this, e.g. self-consistent); ``type`` equal "line" will
            sample high-symmetry edges of the Brillouin zone (as in linear band
            structure calculations).

            Examples::

                kpoint.type = "full"
    """

    bvec: Quantity = field(
        default=None,
        converter=attr.converters.optional(to_quantity_bvec),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    special_points = attr.ib(default=None)
    gamma_centered: bool = attr.ib(
        default=False,
        validator=attr.validators.instance_of(bool),
    )
    grid = attr.ib(default=None)
    fractional_coordinates = attr.ib(default=None)
    kwght = attr.ib(default=None)
    shift: NDArray = attr.ib(
        default=[0.0, 0.0, 0.0],
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    resolution: Quantity = attr.ib(
        default=0.35 / ureg.angstrom,
        converter=lambda x: to_quantity(x, "1 / angstrom"),
        validator=attr.validators.instance_of(Quantity),
    )
    type: str = attr.ib(
        default="full",
        validator=attr.validators.instance_of(str),
    )
    bvec_shape: tuple = attr.ib(default=(3, 3))
    fractional_coordinates_shape: tuple = attr.ib(default=(-1, 3))

    def __attrs_post_init__(self):
        self._reshape()

    def _get_bz_dist(self, kpt0, kpt1):
        dist = np.matmul(kpt1 - kpt0, self.bvec)
        return np.linalg.norm(dist.m) * dist.u

    def _get_bz_segment(self, kpt0, kpt1, n=None, res=None):
        if n is None and res is None:
            raise Exception("n or resolution must be specified.")
        if n is not None:
            kpts = np.zeros((n, 3))
            kpts[:, 0] = np.linspace(kpt0[0], kpt1[0], n)
            kpts[:, 1] = np.linspace(kpt0[1], kpt1[1], n)
            kpts[:, 2] = np.linspace(kpt0[2], kpt1[2], n)
        else:
            dist = self._get_bz_dist(kpt0, kpt1)
            n = np.ceil(dist / res).to("dimensionless")
            n = int(n.m)
            kpts = self._get_bz_segment(kpt0, kpt1, n=n)
        return kpts

    def _get_cell(self):
        avec = 2.0 * np.pi * np.linalg.inv(self.bvec.m).T / self.bvec.u
        return Cell(avec=avec, grid=[1, 1, 1])

    def get_grid(self):
        if self.type != "full":
            raise Exception('Missing implementation type != "full"')
        if self.grid is None:
            ls = self.get_lengths()
            grid = np.round(ls / self.resolution)
            grid.ito("dimensionless")
            grid = grid.m.astype(int)
            self.grid = np.maximum(grid, 1)
        return self.grid

    def get_cartesian_coordinates(self):
        """Computes the k-points Cartesian coordinates."""
        return np.matmul(self.get_fractional_coordinates(), self.bvec)

    def get_fractional_coordinates(self):
        """Computes the k-points Cartesian coordinates."""
        self._reshape()
        return self.fractional_coordinates

    def get_special_points_labels(self):
        """Computes the k-points Cartesian coordinates."""
        fractional_coordinates = self.get_fractional_coordinates()[
            self.special_points, :
        ]
        return self.kpt_2_label(self._get_cell(), fractional_coordinates)

    def get_kpoint_num(self):
        """Returns the number of k-points."""
        self._reshape()
        if self.fractional_coordinates is not None:
            nkpt = self.fractional_coordinates.shape[0]
        elif self.grid is not None:
            nkpt = np.prod(self.grid)
        else:
            raise Exception("Invalid type for attribute fractional_coordinates.")
        return nkpt

    def get_lengths(self):
        cell = Cell(avec=self.bvec, resolution=1.0 * self.bvec.u)
        return cell.get_lengths()

    def kpt_2_label(self, cell, kpts):
        if cell.bravais is None:
            cell.bravais = cell.get_bravais_lattice()
        bravais = cell.bravais
        avec = cell.avec.m
        avecStd = cell.get_standard_lattice()
        pmat = np.matmul(avecStd, np.linalg.inv(avec)).transpose()
        labels = []
        for i in range(0, len(kpts)):
            k = np.matmul(kpts[i], pmat)
            labels.append(kValue2kSymbol(bravais, avecStd, k))
        return labels

    # def refine(self, target=None):
    #     res0 = self.resolution
    #     grd0 = np.array(self.grid)
    #     grd = grd0
    #     if target is None:
    #         target = grd0
    #     while np.all(target >= grd):
    #         self.resolution *= 0.99
    #         self.grid = None
    #         grd = self.get_grid()
    #     self.set_fractional_coordinates(fractional_coordinates=None)

    def set_bvec(self, cell):
        """Sets the reciprocal lattice data from a ``Cell`` object.

        Args:
            cell:
                A ``Cell`` object.
        """
        self.bvec = cell.reciprocal()
        # update grid/res
        if self.type == "full":
            if self.grid is None:
                self.get_grid()
            if self.resolution is None:
                self.resolution = np.average(self.get_lengths() / self.grid)

    def set_cartesian_coordinates(self, cartesian_coordinates, kwght=None):
        """Sets ``fractional_coordinates`` given Cartesian coordinates and optionally the k-point weights."""
        if self.bvec is None:
            raise Exception("bvec attribute is undefined.")
        cartesian_coordinates = to_quantity(cartesian_coordinates, allow_none=False)
        fractional_coordinates = (
            cartesian_coordinates @ np.linalg.inv(self.bvec.m)
        ) / self.bvec.u
        fractional_coordinates = fractional_coordinates.to("dimensionless").m
        self.set_fractional_coordinates(
            fractional_coordinates=fractional_coordinates, kwght=kwght
        )

    def set_fractional_coordinates(self, fractional_coordinates=None, kwght=None):
        """Sets ``fractional_coordinates`` given fractional coordinates and optionally the k-point weights."""
        self.fractional_coordinates = fractional_coordinates
        if self.fractional_coordinates is None:
            if self.type == "full":
                self.get_grid()
                self.set_grid(self.grid, shift=self.shift)
            elif self.type == "line":
                self.set_kpoint_path()
            else:
                raise Exception(f"Invalid value {self.type} for attribute type.")
        else:
            if np.prod(self.grid) != self.get_kpoint_num():
                self.grid = [self.get_kpoint_num()]
        self.set_kwght(kwght)

    def set_kwght(self, kwght=None):
        """Sets the k-point weights."""
        self.kwght = kwght
        if self.kwght is None:
            nkpt = self.get_kpoint_num()
            self.kwght = np.ones(nkpt) / nkpt
        if self.fractional_coordinates is not None:
            if len(self.kwght) != self.get_kpoint_num():
                raise Exception(
                    "kwght and fractional_coordinates have incompatible dimensions."
                )
        if self.kwght is not None:
            if not np.isclose(1.0, np.sum(self.kwght)):
                raise Exception("kwght does not sum to 1.")

    def set_kpoint_path(self, special_points=None, grid=None):
        """Compute k-point coordinates along the line specified in ``Kpoint`` object."""
        if self.type != "line":
            self.__init__(bvec=self.bvec, type="line")
        self.grid = grid
        self.special_points = special_points
        cell = self._get_cell()
        bravais = cell.get_bravais_lattice()
        avecStd = cell.get_standard_lattice()
        avec = cell.avec.m
        pmat = np.matmul(avec, np.linalg.inv(avecStd)).transpose()
        # define checkpoints
        if self.special_points is None:
            special_points = defaultSymmetryKPoints(bravais, avecStd)
        else:
            special_points = self.special_points
        # get line segments
        special_points = split_bz_lines(special_points)
        # convert to numerical format
        for i in range(0, len(special_points)):
            kpt0 = kSymbol2kValue(
                bravais, avecStd, special_points[i][0]
            )  # checkPoint returned as is if not a str
            if isinstance(special_points[i][0], str):
                kpt0 = np.matmul(kpt0, pmat)
            kpt1 = kSymbol2kValue(
                bravais, avecStd, special_points[i][1]
            )  # checkPoint returned as is if not a str
            if isinstance(special_points[i][1], str):
                kpt1 = np.matmul(kpt1, pmat)
            special_points[i] = [kpt0, kpt1]
        # get total length
        klen = 0.0
        for i in range(0, len(special_points)):
            kpt0 = special_points[i][0]
            kpt1 = special_points[i][1]
            klen += self._get_bz_dist(kpt0, kpt1)
        # get resolution
        if self.grid is not None:
            res = klen / self.grid
        else:
            res = 0.025 / ureg.angstrom  # ang^-1
        # interpolate between checkpoints to obtain segments
        fractional_coordinates = np.zeros((0, 3))
        count = 0
        checkIndex = np.zeros(2 * len(special_points)).astype(int)
        for i in range(0, len(special_points)):
            kpt0 = special_points[i][0]
            kpt1 = special_points[i][1]
            ktmp = self._get_bz_segment(kpt0, kpt1, res=res)
            fractional_coordinates = np.concatenate(
                (fractional_coordinates, ktmp), axis=0
            )
            checkIndex[2 * i] = count
            checkIndex[2 * i + 1] = count + ktmp.shape[0] - 1
            count = checkIndex[2 * i + 1] + 1
        self.fractional_coordinates = fractional_coordinates
        nkpt = fractional_coordinates.shape[0]
        self.set_kwght(kwght=None)
        self.grid = [nkpt]
        self.special_points = checkIndex

    def set_grid(self, grid, shift=None, gamma_centered=None):
        """Defines the k-points given a grid size or shape.

        If the k-point object is of type "full", then the ``grid`` argument is expected to
        be a 3-element array. The k-point coordinates and weights are reinitialized accordingly.

        If the k-point object is of type "line", then the ``grid`` argument is expected to
        be an integer. The k-point coordinates are regenerate along a path going around the Brillouin zone.

        Args:
            grid (1D array or int):
                Shape or size of the k-point grid or path.
        """
        if self.type == "full":
            if grid is not None and len(grid) != 3:
                raise ValueError(
                    "grid should be a 3-element vector for a Kpoint object of type 'full'."
                )
            if shift is not None and len(shift) != 3:
                raise ValueError(
                    "shift should be a 3-element vector for a Kpoint object of type 'full'."
                )
            self.grid = np.array(grid)
            self.resolution = np.average(self.get_lengths() / self.grid)
            fractional_coordinates = monkhorst_pack(self.grid)
            if gamma_centered is not None:
                self.gamma_centered = gamma_centered
            elif shift is not None:
                self.gamma_centered = False
                self.shift = np.array(shift)
            if isinstance(self.gamma_centered, bool):
                if self.gamma_centered:
                    self.shift = np.mod(self.grid + 1, 2) / 2.0
            self.fractional_coordinates = fractional_coordinates + (
                self.shift / self.grid
            )
            self.set_kwght(kwght=None)
        elif self.type == "line":
            if grid is not None and len(grid) != 1:
                raise ValueError(
                    "Grid should be a 1-element vector for a Kpoint object of type 'line'."
                )
            self.grid = np.array(grid)
            self.set_kpoint_path()
        else:
            raise ValueError("Type attribute must be set to full.")

    def set_type(self, type):
        """Sets the type of the k-point object.

        The type can be either "full", for a self-consistent or DOS calculation for instance,
        or "line" for a band structure calculation.

        Args:
            type (string):
                Type of the k-point object.
        """
        reset = self.type != type
        self.type = type
        if reset:
            self.__init__(bvec=self.bvec, type=self.type)
            self.set_grid(self.grid, shift=self.shift)


####################
# module functions #
####################


def monkhorst_pack(grid):
    kx = monkhorst_pack_nodes(grid[0])
    ky = monkhorst_pack_nodes(grid[1])
    kz = monkhorst_pack_nodes(grid[2])
    kx, ky, kz = np.meshgrid(kx, ky, kz, indexing="ij")
    fractional_coordinates = np.hstack(
        (
            kx.reshape((-1, 1), order="F"),
            ky.reshape((-1, 1), order="F"),
            kz.reshape((-1, 1), order="F"),
        )
    )
    return fractional_coordinates


def monkhorst_pack_nodes(n):
    k = np.linspace(0.0, 1.0, num=n + 1)[0:n]
    if n % 2 == 0:
        k += 0.5 / n
    k -= np.round(k)
    return k


def split_bz_lines(special_points):
    if is_row_vector(special_points[0], len=3):
        return split_bz_lines([special_points])
    if not isinstance(special_points[0], list):
        return split_bz_lines([special_points])
    newlist = []
    for i in range(0, len(special_points)):
        newlist = newlist + split_list(special_points[i])
    return newlist


def split_list(alist):
    newlist = []
    for i in range(0, len(alist) - 1):
        newlist.append(alist[i : i + 2])
    return newlist


def increase_ksampling(k, kref):
    k0 = k
    kw = np.array(kref).astype(float)
    while all([a >= b for a, b in zip(k0, k)]):
        kw *= 1.1
        k = np.round(kw).astype(int).tolist()
    return k
