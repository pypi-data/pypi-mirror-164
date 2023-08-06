# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xlcsv']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.10,<4.0.0']

setup_kwargs = {
    'name': 'xlcsv',
    'version': '0.3.0',
    'description': 'A Python micropackage for consuming Excel as CSV.',
    'long_description': '[![ci](https://github.com/cnpryer/xlcsv/workflows/ci/badge.svg)](https://github.com/cnpryer/xlcsv/actions)\n[![PyPI Latest Release](https://img.shields.io/pypi/v/xlcsv.svg)](https://pypi.org/project/xlcsv/)\n\n# xlcsv\n\nA Python micropackage for consuming Excel as CSV.\n\nBuild CSV `StringIO` from Excel files.\n\n```py\nimport xlcsv\n\nbuffer = xlcsv.to_csv_buffer("my-file.xlsx")\n```\n\nRead Excel files without Excel using a `DataFrame` library.\n\n```py\n# ...\n\nimport pandas as pd\n\ndf = pd.read_csv(buffer)\n\nimport polars as pl\n\ndf = pl.read_csv(buffer)\n```\n\n## Contributing\n\nSee [CONTRIBUTING.md](./CONTRIBUTING.md).\n',
    'author': 'Chris Pryer',
    'author_email': 'cnpryer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cnpryer/xlcsv.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
