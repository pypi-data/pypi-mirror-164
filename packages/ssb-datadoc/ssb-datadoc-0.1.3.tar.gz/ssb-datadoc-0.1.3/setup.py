# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datadoc',
 'datadoc.backend',
 'datadoc.frontend',
 'datadoc.frontend.callbacks',
 'datadoc.frontend.components',
 'datadoc.frontend.fields',
 'datadoc.tests']

package_data = \
{'': ['*'],
 'datadoc': ['assets/*'],
 'datadoc.tests': ['resources/*', 'resources/existing_metadata_file/*']}

install_requires = \
['dash-bootstrap-components>=1.1.0,<2.0.0',
 'dash>=2.4.1,<3.0.0',
 'jupyter-dash>=0.4.2,<0.5.0',
 'pandas>=1.4.2,<2.0.0',
 'pyarrow>=8.0.0,<9.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'ssb-datadoc-model==0.1.3']

entry_points = \
{'console_scripts': ['datadoc = datadoc:main']}

setup_kwargs = {
    'name': 'ssb-datadoc',
    'version': '0.1.3',
    'description': "Document dataset metadata. For use in Statistics Norway's metadata system.",
    'long_description': '# Datadoc\n\n![Datadoc Unit tests](https://github.com/statisticsnorway/datadoc/actions/workflows/unit-tests.yml/badge.svg) ![Code coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/mmwinther/0c0c5bdfc360b59254f2c32d65914025/raw/pytest-coverage-badge-datadoc.json) ![PyPI version](https://img.shields.io/pypi/v/ssb-datadoc) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)\n\nDocument datasets in Statistics Norway\n\n## Usage example\n\n1. Run `from datadoc import main; main("./path/to/your/dataset")` to run Datadoc on a dataset of your choosing.\n1. Complete metadata as you desire\n1. Click `Lagre` to save a metadata document together with your dataset\n\n### If the datadoc package is not installed\n\n1. Clone this repo to your Jupyter instance (or local machine)\n1. Open the `DataDoc.ipynb` Notebook and run the cell to see the example dataset\n\n![DataDoc in use](./doc/change-language-example.gif)\n\n## Contributing\n\n### Dependency Management\n\nPoetry is used for dependency management.\n\nTo install all required dependencies in a virtual environment run `poetry install`. To add a new dependency to the project run `poetry add <package name>`.\n\n### Run project locally in Jupyter\n\nTo run the project locally in Jupyter run:\n\n```bash\npoetry install\npoetry run jupyter lab\n```\n\nA Jupyter instance should open in your browser. Once there, open the `*.ipynb` file. Before running it, select the correct interpreter via `Kernel > Change Kernel > datadoc`.\n\n### Run tests\n\n1. Install dev dependencies (see [Dependency Management](#dependency-management))\n1. Run `poetry shell` to open a shell in the Virtual Environment for the project\n1. Run `pytest` in the root of the project\n',
    'author': 'Statistics Norway',
    'author_email': 'mmw@ssb.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/statisticsnorway/datadoc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
