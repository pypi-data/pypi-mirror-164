# -*- coding: utf-8 -*-
"""This module defines the ``System`` class."""

import attr
import numpy as np
from rescupy.atoms import Atoms
from rescupy.base import Base, to_quantity
from rescupy.cell import Cell
from rescupy.hamiltonian import Hamiltonian
from rescupy.kpoint import Kpoint
from rescupy.pop import Pop
from rescupy.utils import dict_converter, read_field, ureg
from rescupy.xc import Xc


@attr.s
class System(Base):
    """``System`` class.

    The ``System`` class contains the physical description of an atomic system.

    Examples::

        from rescupy import Atoms, Cell, System
        a = 2.818 # lattice constant (ang)
        cell = Cell(avec=[[0.,a,a],[a,0.,a],[a,a,0.]], resolution=0.12)
        fxyz = [[0.00,0.00,0.00],[0.25,0.25,0.25]]
        atoms = Atoms(fractional_positions=fxyz, formula="GaAs")
        sys = System(cell=cell, atoms=atoms)
        sys.kpoint.set_grid([5,5,5])

    Attributes:
        atoms (Atoms):
            Contains the atomic configuration description (coordinates, species, etc.)
        cell (Cell):
            Contains cell related parameters.
        hamiltonian (Hamiltonian):
            Contains Hamiltonian parameters.
        kpoint (Kpoint):
            Contains k-point related parameters.
        pop (Pop):
            Contains population (occupancy) related parameters.
        xc (Xc):
            Contains the DFT functional parameters.

    """

    # required
    atoms: Atoms = attr.ib(
        converter=lambda d: dict_converter(d, Atoms),
        validator=attr.validators.instance_of(Atoms),
    )
    cell: Cell = attr.ib(
        converter=lambda d: dict_converter(d, Cell),
        validator=attr.validators.instance_of(Cell),
    )
    # optional
    hamiltonian: Hamiltonian = attr.ib(
        factory=Hamiltonian,
        converter=lambda d: dict_converter(d, Hamiltonian),
        validator=attr.validators.instance_of(Hamiltonian),
    )
    kpoint: Kpoint = attr.ib(
        factory=Kpoint,
        converter=lambda d: dict_converter(d, Kpoint),
        validator=attr.validators.instance_of(Kpoint),
    )
    pop: Pop = attr.ib(
        factory=Pop,
        converter=lambda d: dict_converter(d, Pop),
        validator=attr.validators.instance_of(Pop),
    )
    xc: Xc = attr.ib(
        factory=Xc,
        converter=lambda d: dict_converter(d, Xc),
        validator=attr.validators.instance_of(Xc),
    )

    def __attrs_post_init__(self):
        self._finalize_init()
        self._check_init()

    def _finalize_init(self):
        #########
        # atoms #
        #########
        if self.atoms.initial_magnetic_moments is None:
            if self.hamiltonian.ispin == 4:
                natm = self.atoms.get_number_of_atoms()
                self.atoms.set_initial_magnetic_moments(np.zeros((natm, 3)))
        self.atoms._init_vso(self.hamiltonian.soc)
        self.atoms._sync_positions(cell=self.cell)

        ##########
        # kpoint #
        ##########
        self.kpoint.set_bvec(self.cell)
        self.kpoint.set_fractional_coordinates(self.kpoint.fractional_coordinates)

        # gate/dielectric fractional ranges
        for g in self.hamiltonian.extpot.gates:
            self._set_region_frac_ranges(g)
        for g in self.hamiltonian.extpot.dielectrics:
            self._set_region_frac_ranges(g)

    def _check_init(self):
        if self.pop.type in ["tm"] and self.kpoint.grid is None:
            raise Exception('kpoint.grid must be provided if pop.type == "tm"')

        if self.pop.type in ["tm"] and np.product(self.kpoint.grid) < 8:
            raise Exception(
                'kpoint.grid must be at least 2 in every dimension if pop.type == "tm"'
            )
        self._validate_positions()

    @classmethod
    def from_ase_atoms(cls, ase_atoms):
        """Returns a system object given an ASE-atoms object."""
        cell = Cell(avec=ase_atoms.get_cell().array * ureg.angstrom)
        atoms = Atoms(
            positions=ase_atoms.get_positions(),
            formula="".join(ase_atoms.get_chemical_symbols()),
        )
        sys = cls(cell=cell, atoms=atoms)
        return sys

    def get_number_of_atoms(self):
        """Returns the number of atoms."""
        return self.atoms.get_number_of_atoms()

    def get_species_labels(self):
        """Returns a list of the species labels."""
        return self.atoms.get_species_labels()

    def set_cell(self, cell):
        """Rescale avec to a specific volume."""
        self.cell = cell
        self._reset_cell()

    def set_kpoint_path(self, special_points=None, grid=None):
        """Compute k-point coordinates along the line specified in ``Kpoint`` object.

        Args:
            special_points (list):
                List of high symmetry points coordinates or label that create
            the Brillouin zone sampling.

            grid (int):
                Total number of grid points. They will be evenly distributed as possible.
        """
        self.kpoint.__init__(type="line", special_points=special_points, grid=grid)
        self.kpoint.set_bvec(self.cell)
        self.kpoint.set_kpoint_path(special_points=special_points, grid=grid)
        # reset (-1,nk,-1) quantities since shape becomes incorrect
        self.pop.__init__()

    def set_occ(self, bands, occ, num_bands=None):
        """Set the occupancies in the ``pop`` object.

        Args:
            bands (list): Two-element list giving the index range of fixed occupancies.
                The bands below the range are considered fully occupied and those above
                fully unoccupied.

            occ (3D array): Occupancies in the index range given by ``bands``.

            num_bands (int): Total number of bands in the calculation.
        """
        self.pop.set_type("fixed")
        bands = np.array(bands, dtype=int)
        nband = int(bands[1])
        nkpt = self.kpoint.get_kpoint_num()
        nspin = self.hamiltonian.get_spin_num()
        if num_bands is not None:
            nocc = np.zeros((num_bands, nkpt, nspin), order="F")
        else:
            nocc = np.zeros((nband, nkpt, nspin), order="F")
        # bands < bands[0] fully occupied
        nocc[0 : bands[0] - 1, :, :] = 1.0
        nocc[bands[0] - 1 : bands[1], :, :] = occ
        # kpt/spin factor not included
        ntot = np.sum(nocc) * 2 / nspin / nkpt
        self.pop.occ = nocc
        self.set_valence_charge(ntot)

    def set_valence_charge(self, charge, relative=False):
        """Sets the valence change to a new value.

        Update dependent attributes like the number of bands.
        """
        if relative:
            charge += self.atoms.valence_charge
        self.atoms.set_valence_charge(charge)

    def set_volume(self, v):
        """Rescale avec to a specific volume."""
        self.cell.set_volume(v)
        self._reset_cell()

    def set_fractional_positions(self, fractional_positions):
        """Sets the atomic fractional positions."""
        self.atoms.set_fractional_positions(fractional_positions, cell=self.cell)

    def set_positions(self, positions):
        """Sets the atomic positions."""
        self.atoms.set_positions(positions, cell=self.cell)

    def supercell(self, T):
        """
        Create a supercell ``System`` object from a ``System`` object.

        Args:
            T (NDArray): A (3x3) linear transformation.

        Returns:

        """
        from ase.build import make_supercell
        from rescupy.utils import ureg

        T = np.array(T)
        if T.size == 3:
            T = np.diag(T)
        isdiag = np.allclose(T, np.diag(np.diag(T)))

        sup = self.copy()
        atoms0 = self.to_ase_atoms()
        atoms1 = make_supercell(atoms0, T, wrap=True)
        sup.cell.set_avec(atoms1.cell.array * ureg.angstrom)
        grid = None
        if isdiag:
            grid = self.cell.grid * np.diag(T)
        sup.cell.set_grid(grid)
        # call before because set_positions assumes it
        sup.atoms.set_positions(atoms1.positions * ureg.angstrom, cell=sup.cell)
        sup.atoms.set_species_indices(atoms1.get_chemical_symbols())
        sup.atoms.formula = None
        sup.atoms.formula = sup.atoms.get_formula()
        sup.atoms.doping_ratios = np.tile(
            self.atoms.doping_ratios, int(np.round(np.linalg.det(T)))
        )
        sup.atoms.set_ionic_charge()
        sup.atoms.set_valence_charge()
        sup.kpoint.set_bvec(sup.cell)
        grid = None
        if isdiag:
            grid = np.ceil(self.kpoint.grid / np.diag(T)).astype(int)
        sup.kpoint.grid = grid
        sup.kpoint.set_fractional_coordinates()
        self.__dict__.update(sup.__dict__)

    def to_ase_atoms(self):
        """Returns a an ASE-atoms object corresponding to a system object."""
        from ase import Atoms

        sys = self.copy()
        sys.set_units("si")
        avec = sys.cell.avec
        pos = sys.atoms.positions
        symbols = sys.atoms.get_symbols(standard=True)
        atoms = Atoms(
            symbols,
            positions=pos.to("angstrom").m,
            cell=avec.to("angstrom").m,
            pbc=[1, 1, 1],
        )
        return atoms

    def vacate(self, site, keep_aob=True):
        """
        Replaces an atom of a ``System`` with a vacuum atom.

        Args:
            Site (int): site of the site to be vacated (0-based).
            keep_aob (bool): If ``True``, a vacuum atom with the same atomic orbital basis
                is created and introduced in place of the vacated atom; the atom is simply
                vacated otherwise.

        Returns:

        """
        self.atoms.to_vacuum(site, keep_aob=keep_aob)

    def _reset_cell(self):
        """Reset quantities related to cell after setting a new cell."""
        self.atoms.set_fractional_positions(
            self.atoms.fractional_positions, cell=self.cell
        )
        self.kpoint.set_bvec(self.cell)

    def set_open_boundary(self, dir):
        """Set the boundary condition to be the Neumann type on the surface normal to
        the given direction.
        Args:
            dir (List[string]): directions along which the Neumann boundary condition is to be set,
                eg. ["-x","+y","-z"]
        """
        Neuman = 3
        for lab in dir:
            if lab == "-x":
                self.cell.boundary[0] = Neuman
            elif lab == "+x":
                self.cell.boundary[1] = Neuman
            elif lab == "-y":
                self.cell.boundary[2] = Neuman
            elif lab == "+y":
                self.cell.boundary[3] = Neuman
            elif lab == "-z":
                self.cell.boundary[4] = Neuman
            elif lab == "+z":
                self.cell.boundary[5] = Neuman
            else:
                raise Exception("dim not recognized")

    def set_soc(self, soc):
        """Sets ``hamiltonian.soc``.

        This function automatically updates the SO pseudopotential which is not read and stored by default.
        """
        self.hamiltonian.set_soc(soc)
        self.atoms._init_vso(soc)

    def _set_region_frac_ranges(self, region):
        if region.x_range is not None:
            region.fractional_x_range = np.array(region.x_range) / self.cell.get_length(
                axis=0
            )
        if region.y_range is not None:
            region.fractional_y_range = np.array(region.y_range) / self.cell.get_length(
                axis=1
            )
        if region.z_range is not None:
            region.fractional_z_range = np.array(region.z_range) / self.cell.get_length(
                axis=2
            )

    def add_gate(self, region, work_func=0.0 * ureg.eV, Vgs=0.0 * ureg.eV):
        """Add a gate object to the system.

        Args:
            region (Region): object specifying a rectangular/parallelepipedic region in the 3d simulation box.
            work_func (float): metal work function of the gate, eg. 5.28 (eV) for gold.
            Vgs (float): gate - source voltage
            units (string): energy unit
        """
        work_func = to_quantity(work_func, "eV")
        Vgs = to_quantity(Vgs, "eV")
        eps = 1.0e-10
        Dirichlet = 2
        grid = self.kpoint.grid.copy()
        r = region.copy()
        self._set_region_frac_ranges(r)
        r.val = work_func - Vgs  # electro-potential w.r.t. source fermi energy. unit eV
        self.hamiltonian.extpot.gates.append(r)
        if (
            abs(region.fractional_x_range[0] - 0) < eps
            and abs(region.fractional_x_range[1] - 0) < eps
        ):
            self.cell.boundary[0] = Dirichlet
            grid[0] = 1
        elif (
            abs(region.fractional_x_range[0] - 1) < eps
            and abs(region.fractional_x_range[1] - 1) < eps
        ):
            self.cell.boundary[1] = Dirichlet
            grid[0] = 1
        elif (
            abs(region.fractional_y_range[0] - 0) < eps
            and abs(region.fractional_y_range[1] - 0) < eps
        ):
            self.cell.boundary[2] = Dirichlet
            grid[1] = 1
        elif (
            abs(region.fractional_y_range[0] - 1) < eps
            and abs(region.fractional_y_range[1] - 1) < eps
        ):
            self.cell.boundary[3] = Dirichlet
            grid[1] = 1
        elif (
            abs(region.fractional_z_range[0] - 0) < eps
            and abs(region.fractional_z_range[1] - 0) < eps
        ):
            self.cell.boundary[4] = Dirichlet
            grid[2] = 1
        elif (
            abs(region.fractional_z_range[0] - 1) < eps
            and abs(region.fractional_z_range[1] - 1) < eps
        ):
            self.cell.boundary[5] = Dirichlet
            grid[2] = 1
        else:
            raise Exception("Gate position unclear.")
        self.kpoint = Kpoint(grid=grid)
        self.kpoint.set_bvec(self.cell)

    def add_dielectric(self, region, epsilon=1.0):
        """Add a dielectric object to the system.

        Args:
            region (Region): object specifying a rectangular/parallelepipedic region in the 3d simulation box.
            epsilon (float): dielectric constant (relative to vacuum)
        """
        r = region.copy()
        self._set_region_frac_ranges(r)
        eq = ureg.Quantity(epsilon)
        r.val = eq.magnitude * ureg.dimensionless
        self.hamiltonian.extpot.dielectrics.append(r)

    def _validate_positions(self, min_distance=0.1, range_tol=5):
        """Validates that atoms are not too close and not too far outside the domain (cell)."""
        dtol = 1e-12 * ureg.angstrom
        fpos = self.atoms.get_fractional_positions(self.cell)
        if np.any(np.abs(fpos) > range_tol):
            raise Exception(
                """Some atom lies quite far outside the box given by cell. 
            The calculation cannot proceed. Consider using the wrap method of atoms to wrap the 
            atoms back into the first unit cell."""
            )
        atoms = self.atoms.copy()
        atoms.set_units("si")
        cell = self.cell.copy()
        cell.set_units("si")
        dmat = atoms.get_distance_matrix(cell, max_distance=min_distance)
        if np.any(dmat > dtol):
            raise Exception(
                f"""Some atoms lie within {min_distance} Ang from one another. This 
            system is unphysical, please revise your input."""
            )


