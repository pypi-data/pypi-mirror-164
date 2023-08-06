"""
two-probe transport calculator
"""
import attr
import numpy as np
from rescupy.transmission import Transmission
from rescupy.utils import fermi_dirac, to_quantity


@attr.s
class Current(Transmission):
    """The 'Current' class manages the workflow of calculating charge currents in a two-probe system.

    Attributes:
        those of Transmission class
        temperature
    """

    Iup: float = attr.ib(default=0.0)
    Idw: float = attr.ib(default=0.0)
    temperature: float = attr.ib(
        default=300.0,  # default="kelvin"
        converter=float,
        validator=attr.validators.instance_of(float),
    )

    def solve(self, T=None):
        self.calc_charge_current(T=T)

    def calc_charge_current(self, T=None):
        """Calculate charge current.
        This method first computes the transmission of the given two-probe system, and then
        integrates across the bias window (Landauer-Büttiker formula) to get the current.
        This method triggers the ``nanodcalplus_trsm`` executable.

        Args:
            T (float): temperature
        Returns:
            I, unit (tuple[float,string]): total current and its physical unit.
            Iup, Idw, unit (tuple[float,float,string]): spin-resolved currents in the collinear
                spin case, and the unit.
        """
        self.set_units("si")
        kb = 8.617333262e-5  # eV / K
        if T is not None:
            self.temperature = T
        bias_e = -self.center.system.pop.bias
        low = min(0, bias_e) - 10 * kb * self.temperature
        hig = max(0, bias_e) + 10 * kb * self.temperature
        nreal = max(20, self.center.system.pop.nReal)
        egrid = np.linspace(low, hig, num=nreal)
        self.calc_transmission(energies=egrid)
        return self.get_charge_current()

    def get_charge_current(self, T=None):
        """Calculate charge current.
        When calling this method, the transmission calculation is assumed complete already.
        This method integrates the transmission across the bias window (Landauer-Büttiker
        formula) to get the current.

        Args:
            T (float): temperature
        Returns:
            I, unit (tuple[float,string]): total current and its physical unit.
            Iup, Idw, unit (tuple[float,float,string]): spin-resolved currents in the collinear
                spin case, and the unit.
        """
        self.set_units("si")
        if T is not None:
            self.temperature = T
        bias = self.center.system.pop.bias
        dims = np.array([0, 1, 2])
        dims = dims[dims != self.transport_axis]  # dimensions of cross section
        bc = np.array(self.center.system.cell.boundary)
        bc = bc[2 * dims]
        v0 = self.center.system.cell.avec[dims[0], :]
        v1 = self.center.system.cell.avec[dims[1], :]
        if bc[0] == 0 and bc[1] == 0:
            unit = "ampere / angstrom ** 2"
            crossec = np.linalg.norm(np.cross(v0, v1))
        elif bc[0] == 0 and bc[1] != 0:
            unit = "ampere / angstrom"
            crossec = np.linalg.norm(v0)
        elif bc[0] != 0 and bc[1] == 0:
            unit = "ampere / angstrom"
            crossec = np.linalg.norm(v1)
        else:
            unit = "ampere"
            crossec = 1.0

        if bias == 0.0:
            return to_quantity(0, unit)  # not true for thermoelectric
        if self.dos.energy.size < 2:
            print("Warning: not enough energy ampere.")
            return to_quantity(0, unit)

        eFl = 0.0  # left (source) fermi energy
        eFr = -bias  # right (drain) fermi energy
        en = self.dos.energy.copy()
        df = self.dos.energy.copy()
        for i in range(df.size):
            df[i] = fermi_dirac(en[i] - eFr, self.temperature) - fermi_dirac(
                en[i] - eFl, self.temperature
            )
        # energy integration
        e2h = 3.87404585e-5  # e ** 2/h
        dE = en[1] - en[0]
        self._reshape_transmission()
        tr = df[:, np.newaxis, np.newaxis] * self.dos.transmission  # (e,k,s)
        tr = np.sum(tr, axis=0) * (dE * e2h / crossec)  # (k,s)

        # k integration
        kwght = np.array(self.center.system.kpoint.kwght)
        trup = tr[:, 0]  # spin up
        self.Iup = np.sum(trup * kwght)
        if tr.shape[1] > 1:
            trdw = tr[:, 1]  # spin down
            self.Idw = np.sum(trdw * kwght)

        ispin = self.center.system.hamiltonian.ispin
        if ispin == 1:
            return self.Iup * 2
        elif ispin == 2:
            return self.Iup, self.Idw
        elif ispin == 4:
            return self.Iup
        else:
            raise TypeError("invalid ispin")
