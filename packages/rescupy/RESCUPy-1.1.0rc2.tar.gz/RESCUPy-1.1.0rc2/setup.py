# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rescupy', 'rescupy.data', 'rescupy.io']

package_data = \
{'': ['*'], 'rescupy': ['matlab/*']}

install_requires = \
['apipkg>=1.5,<2.0',
 'ase>=3.21.1',
 'attrs>=20.2.0,<21.0.0',
 'execnet>=1.9.0,<2.0.0',
 'filelock>=3.0.12,<4.0.0',
 'h5py>=2.10.0,<3.0.0',
 'joblib>=1.1.0',
 'matplotlib>=3.3.2,<4.0.0',
 'nptyping>=1.3.0,<2.0.0',
 'numpy>=1.19',
 'pint>=0.19.2',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'scipy>=1.5.2',
 'toml>=0.10.2']

setup_kwargs = {
    'name': 'rescupy',
    'version': '1.1.0rc2',
    'description': 'RESCUPy is a Python interface for the material simulation tool RESCU+ and the transport simulation tool NanoDCAL+.',
    'long_description': None,
    'author': 'Vincent Michaud-Rioux',
    'author_email': 'vincentm@nanoacademic.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
