# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kraken_spot']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'kraken-spot',
    'version': '0.1.0',
    'description': 'A zero dependency library for interacting with the Kraken Spot API',
    'long_description': None,
    'author': 'Kevin Bradwick',
    'author_email': 'kevinbradwick@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
