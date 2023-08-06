# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['random_quote_generator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'random-quote-generator-py',
    'version': '0.1.3',
    'description': 'Random quate generator',
    'long_description': '# Random quote generator\n\n[![Workflow for Random quote generator Action](https://github.com/mpita/random-quote-generator/actions/workflows/branch.yaml/badge.svg)](https://github.com/mpita/random-quote-generator/actions/workflows/branch.yml)\n[![codecov](https://codecov.io/gh/mpita/random-quote-generator/branch/master/graph/badge.svg?token=9TBVXODWQ0)](https://codecov.io/gh/mpita/random-quote-generator)\n[![Documentation Status](https://readthedocs.org/projects/random-quote-generator-py/badge/?version=latest)](https://random-quote-generator-py.readthedocs.io/en/latest/?badge=latest)\n[![PyPi page link -- version](https://img.shields.io/pypi/v/random-quote-generator-py.svg)](https://pypi.python.org/pypi/random-quote-generator-py)\n',
    'author': 'Manuel Pita',
    'author_email': 'mpita1984@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://random-quote-generator-py.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
