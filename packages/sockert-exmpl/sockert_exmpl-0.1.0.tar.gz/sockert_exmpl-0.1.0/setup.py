# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sockert_exmpl']

package_data = \
{'': ['*']}

install_requires = \
['sockets>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'sockert-exmpl',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'talel-khairi kchih',
    'author_email': 'talelkhairi.kchih@celadodc-rswl.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
