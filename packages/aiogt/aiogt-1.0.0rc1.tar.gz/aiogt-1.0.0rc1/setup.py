# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogt', 'aiogt.transport']

package_data = \
{'': ['*']}

install_requires = \
['urlcon>=0.1.0rc1,<0.2.0']

extras_require = \
{'aiohttp': ['aiohttp>=3.8.6,<4.0.0'],
 'cache': ['redis>=5.0.1,<6.0.0'],
 'httpx': ['httpx>=0.25.1,<0.26.0']}

setup_kwargs = {
    'name': 'aiogt',
    'version': '1.0.0rc1',
    'description': '',
    'long_description': '',
    'author': 'Robert Stoul',
    'author_email': 'rekiiky@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
