# -*- coding: utf-8 -*-
"""This module defines the ``Species`` class."""

from pathlib import Path
from rescupy.aobasis import NaoBasis
from rescupy.base import Base
from rescupy.orb import RadFunc
from rescupy.pspot import Pspot
from rescupy.utils import get_chemical_symbols, load_dcal
from scipy.integrate import simps
from scipy.interpolate import interp1d
import attr
import copy
import numpy as np
import os
import warnings


@attr.s
class Species(Base):
    """``Species`` class.

    The ``Species`` class stores various parameters and data pertaining to atomic species.
    It contains notably:

        - Labels.
        - Paths to pseudopotential files.
        - Atomic orbital basis functions.
        - Pseudopotentials.

    The species fields is initialized from a list of dictionaries as follows::

        system.species = [{"label": "Ga", "path": "Ga_AtomicData.mat"},
                                  {"label": "As", "path": "As_AtomicData.mat"}]

    A label tags each species and a path defines an atomic orbital basis and a pseudopotential.

    Attributes:
        label (string):
            Species label (e.g. "Si1", "Au_surf").
        charge (float):
            Electron charge.
        mass (float):
            Atomic mass.
        total_magnetic_moment (float):
            Magnetic moment (Cartesian).
        magrad (float):
            Magnetic "radius" (for mag. moment integration).
        alphaZ (float):
            Long-range energy correction (depends on unit cell volume).
        psp (float):
            Pseudopotential.
        aob (float):
            Atomic orbital basis.
        rna (float):
            Neutral atom valence density (short-range).
        vna (float):
            Neutral atom potential (short-range).
    """

    label: str = attr.ib()
    path: str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    alphaZ: float = attr.ib(default=None)
    charge = attr.ib(default=None)
    mass = attr.ib(default=None)
    total_magnetic_moment: float = attr.ib(
        default=0.0, converter=float, validator=attr.validators.instance_of(float)
    )
    magrad: float = attr.ib(
        default=1.2, converter=float, validator=attr.validators.instance_of(float)
    )
    psp = attr.ib(default=None)
    aob = attr.ib(default=None)
    rna = attr.ib(default=None)
    vna = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.path is None:
            n = 0
            if "NANODCALPLUS_PSEUDO" in os.environ:
                path = Path(os.environ["NANODCALPLUS_PSEUDO"])
                n = self._find_path_from_dir(path)
            if n == 0 and "RESCUPLUS_PSEUDO" in os.environ:
                path = Path(os.environ["RESCUPLUS_PSEUDO"])
                n = self._find_path_from_dir(path)
            if n == 0:  # when no file found in RESCUPLUS_PSEUDO
                path = Path(os.getcwd())
                n = self._find_path_from_dir(path)
            if n > 1:
                warnings.warn(
                    f"""Found more than one pseudopotential file for element {self.label}. 
                                    You may fix your atomic label (species.label), pseudopotential
                                    names, or pseudopotential path (NANODCALPLUS_PSEUDO/RESCUPLUS_PSEUDO)."""
                )
                return
            if self.path is None:
                warnings.warn(
                    "Cannot find pseudopotential file. Specify path or set NANODCALPLUS_PSEUDO/RESCUPLUS_PSEUDO."
                )
                return
        self._init_pseudo()

    def get_number_of_orbitals(self):
        """Returns the number of orbitals."""
        return self.aob.get_number_of_orbitals()

    def _set_path(self, path):
        path = Path(path)
        if not path.exists():
            raise Exception(f"Pseudopotential file {path} does not exist.")
        self.path = str(path)
        self._init_pseudo()

    def _init_pseudo(self):
        # do not update fields if they are found
        self._init_aob()
        self._init_psp()
        self._init_rna()
        self._init_vna()
        self.alphaZ = calcAlphaZ(self.psp.vlc.rgrid, self.psp.vlc.rvals, self.psp.Z)
        if self.charge is None:
            self.charge = self.psp.Z

    def get_path(self):
        return self.path

    def _find_path_from_dir(self, dir):
        p = dir.glob("*")
        # p = path.glob('**/*')
        files = [x for x in p if x.is_file()]
        label = label_to_symbol(self.label)
        n = 0
        for f in files:
            if label_to_symbol(f.name, ignore_errors=True) == label:
                try:
                    load_dcal(f, varname=None)
                    n += 1
                    self.path = str(f)
                except:
                    continue
        return n

    def _init_aob(self):
        if not isinstance(self.aob, dict):
            self.aob = {"path": self.path}
        elif "path" not in self.aob.keys():
            self.aob["path"] = self.path
        if set(["path", "symbol", "varname"]).issubset(set(self.aob.keys())):
            self.aob = NaoBasis(**self.aob)
        else:
            self.aob = NaoBasis(
                path=self.aob["path"],
                symbol=self.aob.get("symbol", None),
                varname="OrbitalSet",
            )

    def _init_psp(self):
        if not isinstance(self.psp, dict):
            self.psp = {"path": self.path}
        elif "path" not in self.psp.keys():
            self.psp["path"] = self.path
        self.psp = Pspot(**self.psp)

    def _init_rna(self):
        if isinstance(self.rna, dict) and "path" in self.rna.keys():
            self.rna = RadFunc(**self.rna)
        else:
            self.rna = RadFunc(path=self.path, varname="Rna")

    def _init_vna(self):
        if isinstance(self.vna, dict) and "path" in self.vna.keys():
            self.vna = RadFunc(**self.vna)
        else:
            self.vna = RadFunc(path=self.path, varname="Vna")

    def _init_vso(self):
        self.psp._init_vso()

    def _rm_vso(self):
        if isinstance(self.psp, Pspot):
            self.psp._rm_vso()

    def to_vacuum(self):
        """Convert a species to its equivalent vacuum species.

        A vacuum species has zero pseudopotential but retains an atomic orbital basis.
        """
        va = copy.deepcopy(self)
        va.path = ""
        va.label += "_Va"
        va.alphaZ = 0.0
        va.charge = 0.0
        va.mass = 0.0
        va.total_magnetic_moment = 0.0
        va.aob.to_vacuum()
        va.psp.to_vacuum()
        va.rna.zero_out()
        va.vna.zero_out()
        return va


def get_path(adict):
    if "path" not in adict.keys():
        raise Exception("Input file is missing a value for parameter species.path.")
    return adict["path"]


def calcAlphaZ(rr, vv, Z):
    if rr[0] > 0.0:
        tmp = interp1d(rr, vv, kind="cubic", fill_value="extrapolate")
        x = np.array([0.0])
        rr = np.concatenate((x, rr))
        vv = np.concatenate((tmp(x), vv))
    integrand = rr**2 * vv + Z * rr
    return 4.0 * np.pi * simps(integrand, rr)


def label_to_symbol(label, ignore_errors=False):
    """Convert a label to an atomic species

    Args:
        label (string):
            Should be an atomic species plus a tag. (e.g. H1, H_surf).

    Returns:
        symbol (string):
            The best matching species from the periodic table.

    Raises:
        KeyError:
            Couldn't find an appropriate species.
    """

    chemical_symbols = get_chemical_symbols()
    # two character species
    if len(label) >= 2:
        test_symbol = label[0].upper() + label[1].lower()
        if test_symbol in chemical_symbols:
            return test_symbol
    # one character species
    test_symbol = label[0].upper()
    if test_symbol in chemical_symbols:
        return test_symbol
    elif not ignore_errors:
        raise KeyError("Could not parse species from label {0}." "".format(label))
