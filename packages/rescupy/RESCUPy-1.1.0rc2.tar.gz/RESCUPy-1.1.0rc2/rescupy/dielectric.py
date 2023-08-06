# -*- coding: utf-8 -*-
"""
Created on 2021-06-08

@author: Vincent Michaud-Rioux
"""

from attr import field
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
import attr
import matplotlib.pyplot as plt
import numpy as np


@attr.s
class DielectricConstant(Base):
    """``DielectricConstant`` class.

    Examples::

        from rescupy import Atoms, Cell, System, TotalEnergy
        from rescupy.dielectric import DielectricConstant
        a = 3.562
        cell = Cell(avec=[[a,0.,0.],[0.,a,0.],[0.,0.,a]], resolution=0.15)
        atoms = Atoms(fractional_positions="diamond.fxyz")
        sys = System(cell=cell, atoms=atoms)
        sys.supercell([4,1,1])
        ecalc = TotalEnergy(sys)
        ecalc.solver.set_mpi_command("mpiexec -n 16")
        calc = DielectricConstant(ecalc, axis=0, amplitude=0.1)
        calc.solve()

    Attributes:
        amplitude:
            Sawtooth potential amplitude.
        axis:
            Direction of the sawtooth potential ([0,1,2] == [x,y,z]).
        external_calculator:
            Stores the calculator under external field.
        dielectric_constant:
            Dielectric constant.
        reference_calculator:
            Total energy calculator.
    """

    # input is dictionary with default constructor
    reference_calculator: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )
    amplitude: Quantity = field(
        default=1.0 * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    axis: int = attr.ib(
        default=2, converter=int, validator=attr.validators.instance_of(int)
    )
    dielectric_constant = attr.ib(default=None)
    external_calculator = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.external_calculator is not None:
            s = self.external_calculator
            if isinstance(s, dict):
                self.external_calculator = TotalEnergy(**s)
            elif not isinstance(s, TotalEnergy):
                raise Exception("Invalid TotalEnergy calculators.")

    def get_dielectric_constant(self):
        if self.dielectric_constant is None:
            dv = self._get_pot_delta()
            vext = self._get_vext()
            eext = self.external_calculator
            axis = self.axis
            x = eext.system.cell.get_grid(axis=axis)
            lx = eext.system.cell.get_length(axis=axis)
            u = (x / lx).to("dimensionless").m
            ind = np.logical_and(1 / 6 < u, u < 2 / 6)
            ind = np.logical_and(1 / 6 < u, u < 2 / 6)
            sleft = np.polyfit(u[ind], vext[ind], 1)
            tleft = np.polyfit(u[ind], dv[ind], 1)
            die1 = sleft[0] / tleft[0]
            ind = np.logical_and(4 / 6 < u, u < 5 / 6)
            sright = np.polyfit(u[ind], vext[ind], 1)
            tright = np.polyfit(u[ind], dv[ind], 1)
            die2 = sright[0] / tright[0]
            self.dielectric_constant = 0.5 * (die1 + die2)
        return self.dielectric_constant

    def plot_external_potential(self, filename=None, show=True):
        """Generates a plot of the external potential (+screened potential).

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
        axis = self.axis
        dv = self._get_pot_delta()
        vext = self._get_vext()
        eext = self.external_calculator
        x = eext.system.cell.get_grid(axis=axis)
        lx = eext.system.cell.get_length(axis=axis)
        u = x / lx
        fig = plt.figure()
        plt.plot(x, vext)
        plt.plot(x, dv)
        plt.xticks(np.arange(7) / 6 * lx)
        plt.grid(axis="x")
        plt.xlabel("position (" + eext.system.cell.avec.u + ")")
        plt.ylabel("field average (eV)")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def solve(self):
        self.reference_calculator.solve(output="nano_die_scf_ref")
        self.external_calculator = self.reference_calculator.copy()
        extpot = self.external_calculator.system.hamiltonian.extpot
        extpot.shape = "sawtooth"
        extpot.amplitude = self.amplitude
        extpot.axis = self.axis
        self.external_calculator.system.hamiltonian.extpot = extpot
        self.external_calculator.solve(output="nano_die_scf_ext")
        self.write("nano_die_out.json")

    def _get_vext(self):
        axis = self.axis
        eext = self.external_calculator
        vext = eext.get_average_field("potential/external", axis)
        return vext

    def _get_pot_delta(self):
        axis = self.axis
        eref = self.reference_calculator
        v0 = eref.get_average_field("potential/effective", axis)
        eext = self.external_calculator
        v1 = eext.get_average_field("potential/effective", axis)
        dv = v1 - v0
        return dv
