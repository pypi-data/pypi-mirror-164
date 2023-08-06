# -*- coding: utf-8 -*-
"""This module defines the ``Eig`` class."""


from typing import List

import attr
from rescupy.base import Base
import numpy as np


@attr.s
class Eig(Base):
    """``Eig`` class.

    Attributes:
        abstol (float):
            The absolute error tolerance for the eigenvalues.

        algo (string):
            Determine the algorithm used to diagonalize the Kohn-Sham Hamiltonian, or its
            projection. For projected (dense) eigenvalue problems:

                * "d": calls the divide-and-conquer algorithm of `ScaLAPACK <http://www.netlib.org/scalapack/>`_.
                * "elpa": calls the `ELPA <https://elpa.mpcdf.mpg.de/>`_ library.
                * "mrrr": calls the MRRR routines of `ScaLAPACK <http://www.netlib.org/scalapack/>`_.
                * "x": calls the _expert_ driver of `ScaLAPACK <http://www.netlib.org/scalapack/>`_.

            In our experience "x" is both fast and robust.
            "elpa" is the fastest, especially when solving large systems (i.e. > 1000
            orbitals) and when using a lot of processes (i.e. > 100).
            However, "elpa" requires that ``mpidist.orbblk`` * ``mpidist.orbprc``
            < n, where n is the number of orbitals.

            Examples::

                eig.algo = "elpa"

        elpa_solver (string):
            Sets the ELPA library solver. Allowed values are:

                * ELPA_SOLVER_1STAGE
                * ELPA_SOLVER_2STAGE

        elpa_complex_kernel (string):
            Sets the ELPA solver complex kernel. For all allowed values, see ELPA documentation. Some allowed values are:

                * ELPA_2STAGE_COMPLEX_GENERIC
                * ELPA_2STAGE_COMPLEX_SSE_BLOCK1
                * ELPA_2STAGE_COMPLEX_AVX_BLOCK1
                * ELPA_2STAGE_COMPLEX_AVX2_BLOCK1
                * ELPA_2STAGE_COMPLEX_AVX512_BLOCK1
                * ELPA_2STAGE_COMPLEX_DEFAULT

        elpa_real_kernel (string):
            Sets the ELPA solver real kernel. For all allowed values, see ELPA documentation. Some allowed values are:

                * ELPA_2STAGE_REAL_GENERIC
                * ELPA_2STAGE_REAL_SSE_BLOCK2
                * ELPA_2STAGE_REAL_AVX_BLOCK2
                * ELPA_2STAGE_REAL_AVX2_BLOCK2
                * ELPA_2STAGE_REAL_AVX512_BLOCK2
                * ELPA_2STAGE_REAL_DEFAULT

        inclband (1D array):
            Index range of the energy bands included in the calculation.
            If ``eig.inclband = [il,iu]``, the eigensolver will seek the
            eigenvalues and/or eigenvectors with an index between il and iu. il <= iu is
            required; not all eigenpairs need to converge (see ``target_irange``).

            Examples::

                eig.inclband = [430,470]

        lwork (integer):
            Size of the work array in ScaLAPACK. If ``lwork`` is -1, then ScaLAPACK
            estimates the optimal work array size. If ``lwork`` is too small ScaLAPACK
            will compromise on precision or crash. Don't worry, it will throw at least a
            warning. If that happends, just increase the value of ``lwork`` by a factor 2
            until the message disappear.

            Examples::

                eig.lwork = 2000000

        orfac (float):
            Specifies which eigenvectors should be reorthogonalized. Eigenvectors that
            correspond to eigenvalues which are within ``tol=orfac*norm(A)`` of each other
            are to be reorthogonalized. However, if the workspace is insufficient (see
            ``lwork``), tolerance may be decreased until all eigenvectors to be
            reorthogonalized can be stored in one process. No reorthogonalization will
            be done if ``orfac`` equals zero. A default value of 1e-3 is used if ``orfac``
            is negative. ``orfac`` should be identical on all processes.

            Examples::

                eig.orfac = 1e-8

        reduAlgo (integer):
           Switch between triangular inverse (1) and ScaLAPACK's sygst (2) to reduce the
            eigenvalue problem from general to standard form. If ``algo=elpa`` then
            ``reduAlgo=3`` uses ELPA's Cannon algorithm if the number of process rows divides
            the number of process columns (see ``mpidist.orbprc``).
            This parameter impacts performance.

            Examples::

                eig.reduAlgo = 2

        target_irange (1D array):
            Index range of the energy bands that are forced to converge according to the tolerance given by ``abstol``.

            Examples::

                eig.inclband = [440,460]

    """

    # jobz (string):
    #     If jobz = 'v', eigenvectors are calculated; only eigenvalues are returned
    #     otherwise.
    # uplo (string):
    #     If uplo = 'u', the upper triangular part of the matrices are referenced; if
    #     uplo = 'l', the upper triangular part of the matrices are referenced.
    # range (string):
    #     If range = 'a', all eigenvalues are computed; if range = 'i', the eigenvalues
    #     with index in the interval (il, iu) are computed; if range = 'v', the
    #     eigenvalues
    #     with index in the interval (vl, vu) are computed.
    # ibtype (integer):
    #     Eigenvalue problem type; if ibtype = 1, solve A*x = (lambda)*B*x; if ibtype = 2,
    #     solve A*B*x = (lambda)*x; if ibtype = 3, solve B*A*x = (lambda)*x.
    # il (integer):
    #    Lower index bound.
    # iu (integer):
    #   Upper index bound.
    # vl (float):
    #    Lower value bound.
    # vu (float):
    #     Upper value bound.

    abstol: float = attr.ib(
        default=-1.0,
        converter=float,
        validator=attr.validators.instance_of(float),
    )
    algo: str = attr.ib(
        default="x",
        converter=str,
        validator=attr.validators.instance_of(str),
    )
    elpa_solver: str = attr.ib(
        default="ELPA_SOLVER_2STAGE",
        converter=str,
        validator=attr.validators.instance_of(str),
    )
    elpa_complex_kernel: str = attr.ib(
        default="ELPA_2STAGE_COMPLEX_DEFAULT",
        converter=str,
        validator=attr.validators.instance_of(str),
    )
    elpa_real_kernel: str = attr.ib(
        default="ELPA_2STAGE_REAL_DEFAULT",
        converter=str,
        validator=attr.validators.instance_of(str),
    )
    inclband: List[int] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(int),
                iterable_validator=attr.validators.instance_of(list),
            ),
        ),
    )
    lwork: int = attr.ib(
        default=-1,
        converter=int,
        validator=attr.validators.instance_of(int),
    )
    orfac: float = attr.ib(
        default=1.0e-6,
        converter=float,
        validator=attr.validators.instance_of(float),
    )
    reduAlgo: int = attr.ib(
        default=0,
        converter=int,
        validator=attr.validators.instance_of(int),
    )
    target_irange: List[int] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(int),
                iterable_validator=attr.validators.instance_of(list),
            ),
        ),
    )
    # jobz = attr.ib(default="n")
    # uplo = attr.ib(default="u")
    # range = attr.ib(default="a") ***range is function in python make sure
    # #   shadowing doesnt affect behaviour before uncommenting
    # ibtype = attr.ib(default="1.")
    # il = attr.ib(default=0)
    # iu = attr.ib(default=0)

    # def __attrs_post_init__(self):
    #     return

    def get_number_of_bands(self):
        """Returns the number of bands.

        The total number of bands usually include some bands that act as a buffer
        and hence they are not necessarily accurate. For bands satifying the
        prescribed tolerance, refer to ``target_irange``.
        """
        nbands = self.inclband[1] - self.inclband[0] + 1
        return nbands

    def set_abstol(self, abstol):
        """Sets the parameter abstol.

        The absolute error tolerance for the eigenvalues.
        """
        self.abstol = abstol

    def set_algo(self, algo):
        """Sets the parameter algo.

        Determine the algorithm used to diagonalize the Kohn-Sham Hamiltonian, or its
        projection. For projected (dense) eigenvalue problems:

            * "d": calls the divide-and-conquer algorithm of `ScaLAPACK <http://www.netlib.org/scalapack/>`_.
            * "elpa": calls the `ELPA <https://elpa.mpcdf.mpg.de/>`_ library.
            * "mrrr": calls the MRRR routines of `ScaLAPACK <http://www.netlib.org/scalapack/>`_.
            * "x": calls the _expert_ driver of `ScaLAPACK <http://www.netlib.org/scalapack/>`_.

        In our experience "x" is both fast and robust.
        "elpa" is the fastest, especially when solving large systems (i.e. > 1000
        orbitals) and when using a lot of processes (i.e. > 100).
        However, "elpa" requires that ``mpidist.orbblk`` * ``mpidist.orbprc``
        < n, where n is the number of orbitals.
        """
        self.algo = algo

    def set_elpa_solver(self, elpa_solver):
        """Sets the parameter elpa_solver.

        Allowed values are:

            * ELPA_SOLVER_1STAGE
            * ELPA_SOLVER_2STAGE
        """
        self.elpa_solver = elpa_solver

    def set_elpa_complex_kernel(self, elpa_complex_kernel):
        """Sets the parameter elpa_complex_kernel.

        For all allowed values, see ELPA documentation. Some allowed values are:

            * ELPA_2STAGE_COMPLEX_GENERIC
            * ELPA_2STAGE_COMPLEX_SSE_BLOCK1
            * ELPA_2STAGE_COMPLEX_AVX_BLOCK1
            * ELPA_2STAGE_COMPLEX_AVX2_BLOCK1
            * ELPA_2STAGE_COMPLEX_AVX512_BLOCK1
            * ELPA_2STAGE_COMPLEX_DEFAULT
        """
        self.elpa_complex_kernel = elpa_complex_kernel

    def set_elpa_real_kernel(self, elpa_real_kernel):
        """Sets the parameter elpa_real_kernel.

        For all allowed values, see ELPA documentation. Some allowed values are:

            * ELPA_2STAGE_REAL_GENERIC
            * ELPA_2STAGE_REAL_SSE_BLOCK2
            * ELPA_2STAGE_REAL_AVX_BLOCK2
            * ELPA_2STAGE_REAL_AVX2_BLOCK2
            * ELPA_2STAGE_REAL_AVX512_BLOCK2
            * ELPA_2STAGE_REAL_DEFAULT
        """
        self.elpa_real_kernel = elpa_real_kernel

    # def set_inclband(self, inclband):
    #     """Sets the parameter inclband."""
    #     self.inclband = inclband

    def set_lwork(self, lwork):
        """Sets the parameter lwork.

        Size of the work array in ScaLAPACK. If ``lwork`` is -1, then ScaLAPACK
        estimates the optimal work array size. If ``lwork`` is too small ScaLAPACK
        will compromise on precision or crash. Don't worry, it will throw at least a
        warning. If that happends, just increase the value of ``lwork`` by a factor 2
        until the message disappear.
        """
        self.lwork = lwork

    def set_orfac(self, orfac):
        """Sets the parameter orfac.

        Specifies which eigenvectors should be reorthogonalized. Eigenvectors that
        correspond to eigenvalues which are within ``tol=orfac*norm(A)`` of each other
        are to be reorthogonalized. However, if the workspace is insufficient (see
        ``lwork``), tolerance may be decreased until all eigenvectors to be
        reorthogonalized can be stored in one process. No reorthogonalization will
        be done if ``orfac`` equals zero. A default value of 1e-3 is used if ``orfac``
        is negative. ``orfac`` should be identical on all processes.
        """
        self.orfac = orfac

    def set_reduAlgo(self, reduAlgo):
        """Sets the parameter reduAlgo.

        Switch between triangular inverse (1) and ScaLAPACK's sygst (2) to reduce the
        eigenvalue problem from general to standard form. If ``algo=elpa`` then
        ``reduAlgo=3`` uses ELPA's Cannon algorithm if the number of process rows divides
        the number of process columns (see ``mpidist.orbprc``).
        This parameter impacts performance.
        """
        self.reduAlgo = reduAlgo

    def set_target_irange(self, ispin=1, target_irange=None, valence_charge=None):
        """Sets the included and target bands.

        If ``target_irange`` is not provided, the valence charge is used to determine
        the number of bands.
        """
        # fix number of target bands
        if target_irange is None and valence_charge is None:
            raise ValueError("target_irange or valence_charge cannot be both None.")
        elif target_irange is None:
            if ispin == 4:
                self.target_irange = [0, int(valence_charge) + 7]
            else:
                self.target_irange = [0, int((valence_charge + 1) // 2) + 7]
        else:
            self.target_irange = target_irange
        # fix number of included bands
        self.inclband = self.target_irange


