# -*- coding: utf-8 -*-
"""
Created on 2021-06-02

@author: Vincent Michaud-Rioux
"""
import attr
from pathlib import Path
import io
import json
import os
import shutil
import toml

from rescupy.utils import list_methods


def move_results(funname, filename):
    filename = os.path.splitext(filename)[0]
    shutil.move("nano_" + funname + "_out.json", filename + ".json")
    shutil.move("nano_" + funname + "_out.h5", filename + ".h5")
    with open(filename + ".json", "rt") as f:
        txt = f.read()
        txt = txt.replace("nano_" + funname + "_out", filename)
    with open(filename + ".json", "wt") as f:
        f.write(txt)
    return filename


def read(cls, filename, units="si"):
    if isinstance(filename, io.TextIOWrapper):
        path = Path(filename.name)
    else:
        path = Path(filename)
    if not path.exists():
        raise FileNotFoundError
    with path.open() as fid:
        if path.suffix == ".json":
            adict = json.load(fid)
        elif path.suffix == ".toml":
            adict = toml.load(fid)
        else:
            print(
                f"WARNING: Unkown extension {path.suffix}, attempting to load as json file."
            )
            adict = json.load(fid)
    atts_noneed = []
    dir_cls = [a.name for a in attr.fields(cls)]
    for att in adict.keys():
        if att not in dir_cls:
            atts_noneed.append(att)
    for att in atts_noneed:
        adict.pop(att)
    calc = cls(**adict)
    calc.set_units(units)
    if "_reshape" in list_methods(calc):
        calc._reshape()
    return calc


def solve_generic(self, funname, inputname=None, outputname=None):
    if "cmd" not in self.solver.__dict__.keys():
        raise KeyError("cmd")
    command, binname = self.solver.cmd.get_cmd(funname)
    if inputname is None:
        inputname = binname + ".json"
    else:
        inputname = os.path.splitext(inputname)[0] + ".json"
    self.write(inputname)
    ret = command(inputname)
    ret.check_returncode()
    if outputname is None:
        outputname = binname + "_out"
    else:
        outputname = move_results(funname, outputname)
    return outputname
