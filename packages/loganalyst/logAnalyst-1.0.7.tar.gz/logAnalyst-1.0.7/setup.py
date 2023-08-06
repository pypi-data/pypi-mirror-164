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
    'version': '1.0.7',
    'description': 'Analyse some log files',
    'long_description': '# Log analyst\n\n## Features\n\n- parse log files\n- filters by date / timestamps\n- correlates log lines (start and end of some processing)\n   - show total duration\n- friendly colored output\n- able to output short summaries\n- supports gzipped files\n\n## Usage\n\nFor instance, with systemd logs:\n\n```\njournalctl -b 5 -o short-iso | loga -s correlators/sample.toml -\n```\n\n## Sample correlation\n\n\n*Note*: the "loganalyst" section is a configuration, which is optional, use only in case overriding values is needed.\n\nFind the sample correlation in `correlators/sample.toml`:\n\n```ini\n[loganalyst]\n# patterns required before & after the ISO date to consider the log line valid\nts_lines_prefix = ".*"\nts_lines_suffix = ""\n# What will be searched for in each line to extract the ISO date\niso_regex = \'(\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d\\.\\d+)|(\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d)|(\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d)\'\n# timezone used in dates input by the user\ntimezone = "CEST"\n\n["Basic pattern-less correlation"]\nstart = "this is the start"\nend = "end over"\n\n["Correlation using a pattern"]\nstart = \'starting request (\\d+)\'\nend = \'request (\\d+) ended.\'\ndebug = true # adds some extra verbosity, useful when making new rules\n\n["systemd units start"]\nstart = \'systemd\\[\\d+\\]: Starting (.*?)[.]+\'\nend = \'systemd\\[\\d+\\]: Started (.*)\\.$\'\n\n["systemd units sockets"]\nstart = \'systemd\\[\\d+\\]: Listening on (.*?)[.]+\'\nend = \'systemd\\[\\d+\\]: Closed (.*)\\.$\'\n\n["systemd units duration"]\nstart = \'systemd\\[\\d+\\]: Started (.*?) ?[.]+$\'\nend = \'systemd\\[\\d+\\]: Stopped (.*)\\.$\'\n```\n',
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
