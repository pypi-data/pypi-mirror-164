# -*- coding: utf-8 -*-
"""
Created on 2020-05-11

@author: Vincent Michaud-Rioux
"""


from rescupy.base import Base
import attr


@attr.s
class Basis(Base):
    """Basis class.

    Attributes:
        type : string
            Basis type (e.g. nao, pw).
        sprsthrs : float
            Sparsity threshold.

    """

    type: str = attr.ib(
        default="aob",
        validator=attr.validators.instance_of(str),
    )
    sprsthrs: float = attr.ib(
        default=0.15, converter=float, validator=attr.validators.instance_of(float)
    )
