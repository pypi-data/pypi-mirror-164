# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tads']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'openpyxl', 'pandas', 'python-multipart', 'xlrd']

setup_kwargs = {
    'name': 'tads',
    'version': '0.1.2',
    'description': 'Tads is reserved for ...',
    'long_description': None,
    'author': 'FL03',
    'author_email': 'jo3mccain@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
