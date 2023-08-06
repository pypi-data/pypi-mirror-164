# -*- coding: utf-8 -*-
"""This module defines the ``Solver`` class."""

from rescupy.base import Base
from rescupy.basis import Basis
from rescupy.cmd import Cmd
from rescupy.eig import Eig
from rescupy.mix import Mix
from rescupy.mpidist import Mpidist
from rescupy.restart import Restart
from rescupy.utils import dict_converter
from rescupy.utils import read_field, dict_converter
import attr


@attr.s
class Solver(Base):
    """``Solver`` class.

    Attributes:
        basis:
            Basis related parameters.
        eig:
            Eigensolver related parameters.
        mix:
            Mixer related parameters.
        mpidist:
            Mpi related parameters.
        restart:
            Restart related parameters.
    """

    basis: Basis = attr.ib(
        factory=Basis,
        converter=lambda d: dict_converter(d, Basis),
        validator=attr.validators.instance_of(Basis),
    )
    cmd: Cmd = attr.ib(
        factory=Cmd,
        converter=lambda d: dict_converter(d, Cmd),
        validator=attr.validators.instance_of(Cmd),
    )
    eig: Eig = attr.ib(
        factory=Eig,
        converter=lambda d: dict_converter(d, Eig),
        validator=attr.validators.instance_of(Eig),
    )
    mpidist: Mpidist = attr.ib(
        factory=Mpidist,
        converter=lambda d: dict_converter(d, Mpidist),
        validator=attr.validators.instance_of(Mpidist),
    )
    mix: Mix = attr.ib(
        factory=Mix,
        converter=lambda d: dict_converter(d, Mix),
        validator=attr.validators.instance_of(Mix),
    )
    restart: Restart = attr.ib(
        factory=Restart,
        converter=lambda d: dict_converter(d, Restart),
        validator=attr.validators.instance_of(Restart),
    )
    cache_self_energy = attr.ib(default=True)

    def set_mpi_command(self, cmd):
        """Sets the MPI launcher command for parallel execution.

        Args:
            cmd (str):
                MPI launcher command, for instance "mpiexec -n 16".
        """
        self.cmd.mpi = cmd

    def set_stdout(self, stdout):
        """Sets the standard output.

        Args:
            stdout (str):
                The output of Fortran binaries will be redirected to the file ``stdout``.
        """
        self.cmd.stdout = stdout
