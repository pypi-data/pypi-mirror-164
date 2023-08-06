# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['experiment_server']

package_data = \
{'': ['*'], 'experiment_server': ['static/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'asyncio>=3.4.3,<4.0.0',
 'click>=6.0',
 'easydict>=1,<2',
 'loguru>=0.5,<0.6',
 'pandas>=1,<2',
 'requests>=2.25.1,<3.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'tornado>=6.2,<7.0']

entry_points = \
{'console_scripts': ['experiment-server = experiment_server.cli:cli']}

setup_kwargs = {
    'name': 'experiment-server',
    'version': '0.1',
    'description': 'Server for experiments to get configuarations from',
    'long_description': '# Overview\n\nServer for experiments to get configuarations from\n\n# Setup\n\n## Requirements\n\n* Python 3.8+\n\n## Installation\n\nInstall it directly into an activated virtual environment:\n\n```text\n$ pip install experiment-server\n```\n\nor add it to your [Poetry](https://poetry.eustace.io/) project:\n\n```text\n$ poetry add experiment-server\n```\n\n# Usage\n\nAfter installation, the server can used as:\n\n```text\n$ experiment-server sample_config.expconfig\n```\n\n# The Experiment Configuration\nTBA\n\n\n# Wishlist\n- Single application where the participant_id can be updated and the server would keep running.\n',
    'author': 'Ahmed Shariff',
    'author_email': 'shariff.mfa@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
