# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acapy_plugin_pickup',
 'acapy_plugin_pickup.acapy',
 'acapy_plugin_pickup.protocol']

package_data = \
{'': ['*']}

install_requires = \
['aries-cloudagent>=0.7.3,<0.8.0',
 'pydantic>=1.8.1,<2.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

extras_require = \
{'indy': ['python3-indy>=1.11.1']}

setup_kwargs = {
    'name': 'acapy-plugin-pickup',
    'version': '0.1.0.post1',
    'description': 'Pickup Protocol for ACA-Py',
    'long_description': None,
    'author': 'Daniel Bluhm',
    'author_email': 'dbluhm@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.9,<4.0',
}


setup(**setup_kwargs)
