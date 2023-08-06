# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['loganalyst']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8.2,<3.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['loga = loganalyst.cli:run']}

setup_kwargs = {
    'name': 'loganalyst',
    'version': '1.0.9',
    'description': 'Analyse some log files',
    'long_description': '# Log analyst\n\n## Features\n\n- parse log files\n- filters by date / timestamps\n- correlates log lines (start and end of some processing)\n   - show total duration\n- friendly colored output\n- able to output short summaries\n- "folding" lines\n   - keeps lines not matching an iso timestamp attached to the matching ones\n- supports gzipped files\n\n## Usage\n\n```\nusage: loga [-h] [--extra | --no-extra] [-s] [-n] [-max] [-f F] [-t T] TOML_FILE LOG_FILE\n\nParse some logs.\n\npositional arguments:\n  TOML_FILE            correlation rules to use\n  LOG_FILE             (possibly gzipped) log file\n\noptions:\n  -h, --help           show this help message and exit\n  --extra, --no-extra  show extra log lines (not matched by iso_regex) (default: False)\n  -s                   show summary (default: False)\n  -n                   don\'t show log (default: False)\n  -max                 show max durations (default: False)\n  -f F                 start from a date\n  -t T                 stop to a date\n```\n\nFor instance, with systemd logs:\n\n```\njournalctl -b 5 -o short-iso | loga -s correlators/sample.toml -\n```\n\n## Sample correlation\n\n\n*Note*: the "loganalyst" section is a configuration, which is optional, use only in case overriding values is needed.\n\nUse the documented correlation file in [correlators/sample.toml](https://github.com/fdev31/loganalyst/blob/main/correlators/sample.toml). You can also [download the file](https://raw.githubusercontent.com/fdev31/loganalyst/main/correlators/sample.toml).\n',
    'author': 'fdev31',
    'author_email': 'fdev31@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fdev31/loganalyst',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
