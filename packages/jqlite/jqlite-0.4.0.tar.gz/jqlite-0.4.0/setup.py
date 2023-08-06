# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jqlite', 'jqlite.core']

package_data = \
{'': ['*']}

install_requires = \
['more-itertools>=8.14.0,<9.0.0',
 'orjson>=3.7.11,<4.0.0',
 'pyrsistent>=0.18.1,<0.19.0',
 'termcolor>=1.1.0,<2.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['jqlite = jqlite.cli:main']}

setup_kwargs = {
    'name': 'jqlite',
    'version': '0.4.0',
    'description': 'A lightweight implementation of jq.',
    'long_description': None,
    'author': 'Christian',
    'author_email': 'xian.tuxoid@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
