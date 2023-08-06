# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyprql', 'pyprql.cli', 'pyprql.magic', 'pyprql.pandas_accessor']

package_data = \
{'': ['*'], 'pyprql': ['assets/*']}

install_requires = \
['Pygments>=2.11.2,<3.0.0',
 'SQLAlchemy>=1.4.32,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'duckdb-engine>=0.1.8,<0.2.0',
 'fuzzyfinder>=2.1.0,<3.0.0',
 'icecream>=2.1.2,<3.0.0',
 'ipython-sql>=0.4.0,<0.5.0',
 'prompt-toolkit>=3.0.28,<4.0.0',
 'prql-python>=0.2.6,<0.3.0',
 'pytest>=7.1.2,<8.0.0',
 'rich>=12.0.0,<13.0.0',
 'traitlets>=5.2.0,<6.0.0']

extras_require = \
{':python_full_version >= "3.7.1" and python_full_version < "3.8.0"': ['pandas>=1.3,<1.4',
                                                                       'numpy>=1.21,<1.22',
                                                                       'ipython>=7.33.0,<7.34.0'],
 ':python_version >= "3.8" and python_version < "4.0"': ['pandas>=1.4,<2.0',
                                                         'numpy>=1.22.3,<2.0.0',
                                                         'ipython>=8.0,<9.0']}

entry_points = \
{'console_scripts': ['pyprql = pyprql.cli.__init__:main']}

setup_kwargs = {
    'name': 'pyprql',
    'version': '0.5.6',
    'description': 'Python TUI database client that supports prql',
    'long_description': "# PyPrql\n\n[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)\n![PyPI - License](https://img.shields.io/pypi/l/pyprql)\n![PyPI](https://img.shields.io/pypi/v/pyprql)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyprql)\n\n[![Documentation Status](https://readthedocs.org/projects/pyprql/badge/?version=latest)](https://pyprql.readthedocs.io/en/latest/?badge=latest)\n![Discord](https://img.shields.io/discord/936728116712316989)\n![GitHub contributors](https://img.shields.io/github/contributors/prql/pyprql)\n![GitHub Repo stars](https://img.shields.io/github/stars/prql/pyprql)\n\n[![CI/CD](https://github.com/prql/PyPrql/actions/workflows/cicd.yaml/badge.svg?branch=main)](https://github.com/prql/PyPrql/actions/workflows/cicd.yaml)\n[![codecov](https://codecov.io/gh/prql/PyPrql/branch/main/graph/badge.svg?token=C6J2UI7FR5)](https://codecov.io/gh/prql/PyPrql)\n\n[![Codestyle: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n\nPyPRQL contains these tools:\n\n- pyprql.pandas_accessor - Pandas integration for PRQL\n- pyprql.magic - IPython magic for connecting to databases using `%%prql`\n- pyprql.cli - TUI for databases using PRQL \n\nFor docs, Check out the [PyPRQL Docs](https://pyprql.readthedocs.io/), and the [PRQL Book][prql_docs].\n\nThis project is maintained by [@charlie-sanders](https://github.com/charlie-sanders/) and [@rbpatt2019](https://github.com/rbpatt2019)\n\n## Installation\n\n```bash\npip install pyprql\n```\n\n\n### Try out the Pandas integration\n\n```python\nimport pandas as pd\nimport pyprql.pandas_accessor\n\ndf = (...)\nresults_df = df.prql.query('from df | select [age,name,occupation] | filter age > 21')\n\n```\n\n### Try out the Jupyter Magic \n\n\n```\nIn [1]: %load_ext pyprql.magic\nIn [2]: %prql postgresql://user:password@localhost:5432/database\nIn [3]: %%prql\n   ...: from p\n   ...: group categoryID (\n   ...:   aggregate [average unitPrice]\n   ...: )\nIn [4]: %%prql results <<\n   ...: from p \n   ...: aggregate [min unitsInStock, max unitsInStock]\n   \n```\n\n### Try out the TUI\n\nWith a CSV file:\n\n```bash\ncurl https://people.sc.fsu.edu/~jburkardt/data/csv/zillow.csv\npyprql zillow.csv\n```\n\nWith a Database:\n\n```bash\npyprql 'postgresql://user:password@localhost:5432/database'\nPRQL> show tables\n```\n\n\n[prql]: https://github.com/prql/prql\n[prql_docs]: https://prql-lang.org/reference\n",
    'author': 'qorrect',
    'author_email': 'charlie.fats@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/prql/PyPrql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
