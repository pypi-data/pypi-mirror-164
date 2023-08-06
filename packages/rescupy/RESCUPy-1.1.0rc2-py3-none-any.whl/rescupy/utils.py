# -*- coding: utf-8 -*-
"""
Created on 2020-06-16

@author: Vincent Michaud-Rioux
"""

from pathlib import Path
from pint import Quantity, Unit
import h5py
import json
import numpy as np
import os
import re
import scipy.io as sio
import pint


ureg = pint.UnitRegistry(system="atomic")


def to_quantity(x, units=None, allow_none=True, allow_string=False, shape=None):
    if x is None and not allow_none:
        raise Exception(f"Entry x cannot be None.")
    if isinstance(x, str) and not allow_string:
        raise Exception(f"Entry x cannot be a string.")
    if isinstance(x, list):
        if all([isinstance(e, Quantity) for e in x]):
            x = Quantity.from_list(x)
    if x is None or isinstance(x, Quantity):
        pass
    elif isinstance(x, str):
        if units is None:
            raise Exception(f"x cannot be a string without units.")
        return (x, units)
    elif isinstance(x, dict):
        if x["__class__"] == "Quantity":
            return to_quantity(
                x["magnitude"],
                x["units"],
                allow_string=allow_string,
                allow_none=allow_none,
                shape=shape,
            )
        else:
            cls = x["__class__"]
            raise Exception(f"Invalid class {cls}.")
    elif isinstance(x, tuple):
        return to_quantity(
            x[0],
            units=x[1],
            allow_string=allow_string,
            allow_none=allow_none,
            shape=shape,
        )
    elif units is None:
        raise Exception(f"Invalid None units.")
    else:
        x *= ureg(units)
    if shape is not None:
        if isinstance(x, list):
            x = Quantity.from_list(x)
        x = np.reshape(x.astype(float), shape, order="F")
    return x


def add_ext(s, ext):
    return os.path.splitext(s)[0] + "." + ext


def dict_converter(d, obj):
    if isinstance(d, dict):
        return obj(**d)
    if isinstance(d, obj):
        return d
    else:
        raise TypeError(f"Object of {d.__class__} must be of {obj}")


def is_array_like(var):
    ial = isinstance(var, np.ndarray)
    ial = ial or isinstance(var, list)
    ial = ial or isinstance(var, tuple)
    ial = ial or (isinstance(var, Quantity) and is_array_like(var.m))
    return ial


def is_row_vector(a, len=3):
    na = np.array(a, dtype=object)
    if na.size != len:
        return False
    rv = True
    c = 0
    while rv and c < na.size:
        if not isinstance(na[c], float):
            rv = False
        c += 1
    return rv


def fermi_dirac(dE, T):
    # dE: eV
    # T : Kelvin
    kb = 8.617333262e-5  # eV / K
    kT = kb * T
    de_kt = dE / kT
    if de_kt > 10.0:
        return 0.0
    elif de_kt < -10.0:
        return 1.0
    else:
        return 1.0 / (1.0 + np.exp(de_kt))


def load_dcal(filename, varname=None):
    try:
        fmt = "mat"
        data = sio.loadmat(filename)
        data = data["data"][0]
        if varname is not None:
            data = data[varname][0]
    except:
        fmt = "h5"
        data = h5py.File(filename, "r")
        data = data["data"]
        if varname is not None:
            if not varname in data.keys():
                raise Exception(f"{varname} not found in {filename}")
            if "MATLAB_empty" in data[varname].attrs.keys():
                if data[varname].attrs.get("MATLAB_empty"):
                    return None, fmt
            data = data[varname]
    if len(data) == 0:
        data = None
    return data, fmt


def load_dcal_var(data, varname, fmt, index):
    i = index
    if fmt == "mat":
        if index is None:
            i = 0
        var = data[0][varname][i].squeeze()
    elif index is None:
        var = data[varname][0:].squeeze()
    else:
        var = data[data[varname][i][0]][0:].flatten()
    return var


def load_dcal_parameter(data, varname, fmt, index):
    i = index
    if fmt == "mat":
        data = data[0]
        flds = list(data["Parameter"][i].dtype.names)
        if varname in flds:
            parameter = data["Parameter"][i][varname][0][0]
        else:
            parameter = None
    else:
        tmp = data[data["Parameter"][i][0]]
        flds = tmp.keys()
        if varname in flds:
            parameter = tmp[varname][0]
        else:
            parameter = None
    return parameter


def list_methods(obj):
    """Returns a list of the methods of an object.

    Source: https://stackoverflow.com/questions/1911281/how-do-i-get-list-of-methods-in-a-python-class
    """
    cls = obj.__class__
    methods = [func for func in dir(cls) if callable(getattr(cls, func))]
    return methods


def print_to_console_and_file(fileobj, line):
    print(line)
    fileobj.write(line + "\n")


class SpecialCaseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Quantity):
            return dict(
                __class__="Quantity",
                magnitude=obj.m,
                units=str(obj.u),
            )
        if isinstance(obj, np.ndarray):
            return obj.flatten(order="F").tolist()
        if isinstance(obj, Path):
            return obj.resolve().as_posix()
        return json.JSONEncoder.default(self, obj)


def clean_units(units):
    """Removes spaces and parentheses from a units string."""
    u = units
    u = u.replace(" ", "")
    u = u.replace("(", "")
    u = u.replace(")", "")
    u = u.replace("[", "")
    u = u.replace("]", "")
    u = u.replace("{", "")
    u = u.replace("}", "")
    return u


