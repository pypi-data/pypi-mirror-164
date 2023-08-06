"""
two-probe transport calculator
"""
from matplotlib import pyplot as plt
from nptyping import NDArray
from rescupy.base import Base, Quantity, to_quantity, ureg
from rescupy.current import Current
from rescupy.extpot import Region
from rescupy.twoprobe import TwoProbe
from rescupy.utils import dict_converter
from shutil import copyfile
from typing import List, Union
import attr
import numpy as np
import os


@attr.s
class IV(Base):
    """Calculator that automates the workflow of computing charge currents
    under a series of bias/gate voltages.

    Attributes:
        reference_calculator: instance of TwoProbe
        temperature
        currents: where results are stored
        k_grid_4_current: a denser k-point grid for current computation.
        work_func: work function. used in case of varying gate voltage.
        voltages: the varying voltage values
        varying_elements: list of Region objects or strings indicating what voltages are to be varied.
            The voltages associated with all the elements in the list are varied simultaneously.
            If a string is found in the list, the drain-source voltage is to be varied.
            eg. [extpot.gates[0], extpot.gates[2], "drain-source"]. In this case, Vds=Vg1=Vg2.
    """

    reference_calculator: TwoProbe = attr.ib(
        converter=lambda d: dict_converter(d, TwoProbe),
        validator=attr.validators.instance_of(TwoProbe),
    )
    voltages: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(lambda x: to_quantity(x, "eV", shape=(-1))),
        validator=attr.validators.instance_of(Quantity),
    )
    root: str = attr.ib(default=None)
    sub_dirs: List[str] = attr.ib(factory=list)
    k_grid_4_current = attr.ib(default=None)
    temperature: float = attr.ib(
        default=300.0,  # default="kelvin"
        converter=float,
        validator=attr.validators.instance_of(float),
    )
    currents: Quantity = attr.ib(
        default=None,
        converter=attr.converters.optional(
            lambda x: to_quantity(x, "ampere", shape=(-1))
        ),
        validator=attr.validators.instance_of(Quantity),
    )
    work_func: Quantity = attr.ib(
        default=0.0 * ureg.eV,
        converter=lambda x: to_quantity(x, "eV"),
        validator=attr.validators.instance_of(Quantity),
    )
    varying_elements: List[Union[str, Region]] = attr.ib(
        factory=list
    )  # pointers to reference_calculator..gates[?]

    def __attrs_post_init__(self):
        dev = self.reference_calculator.copy()
        self.reference_calculator = dev.copy()
        self._link_elements()
        if self.root is None:
            self.root = os.getcwd()
        if len(self.sub_dirs) != len(self.voltages):
            self.mk_sub_dir()

    def set_voltages(self, voltages, work_func=None):
        """sets voltage values and optionally the work function for gates
        Args:
            voltages (iterable[float]):
            work_func (float/None): work function
        """
        if work_func is not None:
            self.work_func = work_func
        self.voltages = voltages
        self.mk_sub_dir()

    def set_varying_elements(self, elements):
        """sets the elements to which the varying voltage is to be applied
        Args:
            elements (List[Region/string])
        """
        self.varying_elements = elements
        self._link_elements()

    def set_temperature(self, T):
        self.temperature = T

    def mk_sub_dir(self, dirs=None):
        if dirs is None:
            self.sub_dirs = []
            for v in self.voltages:
                self.sub_dirs.append(self._get_sub_dir(v))
        else:
            self.sub_dirs = dirs.copy()

        for d in self.sub_dirs:
            if not os.path.isdir(d):
                os.mkdir(d)

    def gen_input_files(self):
        """generate input files for each voltage value."""
        self.reference_calculator.solve_left()
        self.reference_calculator.solve_right()
        self.reference_calculator.center.solver.restart.densityPath = "center_out.h5"
        for i in range(len(self.voltages)):
            v = self.voltages[i]
            nwd = self.sub_dirs[i]  # new working directory
            self._write_py_scf(nwd)
            self._write_py_current(nwd)

            copy_or_link(
                os.path.join(self.root, "left_out.json"),
                os.path.join(nwd, "left_out.json"),
            )
            copy_or_link(
                os.path.join(self.root, "left_out.h5"), os.path.join(nwd, "left_out.h5")
            )
            if os.path.isfile(
                os.path.join(self.root, "right_out.json")
            ) and os.path.isfile(os.path.join(self.root, "right_out.h5")):
                copy_or_link(
                    os.path.join(self.root, "right_out.json"),
                    os.path.join(nwd, "right_out.json"),
                )
                copy_or_link(
                    os.path.join(self.root, "right_out.h5"),
                    os.path.join(nwd, "right_out.h5"),
                )

            for ele in self.varying_elements:
                if isinstance(ele, Region):
                    ele.val = self.work_func - v
                elif isinstance(ele, str):
                    # assuming the string == "drain"
                    self.reference_calculator.set_bias(bias=v)
                else:
                    raise Exception("Element neither a string nor Region.")
            self.reference_calculator.write(
                filename=os.path.join(nwd, "nano_2prb_in.json")
            )

        print("find input files in the following directories:")
        print(*self.sub_dirs, sep="\n")
        print(
            "run scf.py for self-consistent calculation and current.py for computing currents."
        )

    def solve(self, output="nano_iv_out"):
        """carries out self-consistent and charge current calculations at each given voltage.

        Several directories will be spawned, holding input and output files for each corresponding
        voltage value. For example, if device/ is the current work directory and the voltages are
        [0.1,0.2,0.3], then the following directories will be spawned in parallel
        device0.1/ device0.2/ device0.3/

        Find results in self.currents
        """
        self.gen_input_files()
        print("preparation done. computation starts ...")
        print(
            "You may interrupt here and run scf.py and current.py under each of the i_v_.. directories."
        )
        self.scf()
        self.calc_currents()
        self.write(filename=output + ".json")

    def scf(self):
        """Enters each of the spawned directories and launch nanodcalplus_2pb
        for self-consistent calculation
        """
        for nwd in self.sub_dirs:
            os.chdir(nwd)
            command, binname = self.reference_calculator.center.solver.cmd.get_cmd(
                "2prb"
            )
            ret = command("nano_2prb_in.json")
        os.chdir(self.root)

    def calc_currents(self):
        """Enters each of the spawned directories and carries out charge
        current calculation.
        """
        ispin = self.reference_calculator.center.system.hamiltonian.ispin
        if ispin == 2:
            self.currents = np.zeros(shape=(len(self.voltages), 2))
        else:
            self.currents = 0 * np.array(self.voltages)

        for i in range(len(self.sub_dirs)):
            os.chdir(self.sub_dirs[i])
            dev = TwoProbe.read(filename="nano_2prb_out.json")
            cal = Current.from_twoprobe(twoprb=dev)
            if self.k_grid_4_current is not None:
                cal.center.system.kpoint.set_grid(self.k_grid_4_current)
            if ispin == 2:
                (
                    self.currents[i, 0],
                    self.currents[i, 1],
                ) = cal.calc_charge_current(T=self.temperature)
            else:
                self.currents[i] = cal.calc_charge_current(T=self.temperature)
        os.chdir(self.root)
        return self.currents

    def get_currents(self):
        """collects results from each spawned directory"""
        ispin = self.reference_calculator.center.system.hamiltonian.ispin
        if ispin == 2:
            self.currents = np.zeros(shape=(len(self.voltages), 2))
        else:
            self.currents = 0 * np.array(self.voltages)

        for i in range(len(self.sub_dirs)):
            os.chdir(self.sub_dirs[i])
            cal = Current.read(filename="nano_trsm_out.json")
            if ispin == 2:
                (
                    self.currents[i, 0],
                    self.currents[i, 1],
                ) = cal.get_charge_current(T=self.temperature)
            else:
                self.currents[i] = cal.get_charge_current(T=self.temperature)
        os.chdir(self.root)
        return self.currents

    def _get_varying_voltage(self):
        vals = self.voltages.copy()
        return vals

    def _get_sub_dir(self, v):
        return os.path.join(self.root, "i_v_" + str(v))

    def _link_elements(self):
        for i in range(len(self.varying_elements)):
            ele = self.varying_elements[i]
            if isinstance(ele, dict):
                self.varying_elements[i] = Region(**ele)

        for i in range(len(self.varying_elements)):
            ele = self.varying_elements[i]
            if isinstance(ele, Region):
                f = self._find_exist_gate(ele)
                if f == -1:
                    self.reference_calculator.center.system.add_gate(region=ele)
                self.varying_elements[
                    i
                ] = self.reference_calculator.center.system.hamiltonian.extpot.gates[f]

    def plot(self, log=False, filename=None, show=True):
        """plots I-V curve"""
        self.set_units("si")
        ispin = self.reference_calculator.center.system.hamiltonian.ispin
        vals = self._get_varying_voltage()
        if log:
            currents = np.abs(self.currents)
        else:
            currents = self.currents.copy()
        fig = plt.figure()
        if ispin == 2:
            plt.plot(vals.m, currents.m[:, 0], "-k^", label="spin-majority")
            plt.plot(vals.m, currents.m[:, 1], "-kv", label="spin-minority")
            plt.legend()
        else:
            plt.plot(vals.m, currents.m, "-ko")
        if log:
            plt.yscale("log")
        plt.xlabel("Voltage (V)")
        plt.ylabel(f"Current ({self.currents.u})")
        fig.tight_layout()
        if show:
            plt.show()
        if filename is not None:
            fig.savefig(filename)
        return fig

    def _find_exist_gate(self, gate):
        existed_gates = self.reference_calculator.center.system.hamiltonian.extpot.gates
        if len(existed_gates) == 0 or existed_gates is None:
            return -1
        i = -1
        c = 0
        for gex in existed_gates:
            if (
                gex.fractional_x_range == gate.fractional_x_range
                and gex.fractional_y_range == gate.fractional_y_range
                and gex.fractional_z_range == gate.fractional_z_range
            ):
                i = c
                break
            c = c + 1
        return i

    def _write_py_scf(self, dir):
        py = """
from rescupy.twoprobe import TwoProbe
calc = TwoProbe.read(filename='nano_2prb_in.json')
calc.solve()
        """
        with open(os.path.join(dir, "scf.py"), "w") as f:
            f.write(py)

    def _write_py_current(self, dir):
        py = """
from rescupy import Current, TwoProbe
dev = TwoProbe.read(filename="nano_2prb_out.json")
cal = Current.from_twoprobe(twoprb=dev)
cal.temperature = %s
# don't forget to set a denser k-point mesh:
# cal.center.system.kpoint.set_grid(k_grid_4_current)
ispin = dev.center.system.hamiltonian.ispin
if ispin == 2:
    Iu, Id, unit = cal.calc_charge_current()
    print(f"majority spin current = {Iu}")
    print(f"minority spin current = {Id}")
    print("unit = " + unit)
else:
    Iu, unit = cal.calc_charge_current()
    print(f"current = {Iu}")
    print("unit = " + unit)
        """
        with open(os.path.join(dir, "current.py"), "w") as f:
            f.write(py % self.temperature)


def copy_or_link(src, dst):
    if os.path.exists(dst):
        os.remove(dst)
    try:
        os.symlink(src, dst)
    except OSError:
        print("symlink fails. use copy instead.")
        copyfile(src, dst)
    except:
        print("copy_or_link fails.")
