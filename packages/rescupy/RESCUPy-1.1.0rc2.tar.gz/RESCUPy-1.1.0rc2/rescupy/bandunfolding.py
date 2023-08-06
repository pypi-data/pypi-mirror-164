# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""


from nptyping import NDArray
from rescupy.bandstructure import plot_bs_driver
from rescupy.base import Base
from rescupy.cell import Cell
from rescupy.energy import Energy
from rescupy.io.calculators import solve_generic
from rescupy.kpoint import Kpoint
from rescupy.solver import Solver
from rescupy.system import System
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
import attr
import numpy as np


@attr.s
class BandUnfoldData(Base):
    """``BandUnfolding`` data class.

    Attributes:
        primitive_avec:
           Lattice vectors of the primitive cell.
        spectral_function:
           Spectral function of the unfolded band structure (i.e. weights in [0, 1] for each Bloch state).
    """

    primitive_cell = attr.ib(
        default=None,
    )
    kpoint: Kpoint = attr.ib(
        factory=Kpoint,
        converter=lambda d: dict_converter(d, Kpoint),
        validator=attr.validators.instance_of(Kpoint),
    )
    spectral_function: NDArray = attr.ib(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
    )
    spectral_function_shape: tuple = attr.ib(default=None)


@attr.s
class BandUnfolding(Base):
    """``BandUnfolding`` class.

    Examples::

        from rescupy import BandUnfolding as BU
        import numpy as np
        calc = BU.from_totalenergy("nano_scf_out.json")
        calc.set_primitive_cell(avec=3.74/2.*(np.ones((3,3)) - np.eye(3)))
        calc.set_kpoint_path(special_points=["L","G","X"])
        calc.solve()

    Attributes:
        system:
           Object containing system related parameters.
        unfold:
           Object containing the unfolding data and parameters (primitive lattice vectors, spectral function, etc.).
        energy:
           Object containing the total energy and its derivatives (force, stress, etc.).
        solver:
           Object containing solver related parameters.
    """

    # input is dictionary with default constructor
    system: System = attr.ib(
        converter=lambda d: dict_converter(d, System),
        validator=attr.validators.instance_of(System),
    )

    # optional
    unfold: BandUnfoldData = attr.ib(
        factory=BandUnfoldData,
        converter=lambda d: dict_converter(d, BandUnfoldData),
        validator=attr.validators.instance_of(BandUnfoldData),
    )
    energy: Energy = attr.ib(
        factory=Energy,
        converter=lambda d: dict_converter(d, Energy),
        validator=attr.validators.instance_of(Energy),
    )
    solver: Solver = attr.ib(
        factory=Solver,
        converter=lambda d: dict_converter(d, Solver),
        validator=attr.validators.instance_of(Solver),
    )

    def __attrs_post_init__(self):
        self._reshape()
        # self.unfold.kpoint = self.system.kpoint
        # self.unfold.kpoint.set_bvec(self.unfold.primitive_cell)
        # self.unfold.kpoint.set_fractional_coordinates(self.unfold.kpoint.fractional_coordinates)
        # fc = np.self.kpoint.get_cartesian_coordinates()
        # fc = np.matmul(fc, np.linalg.inv(self.unfold.kpoint.bvec))
        # self.unfold.kpoint.set_fractional_coordinates(fc)

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        sys = totalenergy.system.copy()
        # sys.set_kpoint_path()
        calc = cls(sys, solver=totalenergy.solver, **kwargs)
        calc.energy = totalenergy.energy.copy()
        return calc

    def plot_bs(self, filename=None, show=True):
        """Generates a plot of the band structure.

        Args:
            filename (str, optional):
                If not None, then the figure is saved to filename.
            show (bool, optional):
                If True block and show figure.
                If False, do not show figure.

        Returns:
            fig (:obj:`matplotlib.figure.Figure`):
                A figure handle.
        """
        fig = plot_bs_driver(
            self.energy,
            self.system.hamiltonian,
            self.unfold.kpoint,
            filename=filename,
            show=show,
        )

    def plot_spectral_function(self, filename=None, show=True):
        """Generates a plot of the spectral function.

        Args:
            filename (str, optional):
                If not None, then the figure is saved to filename.
            show (bool, optional):
                If True block and show figure.
                If False, do not show figure.

        Returns:
            fig (:obj:`matplotlib.figure.Figure`):
                A figure handle.
        """
        fig = plot_bs_driver(
            self.energy,
            self.system.hamiltonian,
            self.unfold.kpoint,
            weights=self.unfold.spectral_function,
            filename=filename,
            show=show,
        )

    def solve(self, input="nano_bsu_in", output="nano_bsu_out"):
        """Performs a non.self-consistent calculation calling ``rescuplus_bsu``.

        Args:
            filename (str):
                The object is saved to an input file ``filename`` which is read by ``rescuplus_bsu``.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        self._check_bsu()
        output = solve_generic(self, "bsu", input, output)
        self._update(output + ".json")

    def set_kpoint_path(self, special_points=None, grid=None):
        """Sets the kpoint path for the band structure calculation.

        Args:
            special_points (list):
                List of high-symmetry point labels or fractional coordinates. For example,
                ["L", "G", "X", "W"].

            grid (int):
                Number of points along the k-point path. Note that a line ["L", "G", "X", "W"]
                is always decomposed into segments [["L", "G"], ["G", "X"], ["X", "W"]]. Since
                "G" and "X" are duplicated, if grid is set to 20, internal quantities like
                ``kpoint.fractional_coordinates`` will have size 22 in the k-point axis.
        """
        self.unfold.kpoint.__init__(
            type="line", special_points=special_points, grid=grid
        )
        self.unfold.kpoint.set_bvec(self.unfold.primitive_cell)
        self.unfold.kpoint.set_kpoint_path(special_points=special_points, grid=grid)
        kcar = self.unfold.kpoint.get_cartesian_coordinates()
        self.system.kpoint.set_cartesian_coordinates(kcar)
        # reset (-1,nk,-1) quantities since shape becomes incorrect
        self.system.pop.__init__()

    def set_primitive_cell(self, avec):
        avecs = self.system.cell.avec
        err = np.linalg.solve(avec.T, avecs.T)
        if not np.allclose(np.round(err), err):
            raise Exception(
                "The target cell is not commensurate with the supercell, please choose a commensurate target cell."
            )
        res = self.system.cell.resolution
        self.unfold.primitive_cell = Cell(avec=avec, resolution=res)
        self.set_kpoint_path()

    def _check_bsu(self):
        return
