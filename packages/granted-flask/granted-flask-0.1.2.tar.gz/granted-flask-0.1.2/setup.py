# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['granted_flask']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.20.0,<0.21.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'granted-flask',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Common Fate',
    'author_email': 'hello@commonfate.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
