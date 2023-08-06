# -*- coding: utf-8 -*-
"""
Created on 2021-06-04

@author: Vincent Michaud-Rioux
"""

import attr
from rescupy.base import Base
import numpy as np
import os
import shutil

from rescupy.io.calculators import move_results
from rescupy.totalenergy import TotalEnergy
from rescupy.utils import dict_converter


@attr.s
class Relax(Base):
    """``Relax`` class.

    Examples::

        from ase.build import bulk
        from rescupy import System, TotalEnergy, Relax

        a = 5.43 # lattice constant in ang
        atoms = bulk("Si", "diamond", a=a, cubic=True)
        # move atoms around a bit
        atoms.rattle(stdev=0.05, seed=1)
        atoms.positions[0,:] = 0.

        sys = System.from_ase_atoms(atoms)
        sys.cell.set_resolution(0.2)
        sys.kpoint.set_grid([5,5,5])
        ecalc = TotalEnergy(sys)
        ecalc.solver.mix.alpha = 0.5
        ecalc.solver.set_mpi_command("mpiexec --bind-to core -n 16")
        rlx = Relax.from_totalenergy(ecalc)
        rlx.solve()

    Attributes:
        fixatoms:
            Atoms with indices in ``fixatoms`` will be kept fixed during the relaxation procedure.
        ftol:
            Force tolerance. The relaxation procedure stop once all forces are less than the tolerance.
        ftol_units:
            Force tolerance units.
        reference_calculator:
            Total energy calculator.
        restart:
            Use real space density matrix to restart between iterations.
    """

    # input is dictionary with default constructor
    reference_calculator: TotalEnergy = attr.ib(
        converter=lambda d: dict_converter(d, TotalEnergy),
        validator=attr.validators.instance_of(TotalEnergy),
    )
    fixatoms = attr.ib(default=None)
    ftol: float = attr.ib(
        default=1.0e-2,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    ftol_units: str = attr.ib(
        default="ev*ang^-1",
        validator=attr.validators.instance_of(str),
    )
    restart: bool = attr.ib(
        default=True,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
    )

    def __attrs_post_init__(self):
        return

    @classmethod
    def from_totalenergy(cls, totalenergy, **kwargs):
        if isinstance(totalenergy, TotalEnergy):
            pass
        else:
            totalenergy = TotalEnergy.read(totalenergy)
        rlx = cls(reference_calculator=totalenergy, **kwargs)
        return rlx

    def solve(self, output="nano_rlx_out.json"):
        from ase.calculators.rescuplus import Rescuplus
        from ase.constraints import FixAtoms
        from ase.io import read as ase_read
        from ase.optimize import BFGS

        # make deep copy
        rsc = self.reference_calculator.copy()
        rsc.set_units("si")
        fixatoms = self.fixatoms
        ftol = self.ftol
        restart = self.restart
        fnd_out = False
        if os.path.exists(output):
            fnd_out = True
            rsctmp = TotalEnergy.read(output)
        init_atom = True
        if os.path.exists("nano_rlx.traj") and restart:
            try:
                atoms = ase_read("nano_rlx.traj@:")
            except:
                atoms = []
            if len(atoms) > 0:
                atoms = ase_read("nano_rlx.traj@-1")
                if fnd_out and np.max(atoms.get_forces()) < ftol:
                    return
                init_atom = False
        if init_atom:
            atoms = rsc.system.to_ase_atoms()
            os.system("rm -f nano_scf_out.h5")
        # get nano_scf command
        rsccmd = "rescuplus_scf"
        if rsc.solver.cmd.mpi is not None:
            rsccmd = rsc.solver.cmd.mpi + " " + rsccmd
        rsccmd += " -i PREFIX.rsi >> resculog.out && mv nano_scf_out.json PREFIX.rso"
        if restart:
            rsc.solver.restart.DMkPath = "nano_scf_out.h5"
        rsc.energy.forces_return = True
        input_data = rsc.asdict()
        atoms.calc = Rescuplus(command=rsccmd, input_data=input_data)
        # relaxation calculation
        if fixatoms is not None:
            atoms.set_constraint(FixAtoms(indices=fixatoms))
        opt = BFGS(
            atoms,
            trajectory="nano_rlx.traj",
            restart="nano_rlx.pckl",
            logfile="nano_rlx_log.out",
        )
        # opt.replay_trajectory("nano_rlx.traj")
        opt.run(fmax=ftol)
        shutil.copy("rescuplus.rso", "nano_scf_out.json")
        fname = move_results("scf", output)
        self.reference_calculator = TotalEnergy.read(fname + ".json")
