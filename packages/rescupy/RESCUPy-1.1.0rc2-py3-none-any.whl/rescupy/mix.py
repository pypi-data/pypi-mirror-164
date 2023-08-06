# -*- coding: utf-8 -*-
"""This module defines the ``Mix`` class."""

from rescupy.base import Base
import attr
import numpy as np
import warnings


@attr.s
class Mix(Base):
    """``Mix`` class.

    Attributes:
        alpha:
            Mixing fraction. ``alpha`` should be a parameter in the interval [0, 1].
            The closer it is to 0, the more stable the convergence of the solver.
            The closer it is to 1, the faster the convergence of the solver.

            Examples::

                mix.alpha = 0.45

        eres:
            On exit, array containing the total energy residuals.

        etol:
            Total energy tolerance.

        imem:
            Maximal number of trial functions retained to compute the new trial function
            in the mixer. For example, in a calculation doing density mixing with
            mix.imem = 10, the mixer will estimate the next trial density based on
            the densities of the last 10 iterations.

            Examples::

                mix.imem = 10

        maxit:
            Maximal number of iterations. Note that the Kohn-Sham solver will
            return an answer even if it has not converged, which can then be use for restart.

            Examples::

                mix.maxit = 50

        method:
            ``method`` takes the following values:

                * "lin": linear mixing.
                * "pul": `Pulay mixing <https://doi.org/10.1016%2F0009-2614%2880%2980396-4>`_.

            Examples::

                mix.method = "pul"

        metric:
            Quasi-Newton methods perform inner products, which can be calculated
            straightforwardly using the identity metric ("eye"). Kresse and Furthmuller have
            however suggested using the `Kerker metric <https://doi.org/10.1016/0927-0256(96)00008-0>`_ ("ker") .

            ``metric`` takes the following values:
                    * ``eye``: identity metric.
                    * ``ker``: Kerker-like metric

            Examples::

                mix.metric = "eye"

        monitored_variables:
            Array of integer giving which variables are monitored and used to determine convergence.

                * 1: monitor density.
                * 2: monitor total energy.

        precond:
            Initial inverse Jacobian. The initial inverse Jacobian is necessary in quasi-Newton methods.
            It is by default "eye" (the identity), in which case the initial inverse Jacobian is ``alpha I``,
            where ``alpha`` = mix.alpha. It can also be "ker"
            (for `Kerker <https://doi.org/10.1103/PhysRevB.23.3082>`_).

            Examples::

                mix.precond = "ker"

        res:
            On exit, array containing the density residuals.

        tol:
            In self-consistent calculations, the convergence procedure stops if the change
            in density per electron becomes smaller than ``tol``.
            In equations,

                .. math:: \delta d = \int \|d_{i}^{out} - d_{i}^{in}\| / N^{el}.


            Examples::

                mix.tol = 1e-6

        type:
            Determine which quantity to mix. Only density ("den") can be mixed currently.

            Examples::

                mix.type = "den"
    """

    alpha: float = attr.ib(default=0.2, validator=attr.validators.instance_of(float))
    converged: bool = attr.ib(
        default=False, validator=attr.validators.instance_of(bool)
    )
    eres = attr.ib(default=None)
    etol: float = attr.ib(default=1e-8, validator=attr.validators.instance_of(float))
    imem: int = attr.ib(default=20, validator=attr.validators.instance_of(int))
    iter: int = attr.ib(default=0, validator=attr.validators.instance_of(int))
    maxit: int = attr.ib(default=100, validator=attr.validators.instance_of(int))
    method: str = attr.ib(default="pul", validator=attr.validators.instance_of(str))
    metric: str = attr.ib(default="eye", validator=attr.validators.instance_of(str))
    monitored_variables: list = attr.ib(
        default=[1], validator=attr.validators.instance_of(list)
    )
    precond: str = attr.ib(default="eye", validator=attr.validators.instance_of(str))
    res = attr.ib(default=None)
    tol: float = attr.ib(default=1e-8, validator=attr.validators.instance_of(float))
    type: str = attr.ib(default="den", validator=attr.validators.instance_of(str))

    def __attrs_post_init__(self):
        if self.imem < 1:
            raise ValueError("imem must be a positive integer")
        self._set_monitored_variables()

    def set_alpha(self, alpha):
        """Sets the mixing fraction.

        ``alpha`` should be a parameter in the interval [0, 1].
        The closer it is to 0, the more stable the convergence of the solver.
        The closer it is to 1, the faster the convergence of the solver.
        """
        if alpha < 0 or alpha > 1:
            warnings.warn(
                "alpha should be a parameter in the interval [0, 1].", UserWarning
            )
        self.alpha = alpha

    def set_etol(self, tol):
        """Sets the total energy tolerance. The tolerance is in Hartree per electron."""
        self.etol = tol
        self.monitored_variables += [2]
        self._set_monitored_variables()

    def set_imem(self, imem):
        """Sets the mixer memory.

        Maximal number of trial functions retained to compute the new trial function
        in the mixer. For example, in a calculation doing density mixing with
        ``mix.imem = 10``, the mixer will estimate the next trial density based on
        the densities of the last 10 iterations.
        """
        if imem < 1:
            raise ValueError(
                f"Invalid value imem={imem}, imem must be a positive integer."
            )
        if imem > 100:
            warnings.warn(
                "Setting imem > 100 will require a lot of memory.", UserWarning
            )
        self.imem = imem

    def set_maxit(self, maxit):
        """Sets the maximal number of iterations.

        Maximal number of iterations. Note that the Kohn-Sham solver will
        return an answer even if it has not converged, which can then be use for restart.
        """
        if maxit < 1:
            raise ValueError(
                f"Invalid value maxit={maxit}, maxit must be a positive integer."
            )
        self.maxit = maxit

    def set_method(self, method):
        """Sets the mixing method.

        ``method`` takes the following values:

                * "lin": linear mixing.
                * "pul": `Pulay mixing <https://doi.org/10.1016%2F0009-2614%2880%2980396-4>`_.
        """
        if not method in ["lin", "pul"]:
            raise ValueError(f"Invalid mixing method {method}.")
        self.method = method

    def set_metric(self, metric):
        """Sets the mixing metric.

        Quasi-Newton methods perform inner products, which can be calculated
        straightforwardly using the identity metric ("eye"). Kresse and Furthmuller have
        however suggested using the `Kerker metric <https://doi.org/10.1016/0927-0256(96)00008-0>`_ ("ker") .

        ``metric`` takes the following values:
                * ``eye``: identity metric.
                * ``ker``: Kerker-like metric.
        """
        if not metric in ["eye", "ker"]:
            raise ValueError(f"Invalid mixing metric {metric}.")
        self.metric = metric

    def set_precond(self, precond):
        """Sets the mixing precond.

        The mixing preconditioner is an initial guess for the inverse Jacobian.
        The initial inverse Jacobian is necessary in quasi-Newton methods.
        It is by default "eye" (for identity), in which case the initial inverse Jacobian is ``alpha I``,
        where ``alpha`` = mix.alpha. It can also be "ker" (for `Kerker <https://doi.org/10.1103/PhysRevB.23.3082>`_).

        ``precond`` takes the following values:
                * ``eye``: identity precond.
                * ``ker``: Kerker precond.
        """
        if not precond in ["eye", "ker"]:
            raise ValueError(f"Invalid mixing precond {precond}.")
        self.precond = precond

    def set_tol(self, tol):
        """Sets the density tolerance. The tolerance is in electron per electron."""
        self.tol = tol
        self.monitored_variables += [1]
        self._set_monitored_variables()

    def set_type(self, type):
        """Sets the mixing type.

        Determines which quantity to mix. Only density ("den") can be mixed currently.
        """
        if not type in ["den"]:
            raise ValueError(f"Invalid mixing type {type}.")
        self.type = type

    def set_monitored_variables(self, var, tol=None):
        """Sets the monitored variables. Allowed values are "density" and "energy"."""
        if var[0:3] == "den" or var[0:3] == "rho":
            self.monitored_variables += [1]
            if tol is not None:
                self.tol = tol
        elif var == "energy" or var == "etot":
            self.monitored_variables += [2]
            if tol is not None:
                self.etol = tol
        else:
            raise ValueError("monitored_variables can be 'density' or 'energy'.")
        self._set_monitored_variables()

    def _set_monitored_variables(self):
        self.monitored_variables = list(set(self.monitored_variables))
