# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flow360']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.2,<2.0.0', 'pytest>=7.1.2,<8.0.0']

setup_kwargs = {
    'name': 'flow360',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'An Li',
    'author_email': 'kidylee@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
