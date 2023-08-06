# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aio_clients', 'aio_clients.multipart']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.0']

setup_kwargs = {
    'name': 'aio-clients',
    'version': '0.1.0b2',
    'description': 'Python aiohttp client',
    'long_description': '# aiohttp client\n\n## What is the difference from aiohttp.Client?\n\nIt is simpler and as a Requests\n',
    'author': 'Denis Malin',
    'author_email': 'denis@malina.page',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skar404/aio-clients',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
