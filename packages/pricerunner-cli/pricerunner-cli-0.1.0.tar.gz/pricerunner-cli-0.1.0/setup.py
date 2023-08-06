# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prcli']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1','click>=8.0.3','requests>=2.27.1','rich>=12.5.1','setuptools>=59.6.0']

entry_points = \
{'console_scripts': ['pricerunner-cli=prcli.pricerunner_cli:cli']}

setup_kwargs = {
    'name': 'pricerunner-cli',
    'version': '0.1.0',
    'description': 'Cli version of pricerunner.dk',
    'long_description': None,
    'author': 'oxnan',
    'author_email': 'pricerunner-cli@oxnan.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