def calc_magnetic_moments_collinear(cell, atoms, denpath):
    rhou = read_field(denpath, "density/spin-up").flatten(order="F")
    rhod = read_field(denpath, "density/spin-down").flatten(order="F")
    mag = rhou - rhod
    xyz = cell.get_grids()
    pos = atoms.positions
    rad = atoms.magnetic_radii
    natm = atoms.get_number_of_atoms()
    dr = cell.get_dr()
    magnetic_moments = np.zeros((natm))
    for i in range(natm):
        r = np.linalg.norm(xyz - pos[i, :], axis=1)
        mask = r < rad[i]
        magnetic_moments[i] = np.sum(mag[mask], axis=0) * dr
    return magnetic_moments


def calc_magnetic_moments_non_collinear(cell, atoms, denpath):
    rhox = read_field(denpath, "density/spin-x").reshape((-1, 1), order="F")
    rhoy = read_field(denpath, "density/spin-y").reshape((-1, 1), order="F")
    rhoz = read_field(denpath, "density/spin-z").reshape((-1, 1), order="F")
    mag = np.hstack((rhox, rhoy, rhoz))
    xyz = cell.get_grids()
    pos = atoms.positions
    rad = atoms.magnetic_radii
    natm = atoms.get_number_of_atoms()
    dr = cell.get_dr()
    magnetic_moments = np.zeros((natm, 3))
    for i in range(natm):
        r = np.linalg.norm(xyz - pos[i, :], axis=1)
        mask = r < rad[i]
        magnetic_moments[i, :] = np.sum(mag[mask, :], axis=0) * dr
    return magnetic_moments


