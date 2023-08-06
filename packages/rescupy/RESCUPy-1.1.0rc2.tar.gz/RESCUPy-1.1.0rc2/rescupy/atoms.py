# -*- coding: utf-8 -*-
"""This module defines the ``Atoms`` class."""

from attr import field
from nptyping import NDArray
from pathlib import Path
from pint import Quantity
from rescupy.base import Base
from rescupy.geometry import cart2sphe
from rescupy.io.xyz import readxyz_pos, readxyz_spin, readxyz_doping
from rescupy.species import Species, label_to_symbol
from rescupy.utils import to_quantity, ureg
from scipy.spatial import distance_matrix, cKDTree
from typing import Any, List
import attr
import numpy as np


def to_quantity_positions(x):
    shape = (-1, 3)
    return to_quantity(x, "angstrom", allow_none=True, allow_string=True, shape=shape)
    # if isinstance(x, Quantity):
    #     return x
    # if isinstance(x, str):
    #     return x
    # if isinstance(x, tuple):
    #     if isinstance(x[0], str):
    #         return x
    #     unit = x[1]
    #     x = np.array(x[0], dtype=float).reshape(shape, order="F")
    #     return to_quantity(x, unit)
    # else:
    #     x = np.array(x, dtype=float).reshape(shape, order="F")
    #     return to_quantity(x, "angstrom")


