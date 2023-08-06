# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdbutil']

package_data = \
{'': ['*']}

install_requires = \
['PyMySQL>=1.0.2,<2.0.0', 'click>=8.1.3,<9.0.0', 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['load-db = mdbutil.loaddb:load_db',
                     'run-sql = mdbutil.runsql:run_sql']}

setup_kwargs = {
    'name': 'mdbutil',
    'version': '0.1.1',
    'description': 'Utilities to run SQL and load a CSV/TSV (gz) file into MariaDB',
    'long_description': None,
    'author': 'Eetu Mäkelä',
    'author_email': 'eetu.makela@iki.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
