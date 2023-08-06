# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baydemir']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0']

setup_kwargs = {
    'name': 'baydemir',
    'version': '1.0.0',
    'description': "Brian A's idiosyncratic utilities",
    'long_description': None,
    'author': 'Brian Aydemir',
    'author_email': 'brian.aydemir@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/brianaydemir/pythonlib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
