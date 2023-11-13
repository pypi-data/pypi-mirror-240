# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xbridge', 'xbridge.cmd', 'xbridge.old', 'xbridge.xidl']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'netifaces>=0.11.0,<0.12.0',
 'progress>=1.6,<2.0',
 'pycryptodome>=3.14.1,<4.0.0',
 'qrcode>=7.3.1,<8.0.0',
 'rsa>=4.8,<5.0',
 'websockets>=10.3,<11.0',
 'zeroconf>=0.38.5,<0.39.0']

entry_points = \
{'console_scripts': ['xbridge = xbridge.cmd.__main__:main']}

setup_kwargs = {
    'name': 'xbridge',
    'version': '1.0.3',
    'description': 'A Binary RPC(Remote Procedure Call) Framework',
    'long_description': 'None',
    'author': 'yudingp',
    'author_email': 'yudingp@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