@attr.s
class Atoms(Base):
    """
    ``Atoms`` class.

    The ``Atoms`` class describes the atomic configuration: positions and species of the atoms.
    It also contains information about the charge of the system.

    Attributes:
        fractional_positions (2D array, string):
            Fractional coordinates of each atom. May be an array of row-vectors or the path to an xyz formatted file.

            Examples::

                atoms.fractional_positions = [[0,0,0],[0.25,0.25,0.25]]
                atoms.fractional_positions = "surface.xyz"
        positions (2D array, string):
            Cartesian coordinates of each atom. May be an array of row-vectors or the path to an xyz formatted file.

            Examples::

                atoms.positions = [[0,0,0],[1.43,1.43,1.43]]
                atoms.positions = "surface.xyz"
        species (list of ``Species``):
            Object containing species related parameters.

            Examples::

                atoms.species_indices = [0,1]
        species_indices (1D array):
            Species index of each atom (atom <==> species correspondence).
        ionic_charge (float):
            Total ionic charge.
        initial_magnetic_moment (float):
            Initial magnetic moment.
        initial_magnetic_moments (float):
            Initial magnetic moments.
        valence_charge (float):
            Total valence charge.

            Examples::

                atoms.valence_charge = 63
    """

    # intialise with list of dictionnaries for species
    species: List[Species] = attr.ib(
        default=None,
        # converter=lambda d: [Species(**d[i]) for i in range(len(d))],
        # validator=attr.validators.optional(attr.validators.deep_iterable(
        #     member_validator=attr.validators.instance_of(Species),
        #     iterable_validator=attr.validators.instance_of(list),
        # )),
    )
    formula: str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
    )
    fractional_positions = attr.ib(
        default=None,
    )
    ionic_charge: float = attr.ib(
        default=None,
        converter=attr.converters.optional(float),
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    initial_magnetic_moment: float = attr.ib(
        default=0.0,
        converter=attr.converters.optional(float),
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    initial_magnetic_moments = attr.ib(
        default=None,
    )
    total_magnetic_moment: float = attr.ib(
        default=0.0,
        converter=attr.converters.optional(float),
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    magnetic_moments = attr.ib(
        default=None,
    )
    magnetic_radii: Quantity = attr.ib(
        default=1.4,
        converter=lambda x: to_quantity(x, "angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    numspc: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
    )
    positions: Quantity = field(
        default=None,
        converter=attr.converters.optional(to_quantity_positions),
        validator=attr.validators.optional(
            attr.validators.instance_of((Quantity, tuple, str))
        ),
    )
    species_indices: NDArray[(Any,), np.int64] = attr.ib(
        default=None,
    )
    doping_ratios = attr.ib(default=None)
    valence_charge: float = attr.ib(
        default=None,
        converter=attr.converters.optional(float),
        validator=attr.validators.optional(attr.validators.instance_of(float)),
    )
    fractional_positions_shape = attr.ib(default=(-1, 3))
    initial_magnetic_moments_shape = attr.ib(default=None)
    magnetic_moments_shape = attr.ib(default=None)
    positions_shape = attr.ib(default=(-1, 3))

    def __attrs_post_init__(self):
        if self.positions is None and self.fractional_positions is None:
            Exception("The keyword atoms.positions must be specified.")
        self._read_fractional_positions()
        self._read_positions()
        self._read_initial_magnetic_moments()
        self._read_doping_ratios()

        natm = self.get_number_of_atoms()
        self.initial_magnetic_moments_shape = (natm, -1)
        self.magnetic_moments_shape = (natm, -1)
        self._reshape()

        if self.species is None:
            specs = self.get_species_labels()
            self.species = [Species(label=s) for s in specs]
        else:
            species = []
            for s in self.species:
                if isinstance(s, dict):
                    species.append(Species(**s))
                elif isinstance(s, Species):
                    species.append(s)
                else:
                    raise Exception("Invalid species input.")
            self.species = species
        if self.formula is None:
            self.formula = self.get_formula()
        if self.species_indices is None:
            self.species_indices = self.get_species_indices()
        self.species_indices = np.array(self.species_indices)

        if self.doping_ratios is None:
            self.doping_ratios = np.ones(self.species_indices.size)

        if self.formula is None and self.species_indices is None:
            raise Exception("The keyword formula must be specified.")
        self.numspc = self.get_number_of_species()

        if self.magnetic_radii is None:
            natm = self.get_number_of_atoms()
            self.magnetic_radii = 1.2 * np.ones((natm), order="F")

        self._species_post_init()

    def add_species(self, species):
        """Add a new species to the ``Atoms`` object.

        The input ``Species`` object is directly appended to the species list.

        Args:
            species (``Species``):
                A properly initialized species object.
        """
        self.species.append(species)
        self.numspc += 1

    def get_formula(self, format=None):
        """Returns the material's formula.

        Args:
            format (str, optional):
                If format is not None, then recomputes the formula.

        Returns:
            formula (str):
                The material's formula.

        """
        if self.formula is not None and format is None:
            return self.formula
        # read species_indices by calling _read_fractional_positions or _read_positions
        self.get_species_indices()
        if self.formula is None and self.species_indices is None:
            raise Exception("Cannot determine formula from None species_indices.")
        formula = ""
        i = 0
        while i < len(self.species_indices):
            s = self.species_indices[i]
            tmp = self.species[s].label
            i += 1
            j = 1
            while (
                i < len(self.species_indices)
                and self.species_indices[i - 1] == self.species_indices[i]
            ):
                j += 1
                i += 1
            if j > 1:
                tmp += f"({j})"
            formula += tmp
        return formula

    def get_ionic_charges(self):
        """Returns the ionic charge of each atom based on the species information."""
        ionic = [
            self.doping_ratios[i] * self.species[self.species_indices[i]].psp.Z
            for i in range(self.species_indices.size)
        ]
        return np.array(ionic)

    """Returns the number of orbitals."""

    def get_number_of_orbitals(self):
        llist = np.array([s.get_number_of_orbitals() for s in self.species], dtype=int)
        slist = self.get_species_indices()
        return np.sum(llist[slist])

    def get_species_index(self, label):
        index = None
        for i, s in enumerate(self.species):
            if s.label == label:
                index = i
                break
        return index

    def get_species_indices(self):
        """Returns the species indices.

        For example, if the formula is "AuCu(3)" and the species labels are ["Cu", "Au"]
        the function returns [2, 1, 1, 1].

        Args:

        Returns:
            species_indices (1D array):
                Array containing the species indices.

        """
        if self.species_indices is not None:
            return self.species_indices
        if self.formula is None:
            self._read_fractional_positions()
            if self.species_indices is not None:
                return self.species_indices
            self._read_positions()
            if self.species_indices is not None:
                return self.species_indices
            raise Exception("Cannot determine species_indices from None formula.")

        def formula_2_indices(formula, dictionary):
            indices = []
            for l in sform:
                if "(" in l:
                    s = l.split("(")
                    n = s[1]
                    n = n.split(")")[0]
                    n = int(n)
                    s = s[0]
                else:
                    s = l
                    n = 1
                indices.append(sdict[s] * np.ones((n), dtype=int))
            return np.concatenate(indices)

        sform = split_formula(self.formula)
        specs = self.get_species_labels()
        sdict = dict(zip(specs, range(len(specs))))
        self.species_indices = formula_2_indices(sform, sdict)
        return self.species_indices

    def get_magnetic_moments(self):
        """Returns an array containing the magnetic moment of each atom."""
        return self.magnetic_moments

    def get_total_magnetic_moment(self):
        """Returns the total magnetic moment."""
        return self.total_magnetic_moment

    def get_label(self, idx):
        """Returns the label of the idx-th atom."""
        idx = self.species_indices[idx]
        return self.species[idx].label

    def get_labels(self):
        """Returns the labels of all atoms."""
        return [self.species[idx].label for idx in self.species_indices]

    def get_number_of_atoms(self):
        """Returns the number of atoms."""
        if self.positions is not None:
            return np.array(self.positions.m).size // 3
        elif self.fractional_positions is not None:
            return np.array(self.fractional_positions).size // 3
        else:
            raise Exception(
                "Couldn't determine the number of atoms from positions attribute."
            )

    def get_number_of_species(self):
        """Returns the number of species."""
        return len(self.species)

    def get_distance_matrix(self, cell=None, max_distance=None):
        pos = self.get_positions(cell)
        unit = pos.u
        pos = pos
        # loop over possible displacements
        dx = []
        for d in range(3):
            if cell.is_periodic(axis=d):
                dx.append([-1, 0, 1])
            else:
                dx.append([0])
        dx = np.meshgrid(*dx, indexing="ij")
        disp = np.stack(
            (dx[0].ravel(order="F"), dx[1].ravel(order="F"), dx[2].ravel(order="F")),
            axis=1,
        )
        if max_distance is None:
            # init to first unit cell distances
            distance = distance_matrix(pos.m, pos.m)
            for i in range(0, disp.shape[0]):
                if np.allclose(disp[i, :], 0):
                    continue
                ipos = self.get_positions(cell, displacement=disp[i, :])
                distance = np.minimum(distance, distance_matrix(pos.m, ipos.m))
        else:
            mytree0 = cKDTree(pos.m)
            # init to first unit cell distances
            distance = mytree0.sparse_distance_matrix(
                mytree0, max_distance, output_type="coo_matrix"
            )
            distance = distance.toarray()
            for i in range(0, disp.shape[0]):
                if np.allclose(disp[i, :], 0):
                    continue
                ipos = self.get_positions(cell, displacement=disp[i, :])
                mytree1 = cKDTree(ipos.m)
                dtmp = mytree0.sparse_distance_matrix(
                    mytree1, max_distance, output_type="coo_matrix"
                )
                dtmp = dtmp.toarray()
                # where distance is zero, update
                mask = np.logical_and(dtmp > 1e-12, distance < 1e-12)
                distance[mask] = dtmp[mask]
                # where dtmp is significant, take the minimum
                mask = dtmp > 1e-12
                distance[mask] = np.minimum(distance[mask], dtmp[mask])
        distance = distance * unit
        if not distance.is_compatible_with(unit):
            raise Exception(f"Invalid unit {unit}.")
        return distance

    def get_fractional_positions(self, cell):
        """Returns the fractional atomic positions."""
        if self.fractional_positions is None:
            if self.positions is None:
                raise Exception(
                    "Both attributes `fractional_positions` and `positions` are None."
                )
            else:
                self.fractional_positions = (
                    self.positions @ np.linalg.inv(cell.avec.m) / cell.avec.u
                )
                self.fractional_positions.ito("dimensionless")
                self.fractional_positions = self.fractional_positions.m
        return self.fractional_positions

    def get_positions(self, cell, displacement=None):
        """Returns the atomic positions in Cartesian coordinates."""
        if self.positions is None:
            if self.fractional_positions is None:
                raise Exception(
                    "Both attributes `positions` and `fractional_positions` are None."
                )
            else:
                self.positions = self.fractional_positions @ cell.avec
        if displacement is not None:
            return np.matmul(
                self.get_fractional_positions(cell) + displacement, cell.avec
            )
        return self.positions

    def get_symbols(self, standard=False):
        """Returns the atomic symbols.

        Args:
            standard (bool, optional):
                If False, the species labels are returned as is.
                If True, the species labels are converted to the standard periodic table symbols.
                For instance, ['Ga1','Ga2'] will become ['Ga','Ga'].
        """
        symbols = self.get_labels()
        if standard:
            symbols = [label_to_symbol(s) for s in symbols]
        return symbols

    def get_symbol(self, idx, standard=False):
        """Returns the atomic symbol of a specific atom.

        Args:
            idx (int):
                Atom index.
            standard (bool, optional):
                If False, the species labels are returned as is.
                If True, the species labels are converted to the standard periodic table symbols.
                For instance, 'Ga1' will become 'Ga'.
        """
        symbol = self.get_label(idx=idx)
        if standard:
            symbol = label_to_symbol(symbol)
        return symbol

    def get_species_labels(self, standard=False):
        """Returns the set of species labels."""
        if self.species is not None:
            return [self.species[idx].label for idx in range(len(self.species))]
        if self.formula is None:
            raise Exception("Cannot determine species from formula.")
        sform = split_formula(self.formula)
        sform = [s.split("(")[0] for s in sform]
        # return set(sform) # random order
        return list(dict.fromkeys(sform))  # fixed order
        # symbols = self.get_symbols(standard=False)
        # return list(set(symbols))

    def set_initial_magnetic_moment(self, total_magnetic_moment):
        """Sets the total initial magnetic moment."""
        self.initial_magnetic_moment = float(total_magnetic_moment)

    def set_initial_magnetic_moments(self, magnetic_moments, coordinates="spherical"):
        """Sets the initial magnetic moments.

        The initial magnetic moments can be specified using arrays or in an xyz file.
        In non-collinear spin calculations, the columns of the arrays correspond to the
        spins in the x, y, z directions in Cartesian coordinates.
        The columns of the arrays correspond to the total spins and the angles theta
        and phi in spherical coordinates.
        In xyz files, the corresponding arrays are given as follows.
        The first two lines are the number of atoms and a comment. To parse spin,
        the function assumes the comment has four tags (usually species, x, y, z)
        and then sx, sy, sz or sr, st, sp at some point (not necessarily right after or in that order).
        The position of sx, sy, sz or sr, st, sp indicates which column has which spin component.
        For collinear spins, only sz or sr must be specified.
        Spins are automatically converted to spherical coordinates.

        Examples::

            3
            species          X          Y          Z          sx         sy         sz
                Cr  +8.021e+00 +1.039e+01 +1.039e+01  -4.999e+00  8.726e-03  3.061e-16
                Cr  +1.039e+01 +1.039e+01 +1.450e+01   3.535e+00  6.170e-03  3.535e+00
                Cr  +1.276e+01 +1.039e+01 +1.039e+01   3.535e+00  6.170e-03 -3.535e+00

        Args:
            magnetic_moments (ndarray):
                Array of initial magnetic moments. In collinear spin calculations, this
                should be a 1D array. In non-collinear spin calculations, this should be
                a 2D array. It can also be a string to an xyz file containing the spins.

            coordinates (str, optional):
                Coordinates system of the spins. Can be Cartesian or spherical.

        Returns:

        """
        natm = self.get_number_of_atoms()
        if isinstance(magnetic_moments, str):
            self.initial_magnetic_moments = magnetic_moments
            self._read_initial_magnetic_moments()
        else:
            self.initial_magnetic_moments = np.array(magnetic_moments)
            self.initial_magnetic_moments_shape = self.initial_magnetic_moments.shape
            self._reshape()
            if coordinates.lower() == "cartesian":
                self.initial_magnetic_moments = cart2sphe(self.initial_magnetic_moments)
        # check natm consistency
        if self.initial_magnetic_moments.shape[0] != natm:
            raise Exception(
                """initial_magnetic_moments must be a [n_atom] array 
                    (for collinear spin calculations) or [n_atom x 3] 
                    array (for non-collinear spin calculations)."""
            )
        # check spin consistency
        nspin = (
            self.initial_magnetic_moments.size // self.initial_magnetic_moments.shape[0]
        )
        if nspin not in [1, 3]:
            raise Exception(
                "magnetic_moments has incorrect spin dimension %d." % (nspin)
            )
        # update initial_magnetic_moment
        self.set_initial_magnetic_moment(np.sum(self.initial_magnetic_moments))

    def set_doping_ratios(self, ratios):
        if isinstance(ratios, str):
            self._read_doping_ratios(ratios)
        else:
            self.doping_ratios = np.array(ratios)
        assert len(self.doping_ratios) == self.species_indices.size
        self.set_ionic_charge()
        self.set_valence_charge()

    def set_ionic_charge(self):
        """Sets the total ionic charge based on the species information."""
        self.ionic_charge = sum(
            self.doping_ratios[i] * self.species[self.species_indices[i]].psp.Z
            for i in range(self.species_indices.size)
        )

    def set_magnetic_moments(self, magnetic_moments):
        """Sets the radii used in magnetic moment integration."""
        self.magnetic_moments = magnetic_moments

    def set_magnetic_radii(self, magnetic_radii):
        """Sets the radii used in magnetic moment integration."""
        self.magnetic_radii = magnetic_radii

    def set_pseudo_path(self, label: str, path: Path):
        path = Path(path)
        idx = self.get_species_index(label)
        if idx is not None:
            self.species[idx]._set_path(path)
        self._species_post_init()
        return

    def set_valence_charge(self, charge=None):
        """Sets the total valence charge.

        Args:
            charge (float, optional):
                Total valence charge. If None, then the total ionic charge is used
                as a default valence charge, making the system neutral.
        """
        if charge is None:
            self.valence_charge = self.ionic_charge
        else:
            self.valence_charge = charge

    def set_fractional_positions(self, fractional_positions, cell=None):
        """Sets the atomic fractional_positions."""
        self.fractional_positions = np.array(fractional_positions).reshape(
            (-1, 3), order="F"
        )
        if cell is not None:
            self._sync_positions(self.fractional_positions, cell=cell, fractional=True)

    def set_positions(self, positions, cell=None):
        """Sets the atomic positions."""
        self.positions = to_quantity_positions(positions)
        # self.positions = np.array(positions).reshape((-1, 3), order="F")
        if cell is not None:
            self._sync_positions(self.positions, cell=cell, fractional=False)

    def set_species_indices(self, species):
        """Sets the ``species_indices`` given a list of species.

        Args:
            species (list): list of species labels.
        """
        uspec = self.get_species_labels()
        if not set(species).issubset(set(uspec)):
            raise ValueError("Some species are not found in atoms.")
        self.species_indices = np.array([uspec.index(s) for s in species], dtype=int)

    def to_vacuum(self, site, keep_aob=True):
        """Converts an atom to a vacuum atom.

        The pseudopotential of the atom in question is set to zero. The atomic orbital
        basis is retained, improving the basis completeness.

        Args:
            site (int):
                Site of the atom to be converted to vacuum.
            keep_aob (bool): If ``True``, a vacuum atom with the same atomic orbital basis
                is created and introduced in place of the vacated atom; the atom is simply
                vacated otherwise.
        """
        if keep_aob:
            va = self.species[site].to_vacuum()
            self.add_species(va)
            chemsym = self.get_symbols()
            chemsym[site] = va.label
            self.set_species_indices(chemsym)
        else:
            self.fractional_positions = np.delete(
                self.fractional_positions, site, axis=0
            )
            self.positions = np.delete(self.positions, site, axis=0)
            self.species_indices = np.delete(self.species_indices, site)
        self.set_ionic_charge()
        self.set_valence_charge()

    def wrap_positions(self, cell):
        eps = 1e-8
        fpos = self.get_fractional_positions(cell)
        for d in range(3):
            if cell.is_periodic(axis=d):
                fpos[:, d] += eps
                fpos[:, d] %= 1.0
                fpos[:, d] -= eps
        self.set_fractional_positions(fpos, cell=cell)

    def write_xyz(self, filename):
        with open(filename, "w") as f:
            natm = self.get_number_of_atoms()
            f.write("%d\n\n" % (natm))
            labels = self.get_labels()
            for i in range(natm):
                pos = self.positions[i, :]
                f.write(
                    "%3s %1.11e %1.11e %1.11e\n" % (labels[i], pos[0], pos[1], pos[2])
                )

    def _read_doping_ratios(self, filename=None):
        if filename is not None:
            self.doping_ratios = readxyz_doping(filename)
            return
        if self.doping_ratios is not None:
            if isinstance(self.doping_ratios, str):
                self.doping_ratios = readxyz_doping(self.doping_ratios)
        return

    def _read_fractional_positions(self):
        if self.fractional_positions is not None:
            if isinstance(self.fractional_positions, str):
                self.formula, self.fractional_positions = readxyz_pos(
                    self.fractional_positions
                )
                self.formula = compress_formula(self.formula)
            self._reshape()
        return

    def _read_initial_magnetic_moments(self):
        if self.initial_magnetic_moments is not None:
            if isinstance(self.initial_magnetic_moments, str):
                self.initial_magnetic_moments, coordinates = readxyz_spin(
                    self.initial_magnetic_moments
                )
                ns = self.initial_magnetic_moments.shape[1]
                natm = self.initial_magnetic_moments.shape[0]
                self.initial_magnetic_moments_shape = (natm, -1)
                self._reshape()
                if ns == 3 and coordinates == "Cartesian":
                    self.initial_magnetic_moments = cart2sphe(
                        self.initial_magnetic_moments
                    )

        return

    def _read_positions(self):
        if self.positions is not None:
            unit = None
            if isinstance(self.positions, tuple):
                self.positions, unit = self.positions[0], self.positions[1]
            if isinstance(self.positions, str):
                self.formula, self.positions = readxyz_pos(self.positions)
                if unit is None:
                    self.positions = to_quantity_positions(self.positions)
                else:
                    self.positions *= getattr(ureg, unit)
                self.formula = compress_formula(self.formula)
            self._reshape()
        return

    def _init_vso(self, soc):
        for i in range(len(self.species)):
            if soc:
                self.species[i]._init_vso()
            else:
                self.species[i]._rm_vso()

    def _species_post_init(self):
        paths = [s.get_path() for s in self.species]
        if None in paths:
            return
        self.set_ionic_charge()
        self.set_valence_charge(charge=self.valence_charge)

    def _sync_positions(self, positions=None, cell=None, fractional=False):
        """Sets the atomic positions.

        Args:
            cell (``Cell``):
                ``Cell`` object to convert fractional positions to Cartesian and vice versa.
            positions (2D array, optional):
                Array of row-vectors of coordinates.
            fractional (bool, optional):
                If True, ``positions`` is assumed to be fractional, and Cartesian otherwise.
        """
        cellcp = cell.copy()
        if positions is not None:
            if fractional:
                self.fractional_positions = positions
                self.positions = None
            else:
                self.fractional_positions = None
                self.positions = positions
        if self.positions is not None:
            self.fractional_positions = (
                self.positions @ np.linalg.inv(cellcp.avec.m) / cellcp.avec.u
            )
            self.fractional_positions.ito("dimensionless")
            self.fractional_positions = self.fractional_positions.m

        elif self.fractional_positions is not None:
            self.positions = self.fractional_positions @ cellcp.avec
        else:
            raise Exception(
                "Both attributes `positions` and `fractional_positions` are None."
            )


def compress_formula(formula):
    sform = split_formula(formula)
    cform = []
    tmp0 = sform[0]
    count = 0
    for s in sform:
        if s == tmp0:
            count += 1
        else:
            if count > 1:
                cform.append(f"{tmp0}({count})")
            else:
                cform.append(f"{tmp0}")
            count = 1
            tmp0 = s
    if count > 1:
        cform.append(f"{tmp0}({count})")
    else:
        cform.append(f"{tmp0}")
    return "".join(cform)


def split_formula(formula):
    sform = []
    i = 0
    while i < len(formula):
        tmp = formula[i]
        i += 1
        while i < len(formula) and not formula[i].isupper():
            tmp += formula[i]
            i += 1
        sform.append(tmp)
    return sform
