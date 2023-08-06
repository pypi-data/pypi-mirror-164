# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from attr import field
from rescupy.base import Base, Quantity, to_quantity
from rescupy.energy import Energy
from rescupy.io.calculators import solve_generic
from rescupy.solver import Solver
from rescupy.system import System
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
import attr
import numpy as np


@attr.s
class LDOSData(Base):
    """``LocalDOS`` data class.

    Attributes:
        energies:
           Energies at which the LDOS is calculated.
    """

    energies: Quantity = field(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV", shape=(-1))),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )

    def set_energies(self, energies):
        self.energies = to_quantity(energies, "eV", shape=(-1))


@attr.s
class LocalDOS(Base):
    """``LocalDOS`` class.

    Examples::

        from rescupy import LocalDOS
        import numpy as np
        calc = LocalDOS.from_totalenergy("nano_scf_out.json")
        calc.system.kpoint.set_grid([45,45,1])
        calc.ldos.energies = [calc.energy.efermi - 0.001]
        calc.solve()

    Attributes:
        system:
           Object containing system related parameters.
        ldos:
           Object containing the local density of states data.
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
    ldos: LDOSData = attr.ib(
        factory=LDOSData,
        converter=lambda d: dict_converter(d, LDOSData),
        validator=attr.validators.instance_of(LDOSData),
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
        self._validate()
        self._reshape()

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        sys = totalenergy.system.copy()
        calc = cls(sys, solver=totalenergy.solver, **kwargs)
        calc.energy = totalenergy.energy.copy()
        return calc

    def solve(self, input="nano_ldos_in", output="nano_ldos_out"):
        """Performs a non.self-consistent calculation calling ``rescuplus_ldos``.

        Args:
            filename (str):
                The object is saved to an input file ``filename`` which is read by ``rescuplus_ldos``.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        self._validate()
        self._check_ldos()
        output = solve_generic(self, "ldos", input, output)
        self._update(output + ".json")

    def _check_ldos(self):
        if self.system.kpoint.type != "full":
            raise ValueError(
                "system.kpoint.type must be set to full for an ldos calculation."
            )

    def _validate(self):
        if self.solver.mpidist.kptprc is not None:
            if self.solver.mpidist.kptprc > 1:
                # raise ValueError("solver.mpidist.kptprc must be None or 1 in an ldos calculation.")
                print(
                    "Warning: solver.mpidist.kptprc must be None or 1 in an ldos calculation."
                )
                self.solver.mpidist.kptprc = 1

    # def plot_ldos(self, value, index=0, filename=None, show=True):
    #     """Generates a plot of the band structure.

    #     Args:
    #         filename (str, optional):
    #             If not None, then the figure is saved to filename.
    #         show (bool, optional):
    #             If True block and show figure.
    #             If False, do not show figure.

    #     Returns:
    #         fig (:obj:`matplotlib.figure.Figure`):
    #             A figure handle.
    #     """
    #     import plotly.graph_objects as go
    #     import numpy as np

    #     h5file = self.solver.restart.densityPath
    #     values = read_field(h5file, f"ldos/{index+1}/total")
    #     xyz = self.system.cell.get_grids()
    #     g = self.system.cell.grid
    #     X, Y, Z = np.mgrid[range(g[0]), range(g[1]), range(g[2])]

    #     fig = go.Figure(data=go.Isosurface(
    #         x=X.flatten(),
    #         y=Y.flatten(),
    #         z=Z.flatten(),
    #         value=values.flatten(),
    #         isomin=value*0.99,
    #         isomax=value*1.01,
    #         surface_count=1,
    #         caps=dict(x_show=False, y_show=False)
    #         ))
    #     if show:
    #         fig.show()
    #     if filename is not None:
    #         fig.savefig(filename)
    #     return fig
