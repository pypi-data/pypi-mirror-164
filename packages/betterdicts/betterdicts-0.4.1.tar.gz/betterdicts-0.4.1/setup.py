# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['betterdicts']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'betterdicts',
    'version': '0.4.1',
    'description': 'Better dictionary types.',
    'long_description': None,
    'author': 'Frank S. Hestvik',
    'author_email': 'tristesse@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
