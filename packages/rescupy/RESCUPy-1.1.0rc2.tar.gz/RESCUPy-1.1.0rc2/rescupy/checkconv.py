# -*- coding: utf-8 -*-
"""
Created on 2021-06-16

@author: Vincent Michaud-Rioux
"""

from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.kpoint import increase_ksampling
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
from typing import List
import attr
import matplotlib.pyplot as plt
import numpy as np


@attr.s
class CheckPrecision(Base):
    """``CheckPrecision`` class.

    Examples::

        from rescupy.checkprecision import CheckPrecision
        from rescupy.totalenergy import TotalEnergy
        ecalc = TotalEnergy.read("nano_scf_out.json")
        ecalc.solver.set_stdout("resculog.out")
        calc = CheckPrecision(ecalc, parameter="resolution", etol=1.e-3)
        calc.solve()

    Attributes:
        calculators (list):
            Stores the calculators for each element of ``charge_deltas``.
        etol:
            Total energy tolerance.
        parameter:
            Parameter to converge ("k-sampling" or "resolution").
    """

    reference_calculator: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )
    # input is dictionary with default constructor
    calculators: List[TotalEnergy] = attr.ib(default=[])
    etol: Quantity = attr.ib(
        default=1.0e-3 * ureg.eV,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.instance_of(Quantity),
    )
    parameter: str = attr.ib(
        default="resolution",
        validator=attr.validators.instance_of(str),
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
        if self.parameter not in ["k-sampling", "resolution"]:
            raise Exception(
                'The parameter attribute must be "k-sampling" or "resolution"'
            )

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        calc = cls(reference_calculator=totalenergy, **kwargs)
        return calc

    def get_delta_etots(self):
        """Returns the energy errors taking the highest resolution as reference."""
        etot = self.get_etots()
        return etot - etot[-1]

    def get_etots(self):
        return Quantity.from_list(
            [c.get_total_energy_per_atom() for c in self.calculators]
        )

    def get_ksamplings(self):
        return [c.system.kpoint.grid for c in self.calculators]

    def get_resolutions(self):
        return Quantity.from_list([c.system.cell.resolution for c in self.calculators])

    def plot(self, filename=None, show=True):
        """Generates a plot of the error as a function of parameter.

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
        detot = self.get_delta_etots()
        if self.parameter == "resolution":
            x = self.get_resolutions()
            units = x.u
            x = x.m
        else:
            kall = self.get_ksamplings()
            x = np.array([np.prod(k) for k in kall])
            units = "n"

        fig = plt.figure()
        plt.semilogy(x, np.abs(detot.m), "bo--")
        ef = np.ones(x.size) * self.etol.to(detot.u)
        plt.plot(x, ef.m, "--k")
        plt.xlabel(f"{self.parameter} ({units})")
        plt.ylabel(f"delta energy ({detot.u})")
        if filename is not None:
            fig.savefig(filename)
        if show:
            plt.show()
        return fig

    def print_summary(self):
        if self.parameter == "resolution":
            self._print_summary_res()
        else:
            self._print_summary_kpt()

    def solve(self):
        if self.parameter == "resolution":
            self._solve_res()
        else:
            self._solve_kpt()

    def _print_summary_kpt(self):
        detot = self.get_delta_etots()
        etot = self.get_etots()
        kall = self.get_ksamplings()
        line = "%20s | %25s | %20s" % (
            "k-sampling",
            "total energy/atom (eV)",
            "energy error (eV)",
        )
        print(line)
        for k, e, d in zip(kall, etot, detot):
            line = "%6d %6d %6d | %+20.8f | %+20.8f" % (
                k[0],
                k[1],
                k[2],
                e.to("eV").m,
                d.to("eV").m,
            )
            print(line)

    def _print_summary_res(self):
        detot = self.get_delta_etots()
        etot = self.get_etots()
        resolution = self.get_resolutions()
        line = "%20s | %25s | %20s" % (
            "resolution (ang)",
            "total energy/atom (eV)",
            "energy error (eV)",
        )
        print(line)
        for r, e, d in zip(resolution, etot, detot):
            line = "%20.8f | %+25.8f | %+20.8f" % (
                r.to("angstrom").m,
                e.to("eV").m,
                d.to("eV").m,
            )
            print(line)

    def _solve_kpt(self):
        """
        Perform a series of calculations of increasing k-sampling until the total energy
        varies by less than a prescribed tolerance.
        """
        detot = self.etol * 2.0
        count = 0
        kref = self.reference_calculator.system.kpoint.grid
        k1 = kref
        etot = []
        kall = []
        line = "%20s | %25s | %20s" % (
            "k-sampling",
            "total energy/atom (eV)",
            "delta energy (eV)",
        )
        print(line)
        while abs(detot) > self.etol:
            output = "kpt_scf_out_" + str(count)
            ecalc = self.reference_calculator.copy()
            # ecalc.system.kpoint.gamma_centered = True
            ecalc.system.kpoint.set_grid(k1)
            ecalc.solve(output=output)
            self.calculators.append(ecalc)
            self.write("nano_check_ksampling.json")
            etot.append(ecalc.get_total_energy_per_atom())
            kall.append(ecalc.system.kpoint.grid)
            detot = etot[-1]
            if count > 0:
                detot -= etot[-2]
            line = "%6d %6d %6d | %+20.8f | %+20.8f" % (
                k1[0],
                k1[1],
                k1[2],
                etot[-1].m,
                detot.m,
            )
            print(line)
            k1 = increase_ksampling(k1, kref)
            count += 1
        self.print_summary()

    def _solve_res(self):
        """
        Perform a series of calculations of increasing real space resolution until the total energy
        varies by less than a prescribed tolerance.
        """
        # make sure units are consistent
        detot = self.etol * 2.0
        count = 0
        res1 = self.reference_calculator.system.cell.resolution
        etot = []
        resolution = []
        line = "%20s | %25s | %20s" % (
            "resolution (ang)",
            "total energy/atom (eV)",
            "delta energy (eV)",
        )
        print(line)
        while abs(detot) > self.etol:
            output = "res_scf_out_" + str(count)
            ecalc = self.reference_calculator.copy()
            ecalc.system.cell.set_resolution(res1)
            ecalc.solve(output=output)
            self.calculators.append(ecalc)
            self.write("nano_check_resolution.json")
            etot.append(ecalc.get_total_energy_per_atom())
            resolution.append(ecalc.system.cell.resolution)
            detot = etot[-1]
            if count > 0:
                detot -= etot[-2]
            line = "%20.8f | %+25.8f | %+20.8f" % (
                resolution[-1].to("angstrom").m,
                etot[-1].to("eV").m,
                detot.to("eV").m,
            )
            print(line)
            res1 *= 0.9
            count += 1
        self.print_summary()
