# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""

import attr
from rescupy.base import Base
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.signal

from rescupy.system import (
    System,
    calc_magnetic_moments_collinear,
    calc_magnetic_moments_non_collinear,
)
from rescupy.energy import Energy
from rescupy.io.calculators import solve_generic
from rescupy.solver import Solver
from rescupy.utils import read_field, dict_converter


@attr.s
class TotalEnergy(Base):
    """``TotalEnergy`` class.

    Examples::

        a = 2.818 # lattice constant (ang)
        cell = Cell(avec=[[0.,a,a],[a,0.,a],[a,a,0.]], resolution=0.12)
        fxyz = [[0.00,0.00,0.00],[0.25,0.25,0.25]]
        atoms = Atoms(fractional_positions=fxyz, formula="GaAs")
        sys = System(cell=cell, atoms=atoms)
        sys.kpoint.set_grid([5,5,5])
        calc = TotalEnergy(sys)
        calc.solve()
        print(calc.energy.etot)

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

    def get_total_magnetic_moment(self):
        """Returns the total magnetic moment."""
        return self.system.atoms.get_total_magnetic_moment()

    def get_magnetic_moments(self):
        """Returns the magnetic moments."""
        magnetic_moments = self.system.atoms.get_magnetic_moments()
        if magnetic_moments is None:
            natm = self.system.atoms.get_number_of_atoms()
            if self.system.hamiltonian.ispin == 1:
                magnetic_moments = np.zeros((natm))
            elif self.system.hamiltonian.ispin == 2:
                denpath = self.solver.restart.densityPath
                magnetic_moments = calc_magnetic_moments_collinear(
                    self.system.cell, self.system.atoms, denpath
                )
            elif self.system.hamiltonian.ispin == 4:
                denpath = self.solver.restart.densityPath
                magnetic_moments = calc_magnetic_moments_non_collinear(
                    self.system.cell, self.system.atoms, denpath
                )
        self.system.atoms.set_magnetic_moments(magnetic_moments)
        return magnetic_moments

    def get_number_of_atoms(self):
        """Returns the number of atoms."""
        return self.system.atoms.get_number_of_atoms()

    def get_potential(self, name, units="si"):
        """Returns the number of atoms.

        Args:
            name (string):
                Path to the HDF5 file containing the potential data.
            units (string, optional):
                Unit of energy for the potential.
        """
        from rescupy.data.units import units_dict as u

        filename = self.solver.restart.densityPath
        if name == "electrostatic":
            vna = read_field(filename, "potential/neutralatom")
            vdh = read_field(filename, "potential/deltahartree")
            v = vna + vdh
        elif name == "deltahartree":
            v = read_field(filename, "potential/deltahartree")
        elif name == "effective":
            v = read_field(filename, "potential/effective")
        elif name == "external":
            v = read_field(filename, "potential/external")
        elif name == "neutralatom":
            v = read_field(filename, "potential/neutralatom")
        elif name == "xc":
            v = read_field(filename, "potential/xc")
        else:
            raise ValueError("No potential %s." % (name))
        if units == "atomic":
            v = v / u["ha"]
        elif units != "si":
            raise ValueError("Invalid units %s." % (units))
        return v

    def get_total_energy(self):
        """Returns the total energy."""
        return self.energy.etot

    def get_total_energy_per_atom(self):
        """Returns the total energy per atom."""
        n = self.get_number_of_atoms()
        etot = self.get_total_energy()
        return etot / n

    def get_average_field(self, field, axis):
        """Loads field from ``self.solver.restart.densityPath`` and compute the average along a given axis.

        Args:
            field (str/NDArray):
                str: HDF5 path. For example, "potential/effective".
                NDArray: 3d array.
            axis (int):
                Axis remaining after averaging. The value should be between 0 and 2.

        Returns:
            NDArray: Average field.
        """
        if axis not in [0, 1, 2]:
            raise ValueError("Axis must be in [0,1,2].")
        avg = list(range(3))
        avg.pop(axis)
        if type(field) == str:
            field = self.get_field(field)
        return np.mean(field, axis=tuple(avg))

    def get_field(self, field):
        """Loads field from ``self.solver.restart.densityPath``."""
        filename = self.solver.restart.densityPath
        field = read_field(filename, field)
        return field

    def plot_field(self, field, axis, filename=None, show=True):
        """Plots a field averaged along a given axis.

        Args:
            field (str):
                Path in the HDF5 filed pointed to by self.solver.restart.densityPath.
            axis (int):
                Axis remaining after averaging. The value should be between 0 and 2.
            filename (str, optional):
                If not None, then the figure is saved to filename.
            show (bool, optional):
                If True block and show figure.
                If False, do not show figure.

        Returns:
            fig (:obj:`matplotlib.figure.Figure`):
                A figure handle.
        """
        if axis not in [0, 1, 2]:
            raise Exception("axis must take the value 0, 1 or 2.")
        if isinstance(field, np.ndarray):
            vavg = field
        else:
            vavg = self.get_average_field(field, axis)
        x = self.system.cell.get_grid(axis=axis)
        lx = self.system.cell.get_length(axis=axis)
        fig = plt.figure()
        plt.plot(x, vavg)
        plt.xticks(np.arange(7) / 6 * lx)
        plt.grid(axis="x")
        plt.xlabel("position (" + self.system.cell.avec.u + ")")
        plt.ylabel("field average (eV)")
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def smooth_field(self, field, axis, width=2.0, shape="erf"):
        """Smooths a field by circular convolution.

        Args:
            field (str/NDArray):
                str: Path in the HDF5 filed pointed to by self.solver.restart.density. For example, "potential/effective".
                NDArray: 3d array.
            axis (int):
                Axis remaining after averaging. The value should be between 0 and 2.
            width (float):
                Unit system ('atomic' or 'si')
        """
        field = self.get_average_field(field, axis)
        field3 = np.concatenate((field, field, field))
        x = self.system.cell.get_grid(axis=axis)
        dx = self.system.cell.get_dx(axis)
        lx = self.system.cell.get_length(axis=axis)
        x3 = np.concatenate((x - lx, x, x + lx))
        if shape == "n-points":
            cn = int(width // dx)  # half-stencil width
            cn += cn % 2
            cn = int(cn // 2)
            conv = np.zeros_like(x)
            conv[0 : cn + 1] = 1.0 / (2 * cn + 1)
            conv[-1 : -cn - 1 : -1] = 1.0 / (2 * cn + 1)
            conv = scipy.linalg.circulant(conv)
            sfield = field
            for i in np.arange(4):
                sfield = np.matmul(conv, sfield)
        else:
            pulse = 0.5 * (scipy.special.erf((x3 - width / 2.0)) + 1.0) - 0.5 * (
                scipy.special.erf((x3 + width / 2.0)) + 1.0
            )
            pulse = pulse / np.sum(pulse) / dx
            sfield = field
            for i in np.arange(2):
                sfield = (
                    scipy.signal.convolve(np.tile(sfield, 3), pulse, mode="full") * dx
                )
                sfield = sfield[2 * x.size : 3 * x.size]
        return sfield

    def solve(self, input="nano_scf_in", output="nano_scf_out"):
        """
        Performs a self-consistent calculation to obtain the ground state total energy.

        Args:
            input (str):
                The object is saved to an input file ``input`` to be read by the Fortran program.
            output (str):
                The results (with various extensions) are moved to files ``output`` and the results are
                loaded to the object.
        """
        output = solve_generic(self, "scf", input, output)
        self._update(output + ".json")

    def supercell(self, T):
        """
        Replaces the underlying ``System`` object with a supercell ``System`` object.

        Args:
            T (NDArray): A (3x3) linear transformation.

        Returns:

        """
        self.system.supercell(T=T)
        self.solver.restart.clear_paths()
        self.solver.eig.set_target_irange(
            ispin=self.system.hamiltonian.ispin,
            valence_charge=self.system.atoms.valence_charge,
        )
