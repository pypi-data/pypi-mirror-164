# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aio_telegram_client']

package_data = \
{'': ['*']}

install_requires = \
['aio-clients>=0.1.0-alpha.2']

setup_kwargs = {
    'name': 'aio-telegram-client',
    'version': '0.1.0a0',
    'description': 'Python aiohttp telegram client ',
    'long_description': '# aiohttp telegram client\n\nOnly http client for telegram bot.\nuse with my telegram bot SDK \n',
    'author': 'Denis Malin',
    'author_email': 'denis@malina.page',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skar404/aio-clients',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
