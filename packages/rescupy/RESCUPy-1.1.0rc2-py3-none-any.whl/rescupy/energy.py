# -*- coding: utf-8 -*-
"""This module defines the ``Energy`` class."""

from attr import field
from pint import Quantity
from rescupy.base import Base
from rescupy.utils import to_quantity
import attr
import numpy as np


@attr.s(auto_detect=True, eq=False)
class Energy(Base):
    """``Energy`` class.

    The ``Energy`` class stores energy data. It is typically empty before a calculation.
    It gets overwritten during a calculation.

    Attributes:
        esr:
            esr is the short-range energy.
            Example::

                esr = energy.esr
        ebs:
            ebs is the band structure energy.
            Example::

                ebs = energy.ebs
        edh:
            edh is the delta Hartree energy.
            Example::

                edh = energy.edh
        efermi:
            efermi is the Fermi energy.
            Example::

                efermi = energy.efermi
        etot:
            etot is the total energy.
            Example::

                etot = energy.etot
        evxc:
            evxc is the exchange-correlation potential energy.
            Example::

                evxc = energy.evxc
        exc:
            exc is the exchange-correlation energy.
            Example::

                exc = energy.exc
        eigenvalues:
            eigenvalues is a three-dimensional array containing the Kohn-Sham energies (the eigenvalues of the Kohn-Sham equation). The dimensions are the following: bands, k-point, spin.
            Example::

                eigenvalues = energy.eigenvalues
        forces:
            forces is a two-dimensional array containing the atomic forces (as calculated by the Hellman-Feynman theorem).
            Example::

                forces = energy.forces
        forces_return:
            If True, the forces are computed and written to energy.forces. They are not computed otherwise.
            Example::

                energy.forces_return = True
        stress:
            stress is a two-dimensional array containing the stress tensor (as calculated by the Hellman-Feynman theorem).
            Example::

                stress = energy.stress
        stress_return:
            If True, the stress tensor is computed and written to energy.stress. It is not computed otherwise.
            Example::

                energy.stress_return = True
    """

    esr: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    ebg: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    ebs: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    edh: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    exc: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    evxc: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    etot: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    efermi: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    eigenvalues: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    efree: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    entropy: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    forces: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    forces_return: bool = field(
        default=False,
        converter=attr.converters.optional(bool),
        validator=attr.validators.instance_of(bool),
    )
    stress: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom ** 3"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    stress_return: bool = field(
        default=False,
        converter=attr.converters.optional(bool),
        validator=attr.validators.instance_of(bool),
    )
    eigenvalues_shape: tuple = field(default=None)
    stress_shape: tuple = field(default=(3, 3))
    forces_shape: tuple = field(default=(-1, 3))
    frc_t_shape: tuple = field(default=(-1, 3))
    frc_s_shape: tuple = field(default=(-1, 3))
    frc_vnl_shape: tuple = field(default=(-1, 3))
    frc_veff_shape: tuple = field(default=(-1, 3))
    frc_sr_shape: tuple = field(default=(-1, 3))
    frc_vna_shape: tuple = field(default=(-1, 3))
    frc_vdh_shape: tuple = field(default=(-1, 3))
    frc_rpc_shape: tuple = field(default=(-1, 3))
    frc_t: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_s: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_vnl: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_veff: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_sr: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_vna: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_vdh: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )
    frc_rpc: Quantity = field(
        default=None,
        converter=lambda x: to_quantity(x, "eV / angstrom"),
        validator=attr.validators.optional(attr.validators.instance_of(Quantity)),
    )

    def __attrs_post_init__(self):
        self._reshape()

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented

        valid = True
        for at in (
            "eigenvalues",  # arrays of floats
            "forces",
            "stress",
            "esr",  # floats
            "ebg",
            "ebs",
            "edh",
            "exc",
            "evxc",
            "etot",
            "efermi",
            "efree",
            "entropy",
        ):
            if getattr(self, at) is None:
                valid = valid and getattr(self, at) == getattr(other, at)
            else:
                valid = valid and np.allclose(getattr(self, at), getattr(other, at))
        return valid and (
            self.esr.u,
            self.ebg.u,
            self.ebs.u,
            self.edh.u,
            self.exc.u,
            self.evxc.u,
            self.etot.u,
            self.efermi.u,
            self.eigenvalues.u,
            self.efree.u,
            self.entropy.u,
            self.forces.u,
            self.forces_return,
            self.stress.u,
            self.stress_return,
        ) == (
            other.esr.u,
            other.ebg.u,
            other.ebs.u,
            other.edh.u,
            other.exc.u,
            other.evxc.u,
            other.etot.u,
            other.efermi.u,
            other.eigenvalues.u,
            other.efree.u,
            other.entropy.u,
            other.forces.u,
            other.forces_return,
            other.stress.u,
            other.stress_return,
        )

    def get_band_edges(self):
        emin = np.min(self.eigenvalues)
        emax = np.max(self.eigenvalues)
        return emin - 1, emax + 1

    def get_free_energy(self):
        """Returns the free energy."""
        return self.efree

    def get_total_energy(self):
        """Returns the total energy."""
        return self.etot

    def get_vbm(self):
        """
        Returns the energy of the highest occupied Kohn-Sham state.

        If partially occupied bands are detected, as in metals, then the function returns ``None``.
        """
        eigenvalues = self.eigenvalues
        lvals = eigenvalues < self.efermi
        if np.all(lvals == lvals[:, 0:1, 0:1]):
            vbm = np.max(eigenvalues[lvals])
        else:
            vbm = None
        return vbm
