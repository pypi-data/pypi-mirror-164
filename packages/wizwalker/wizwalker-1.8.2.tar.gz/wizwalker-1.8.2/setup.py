# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wizwalker',
 'wizwalker.cli',
 'wizwalker.combat',
 'wizwalker.extensions.scripting',
 'wizwalker.file_readers',
 'wizwalker.memory',
 'wizwalker.memory.memory_objects']

package_data = \
{'': ['*']}

install_requires = \
['aioconsole>=0.2.1,<0.3.0',
 'aiofiles>=0.7.0,<0.8.0',
 'aiomonitor>=0.4.5,<0.5.0',
 'appdirs>=1.4.4,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'click_default_group>=1.2.2,<2.0.0',
 'janus>=0.6.1,<0.7.0',
 'loguru>=0.5.1,<0.6.0',
 'pefile>=2021.5.24,<2022.0.0',
 'pymem==1.8.3',
 'regex>=2022.1.18,<2023.0.0',
 'terminaltables>=3.1.0,<4.0.0']

entry_points = \
{'console_scripts': ['wizwalker = wizwalker.__main__:main']}

setup_kwargs = {
    'name': 'wizwalker',
    'version': '1.8.2',
    'description': 'Wizard101 scripting library',
    'long_description': 'moved to https://github.com/wizwalker/wizwalker\n\n# WizWalker\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nWizard101 scripting library\n\n## Installation\n`pip install wizwalker`\n\n## Documentation\nyou can find the documentation [here](https://starrfox.github.io/wizwalker/)\n\n## Discord\nyou can join the offical discord [here](https://discord.gg/JHrdCNK)\n\n## Just\nthis package uses [just](https://github.com/casey/just) for command running\n```shell\njust cli          # start wiz instance and then start debug cli\njust docs         # build docs\njust install      # install enviroment\njust publish TYPE # publish a major, minor, or patch version\n```\n\n## Console commands\n```shell\nwizwalker           # Runs the wizwalker cli\nwizwalker start-wiz # start wizard101 instances\nwizwalker wad       # edit and extract wizard101 wad files\n```\n',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/StarrFox/wizwalker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
