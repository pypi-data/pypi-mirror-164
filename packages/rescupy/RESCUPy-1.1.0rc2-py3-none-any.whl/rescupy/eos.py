# -*- coding: utf-8 -*-
"""
Created on 2021-06-03

@author: Vincent Michaud-Rioux
"""

from nptyping import NDArray
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
from typing import List
import attr
import numpy as np


@attr.s
class EquationOfState(Base):
    """``EquationOfState`` class.

    Examples::

        from rescupy import Atoms, Cell, System, TotalEnergy
        from rescupy.eos import EquationOfState as EOS
        a = 5.64 / 2. # lattice constant (ang)
        cell = Cell(avec=[[0.,a,a],[a,0.,a],[a,a,0.]], resolution=0.15)
        fxyz = [[0.00,0.00,0.00],[0.25,0.25,0.25]]
        atoms = Atoms(fractional_positions=fxyz, formula="GaAs")
        sys = System(cell=cell, atoms=atoms)
        sys.kpoint.set_grid([7,7,7])
        calc = TotalEnergy(sys)
        eos = EOS.from_totalenergy(calc)
        eos.relative_volumes = [0.96, 0.98, 1.00, 1.02, 1.04]
        eos.solve()
        eos.plot_eos()

    Attributes:
        calculators:
            Stores the calculators for each volume.
        equilibrium_volume:
            Equilibrium volume.
        initial_volume:
            Initial volume.
        reference_calculator:
            Total energy calculator.
        relative_volumes:
            Relative volumes used to compute the equation of states. For instance, setting
            [0.96, 0.98, 1.  , 1.02, 1.04] will compute the total energy for five volumes
            corresponding to 96% up to 104% of initial_volume.
    """

    # input is dictionary with default constructor
    reference_calculator: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.optional(attr.validators.instance_of(TotalEnergy)),
    )
    bulk_modulus: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(
            lambda x: to_quantity(x, "ev / angstrom ** 3")
        ),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    equilibrium_volume: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "angstrom ** 3")),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    initial_volume: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "angstrom ** 3")),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    relative_volumes: NDArray = attr.ib(
        default=np.arange(0.94, 1.06, 0.02),
        converter=lambda v: np.array(v),
    )
    calculators: List[TotalEnergy] = attr.ib(default=[])

    def __attrs_post_init__(self):
        if self.calculators is not None:
            calc = []
            for s in self.calculators:
                if isinstance(s, dict):
                    calc.append(TotalEnergy(**s))
                elif isinstance(s, TotalEnergy):
                    calc.append(s)
                else:
                    raise Exception("Invalid TotalEnergy calculators.")
            self.calculators = calc

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        calc = cls(totalenergy, **kwargs)
        calc.initial_volume = totalenergy.system.cell.get_volume()
        return calc

    def get_bulk_modulus(self):
        """Returns the bulk modulus as calculated with a Birch-Murnaghan fit."""
        if self.bulk_modulus is not None:
            return self.bulk_modulus
        self.get_equilibrium_volume_per_atom()
        return self.bulk_modulus

    def get_equilibrium_volume(self):
        """Returns the equilibrium volume as calculated with a Birch-Murnaghan fit."""
        if self.equilibrium_volume is not None:
            return self.equilibrium_volume
        eos = self._get_eos()
        v0, e0, B = eos.fit()
        self.equilibrium_volume = v0 * ureg.angstrom**3
        self.bulk_modulus = B * ureg.eV / ureg.angstrom**3
        return self.equilibrium_volume

    def get_total_energies(self):
        return Quantity.from_list(
            [c.energy.get_total_energy() for c in self.calculators]
        )

    def get_total_energies_per_atom(self):
        return Quantity.from_list(
            [c.get_total_energy_per_atom() for c in self.calculators]
        )

    def get_volumes(self):
        return Quantity.from_list(
            [c.system.cell.get_volume() for c in self.calculators]
        )

    def get_volumes_per_atom(self):
        natom = self.reference_calculator.system.get_number_of_atoms()
        return self.get_volumes() / natom

    def plot_eos(self, filename=None, show=True):
        """Generates a plot of the equation of states (+ fit).

        Args:
            filename (str, optional):
                If not None, then the figure is saved to filename.
            show (bool, optional):
                If True block and show figure.
                If False, do not show figure.
        """
        eos = self._get_eos()
        eos.plot(filename=filename, show=show)

    def solve(self):
        # make sure units are consistent
        self.set_units("si")
        n = 0
        for rv in self.relative_volumes:
            calc = self.reference_calculator.copy()
            v = self.initial_volume * rv
            calc.system.set_volume(v)
            calc.solve(output=f"nano_scf_out_{n}.json")
            self.calculators.append(calc)
            n += 1
        self.write("nano_eos_out.json")

    def _get_eos(self):
        from ase.eos import EquationOfState

        volumes = self.get_volumes_per_atom().to("angstrom ** 3")
        energies = self.get_total_energies_per_atom().to("eV")
        eos = EquationOfState(volumes.m, energies.m, eos="birchmurnaghan")
        return eos