def plot_isosurfaces(system, field, vals=None):
    """
    plot isosurface of selected wavefunction at given contour-values
        Args:
            system  (system)
            field (3d-array)
            vals (list of float): contour values
    """
    from ase.visualize import mlab

    # remove complex phase
    f_abs = np.abs(field)
    f_div = np.where(np.abs(np.angle(field)) < np.pi / 2, f_abs, -f_abs)

    if vals is None:
        # default contour value
        vals_arr = np.array([(f_abs.max() + f_abs.min()) / 2])
    else:
        vals_arr = np.array(vals)

    if np.any(f_div < 0) and np.all(vals_arr > 0):
        # show negative counterpart if any
        val_list = list(vals_arr.ravel()) + list(-vals_arr.ravel())
    else:
        val_list = list(vals_arr.ravel())

    # remove values that are out of bounds
    vals_arr = np.array(val_list)
    vals_arr = vals_arr[np.logical_and(f_div.min() < vals_arr, vals_arr < f_div.max())]
    val_list = list(vals_arr)

    # shift atoms' positions because fortran uses 1-based grid
    # whereas python assumes 0-based grid
    atoms = system.to_ase_atoms()
    grid = system.cell.grid
    uvw = atoms.get_cell()
    du = uvw[0] / grid[0]
    dv = uvw[1] / grid[1]
    dw = uvw[2] / grid[2]
    pos = atoms.get_positions() - (du + dv + dw)
    atoms.set_positions(pos)

    mlab.plot(atoms, f_div, contours=val_list)
