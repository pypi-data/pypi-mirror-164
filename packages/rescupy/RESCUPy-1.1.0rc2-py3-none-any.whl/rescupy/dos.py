# -*- coding: utf-8 -*-
"""This module defines the ``Dos`` class."""

from attr import field
from nptyping import NDArray
from pathlib import Path
from rescupy.base import Base, Quantity, to_quantity, ureg
import attr
import h5py
import numpy as np

# TODO: efermi type
# custom converters
def pdos_conv(pdos):
    if pdos is None:
        return None
    if isinstance(pdos, list):
        pdos = np.array(pdos)
    if isinstance(pdos, str):
        path = Path(pdos).absolute()
        if not path.exists():
            Warning(f"File {pdos} not found.")
            return None
        f = h5py.File(pdos, "r")
        if "total" in f["dos"]["pdos"].keys():
            pdos = f["dos"]["pdos"]["total"][0:].T
        elif "spin-up" in f["dos"]["pdos"].keys():
            pdosu = f["dos"]["pdos"]["spin-up"][0:].T
            pdosd = f["dos"]["pdos"]["spin-down"][0:].T
            pdos = np.stack((pdosu, pdosd), axis=2)
    pdos /= ureg.hartree
    return pdos.to("1 / eV")


@attr.s(auto_detect=True, eq=False)
class Dos(Base):
    """``Dos`` class.

    The ``Dos`` class stores density of states data. It is typically empty before a calculation.
    It gets overwritten during a DOS calculation.

    Attributes:
        dos:
            Density of states.

            Examples::

                dos = system.dos.dos

        efermi:
            ``efermi`` is the Fermi energy.

            Examples::

                ef = system.dos.efermi

        energy:
            Energies at which the DOS is computed.

            Examples::

                e = system.dos.energy

        interval:
            Interval on which the DOS is calculated. The interval is relative to the Fermi energy and is sampled uniformly.

            Examples::

                dos.interval = [-5.,5.]

        pdos_return:
            If ``pdos_return`` is True, the partial DOS is calculated and saved in the HDF5 file.

            Examples::

                dos.pdos_return = True

        orbA:
            Atomic index of each partial DOS. This is useful to further analyze pDOS results.

            Examples::

                orbA = system.dos.orbA

        orbL:
            Orbital angular momentum of each partial DOS. This is useful to further analyze pDOS results.

            Examples::

                orbL = system.dos.orbL

        orbM:
            z-component of the orbital angular momentum of each partial DOS. This is useful to further analyze pDOS results.

            Examples::

                orbM = system.dos.orbM

        pdos:
            Parital density of states. Each column is the pDOS of one atomic orbital.

            Examples::

                pdos = system.dos.pdos

        resolution:
            ``resolution`` gives the sampling density in the energy interval.

            Examples::

                dos.resolution = 0.01


        transmission:
    """

    dos: Quantity = field(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "1 / eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    efermi: Quantity = field(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    energy: Quantity = field(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV", shape=(-1))),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    interval: Quantity = field(
        factory=lambda: [-10.0, 10.0] * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    pdos_return: bool = field(
        default=False,
        validator=attr.validators.instance_of(bool),
    )
    orbA: NDArray = field(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(
            attr.validators.instance_of(NDArray),
        ),
    )
    orbL: NDArray = field(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(
            attr.validators.instance_of(NDArray),
        ),
    )
    orbM: NDArray = field(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(
            attr.validators.instance_of(NDArray),
        ),
    )
    pdos: Quantity = field(
        default=None,
        converter=pdos_conv,
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    resolution: Quantity = field(
        default=0.025 * ureg.eV,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV")),
        validator=attr.validators.optional(
            attr.validators.instance_of(Quantity),
        ),
    )
    transmission: NDArray = field(
        default=None,
        converter=attr.converters.optional(np.array),
        validator=attr.validators.optional(
            attr.validators.instance_of(NDArray),
        ),
    )

    def __attrs_post_init__(self):
        if self.energy is None:
            n = (self.interval[1] - self.interval[0]) / self.resolution
            n = int(np.around(n))
            self.energy = np.linspace(self.interval[0], self.interval[1], num=n + 1)
        else:
            self.set_energy(self.energy)
        if isinstance(self.dos, Quantity):
            self.dos = np.reshape(self.dos, (self.energy.size, -1), order="F")

    def set_energy(self, energy):
        self.energy = to_quantity(energy, "eV", shape=(-1), allow_none=False)
        if len(self.energy) <= 1:
            self.resolution = 0.0 * ureg.eV
        else:
            self.resolution = (self.energy[-1] - self.energy[0]) / (
                len(self.energy) - 1
            )
        self.interval = Quantity.from_list([self.energy[0], self.energy[-1]])

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented

        valid = True
        for at in (
            "dos",
            "efermi",
            "energy",
            "interval",
            "orbA",
            "orbL",
            "orbM",
            "pdos",
            "resolution",
        ):
            if getattr(self, at) is None:
                valid = valid and getattr(self, at) == getattr(other, at)
            else:
                valid = valid and np.allclose(getattr(self, at), getattr(other, at))

        return valid and (
            self.dos.u,
            self.efermi.u,
            self.energy.u,
            self.interval.u,
            self.pdos_return,
            self.pdos.u,
            self.resolution.u,
        ) == (
            other.dos.u,
            other.efermi.u,
            other.energy.u,
            other.interval.u,
            other.pdos_return,
            other.pdos.u,
            other.resolution.u,
        )
