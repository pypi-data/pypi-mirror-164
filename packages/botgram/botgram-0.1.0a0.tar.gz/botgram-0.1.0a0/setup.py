# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aio_telegram']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.0']

setup_kwargs = {
    'name': 'botgram',
    'version': '0.1.0a0',
    'description': 'Python aiohttp telegram SDK',
    'long_description': None,
    'author': 'Denis Malin',
    'author_email': 'denis@malina.page',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
