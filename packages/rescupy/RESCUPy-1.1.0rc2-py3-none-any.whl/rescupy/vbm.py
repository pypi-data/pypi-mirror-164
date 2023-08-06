# -*- coding: utf-8 -*-
"""
Created on 2021-06-04

@author: Vincent Michaud-Rioux
"""

from nptyping import NDArray
from typing import List
import attr
import matplotlib.pyplot as plt
import numpy as np
from rescupy.base import Base
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter, to_quantity, Quantity


@attr.s
class ValenceBandMaximum(Base):
    """``ValenceBandMaximum`` class.

    Examples::

        from rescupy.vbm import ValenceBandMaximum as VBM
        from rescupy.totalenergy import TotalEnergy
        ecalc = TotalEnergy.read("nano_scf_init.json")
        calc = VBM.from_totalenergy(ecalc)
        calc.delta_charges = [0.001]
        calc.solve()
        vbm = calc.get_vbm()
        print(f"The VBM is = {vbm}")

    Attributes:
        calculators:
            Stores the calculators for each element of ``charge_deltas``.
        charge_deltas:
            Charge variations in electrons.
        reference_calculator:
            Total energy calculator.
        vbm:
            Valence band maximum.
    """

    # input is dictionary with default constructor
    reference_calculator: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )
    calculators: List[TotalEnergy] = attr.ib(default=[])
    charge_deltas: NDArray = attr.ib(
        default=np.array([0.001]),
        converter=lambda v: np.array(v),
    )
    vbm: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )

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
        calc = cls(reference_calculator=totalenergy, **kwargs)
        return calc

    def get_charge_deltas(self):
        delta = [self.reference_calculator.system.atoms.valence_charge]
        delta += [c.system.atoms.valence_charge for c in self.calculators]
        return delta[0] - np.array(delta)

    def get_total_energies(self):
        etots = [self.reference_calculator.energy.etot]
        etots += [c.energy.etot for c in self.calculators]
        return Quantity.from_list(etots)

    def get_vbm(self):
        if self.vbm is None:
            deltas = self.get_charge_deltas()
            etots = self.get_total_energies()
            self.vbm = (etots[0] - etots[1:]) / deltas[1:]
        return self.vbm

    def print_vbm(self):
        vbm = self.get_vbm()
        for (v, d) in zip(vbm, self.charge_deltas):
            print("The VBM is = %f %s (delta = %f)" % (v.m, v.u, d))

    def plot_vbm(self, filename=None, show=True):
        """Generates a semilogx plot of the VBMs (one for each charge_delta).

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
        vbm = self.get_vbm()
        fig = plt.figure()
        x = self.charge_deltas
        y = vbm.m
        plt.semilogx(x, y, "o-k")
        plt.xlabel("Delta (e)")
        plt.ylabel("VBM ({vbm.u})")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def solve(self):
        # make sure units are consistent
        self.reference_calculator.solve()
        n = 0
        for delta in self.charge_deltas:
            if delta < 0.0:
                raise Exception("delta must be positive.")
            calc = self.reference_calculator.copy()
            calc.system.atoms.valence_charge -= delta
            calc.solve(output=f"nano_scf_out_{n}.json")
            self.calculators.append(calc)
            self.write("nano_vbm_out.json", units="si")
            n += 1
