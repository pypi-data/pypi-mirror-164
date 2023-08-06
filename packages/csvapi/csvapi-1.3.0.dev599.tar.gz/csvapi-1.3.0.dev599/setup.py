# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['csvapi']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<3.1.0',
 'Quart>=0.14.1,<0.15.0',
 'Werkzeug>=1.0.0,<1.1.0',
 'agate-excel>=0.2.3,<0.3.0',
 'agate-sql>=0.5.5,<0.6.0',
 'agate>=1.6.1,<1.7.0',
 'aiohttp>=3.7.3,<3.8.0',
 'aiosqlite>=0.16.1,<0.17.0',
 'boto3>=1.21.21,<1.22.0',
 'cchardet>=2.1.7,<2.2.0',
 'click>=8.1.3,<8.2.0',
 'click_default_group>=1.2.2,<1.3.0',
 'pandas-profiling>=3.2.0,<3.3.0',
 'pandas>=1.4.3,<1.5.0',
 'python-stdnum>=1.15,<1.16',
 'quart-cors>=0.3.0,<0.4.0',
 'requests>=2.27.1,<2.28.0',
 'sentry-sdk>=1.0.0,<1.1.0',
 'udata-event-service>=0.0.8,<0.1.0',
 'validators>=0.18.2,<0.19.0']

entry_points = \
{'console_scripts': ['csvapi = csvapi.cli:cli']}

setup_kwargs = {
    'name': 'csvapi',
    'version': '1.3.0.dev599',
    'description': 'An instant JSON API for your CSV',
    'long_description': None,
    'author': 'Opendatateam',
    'author_email': 'opendatateam@data.gouv.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
