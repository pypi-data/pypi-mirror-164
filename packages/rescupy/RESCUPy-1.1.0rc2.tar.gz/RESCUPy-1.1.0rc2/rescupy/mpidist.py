# -*- coding: utf-8 -*-
"""This module defines the ``Mpidist`` class."""


import attr
from rescupy.base import Base


@attr.s
class Mpidist(Base):
    """``Mpidist`` class.

    The ``Mpidist`` class defines parameters to control the data and computational load over MPI processes.
    RESCU+ data is distributed using a generalized block-cyclic distribution scheme.
    The 2D block-cyclic distribution is implemented in ScaLAPACK as described `here <http://www.netlib.org/utk/papers/factor/node3.html>`_.
    The main concepts here are data blocks and process-grids.
    Data block sizes determine the chunking of the data.
    Process-grids determine to which processes the data blocks are assigned.
    Usually, efficiency is optimal when process-grids have similar shape as the (distributed) array they are storing.

    Attributes:

        grdblk:
            Blocking factor for the grid. For instance, if ``grdblk`` is 10 and the domain is discretized on a ($20 \times 20 \times 20$) grid, the grid is split in eight ($10 \times 10 \times 10$) subgrids which are distributed among processes.

            Examples::

                mpi.grdblk = 8

        grdprc:
            Process grid dimensions for the grids.

            Examples::

                mpi.grdprc = [2,3,4]

        kptblk:
            Blocking factor for the k-points.

            Examples::

                mpi.kptblk = 8

        kptprc:
            Process grid dimensions for the k-points. Setting ``kptprc`` to 1 is tantamount to turning k-point parallelization off.

            Examples::

                mpi.kptprc = 1

        zptprc:
            Process grid dimensions for the energy points on complex contour. Only useful in ground state calculations for two-probe systems.

            Examples::

                mpi.zptprc = 1

        orbblk:
            Blocking factor for the atomic orbital matrices. A large value will result in load imbalance. A small value will result in high communication load. The ideal value usually lies between 32 and 128.

            Examples::

                mpi.orbblk = 32

        orbprc:
            Process grid dimensions for the atomic orbital matrices. It is usually preferable to aim at a square process grid.

            Examples::

                mpi.orbprc = [20,20]
    """

    bndblk: int = attr.ib(
        default=4, converter=int, validator=attr.validators.instance_of(int)
    )
    bndprc = attr.ib(default=None)
    grdblk: int = attr.ib(
        default=5, converter=int, validator=attr.validators.instance_of(int)
    )
    grdprc = attr.ib(default=None)
    imgblk: int = attr.ib(
        default=1, converter=int, validator=attr.validators.instance_of(int)
    )
    imgprc = attr.ib(default=None)
    kptblk: int = attr.ib(
        default=1, converter=int, validator=attr.validators.instance_of(int)
    )
    kptprc = attr.ib(default=None)
    nrgblk: int = attr.ib(
        default=1, converter=int, validator=attr.validators.instance_of(int)
    )
    nrgprc = attr.ib(default=None)
    orbblk: int = attr.ib(
        default=32, converter=int, validator=attr.validators.instance_of(int)
    )
    orbprc = attr.ib(default=None)
    zptprc = attr.ib(default=None)

    def set_bndblk(self, bndblk):
        """Sets the parameter bndblk."""
        if bndblk <= 0:
            raise Exception(
                f"Invalid value bndblk={bndblk}, bndblk must be a positive integer."
            )
        self.bndblk = bndblk

    def set_bndprc(self, bndprc):
        """Sets the parameter bndprc."""
        if bndprc <= 0:
            raise Exception(
                f"Invalid value bndprc={bndprc}, bndprc must be a positive integer."
            )
        self.bndprc = bndprc

    def set_grdblk(self, grdblk):
        """Sets the parameter grdblk."""
        if grdblk <= 0:
            raise Exception(
                f"Invalid value grdblk={grdblk}, grdblk must be a positive integer."
            )
        self.grdblk = grdblk

    def set_grdprc(self, grdprc):
        """Sets the parameter grdprc."""
        if grdprc <= 0:
            raise Exception(
                f"Invalid value grdprc={grdprc}, grdprc must be a positive integer."
            )
        self.grdprc = grdprc

    def set_imgblk(self, imgblk):
        """Sets the parameter imgblk."""
        if imgblk <= 0:
            raise Exception(
                f"Invalid value imgblk={imgblk}, imgblk must be a positive integer."
            )
        self.imgblk = imgblk

    def set_imgprc(self, imgprc):
        """Sets the parameter imgprc."""
        if imgprc <= 0:
            raise Exception(
                f"Invalid value imgprc={imgprc}, imgprc must be a positive integer."
            )
        self.imgprc = imgprc

    def set_kptblk(self, kptblk):
        """Sets the parameter kptblk."""
        if kptblk <= 0:
            raise Exception(
                f"Invalid value kptblk={kptblk}, kptblk must be a positive integer."
            )
        self.kptblk = kptblk

    def set_kptprc(self, kptprc):
        """Sets the parameter kptprc."""
        if kptprc <= 0:
            raise Exception(
                f"Invalid value kptprc={kptprc}, kptprc must be a positive integer."
            )
        self.kptprc = kptprc

    def set_nrgblk(self, nrgblk):
        """Sets the parameter nrgblk."""
        if nrgblk <= 0:
            raise Exception(
                f"Invalid value nrgblk={nrgblk}, nrgblk must be a positive integer."
            )
        self.nrgblk = nrgblk

    def set_nrgprc(self, nrgprc):
        """Sets the parameter nrgprc."""
        if nrgprc <= 0:
            raise Exception(
                f"Invalid value nrgprc={nrgprc}, nrgprc must be a positive integer."
            )
        self.nrgprc = nrgprc

    def set_orbblk(self, orbblk):
        """Sets the parameter orbblk."""
        if orbblk <= 0:
            raise Exception(
                f"Invalid value orbblk={orbblk}, orbblk must be a positive integer."
            )
        self.orbblk = orbblk

    def set_orbprc(self, orbprc):
        """Sets the parameter orbprc."""
        if orbprc <= 0:
            raise Exception(
                f"Invalid value orbprc={orbprc}, orbprc must be a positive integer."
            )
        self.orbprc = orbprc

    def set_zptprc(self, zptprc):
        """Sets the parameter zptprc."""
        if zptprc <= 0:
            raise Exception(
                f"Invalid value zptprc={zptprc}, zptprc must be a positive integer."
            )
        self.zptprc = zptprc
