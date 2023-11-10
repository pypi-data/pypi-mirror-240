# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pears']

package_data = \
{'': ['*']}

install_requires = \
['fastkde>=1.0.20,<2.0.0', 'matplotlib>=3.4,<4.0', 'numpy>=1.21,<2.0']

setup_kwargs = {
    'name': 'pears',
    'version': '0.1.6',
    'description': 'Tools for dealing with 2D densities.',
    'long_description': 'None',
    'author': 'Jeff Shen',
    'author_email': 'jshen2014@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1',
}


setup(**setup_kwargs)
