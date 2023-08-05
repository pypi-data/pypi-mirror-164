# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['steam_market_history', 'steam_market_history.modules']

package_data = \
{'': ['*'], 'steam_market_history': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'steam>=1.2.1,<2.0.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['steam-market-history = steam_market_history.main:app']}

setup_kwargs = {
    'name': 'steam-market-history',
    'version': '3.0.3',
    'description': 'An easy-to-use CLI to export your steam market history to various formats',
    'long_description': '<div id="top"></div>\n\n<!-- PROJECT SHIELDS -->\n\n![PyPI](https://img.shields.io/pypi/v/steam-market-history?style=for-the-badge)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/steam-market-history?style=for-the-badge)\n![Gitlab pipeline status](https://img.shields.io/gitlab/pipeline-status/fabieu-ci/steam-market-history?style=for-the-badge)\n![GitLab issues](https://img.shields.io/gitlab/issues/open/fabieu-ci/steam-market-history?style=for-the-badge)\n![GitLab merge requests](https://img.shields.io/gitlab/merge-requests/open-raw/fabieu-ci/steam-market-history?style=for-the-badge)\n![GitLab](https://img.shields.io/gitlab/license/fabieu-ci/steam-market-history?style=for-the-badge)\n\n<!-- PROJECT LOGO -->\n<br />\n<div align="center">\n  <a href="https://gitlab.com/fabieu-ci/steam-market-history">\n    <img src="https://gitlab.com/fabieu-ci/steam-market-history/-/raw/main/docs/images/logo.svg" alt="Logo" width="120" height="120">\n  </a>\n\n<h3 align="center">steam-market-history</h3>\n\n  <p align="center">\n    An easy-to-use CLI to export your steam market history to various formats\n    <br />\n    <a href="https://gitlab.com/fabieu-ci/steam-market-history/-/raw/main/docs/demo.gif">View Demo</a>\n    ·\n    <a href="https://gitlab.com/fabieu-ci/steam-market-history/-/issues">Report Bug</a>\n    ·\n    <a href="https://gitlab.com/fabieu-ci/steam-market-history/-/issues">Request Feature</a>\n  </p>\n</div>\n\n<!-- TABLE OF CONTENTS -->\n<details>\n  <summary>Table of Contents</summary>\n  <ol>\n    <li>\n      <a href="#about-the-project">About The Project</a>\n      <ul>\n        <li><a href="#built-with">Built With</a></li>\n      </ul>\n    </li>\n    <li>\n      <a href="#getting-started">Getting Started</a>\n      <ul>\n        <li><a href="#prerequisites">Prerequisites</a></li>\n        <li><a href="#installation">Installation</a></li>\n      </ul>\n    </li>\n    <li><a href="#usage">Usage</a></li>\n    <li><a href="#roadmap">Roadmap</a></li>\n    <li><a href="#contributing">Contributing</a></li>\n    <li><a href="#license">License</a></li>\n    <li><a href="#contact">Contact</a></li>\n    <li><a href="#acknowledgments">Acknowledgments</a></li>\n  </ol>\n</details>\n\n<!-- ABOUT THE PROJECT -->\n\n## About The Project\n\nsteam-market-history is a command line tool written in Python which allows you to extract your entire Steam Market History with all transaction (sales/purchases) in a CSV or HTML file.\n\n### Key features\n\n- Extract your **entire** Steam Market History\n- Create a CSV-File with all transactions\n- Overview of _all_ transactions on a user-friendly webpage with searchable and filterable results\n\n### Built With\n\n- [Python](https://www.python.org/)\n- [Typer](https://typer.tiangolo.com/)\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- GETTING STARTED -->\n\n## Getting Started\n\nTo get a local copy up and running follow these simple example steps.\n\n### Prerequisites\n\n- Python >= 3.8\n\n### Installation\n\nPip (recommended):\n\n```python\npip install steam-market-history\n```\n\nManual:\n\n1. Clone the repo\n   ```sh\n   git clone https://gitlab.com/fabieu-ci/steam-market-history.git\n   ```\n2. Install poetry (if not already installled)\n   ```sh\n   pip install poetry\n   ```\n3. Install dependencies and start virtual environment\n   ```sh\n   poetry install && poetry shell\n   ```\n4. Start virtual environment\n   ```sh\n   poetry shell\n   ```\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- USAGE EXAMPLES -->\n\n## Usage\n\nCurrently the following commands are supported:\n\n### `export`\n\nExport your steam market history to a CSV or HTML file\n\n> When running the tool you will be prompted to insert your steam credentials. All processing is done locally on your own computer. This package does not save your credentials in any way.\n\nOptions:\n\n- `--csv` - Export to csv file\n- `--html` - Export to html file\n- `--path` - Output directory for all file based operations (default: current working directory)\n- `--launch` / `--no-launch` - Automatically open file(s) after export (default: `--launch`)\n- `--cache` / `--no-cache` - Create a file cache for all market transactions (default: `--no-cache`)\n- `--interactive` / `--non-interactive` - Interactive or non-interactive steam authentication [default: `--interactive`]\n\nExample:\n\n```\nsteam-market-history export --csv --path /tmp/out\n```\n\n### `version`\n\nDisplay detailed information about this package\n\n```\nsteam-market-history version\n```\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- ROADMAP -->\n\n## Roadmap\n\n- [ ] Add options of verbosity\n- [ ] Export to JSON\n\nSee the [open issues](https://gitlab.com/fabieu-ci/steam-market-history/-/issues) for a full list of proposed features (and known issues).\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- CONTRIBUTING -->\n\n## Contributing\n\nContributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.\n\nIf you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".\nDon\'t forget to give the project a star! Thanks again!\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- LICENSE -->\n\n## License\n\nDistributed under the MIT License. See `LICENSE` for more information.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- CONTACT -->\n\n## Contact\n\nsustineo\\_ - [@sustineo\\_](https://twitter.com/sustineo_) - dev@sustineo.de\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- ACKNOWLEDGMENTS -->\n\n## Acknowledgments\n\n- [Typer](https://typer.tiangolo.com/)\n- [Choose a license](https://choosealicense.com/)\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## Disclaimer:\n\nThe Steam Market History Exported is a community project and is not affiliated with Valve or Steam.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n',
    'author': 'Fabian Eulitz',
    'author_email': 'dev@sustineo.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fabieu/steam-market-history',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
