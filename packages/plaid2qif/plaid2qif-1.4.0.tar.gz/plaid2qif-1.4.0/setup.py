# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plaid2qif']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0',
 'plaid-python>=9.4.0,<10.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'python-dotenv>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['plaid2qif = plaid2qif.plaid2qif:main']}

setup_kwargs = {
    'name': 'plaid2qif',
    'version': '1.4.0',
    'description': 'Download financial transactions from Plaid as QIF files.',
    'long_description': '[![CircleCI](https://circleci.com/gh/ebridges/plaid2qif/tree/master.svg?style=svg)](https://circleci.com/gh/ebridges/plaid2qif/tree/master)\n[![GitHub watchers](https://img.shields.io/github/watchers/badges/shields.svg?style=social&label=Watch&style=flat-square)]()\n[![Crates.io](https://img.shields.io/crates/l/rustc-serialize.svg?style=flat-square)]()\n[![PyPi](https://img.shields.io/pypi/v/plaid2qif.svg?style=flat-square)](https://pypi.org/project/plaid2qif)\n\\\n\\\n[![Plaid2QIF Logo](gen-access-token/icon.svg)](https://github.com/eqbridges/plaid2qif)\n# Plaid2QIF\n\n## Description\n\nPlaid2QIF downloads transactions from various financial institutions in JSON format and converts to formats usable by financial software.\n\n### Output Formats supported:\n* [QIF](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)\n* CSV\n* JSON\n* Extensible to others\n\n### Notes\n* Tested extensively with [GnuCash](https://www.gnucash.org/).  Supported by any financial software that supports import from [QIF](https://en.wikipedia.org/wiki/Quicken_Interchange_Format).\n* Supports any institution supported by [Plaid](https://www.plaid.com).\n\n## Summary\n\n```\n  # Download transactions in various formats (default QIF) from Plaid\n  plaid2qif download \\\n    --account=<account-name> \\\n    --account-type=<type> \\\n    --account-id=<acct-id> \\\n    --from=<from-date> \\\n    --to=<to-date> \\\n    [--output-format=<format>] \\\n    [--output-dir=<path>] \\\n    [--ignore-pending] \\\n    [--verbose]\n```\n\n## Usage\n\n1. Install the `plaid2qif` command using `pip`\n\n        $ pip install plaid2qif\n\n2. Authenticate and link with your financial institution (first time only).  To do this, follow the steps for using the associated [Account Linker](gen-access-token/README.md) tool.\n\n3. Configure your environment with required values. See "Authentication Configuration" below.\n\n3. Once configured, you\'re ready to download transactions and save them as QIF files:\n\n        plaid2qif download \\\n            --from=<yyyy-mm-dd> \\\n            --to=<yyyy-mm-dd> \\\n            --account-type=<type> \\\n            --account=<account-name> \\\n            --account-id=<plaid-account-id> \\\n            --credentials=<file>\n\n  * `account` is the path to an account in the ledger in GnuCash that you ultimately want to import the transactions to.  This is added to the `!Account` header in the QIF file.  e.g.: `Assets: Checking Accounts:Personal Checking Account`.  If the name has spaces be sure to quote this param.\n  * `account-type` is a GnuCash account identifier type as [documented here](https://github.com/Gnucash/gnucash/blob/cdb764fec525642bbe85dd5a0a49ec967c55f089/gnucash/import-export/qif-imp/file-format.txt#L23).\n  * `account-id` is Plaid\'s account ID for the account you want to download, as obtained via `list-accounts` above.\n  * By default, output will go to stdout to be redirected.  If you want it to be written to a location use the `output-dir` parameter.\n\n## Authentication Configuration\n\n* You will need the following information configured in your environment in order to use this tool.\n* The suggested way to populate your environment would be to use a file named `.env` in your current working directory.  Alternatively you could put the values in your `~/.profile` or however you normally initialize your environment.\n\nConfiguration Parameter | Environment Variable Name | Description | Notes\n---------|----------|---------|---------\n Client ID | `PLAID_CLIENT_ID` | Plaid\'s unique indentifier for your Plaid account. [Obtain from your dashboard](https://dashboard.plaid.com/overview/development) | Required.\n Client Secret | `PLAID_SECRET` | Plaid\'s authentication token for your Plaid account. [Obtain from your dashboard](https://dashboard.plaid.com/overview/development) | Required.\n Plaid Environment | `PLAID_ENV` | Operating environment. | Optional. Should be one of: `sandbox`, `development`, or `production`.  Defaults to `development`.\n Plaid API Version | `PLAID_API_VERSION` | Version of the API that the `plaid-python` library supports. | Optional.  Defaults to `2020-09-14`\n Access Token location | `ACCESS_TOKEN_FILE` | Location of the token that grants access to a particular financial institution for downloading records from. | Required.\n\n### **Notes on Authentication Configuration**\n\n* The access token and Plaid credentials are sensitive material as they grant access to data within your financial accounts.  They should be handled carefully and not shared.\n\n* These are the most important values that need configuration in order to authenticate with your institution and then download records.  Other values can be found in the [sample.env](./sample.env).\n\n* If you\'re downloading from different institutions that result in multiple access token files, you can override the location of the file at the command line; see below for an example.  _This approach is open to suggestions for improvement if this doesn\'t work well for others. See Issue #27._\n\n        $ ACCESS_TOKEN_FILE=./cfg/chase.txt plaid2qif ...\n        $ ACCESS_TOKEN_FILE=./cfg/citi.txt plaid2qif ...\n\n\n## Distribution\n\n```\n# increment version in `plaid2qif/__init__.py`\n# commit everything & push\n$ git tag -s vX.Y.Z\n$ git push --tags\n$ python3 setup.py sdist bdist_wheel\n$ twine upload dist/*\n```\n',
    'author': 'Edward Q. Bridges',
    'author_email': 'github@eqbridges.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ebridges/plaid2qif',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
