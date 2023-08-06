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
    'version': '1.0.4',
    'description': 'Analyse some log files',
    'long_description': '# Log analyst\n\n## Features\n\n- parse log files\n- filters by date / timestamps\n- correlates log lines (start and end of some processing)\n   - show total duration\n- friendly colored output\n- able to output quick summaries\n\n## Sample correlation\n\n```\n["Basic pattern-less correlation"]\nstart = "this is the start"\nend = "end over"\n\n["Correlation using a pattern"]\nstart = "starting request (\\d+)"\nend = "request (\\d+) ended."\ndebug = true # adds some extra verbosity, useful when making new rules\n```\n',
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
