# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dune_quote']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dune-quote',
    'version': '0.1.1',
    'description': '',
    'long_description': 'usage:\nimport dune_quote\n',
    'author': 'teodororo',
    'author_email': 'giovanna.teod@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
