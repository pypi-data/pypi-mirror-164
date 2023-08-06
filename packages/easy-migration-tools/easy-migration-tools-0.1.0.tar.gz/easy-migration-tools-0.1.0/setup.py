# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['easymigration', 'easymigration.scripts']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'easy-migration-tools',
    'version': '0.1.0',
    'description': 'Utility scripts for the migration from EASY to Data Stations',
    'long_description': None,
    'author': 'DANS-KNAW',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
