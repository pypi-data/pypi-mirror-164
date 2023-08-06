import io
import json
import toml
import numpy as np
from pathlib import Path


def read_json2dict(filename):
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
    return adict


def json_read(filename):
    fid = open(filename, "r")
    adict = json.load(fid)
    fid.close()
    return adict


def json_write(filename, adict):
    if isinstance(filename, io.TextIOWrapper):
        fid = filename
    else:
        fid = open(filename, "w")
    json.dump(adict, fid, indent=2, sort_keys=True, cls=NumpyEncoder)
    fid.close()


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.flatten().tolist()
        return json.JSONEncoder.default(self, obj)


class SpecialCaseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.flatten(order="F").tolist()
        if isinstance(obj, Path):
            return obj.resolve().as_posix()
        return json.JSONEncoder.default(self, obj)
