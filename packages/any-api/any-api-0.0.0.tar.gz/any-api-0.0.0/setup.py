# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['any_api']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'any-api',
    'version': '0.0.0',
    'description': 'Quick and easy to create OpenAPI/AsyncAPI, and provide corresponding extensions',
    'long_description': None,
    'author': 'so1n',
    'author_email': 'qaz6803609@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
