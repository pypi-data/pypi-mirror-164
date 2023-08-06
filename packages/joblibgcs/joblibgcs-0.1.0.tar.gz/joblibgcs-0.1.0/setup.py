# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['joblibgcs']

package_data = \
{'': ['*']}

install_requires = \
['gcsfs>=2022.7.1,<2023.0.0', 'joblib>=1.1.0,<2.0.0']

extras_require = \
{'book': ['ipykernel>=6.15.1,<7.0.0']}

setup_kwargs = {
    'name': 'joblibgcs',
    'version': '0.1.0',
    'description': 'a google cloud storage memory backend for joblib',
    'long_description': None,
    'author': 'Gautam Sisodia',
    'author_email': 'gautam.sisodia@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
