# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfg4py', 'cfg4py.resources', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['APScheduler>=3.9.1,<4.0.0',
 'fire==0.4.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'watchdog>=2.1.9,<3.0.0']

extras_require = \
{'dev': ['black>=22.3.0,<23.0.0',
         'tox>=3.24.5,<4.0.0',
         'virtualenv>=20.13.1,<21.0.0',
         'pip>=22.0.3,<23.0.0',
         'twine>=3.8.0,<4.0.0',
         'pre-commit>=2.17.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.2.3,<2.0.0',
         'mkdocs-include-markdown-plugin>=3.2.3,<4.0.0',
         'mkdocs-material>=8.1.11,<9.0.0',
         'mkdocstrings>=0.18.0,<0.19.0',
         'mkdocs-autorefs>=0.4.1,<0.5.0',
         'mike>=1.1.2,<2.0.0'],
 'test': ['isort==5.10.1',
          'flake8==4.0.1',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=7.0.1,<8.0.0',
          'pytest-cov>=3.0.0,<4.0.0',
          'redis>=4.3.4,<5.0.0']}

entry_points = \
{'console_scripts': ['cfg4py = cfg4py.cli:main']}

setup_kwargs = {
    'name': 'cfg4py',
    'version': '0.9.4',
    'description': 'Easy config (template, auto-complete), hierarchichal design, monitor config change and load on-the-fly .',
    'long_description': '# Overview\n\n[![Version](http://img.shields.io/pypi/v/cfg4py?color=brightgreen)](https://pypi.python.org/pypi/cfg4py)\n[![CI Status](https://github.com/zillionare/cfg4py/actions/workflows/release.yml/badge.svg)](https://github.com/zillionare/cfg4py)\n[![Code Coverage](https://img.shields.io/codecov/c/github/zillionare/cfg4py)](https://app.codecov.io/gh/zillionare/cfg4py)\n[![Downloads](https://pepy.tech/badge/cfg4py)](https://pepy.tech/project/cfg4py)\n[![License](https://img.shields.io/badge/License-MIT.svg)](https://opensource.org/licenses/MIT)\n[![Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n* Free software: MIT license\n* Documentation: https://zillionare.github.io/cfg4py\n\n\nA python config module that:\n\n1. Adaptive deployment (default, dev, test, production) support\n2. Cascading configuration (central vs local) support\n3. Auto-complete\n4. Templates (logging, database, cache, message queue,...)\n5. Environment variables macro support\n6. Enable logging in one line\n7. Built on top of yaml\n\n## Features\n\nIt\'s common to see that you have different settings for development machine, test machine and production site. They share many common settings, but a few of them has to be different.\n\nFor example, developers should connect to local database server when performing unittest, and tester should connect to their own database server. All these servers should be deployed separately and no data should be messed up.\n\nCfg4Py has perfect solution supporting for this: adaptive deployment environment support.\n\n### Adaptive Deployment Environment Support\n\nIn any serious projects, your application may run at both development, testing and production site. Except for effort of copying similar settings here and there, sometimes we\'ll mess up with development environment and production site. Once this happen, it could result in very serious consequence.\n\nTo solve this, Cfg4Py developed a mechanism, that you provide different sets for configurations: dev for development machine, test for testing environment and production for production site, and all common settings are put into a file called `defaults`.\n\ncfg4py module knows which environment it\'s running on by looking up environment variable __cfg4py_server_role__. It should be one of `DEV`, `TEST` and `PRODUCTION`. If nothing found, it means setup is not finished, and Cfg4Py will refuse to work. If the environment is set, then Cfg4Py will read settings from defaults set, then apply update from either of `DEV`, `TEST` and `PRODUCTION` set, according to the environment the application is running on.\n\n!!! important\n\n    Since 0.9.0, cfg4py can still work if __cfg4py_server_role__ is not set, when it work at non-strict mode.\n\n### Cascading design\n\n\nAssuming you have a bunch of severs for load-balance, which usually share same configurations. So you\'d like put the configurations on a central repository, which could be a redis server or a relational database. Once you update configuration settings at central repository, you update configurations for all servers. But somehow for troubleshooting or maintenance purpose, you\'d like some machines could have its own settings at a particular moment.\n\nThis is how Cfg4Py solves the problem:\n\n1. Configure your application general settings at remote service, then implement a `RemoteConfigFetcher` (Cfg4Py has already implemented one, that read settings from redis), which pull configuration from remote serivce periodically.\n2. Change the settings on local machine, after the period you\'ve set, these changes are popluated to all machines.\n\n### Auto-complete\n\n[auto-complete](http://images.jieyu.ai/images/projects/cfg4py/auto-complete.gif)\n\n\nWith other python config module, you have to remember all the configuration keys, and refer to each settings by something like cfg["services"]["redis"]["host"] and etc. Keys are hard to rememb, prone to typo, and way too much tedious.\n\nWhen cfg4py load raw settigns from yaml file, it\'ll compile all the settings into a Python class, then Cfg4Py let you access your settings by attributes. Compares the two ways to access configure item:\n\n```python\n\n        cfg["services"]["redis"]["host"]\n```\nvs:\n\n```python\n\n        cfg.services.redis.host\n```\n\nApparently the latter is the better.\n\nAnd, if you trigger a build against your configurations, it\'ll generate a python class file. After you import this file (named \'schema.py\') into your project, then you can enjoy code auto-complete!\n\n### Templates\n\nIt\'s hard to remember how to configure log, database, cache and etc, so cfg4py provide templates.\n\nJust run cfg4py scaffold, follow the tips then you\'re done.\n\n[scaffold](http://images.jieyu.ai/images/projects/cfg4py/scaffold.png)\n\n\n### Environment variables macro\n\nThe best way to keep secret, is never share them. If you put account/password files, and these files may be leak to the public. For example, push to github by accident.\n\nWith cfg4py, you can set these secret as environment variables, then use marco in config files. For example, if you have the following in defaults.yaml (any other files will do too):\n\n```text\n\n        postgres:\n                dsn: postgres://${postgres_account}:${postgres_password}@localhost\n```\n\nthen cfg4py will lookup postgres_account, postgres_password from environment variables and make replacement.\n\n\n### Enable logging with one line\n\nwith one line, you can enable file-rotating logging:\n\n```python\n\n    cfg.enable_logging(level, filename=None)\n```\n\n### Apply configuration change on-the-fly\n\nCfg4Py provides mechanism to automatically apply configuration changes without restart your application. For local files configuration change, it may take effect immediately. For remote config change, it take effect up to `refresh_interval` settings.\n\n### On top of yaml\n\nThe raw config format is backed by yaml, with macro enhancement. YAML is the best for configurations.\n\n\n\n### Credits\n\n\nThis package was created [ppw](https://zillionare.github.io/python-project-wizard)\n',
    'author': 'Aaron Yang',
    'author_email': 'aaron_yang@jieyu.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zillionare/cfg4py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
