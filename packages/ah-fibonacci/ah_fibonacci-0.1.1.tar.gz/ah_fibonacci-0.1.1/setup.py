# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ah_fibonacci']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ah-fibonacci',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Albin',
    'author_email': 'albin.henningsson1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
