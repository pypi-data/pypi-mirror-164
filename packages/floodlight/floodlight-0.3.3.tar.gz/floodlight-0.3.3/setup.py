# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['floodlight',
 'floodlight.core',
 'floodlight.io',
 'floodlight.metrics',
 'floodlight.models',
 'floodlight.transforms',
 'floodlight.utils',
 'floodlight.vis']

package_data = \
{'': ['*'],
 'floodlight': ['.data/eigd_dataset/*',
                '.data/statsbomb_dataset/*',
                '.data/statsbomb_dataset/matches/11/*',
                '.data/statsbomb_dataset/matches/16/*',
                '.data/statsbomb_dataset/matches/2/*',
                '.data/statsbomb_dataset/matches/37/*',
                '.data/statsbomb_dataset/matches/43/*',
                '.data/statsbomb_dataset/matches/49/*',
                '.data/statsbomb_dataset/matches/55/*',
                '.data/statsbomb_dataset/matches/72/*']}

install_requires = \
['h5py>=3.6.0,<4.0.0',
 'iso8601>=1.0.2,<2.0.0',
 'lxml>=4.6.4,<5.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.4,<2.0.0',
 'pytz>=2021.3,<2022.0',
 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'floodlight',
    'version': '0.3.3',
    'description': 'A high-level framework for sports data analysis',
    'long_description': "[version-image]: https://img.shields.io/pypi/v/floodlight?color=006666\n[version-url]: https://pypi.org/project/floodlight/\n[python-image]: https://img.shields.io/pypi/pyversions/floodlight?color=006666\n[python-url]: https://pypi.org/project/floodlight/\n[docs-image]: https://readthedocs.org/projects/floodlight/badge/?version=latest\n[docs-url]: https://floodlight.readthedocs.io/en/latest/?badge=latest\n[tutorial-url]: https://floodlight.readthedocs.io/en/latest/guides/getting_started.html\n[build-image]: https://github.com/floodlight-sports/floodlight/actions/workflows/build.yaml/badge.svg\n[build-url]: https://github.com/floodlight-sports/floodlight/actions/workflows/build.yaml\n[lint-image]: https://github.com/floodlight-sports/floodlight/actions/workflows/linting.yaml/badge.svg\n[lint-url]: https://github.com/floodlight-sports/floodlight/actions/workflows/linting.yaml\n[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg\n[black-url]: https://github.com/psf/black\n[contrib-image]: https://img.shields.io/badge/contributions-welcome-006666\n[contrib-url]: https://github.com/floodlight-sports/floodlight/blob/main/CONTRIBUTING.md\n[arxiv-image]: https://img.shields.io/badge/arXiv-2206.02562-b31b1b.svg\n[arxiv-url]: https://arxiv.org/abs/2206.02562\n[codecov-image]: https://codecov.io/gh/floodlight-sports/floodlight/branch/develop/graph/badge.svg?token=RLY582UBC6\n[codecov-url]: https://codecov.io/gh/floodlight-sports/floodlight\n\n\n# floodlight\n[![Latest Version][version-image]][version-url]\n[![Python Version][python-image]][python-url]\n[![Documentation Status][docs-image]][docs-url]\n[![Build Status][build-image]][build-url]\n[![Linting Status][lint-image]][lint-url]\n[![Codecov][codecov-image]][codecov-url]\n[![Code style: black][black-image]][black-url]\n[![arXiv][arxiv-image]][arxiv-url]\n\n## A high-level, data-driven sports analytics framework\n\n**floodlight** is a Python package for streamlined analysis of sports data. It is\ndesigned with a clear focus on scientific computing and built upon popular libraries\nsuch as *numpy* or *pandas*.\n\nLoad, integrate, and process tracking and event data, codes and other match-related\ninformation from major data providers. This package provides a set of  standardized\ndata objects to structure and handle sports data, together with a suite of common\nprocessing operations such as transforms or data manipulation methods.\n\nAll implementations run completely provider- and sports-independent, while maintaining\na maximum of flexibility to incorporate as many data flavours as possible. A high-level\ninterface allows easy access to all standard routines, so that you can stop worrying\nabout data wrangling and start focussing on the analysis instead!\n\n----------------------------------------------------------------------------------------\n\n* [Quick Demo](#quick-demo)\n* [Features](#features)\n* [Installation](#installation)\n* [Documentation](#documentation)\n* [How to contribute](#contributing)\n\n----------------------------------------------------------------------------------------\n\n### Quick Demo\n\n**floodlight** simplifies sports data loading, processing and advanced performance\nanalyses. Check out the example below, where querying a public data sample, filtering\nthe data and computing the expended metabolic work of the active home team players is\ndone in a few lines of code:\n\n```\n>>> from floodlight.io.datasets import EIGDDataset\n>>> from floodlight.transforms.filter import butterworth_lowpass\n>>> from floodlight.models.kinetics import MetabolicPowerModel\n\n>>> dataset = EIGDDataset()\n>>> home_team_data, away_team_data, ball_data = dataset.get()\n\n>>> home_team_data = butterworth_lowpass(home_team_data)\n\n>>> model = MetabolicPowerModel()\n>>> model.fit(home_team_data)\n>>> metabolic_power = model.cumulative_metabolic_power()\n\n>>> print(metabolic_power[-1, 0:7])\n\n[1669.18781115 1536.22481121 1461.03243489 1488.61249785  773.09264071\n 1645.01702421  746.94057676]\n```\n\nTo find out more, see the full set of features below or get started quickly with\n[one of our many tutorials][tutorial-url] from the official documentation!\n\n\n### Features\n\nThis project is still under development, and we hope to expand the set\nof features in the future. At this point, we provide core data structures,\nparsing functionality for major data providers, access to public data sets, data\nfiltering, basic plotting routines and computational models.\n\n#### Data-level Objects\n\n- Tracking data\n- Event data\n- Pitch information\n- Codes such as ball possession information\n- Properties such as distances or advanced computations\n\n#### Parser\n\n- ChyronHego (Tracking data, Codes)\n- DFL (Tracking data, Event data, Codes)\n- Kinexon (Tracking data)\n- Opta (Event data - F24 feeds)\n- Second Spectrum (Tracking data)\n- StatsPerform (Tracking data, Event data - also directly from URLs)\n- StatsBomb (Event data)\n\n#### Datasets\n\n- EIGD-H (Handball tracking data)\n- StatsBomb OpenData (Football event data)\n\n#### Manipulation and Plotting\n\n- Spatial transformations for all data structures\n- Lowpass-filter tracking data\n- Slicing and selection methods\n- Plot pitches and tracking data\n\n#### Models and Metrics\n\n- Centroids\n- Distances, Velocities, Accelerations\n- Metabolic Power and Equivalent Distances\n- Approximate Entropy\n\n### Installation\n\nThe package can be installed easily via pip:\n\n```\npip install floodlight\n```\n\n\n### Documentation\n\nYou can find all documentation [here][docs-url].\n\n\n\n### Contributing\n\n[![Contributions][contrib-image]][contrib-url]\n\nCheck out [Contributing.md][contrib-url] for a quick rundown of what you need to\nknow to get started. We also provide an extended, beginner-friendly guide on how to\nstart contributing in our documentation.\n\n\n\n### Citing\n\nIf you've used *floodlight* in your scientific work, please cite the [corresponding paper][arxiv-url].\n\n```\n@misc{Raabe2022floodlight,\n  doi = {10.48550/ARXIV.2206.02562},\n  url = {https://arxiv.org/abs/2206.02562},\n  author = {Raabe, Dominik and Biermann, Henrik and Bassek, Manuel and Wohlan, Martin and Komitova, Rumena and Rein,\n           Robert and Groot, Tobias Kuppens and Memmert, Daniel},\n  title = {floodlight -- A high-level, data-driven sports analytics framework},\n  publisher = {arXiv},\n  year = {2022},\n}\n```\n\n\n\n### Why\n\nWhy do we need another package that introduces its own data structures and ways of dealing with certain problems?\nAnd what's the purpose of trying to integrate all different data sources and fit them into a single framework?\nEspecially since there already exist packages that aim to solve certain parts of that pipeline?\n\nOur answer is - although we love those packages out there - that we did not find a solution that did fit our needs.\nAvailable packages are either tightly connected to a certain data format/provider, adapt to the subtleties of a\nparticular sport, or solve *one* particular problem. This still left us with the essential problem of adapting to\ndifferent interfaces.\n\nWe felt that as long as there is no underlying, high-level framework, each and every use case again and again needs its\nown implementation. At last, we found ourselves refactoring the same code - and there are certain data processing or\nplotting routines that are required in *almost every* project - over and over again just to fit the particular data\nstructures we're dealing with at that time.\n\n\n### About\n\nThis project has been kindly supported by the [Institute of Exercise Training and Sport\nInformatics](https://www.dshs-koeln.de/en/institut-fuer-trainingswissenschaft-und-sportinformatik/) at the German Sport\nUniversity Cologne under supervision of Prof. Daniel Memmert.\n\n\n\n### Related Projects\n\n- [matplotsoccer](https://github.com/TomDecroos/matplotsoccer)\n- [kloppy](https://github.com/PySport/kloppy)\n- [codeball](https://github.com/metrica-sports/codeball)\n",
    'author': 'draabe',
    'author_email': 'draabx@posteo.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/floodlight-sports/floodlight',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
