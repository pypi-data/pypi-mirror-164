# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyvalve']

package_data = \
{'': ['*']}

install_requires = \
['aiofile>=3.7.4,<4.0.0', 'aiopath>=0.5.12,<0.6.0', 'asyncinit>=0.2.4,<0.3.0']

setup_kwargs = {
    'name': 'pyvalve',
    'version': '0.1.1',
    'description': 'Asyncio python clamav client',
    'long_description': None,
    'author': 'Bradley Sacks',
    'author_email': 'bradsacks99@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
