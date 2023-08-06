# -*- coding: utf-8 -*-
"""
Created on 2020-06-16

@author: Vincent Michaud-Rioux
"""

import attr
from rescupy.base import Base
import numpy as np


@attr.s
class Restart(Base):
    """``Restart`` class.

    The ``restart`` class gathers the paths of files containing previously calculated results,
    which can be used for restart.

    By default, the density is saved upon completing a ground state calculation. The ``densityPath``
    field is then updated to point to the results. Any kind of restart will then automatically
    import the density given in ``densityPath``. If the ground state density is not found in ``densityPath``
    then the code ignores it and proceeds without restart.

    If ``DMkPath`` or ``DMRPath`` is set, then the k-space or real space density matrix is saved
    to the specified path. Next, a calculation can be restarted from either density matrix.
    If the ground state density matrix is not found then the code ignores it and proceeds without restart.

    If several attributes have valid restart data, then the precedence goes as follows: ``densityPath``,
    ``DMkPath``, ``DMRPath``.

    Example::

        from rescupy import Atoms, Cell, Kpoint, System, TotalEnergy
        a = 2.818 # lattice constant (ang)
        cell = Cell(avec=[[0.,a,a],[a,0.,a],[a,a,0.]], resolution=0.12)
        fxyz = [[0.00,0.00,0.00],[0.25,0.25,0.25]]
        atoms = Atoms(fractional_positions=fxyz, formula="GaAs")
        sys = System(cell=cell, atoms=atoms)
        sys.kpoint.set_grid([5,5,5])
        calc = TotalEnergy(sys)
        calc.set_cmd(mpi="mpiexec -n 4")
        calccpy = calc.copy()

        # SCF
        calc.solve()

        # Restart from density and save k-space density matrix
        calc = calccpy.copy()
        calc.solver.mix.maxit = 1
        calc.solver.restart.densityPath = "nano_scf_out.h5"
        calc.solver.restart.DMkPath = "nano_scf_out.h5"
        calc.solve()

        # Restart from k-space density matrix and save real space density matrix
        calc = calccpy.copy()
        calc.solver.mix.maxit = 1
        calc.solver.restart.DMkPath = "nano_scf_out.h5"
        calc.solver.restart.DMRPath = "nano_scf_out.h5"
        calc.solve()

        # Restart from real space density matrix
        calc = calccpy.copy()
        calc.solver.mix.maxit = 1
        calc.solver.restart.DMRPath = "nano_scf_out.h5"
        calc.solve()


    Attributes:

    densityPath (string):
        Path to an HDF5 file. The group ``/density/groundstate`` will be read and used as an initial guess.
        Examples::

            restart.densityPath = "/path/to/hdf5/file"

    DMkPath (string):
        Path to an HDF5 file. The group ``/aomtrx/DMk``, containing the k-space density matrix, will be read and used as an initial guess.
        Examples::

            restart.DMkPath = "/path/to/hdf5/file"

    DMRPath (string):
        Path to an HDF5 file. The group ``/aomtrx/DMR``, containing the real space density matrix, will be read and used as an initial guess.
        Examples::

            restart.DMRPath = "/path/to/hdf5/file"

    ground_state_density_return (bool):
        Save the ground state density to ``densityPath`` if True, and do not save otherwise.
    partial_core_density_return (bool):
        Save the partial core density to ``densityPath`` if True, and do not save otherwise.
    neutral_atom_density_return (bool):
        Save the neutral atom density to ``densityPath`` if True, and do not save otherwise.
    potential_return (bool):
        Save the potential to ``densityPath`` if True, and do not save otherwise.

    """

    densityPath: str = attr.ib(
        default="",
        validator=attr.validators.instance_of(str),
    )
    DMkPath: str = attr.ib(
        default="",
        validator=attr.validators.instance_of(str),
    )
    DMRPath: str = attr.ib(
        default="",
        validator=attr.validators.instance_of(str),
    )

    ground_state_density_return: bool = attr.ib(
        default=True,
        validator=attr.validators.instance_of(bool),
    )
    partial_core_density_return: bool = attr.ib(
        default=True,
        validator=attr.validators.instance_of(bool),
    )
    neutral_atom_density_return: bool = attr.ib(
        default=True,
        validator=attr.validators.instance_of(bool),
    )
    potential_return: bool = attr.ib(
        default=True,
        validator=attr.validators.instance_of(bool),
    )

    def clear_paths(self):
        self.densityPath = ""
        self.DMkPath = ""
        self.DMRPath = ""
