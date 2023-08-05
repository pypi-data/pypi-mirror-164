# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netprotocols',
 'netprotocols.base',
 'netprotocols.layer2',
 'netprotocols.layer3',
 'netprotocols.layer4',
 'netprotocols.utils',
 'netprotocols.utils.validation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'netprotocols',
    'version': '0.8.0',
    'description': 'Low-level implementations of common networking protocols',
    'long_description': None,
    'author': 'EONRaider',
    'author_email': 'livewire_voodoo@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
