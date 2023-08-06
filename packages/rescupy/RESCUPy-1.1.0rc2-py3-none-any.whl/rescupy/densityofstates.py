# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from rescupy.base import Base, Quantity
from rescupy.dos import Dos
from rescupy.energy import Energy
from rescupy.io.calculators import solve_generic
from rescupy.solver import Solver
from rescupy.system import System
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter
import attr
import matplotlib.pyplot as plt
import numpy as np


@attr.s
class DensityOfStates(Base):
    """``DensityOfStates`` class.

    Examples::

        from rescupy import DensityOfStates as DOS
        calc = DOS.from_totalenergy("nano_scf_out.json")
        calc.dos.pdos_return = True
        calc.system.kpoint.set_grid([10,10,10])
        calc.system.pop.set_type("tm")
        calc.solve()
        fig = calc.plot_dos()
        fig.savefig("gaas_dos.png", dpi=600)  # save fig
        fig = calc.plot_pdos(sumA=[1,2])
        fig.savefig("gaas_pdos.png", dpi=600) # save fig

    Attributes:
        system:
           Object containing system related parameters.
        dos:
           Object containing the density of states.
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
    dos: Dos = attr.ib(
        factory=Dos,
        converter=lambda d: dict_converter(d, Dos),
        validator=attr.validators.instance_of(Dos),
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
        # atomic system
        if self.system is None:
            raise Exception('"system" parameters not found in input file.')
        self.solver.eig.set_target_irange(
            ispin=self.system.hamiltonian.ispin,
            valence_charge=self.system.atoms.valence_charge,
        )

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

    def set_energy_grid(self, energies):
        # set energy-grid for (central) transmission/dos calculation
        self.dos.set_energy(energies)
        self.dos.resolution = (self.dos.energy[-1] - self.dos.energy[0]) / (
            len(self.dos.energy) - 1
        )
        self.dos.interval = Quantity.from_list(
            [self.dos.energy[0], self.dos.energy[-1]]
        )

    def plot_dos(self, filename=None, show=True):
        """Generates a plot of the density of states.

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
        fig = plt.figure()
        ispin = self.dos.dos.size // self.dos.energy.size
        x = self.dos.energy.m
        y = self.dos.dos.m
        xunit = self.dos.energy.u
        yunit = self.dos.dos.u
        linespecs = ["-b", "--r"]
        if ispin == 1:
            legends = ["total"]
        elif ispin == 2:
            legends = ["spin-up", "spin-down"]
            plt.plot(x, np.sum(y, axis=1), "-k")
        for s in range(ispin):
            plt.plot(x, y[:, s], linespecs[s], label=legends[s])
        ef = np.ones(2) * self.energy.efermi.to(xunit)
        h = [0.0, plt.gca().get_ylim()[1]]
        plt.plot(ef.m, h, "--k", label="Efermi")
        plt.xlabel(f"Energy ({xunit})")
        plt.ylabel(f"DOS ({yunit})")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def plot_pdos(self, sumA=None, sumL=None, sumM=None, filename=None, show=True):
        """Generates a plot of the projected density of states.

        The projected density of states is computed and plotted on the fly.
        If several optional inputs are specified, the Cartesian product of
        all parameters will be shown.

        Args:
            sumA (1D array, optional):
                Atom indices. If sumA = [1,2], then both the contributions of atom 1 and 2's orbitals
                are computed and plotted.
            sumL (1D array, optional):
                Orbital angular momentum. If sumL = [0,1,2], then the contributions of s, p and d orbitals respectively
                are computed and plotted.
            sumM (1D array, optional):
                z-component of the orbital angular momentum. If sumM = 0, then both the contributions of z=0-orbitals
                are computed and plotted.
            filename (str, optional):
                If not None, then the figure is saved to filename.
            show (bool, optional):
                If True block and show figure.
                If False, do not show figure.

        Returns:
            fig (:obj:`matplotlib.figure.Figure`):
                A figure handle.
        """
        ispin = self.system.hamiltonian.ispin
        x = self.dos.energy
        y = self.dos.dos
        linespecs = ["-", "--"]
        if ispin == 1:
            prefixes = [""]
        elif ispin == 2:
            prefixes = ["(spin-u)", "(spin-d)"]
        fig = plt.figure()
        plt.plot(x, np.sum(y, axis=1), "-k")
        if all([sumA is None, sumL is None, sumM is None]):
            if show:
                plt.show()
        else:
            y = self.dos.pdos.reshape((x.size, -1, ispin), order="F")
            # plt.plot(x, np.sum(y, axis=(1,2)), "--g")
            if sumA is None:
                sumA = [sumA]
            if sumL is None:
                sumL = [sumL]
            if sumM is None:
                sumM = [sumM]
            for s in range(ispin):
                plot_pdos_core(
                    x,
                    y[:, :, s],
                    [
                        [self.dos.orbA, sumA, "A"],
                        [self.dos.orbL, sumL, "L"],
                        [self.dos.orbM, sumM, "M"],
                    ],
                    linespec=linespecs[s],
                    label_prefix=prefixes[s],
                )
        ef = np.ones(2) * self.energy.efermi
        h = [0.0, plt.gca().get_ylim()[1]]
        plt.plot(ef, h, "--k", label="Efermi")
        plt.xlabel("Energy (" + self.dos.energy.u + ")")
        plt.ylabel("DOS (" + self.dos.dos.u + ")")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def solve(self, input="nano_dos_in", output="nano_dos_out"):
        """Performs a non.self-consistent calculation calling ``rescuplus_dos``.

        Args:
            filename (str):
                The object is saved to an input file ``filename`` which is read by ``rescuplus_dos``.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        self._check_dos()
        output = solve_generic(self, "dos", input, output)
        self._update(output + ".json")

    def _check_dos(self):
        if self.system.kpoint.type != "full":
            raise ValueError(
                "system.kpoint.type must be set to full for a dos calculation."
            )


def plot_pdos_core(x, pdos, orbXXX, linespec="-", label_prefix=""):
    for a in orbXXX[0][1]:
        if a is None:
            orbA = np.ones_like(orbXXX[0][0], dtype=bool)
            labA = []
        else:
            orbA = orbXXX[0][0] == a
            labA = [orbXXX[0][2], " = ", str(a), ","]
        for l in orbXXX[1][1]:
            if l is None:
                orbL = np.ones_like(orbXXX[1][0], dtype=bool)
                labL = []
            else:
                orbL = orbXXX[1][0] == l
                labL = [orbXXX[1][2], " = ", str(l), ","]
            for m in orbXXX[2][1]:
                if m is None:
                    orbM = np.ones_like(orbXXX[2][0], dtype=bool)
                    labM = []
                else:
                    orbM = orbXXX[2][0] == m
                    labM = [orbXXX[2][2], " = ", str(m), ","]
                orbX = np.logical_and(orbA, orbL)
                orbX = np.logical_and(orbX, orbM)
                d = np.sum(pdos[:, orbX], axis=1)
                label = "".join(labA + labL + labM)[0:-1]
                plt.plot(x, d, linespec, label=label_prefix + label)
                plt.legend(loc="upper right")
