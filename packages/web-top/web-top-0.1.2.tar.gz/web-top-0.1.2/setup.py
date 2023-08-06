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
    'version': '0.1.2',
    'description': 'web-top is a UNIX top-like tool to live HTTP requests and responses of any web server.',
    'long_description': 'web-top\n=======\n\nWeb-top is a UNIX top-like tool to live HTTP requests and responses of any web server.\nIt is build using [Top Framework for Python](https://github.com/tradingstrategy-ai/top-framework).\n\n![screenshot](https://raw.githubusercontent.com/tradingstrategy-ai/top-framework/master/docs/source/web-top/screenshot2.png)\n\n- [Installation](https://top-framework.readthedocs.io/en/latest/web-top/installation.html)\n- [Usage](https://top-framework.readthedocs.io/en/latest/web-top/usage.html)\n\n# Features\n\n- Easily integrate with any web server\n\n- Display active and recently completed HTTP requests/responses\n\n- Live top-like monitoring\n\n- Easily locate stalled requests, as requests not making progress\n  are sorted first and marked red\n\n- IP address and country geolocation to understand who is using your web\n  service\n\n\n# Documentation\n\n- [Browse documentation](https://top-framework.readthedocs.io/en/latest/web-top/index.html)\n\n# Community \n\n- [Join Discord for any questions](https://tradingstrategy.ai/community)\n\n# Social media\n\n- [Follow on Twitter](https://twitter.com/TradingProtocol)\n- [Follow on Telegram](https://t.me/trading_protocol)\n- [Follow on LinkedIn](https://www.linkedin.com/company/trading-strategy/)\n\n# License\n\nMIT.\n\n[Developed and maintained by Trading Strategy](https://tradingstrategy.ai).',
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
