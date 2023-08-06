# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from rescupy.base import Base, to_quantity, ureg
from rescupy.energy import Energy
from rescupy.solver import Solver
from rescupy.system import System
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import read_field, dict_converter, Quantity
import attr
import numpy as np

# @attr.s
# class DipoleData(Base):
#     center_of_charge: NDArray = attr.ib(
#         default=None,
#         converter=attr.converters.optional(np.array),
#         validator=attr.validators.optional(attr.validators.instance_of(NDArray)),
#     )


@attr.s
class Dipole(Base):
    """``Dipole`` class.

    Examples::

        calc = Dipole.from_totalenergy("nano_scf_out.json")
        print(calc.get_dipole_moment())

    Attributes:
        system (System):
           Object containing system related parameters.
        energy (Energy):
           Object containing the total energy and its derivatives (force, stress, etc.).
        solver (Solver):
           Object containing solver related parameters.
    """

    # input is dictionary with default constructor
    system: System = attr.ib(
        converter=lambda d: dict_converter(d, System),
        validator=attr.validators.instance_of(System),
    )

    # optional
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

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        """Initializes a ``Dipole`` object from a ``TotalEnergy`` calculator."""
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        sys = totalenergy.system.copy()
        calc = cls(sys, solver=totalenergy.solver)
        calc.energy = totalenergy.energy.copy()
        return calc

    def get_real_space_density(self):
        """Returns a 3D array containing the real space density."""
        filename = self.solver.restart.densityPath
        ispin = self.system.hamiltonian.get_ispin()
        if ispin == 1 or ispin == 4:
            rho = read_field(filename, "density/total")
        elif ispin == 2:
            rhou = read_field(filename, "density/spin-up")
            rhod = read_field(filename, "density/spin-down")
            rho = rhou + rhod
        else:
            raise Exception("Invalid ispin value " + str(ispin) + " .")
        return rho

    def get_center_of_charge(self):
        """Returns the center of charge."""
        rho = self.get_real_space_density()
        x, y, z = self.system.cell.get_grids(shape="grid")
        dr = self.system.cell.get_dr()
        Q = np.sum(rho) * dr
        x0 = np.sum(rho * x) * dr / Q
        y0 = np.sum(rho * y) * dr / Q
        z0 = np.sum(rho * z) * dr / Q
        ecoc = np.array([x0, y0, z0])
        return ecoc
        # pos = self.system.atoms.positions
        # z = self.system.atoms.get_ionic_charges()
        # Z = np.sum(z)
        # icoc = np.sum(z[:,None] * pos, axis=0) / Z
        # print(ecoc, Q, icoc, Z)
        # return (Q * ecoc - Z * icoc) / (Q - Z)

    def get_dipole_moment(self, center=np.zeros(3) * ureg.angstrom):
        """Returns the dipole moment calculated with respect to center."""
        center = to_quantity(center, "angstrom", shape=(-1))
        rho = self.get_real_space_density()
        x, y, z = self.system.cell.get_grids(shape="grid")
        dr = self.system.cell.get_dr()
        em = np.empty(3) * center.u
        em[0] = np.sum(rho * (x - center[0])) * dr
        em[1] = np.sum(rho * (y - center[1])) * dr
        em[2] = np.sum(rho * (z - center[2])) * dr
        pos = self.system.atoms.positions
        z = self.system.atoms.get_ionic_charges()
        im = np.sum(z[:, None] * (pos - center[None, :]), axis=0)
        return em - im