def convert_units(q, q_units, units_system):
    """Converts quantity "q" with units "units" to system "units"."""
    tmp_units, q_pow = split_units(q_units)
    tmp_units, ratios = convert_units_and_ratios(tmp_units, units_system)
    new_units = create_units_string(tmp_units, q_pow)
    if isinstance(q, list):
        q = [convert_units(s, q_units, units_system)[0] for s in q]
        return q, new_units
    elif isinstance(q, dict):
        for k in q.keys():
            q[k], dum = convert_units(q[k], q_units, units_system)
        return q, new_units
    if q is not None:
        q_out = q * np.prod(ratios**q_pow)
        return q_out, new_units
    return q, new_units


def convert_units_and_ratios(units, units_system):
    """Converts units to a system of units and return units numerical ratio."""
    from rescupy.data.units import units_dict

    new_units = []
    ratios = np.ones(len(units))
    for u, i in zip(units, range(len(units))):
        if u in ["ang", "bohr"]:
            if units_system == "atomic":
                new_units.append("bohr")
            elif units_system == "si":
                new_units.append("ang")
            else:
                raise Exception(f"Invalid units system {units_system}.")
            ratios[i] = units_dict[u] / units_dict[new_units[i]]
        elif u in ["ev", "ha"]:
            if units_system == "atomic":
                new_units.append("ha")
            elif units_system == "si":
                new_units.append("ev")
            else:
                raise Exception(f"Invalid units system {units_system}.")
            ratios[i] = units_dict[u] / units_dict[new_units[i]]
        else:
            raise Exception(f"Invalid units {u}.")
    return tuple(new_units), ratios


def create_units_string(units, powers):
    """Converts a list of base units and powers into a product of powers of units."""
    tmp = ""
    for u, p in zip(units, powers):
        if p == 1:
            tmp += f"*{u}"
        else:
            tmp += f"*{u}^{p}"
    return tmp[1:]


def fix_units(units):
    """Fix units case and contracts keywords.s"""
    if isinstance(units, tuple):
        return tuple([fix_units(u) for u in units])
    lu = units.lower()
    if lu in ["ang", "angstrom"]:
        return "ang"
    elif lu in ["bohr"]:
        return "bohr"
    elif lu in ["ev", "electronvolt"]:
        return "ev"
    elif lu in ["ha", "hartree"]:
        return "ha"
    else:
        raise Exception(f"Invalid units {units}.")


def split_units(units):
    """Splits a units string into unique units and powers."""
    ul, pl = split_units_core(units)
    ul = fix_units(ul)
    ul = list(ul)
    ul, pl = zip(*sorted(zip(ul, pl)))
    uu = list(dict.fromkeys(ul))
    up = np.zeros(len(uu), dtype=int)
    for u, i in zip(uu, range(len(uu))):
        for l, j in zip(ul, range(len(ul))):
            if u == l:
                up[i] += pl[j]
    return tuple(uu), up


def split_units_core(units):
    """Splits a units string into units and powers."""
    units_prod = clean_units(units)
    units_prod = units_prod.split("*")
    units_nam = []
    units_pow = np.ones(len(units_prod), dtype=int)
    for u, i in zip(units_prod, range(len(units_prod))):
        tmp = u.split("^")
        if len(tmp) == 1:
            units_nam.append(tmp[0])
        elif len(tmp) == 2:
            units_nam.append(tmp[0])
            units_pow[i] = int(tmp[1])
        else:
            raise Exception(f"Invalid units {units}.")
    return tuple(units_nam), units_pow


def read_field(filename, fieldname, convert=True):
    """
    Read a field from an HDF5 file.

    Args:
        filename (str):
            Path the the HDF5 file. For example, "nano_scf_out.h5".

        fieldname (str):
            Path of the field in the HDF5 file. For example, "potential/effective".

    Returns:
        fld (ndarray):
            3D numpy array containing the field.
    """
    from rescupy.data.units import units_dict

    f = h5py.File(filename, mode="r")
    fld = f[fieldname][0:]
    fld = np.transpose(fld, [i for i in range(fld.ndim - 1, -1, -1)])
    fld = np.asfortranarray(fld)
    if not convert:
        return fld
    if re.match("potential", fieldname):
        fld = fld * ureg.hartree
        fld.ito("eV")
    elif re.match("density", fieldname):
        fld = fld / ureg.bohr**3
        fld.ito("angstrom ** -3")
    elif re.match("ldos", fieldname):
        fld = fld / ureg.bohr**3
        fld.ito("angstrom ** -3")
    elif re.search("wavefunction", fieldname):
        fld = fld / ureg.bohr**1.5
        fld = fld[::2, :] + 1j * fld[1::2, :]
        fld.ito("angstrom ** -1.5")
    else:
        raise Exception("Unknown field type.")
    return fld


def get_chemical_symbols():
    """Returns an ordered list of atomic species."""
    chemical_symbols = [
        # not found
        "X",
        # row-1
        "H",
        "He",
        # row-2
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        # row-3
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        # row-4
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        # row-5
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        # row-6
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        # row-7
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
        "Ds",
        "Rg",
        "Cn",
        "Nh",
        "Fl",
        "Mc",
        "Lv",
        "Ts",
        "Og",
    ]
    return chemical_symbols
