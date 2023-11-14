# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gimme_db_token']

package_data = \
{'': ['*']}

install_requires = \
['awscli>=1.22.55,<2.0.0',
 'click>=8.0.3,<9.0.0',
 'cryptography>=39.0.1,<40.0.0',
 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['gimme_db_token = gimme_db_token.__main__:run']}

setup_kwargs = {
    'name': 'cyral-gimme-db-token',
    'version': '0.8.4',
    'description': 'Eases using Cyral for SSO login to databases.',
    'long_description': '# Cyral Gimme DB Token\n\nThe Cyral Gimme DB Token is a tool used for easing the process of SSO login to databases through the command line.\n\n## Deprecated\nThis tool is **deprecated** and no longer valid with Cyral Control Plane version `4.12` or later. Please use the [Cyral CLI](https://pypi.org/project/cyral/) to retrieve tokens going forward.\n',
    'author': 'Cyral',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
