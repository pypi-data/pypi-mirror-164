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
    'version': '0.1.0b5',
    'description': 'Python aiohttp client',
    'long_description': "# aiohttp client\n\n### What is the difference from aiohttp.Client?\n\nIt is simpler and as a Requests\n\n----\n# Example: \n\n```python\nimport asyncio\nfrom aio_clients import Http, Options\n\n\nasync def main():\n    r = await Http().get('http://google.com', o=Options(is_json=False, is_raw=True, is_close_session=True))\n    print(f'code={r.code} body={r.raw_body}')\n\n\nasyncio.run(main())\n```\n",
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
