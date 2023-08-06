# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webtop']

package_data = \
{'': ['*']}

install_requires = \
['top-framework>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'web-top',
    'version': '0.1.1',
    'description': 'web-top is a UNIX top-like tool to live HTTP requests and responses of any web server.',
    'long_description': None,
    'author': 'Mikko Ohtamaa',
    'author_email': 'mikko@opensourcehacker.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://top-framework.readthedocs.io/en/latest/web-top/index.html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
