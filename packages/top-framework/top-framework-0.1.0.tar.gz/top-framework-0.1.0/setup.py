# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['top', 'top.core', 'top.gunicorn', 'top.redis', 'top.tui', 'top.web']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0',
 'emoji-country-flag>=1.3.1,<2.0.0',
 'redispy>=3.0.0,<4.0.0',
 'textual>=0.1.18,<0.2.0',
 'typer>=0.6.1,<0.7.0']

extras_require = \
{'docs': ['sphinx-sitemap>=2.2.0,<3.0.0',
          'Sphinx>=5.1.1,<6.0.0',
          'furo>=2022.6.21,<2023.0.0',
          'sphinx-autodoc-typehints>=1.16.0,<2.0.0'],
 'gunicorn': ['gunicorn>=20.1.0,<21.0.0', 'python-lorem>=1.1.2,<2.0.0']}

entry_points = \
{'console_scripts': ['random-http-requests = top.web.random_requests:main',
                     'web-top = top.web.main:app']}

setup_kwargs = {
    'name': 'top-framework',
    'version': '0.1.0',
    'description': 'Python framework for creating UNIX top like TUI applications easily',
    'long_description': None,
    'author': 'Mikko Ohtamaa',
    'author_email': 'mikko@opensourcehacker.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
