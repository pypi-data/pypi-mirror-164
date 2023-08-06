# -*- coding: utf-8 -*-
"""Command module."""

import os
import shutil
from pathlib import Path, PosixPath
import subprocess

import attr
from rescupy.base import Base
import numpy as np


@attr.s
class Cmd(Base):
    """``Cmd`` class.

    Attributes:
        mpi (string):
            MPI-launcher command.
        stdout (string):
            Standard output. If specified, the standard output is redirected to
            the file specified by ``stdout`` instead of to screen.
        path (string):
            Path to the nanodcal+ and rescu+ binaries.
    """

    mpi: str = attr.ib(
        default="",
        validator=attr.validators.instance_of(str),
    )
    path: str = attr.ib(default=None)
    stdout = attr.ib(default=None)

    def __attrs_post_init__(self):
        return
        #    if self.path is not None:
        #        self.set_path(self.path)

    def set_path(self, path):
        if isinstance(path, PosixPath):
            tmp = str(path).split(":")
        elif isinstance(path, str):
            tmp = path.split(":")
        else:
            if not isinstance(path, list):
                raise Exception(
                    f"Invalid object of type {path.__class__.__name__}, must be a str or PosixPath."
                )
            tmp = path
        tmp = [Path(p) for p in tmp]
        for p in tmp:
            if not p.exists():
                raise Exception(f"Failed to set path, directory {p} does not exist.")
        self.path = tmp

    def get_cmd(self, cmdname):
        """Generates NanoDCAL+ or RESCU+ command for a binary of type ``cmdname``.

        For instance, if ``cmdname = scf``, then it searches for ``nanodcalplus_scf``
        and ``rescuplus_scf`` in the path. Then it wraps it with an mpi-launcher
        command or script, which gives ``mpiexec -n 4 rescuplus_scf``.
        """
        # search, in order, RESCU+ or NanoDCAL+ binary to update path
        binfound = False
        if cmdname in ("bsu"):
            codenames = ["rescuplus"]
        elif cmdname in ("2prb", "trsm"):
            codenames = ["nanodcalplus"]
        else:
            codenames = ["nanodcalplus", "rescuplus"]
        for codename in codenames:
            binname = f"{codename}_{cmdname}"
            if self.path is not None:
                for p in self.path:
                    cmd = Path(p) / f"{binname}"
                    if cmd.exists():
                        binfound = True
                        break
            if binfound:
                break
            fpath = shutil.which(f"{binname}")
            if fpath is None:
                continue
            else:
                binfound = True
                self.path = [Path(fpath).parent]
                break

        if not binfound:
            binnames = [f"{codename}_{cmdname}" for codename in codenames]
            if len(binnames) == 1:
                binnames = binnames[0]
            else:
                binnames = " or ".join(binnames)
            raise Exception(
                f"Cannot find binary {binnames}. Please make sure it is installed and in your PATH."
            )

        # make sure binary exists and executable
        binfound = False
        for codename in codenames:
            if binfound:
                break
            binname = f"{codename}_{cmdname}"
            cmd = None
            for p in self.path:
                cmd = Path(p) / f"{binname}"
                if cmd.exists():
                    binfound = True
                    break

        if cmd is None:
            raise Exception(f"{binname} not found in {cmd.parent}.")

        if not os.access(cmd, os.X_OK):
            raise Exception(f"{binname} found but not executable.")

        # create launch command and return binname
        if self.stdout is None:
            function = lambda file: subprocess.run(
                f"{self.mpi} {cmd} -i {file}".split()
            )
        else:
            f = open(self.stdout, "a")
            function = lambda file: subprocess.run(
                f"{self.mpi} {cmd} -i {file}".split(),
                stdout=f,
                stderr=subprocess.STDOUT,
            )
        return function, binname
