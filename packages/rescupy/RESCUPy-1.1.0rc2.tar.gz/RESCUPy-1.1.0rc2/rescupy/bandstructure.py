# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

from rescupy.base import Base, Quantity, ureg
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
class BandStructure(Base):
    """``BandStructure`` class.

    Examples::

        from rescupy.bandstructure import BandStructure as BS
        calc = BS.from_totalenergy("nano_scf_out.json")
        calc.solve()
        fig = calc.plot_bs() # plot results
        fig.savefig("gaas_bs.png", dpi=600) # save fig

    Attributes:
        system:
           Object containing system related parameters.
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
        sys.set_kpoint_path()
        calc = cls(sys, solver=totalenergy.solver, **kwargs)
        calc.energy = totalenergy.energy.copy()
        # calc.energy.efermi = totalenergy.energy.efermi
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
            self.system.kpoint,
            filename=filename,
            show=show,
        )

    def solve(self, input="nano_bs_in", output="nano_bs_out"):
        """
        Perform a self-consistent calculation calling ``rescuplus_bs``.

        Args:
            filename (str):
                The object is saved to an input file ``filename`` which is read by ``rescuplus_bs``.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        self._check_bs()
        output = solve_generic(self, "bs", input, output)
        self._update(output + ".json")

    def _check_bs(self):
        if self.system.kpoint.type != "line":
            raise ValueError(
                "system.kpoint.type must be set to line for a dos calculation."
            )


def plot_bs_driver(energy, hamiltonian, kpoint, weights=None, filename=None, show=True):
    """Generates a plot of the band structure.

    Args:
        energy (Energy):
            Energy object containing the eigenvalues.
        hamiltonian (Hamiltonian):
            Hamiltonian object containing the spin treatment level.
        kpoint (Kpoint):
            Kpoint object containing the high-symmetry points, k-point coordinates and indices.
        weights (NDArray, optional):
            Array of weights, commensurate with energy.eigenvalues. If weights is not None, then
            bands have a width varying between 0 and .1 eV modulated by weights. This is used
            to plot spectral functions among other things.
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
    ispin = hamiltonian.ispin
    ns = hamiltonian.get_spin_num()
    ylim = Quantity.from_list(
        [energy.efermi - 5.0 * ureg.eV, energy.efermi + 5.0 * ureg.eV]
    )
    ylim = ylim.to(energy.eigenvalues.u).m
    efermi = energy.efermi.to(energy.eigenvalues.u).m
    linespecs = ["-b", "--r"]
    shadspecs = ["b", "r"]
    if ispin == 2:
        legends = ["spin-up", "spin-down"]
    else:
        legends = ["total"]
    for s in range(ns):
        eigenvalues = energy.eigenvalues[:, :, s].m.T
        if weights is not None:
            sf = weights[:, :, s].T
        # extract labels
        chpts = kpoint.special_points.copy()
        labels = kpoint.get_special_points_labels()
        # labels = kpoint.kpt_2_label(self.system.cell.copy(), fractional_coordinates)
        # remove doublons (e.g. 'X' following 'X')
        for i in range(0, len(chpts) - 1):
            if chpts[i] + 1 == chpts[i + 1] and labels[i] == labels[i + 1]:
                j = chpts[i]
                eigenvalues = np.delete(eigenvalues, j, axis=0)
                if weights is not None:
                    sf = np.delete(sf, j, axis=0)
                del chpts[i]
                del labels[i]
                for k in range(i, len(chpts)):
                    chpts[k] = chpts[k] - 1
            if i + 2 >= len(chpts):
                break
        # plot
        x = np.arange(0, eigenvalues.shape[0])
        if weights is None:
            plt.plot(x, eigenvalues[:, 0:1], linespecs[s], label=legends[s])
            plt.plot(x, eigenvalues[:, 1::], linespecs[s], label="_nolegend_")
        else:
            linewidth = 0.1  # in eV
            for j in range(0, eigenvalues.shape[1]):
                plt.fill_between(
                    x,
                    eigenvalues[:, j] - sf[:, j] / 2 * linewidth,
                    eigenvalues[:, j] + sf[:, j] / 2 * linewidth,
                    facecolor=shadspecs[s],
                    alpha=1.0,
                    label="_nolegend_",
                )
    ef = np.ones(eigenvalues.shape[0]) * efermi
    plt.plot(ef, "--k", label="Efermi")
    plt.ylim(ylim)
    plt.legend(loc="upper right")
    plt.xlabel(f"BZ ({kpoint.bvec.u})")
    plt.ylabel(f"Energy ({energy.eigenvalues.u})")
    plt.xticks(chpts, labels)
    plt.grid(axis="x")
    if show:
        plt.show()
    if filename is not None:
        fig.savefig(filename)
    return fig
