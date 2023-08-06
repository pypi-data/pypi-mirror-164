# -*- coding: utf-8 -*-
"""
Created on 2020-08-27

@author: Vincent Michaud-Rioux
"""

import numpy as np


def readxyz_spin(filename):
    """Reads an xyz file and returns the spin.

    The first two lines are the number of atoms and a comment. To parse spin,
    the function assumes the comment has four tags (usually species, x, y, z)
    and then sx, sy, sz at some point. The position of sx, sy, sz or sr, st, sp indicates
    which column has which spin.

    Args:
        filename (str):
            Path of the xyz file.

    Returns:
        spins (array):
            2D array of the spins in Cartesian format. If no spin is found, then
            None is returned. If only sz is found then a 1D array of spin-z is
            returned. If any of sx, sy, sz are found then a 2D array of spins
            is returned. If any of sr, st, sp are found then a 2D array of spins
            is returned.

    """
    f = open(filename, "r")

    lines = f.readlines()
    natoms = int(lines[0])
    comment = lines[1].strip().split()
    if not any([s in comment for s in ["sx", "sy", "sz", "sr", "st", "sp"]]):
        return None, None
    if any([s in comment for s in ["sx", "sy", "sz"]]) and any(
        [s in comment for s in ["sr", "st", "sp"]]
    ):
        raise Exception(
            "Cannot specify spin in both Cartesian and spherical coordinates."
        )
    if "sx" in comment:
        isx = comment.index("sx")
    else:
        isx = None
    if "sy" in comment:
        isy = comment.index("sy")
    else:
        isy = None
    if "sz" in comment:
        isz = comment.index("sz")
    else:
        isz = None
    if "sr" in comment:
        isr = comment.index("sr")
    else:
        isr = None
    if "st" in comment:
        ist = comment.index("st")
    else:
        ist = None
    if "sp" in comment:
        isp = comment.index("sp")
    else:
        isp = None
    if any([s in comment for s in ["sx", "sy", "sz"]]):
        iscart = True
        coordinates = "Cartesian"
    else:
        iscart = False
        coordinates = "spherical"
    if isx is None and isy is None and ist is None and isp is None:
        iscollinear = True
        spins = np.zeros((natoms, 1))
    else:
        iscollinear = False
        spins = np.zeros((natoms, 3))
    for l in range(2, 2 + natoms):
        line = lines[l].split()
        if iscollinear:
            if iscart:
                spins[l - 2, 0] = float(line[isz])
            else:
                spins[l - 2, 0] = float(line[isr])
            continue
        if iscart:
            if isx is not None:
                spins[l - 2, 0] = float(line[isx])
            if isy is not None:
                spins[l - 2, 1] = float(line[isy])
            if isz is not None:
                spins[l - 2, 2] = float(line[isz])
        else:
            if isr is not None:
                spins[l - 2, 0] = float(line[isr])
            if ist is not None:
                spins[l - 2, 1] = float(line[ist])
            if isp is not None:
                spins[l - 2, 2] = float(line[isp])
    f.close()
    return spins, coordinates


def readxyz_doping(filename):
    """Reads an xyz file and returns the doping ratios."""
    f = open(filename, "r")
    lines = f.readlines()
    natoms = int(lines[0])
    comment = lines[1].strip().split()
    if not ("doping_ratio" in comment):
        return None
    ind = comment.index("doping_ratio")
    rates = np.zeros(natoms)
    for l in range(2, 2 + natoms):
        line = lines[l].split()
        rates[l - 2] = float(line[ind])
    f.close()
    return rates


def readxyz_pos(filename):
    """
    Reads an xyz file.

    The first two lines are the number of atoms and a comment. Then each lines has
    4 columns: species, x, y, z.

    Args:
        filename (str):
            Path of the xyz file.

    Returns:
        formula (str):
        xyz (array):
            2D array of the coordinates.

    """
    f = open(filename, "r")

    lines = f.readlines()
    natoms = int(lines[0])
    formula = ""
    xyz = np.zeros((natoms, 3))
    for l in range(2, 2 + natoms):
        symbol, x, y, z = lines[l].split()[:4]
        formula += symbol
        xyz[l - 2, :] = [float(x), float(y), float(z)]
    f.close()
    return formula, xyz
