# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quarterback']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=37.0.4,<38.0.0',
 'minio>=7.1.11,<8.0.0',
 'opcua>=0.98.13,<0.99.0',
 'pandas>=1.4.3,<2.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'rocketry>=2.3.0,<3.0.0']

setup_kwargs = {
    'name': 'quarterback',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'gbPagano',
    'author_email': 'guilhermebpagano@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
