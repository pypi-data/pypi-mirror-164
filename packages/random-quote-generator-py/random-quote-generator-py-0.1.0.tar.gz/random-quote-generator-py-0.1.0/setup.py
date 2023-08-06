# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['random_quote_generator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'random-quote-generator-py',
    'version': '0.1.0',
    'description': 'Random quate generator',
    'long_description': None,
    'author': 'Manuel Pita',
    'author_email': 'mpita1984@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
