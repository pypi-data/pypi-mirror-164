# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['granted_flask']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'granted-flask',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Common Fate',
    'author_email': 'hello@commonfate.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
