from numpy import pi

# CODATA 2018 taken from
# https://physics.nist.gov/cuu/Constants/index.html
units_dict = {
    "_c": 299792458.0,  # Exact
    "_mu0": 4.0e-7 * pi,  # Exact
    "_grav": 6.67430e-11,  # +/- 0.000_15e-11
    "_hplanck": 6.62607015e-34,  # Exact
    "_e": 1.602176634e-19,  # Exact
    "_me": 9.1093837015e-31,  # +/- 0.000_000_0028e-31
    "_mp": 1.67262192369e-27,  # +/- 0.000_000_000_51e-27
    "_nav": 6.02214076e23,  # Exact
    "_k": 1.380649e-23,  # Exact
    "_amu": 1.66053906660e-27,
}  # +/- 0.000_000_000_50e-27

# derived from the CODATA values
units_dict["_eps0"] = (
    1 / units_dict["_mu0"] / units_dict["_c"] ** 2
)  # permittivity of vacuum
units_dict["_hbar"] = units_dict["_hplanck"] / (2 * pi)  # Planck constant / 2pi, J s

units_dict["ang"] = units_dict["angstrom"] = 1.0
units_dict["nm"] = 10.0
units_dict["bohr"] = (
    4e10
    * pi
    * units_dict["_eps0"]
    * units_dict["_hbar"] ** 2
    / units_dict["_me"]
    / units_dict["_e"] ** 2
)  # Bohr radius
units_dict["ang^-1"] = 1.0 / units_dict["ang"]
units_dict["bohr^-1"] = 1.0 / units_dict["bohr"]

units_dict["ev"] = 1.0
units_dict["hartree"] = (
    units_dict["_me"]
    * units_dict["_e"] ** 3
    / 16
    / pi**2
    / units_dict["_eps0"] ** 2
    / units_dict["_hbar"] ** 2
)
units_dict["rydberg"] = 0.5 * units_dict["hartree"]
units_dict["ry"] = units_dict["rydberg"]
units_dict["ha"] = units_dict["hartree"]
# units_dict["kj"] = 1000.0 / units_dict["_e"]
# units_dict["kcal"] = 4.184 * units_dict["kj"]
# units_dict["mol"] = units_dict["_nav"]

units_dict["ev^-1"] = 1.0 / units_dict["ev"]
units_dict["ha^-1"] = 1.0 / units_dict["ha"]

units_dict["ev*ang^-1"] = 1.0
units_dict["ha/bohr"] = 1.0 * units_dict["ha"] / units_dict["bohr"]

units_dict["ang^3"] = 1.0
units_dict["bohr^3"] = units_dict["bohr"] ** 3

units_dict["ev*ang^-3"] = 1.0
units_dict["ha*bohr^-3"] = 1.0 * units_dict["ha"] / (units_dict["bohr"] ** 3)

# units_dict["second"] = 1e10 * sqrt(units_dict["_e"] / units_dict["_amu"])
# units_dict["fs"] = 1e-15 * units_dict["second"]

units_dict["kelvin"] = units_dict["_k"] / units_dict["_e"]  # Boltzmann constant, eV/K

units_dict["pascal"] = (1 / units_dict["_e"]) / 1e30  # J/m^3
units_dict["gpa"] = 1e9 * units_dict["pascal"]

# units_dict["debye"] = 1.0 / 1e11 / units_dict["_e"] / units_dict["_c"]
# units_dict["alpha"] = (units_dict["_e"]**2 / (4 * pi * units_dict["_eps0"]) /
#             units_dict["_hbar"] / units_dict["_c"])  # fine structure constant
# units_dict["invcm"] = (100 * units_dict["_c"] * units_dict["_hplanck"] /
#             units_dict["_e"])  # cm^-1 energy unit

# # Derived atomic units that have no assigned name:
# # atomic unit of time, s:
# units_dict["_aut"] = units_dict["_hbar"] / (units_dict["alpha"]**2 * units_dict["_me"] * units_dict["_c"]**2)
# # atomic unit of velocity, m/s:
# units_dict["_auv"] = units_dict["_e"]**2 / units_dict["_hbar"] / (4 * pi * units_dict["_eps0"])
# # atomic unit of force, N:
# units_dict["_auf"] = units_dict["alpha"]**3 * units_dict["_me"]**2 * units_dict["_c"]**3 / units_dict["_hbar"]
# # atomic unit of pressure, Pa:
# units_dict["_aup"] = units_dict["alpha"]**5 * units_dict["_me"]**4 * units_dict["_c"]**5 / units_dict["_hbar"]**3

# units_dict["aut"] = units_dict["second"] * units_dict["_aut"]

# # SI units
# units_dict["m"] = 1e10 * units_dict["ang"]  # metre
# units_dict["kg"] = 1. / units_dict["_amu"]  # kilogram
# units_dict["s"] = units_dict["second"]  # second
# units_dict["a"] = 1.0 / units_dict["_e"] / units_dict["s"]  # ampere
# # derived
# units_dict["j"] = units_dict["kj"] / 1000  # Joule = kg * m**2 / s**2
# units_dict["c"] = 1.0 / units_dict["_e"]  # Coulomb = A * s
