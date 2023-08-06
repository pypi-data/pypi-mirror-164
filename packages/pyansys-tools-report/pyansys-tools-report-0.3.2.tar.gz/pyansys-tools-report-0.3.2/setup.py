# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ansys', 'ansys.tools.report']

package_data = \
{'': ['*']}

install_requires = \
['pyvista>=0.34.1', 'scooby>=0.5.12']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.0,<5.0'],
 'doc': ['Sphinx==5.1.1',
         'numpydoc==1.4.0',
         'ansys_sphinx_theme==0.5.1',
         'Sphinx-copybutton==0.5.0',
         'myst-parser==0.18.0'],
 'test': ['pytest==7.1.2', 'pytest-cov==3.0.0']}

setup_kwargs = {
    'name': 'pyansys-tools-report',
    'version': '0.3.2',
    'description': "Ansys tool for reporting your Python environment's package versions and hardware resources in a standardized way.",
    'long_description': '# PyAnsys Tools Report\n\n[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)\n[![Python](https://img.shields.io/pypi/pyversions/pyansys-tools-report?logo=pypi)](https://pypi.org/project/pyansys-tools-report/)\n[![PyPi](https://img.shields.io/pypi/v/pyansys-tools-report.svg?logo=python&logoColor=white)](https://pypi.org/project/pyansys-tools-report)\n[![codecov](https://codecov.io/gh/pyansys/pyansys-tools-report/branch/main/graph/badge.svg)](https://codecov.io/gh/pyansys/pyansys-tools-report)\n[![GH-CI](https://github.com/pyansys/pyansys-tools-report/actions/workflows/ci.yml/badge.svg)](https://github.com/pyansys/pyansys-tools-report/actions/workflows/ci.yml)\n[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)\n\nAnsys tool for reporting your Python environment\'s package versions and hardware resources in a standardized way.\n\n## Table of contents\n\n<!--ts-->\n   * [Introduction](#introduction)\n   * [Documentation and issues](#documentation-and-issues)\n   * [How does it work?](#how-does-it-work)\n   * [Installation](#installation)\n      * [Offline Installation](#offline-installation)\n   * [Rendering the docs](#rendering-the-docs)\n   * [Running the tests](#running-the-tests)\n   * [Requirements](#requirements)\n<!--te-->\n\n\n## Introduction\nThe PyAnsys Tools Report is a PyAnsys package to homogenize among all the different repositories\nthe output of system and environment reports related to Ansys products. Its main goals are:\n\n* Provide an homogeneous output style to system and environment reports.\n* Allows for customization when reporting Ansys variables and libraries.\n\nYou are welcome to help contribute to it in any possible way. Please submit an issue with\nany proposal you may have.\n\n## Documentation and issues\n\nSee the [documentation](https://report.tools.docs.pyansys.com/) page for more details.\n\nYou are welcome to help contribute to it in any possible way. Please submit\n[here](https://github.com/pyansys/pyansys-tools-report/issues) an issue with\nany proposal you may have. This is the best place to post questions and code.\n\n## How does it work?\nThis repository basically contains a simple Python package which you can import as follows\n(once installed):\n\n```python\n    import ansys.tools.report as pyansys_report\n```\n\nOnce imported, you can then start playing around with it:\n\n```python\n    # Instantiate a "default" Report\n    rep = pyansys_report.Report()\n```\n\nRefer to the [online documentation](https://report.tools.docs.pyansys.com/) to see the details of the module.\n\n## Installation\n\nThis package may be installed following two procedures: either the pip package manager installation or\nthe manual installation. The process to be followed for each of them is shown in the upcoming sections.\n\nThe ``pyansys-tools-report`` package currently supports Python >=3.7 on Windows, Mac OS, and Linux.\n\n### Standard installation\nInstall the latest release from [PyPi](https://pypi.org/project/pyansys-tools-report) with:\n\n```bash\n   pip install pyansys-tools-report\n```\n\nAlternatively, install the latest from GitHub via:\n\n```bash\n   pip install git+https://github.com/pyansys/pyansys-tools-report.git\n```\n\nFor a local "development" version, install with (requires pip >= 22.0):\n\n```bash\n   git clone https://github.com/pyansys/pyansys-tools-report.git\n   cd pyansys-tools-report\n   pip install .\n```\n\n\n### Offline installation\n\nIf you lack an internet connection on your install machine, the recommended way\nof installing PyAnsys Tools Report is downloading the wheelhouse archive from the\n[Releases Page](https://github.com/pyansys/pyansys-tools-report/releases) for your\ncorresponding machine architecture.\n\nEach wheelhouse archive contains all the python wheels necessary to install\nPyAnsys Tools Report from scratch on Windows and Linux for Python >=3.7. You can install\nthis on an isolated system with a fresh python or on a virtual environment.\n\nFor example, on Linux with Python 3.7, unzip it and install it with the following:\n\n```bash\n   unzip pyansys-tools-report-v0.3.2-wheelhouse-Linux-3.7.zip wheelhouse\n   pip install pyansys-tools-report -f wheelhouse --no-index --upgrade --ignore-installed\n```\n\nIf you\'re on Windows with Python 3.9, unzip to a ``wheelhouse`` directory and\ninstall using the same command as before.\n\nConsider installing using a [virtual environment](https://docs.python.org/3/library/venv.html).\nMore information on general PyAnsys development can be found in the\n[PyAnsys Developer\'s Guide](https://dev.docs.pyansys.com/).\n\n## Rendering the docs\n\nIn case you were interested in rendering the docs locally, you need to clone the repository and\ninstall the docs requirements first:\n\n```bash\n   git clone https://github.com/pyansys/pyansys-tools-report.git\n   cd pyansys-tools-report\n   pip install -e .[doc]\n```\n\nOnce you have the requirements, render the docs by running the following:\n\n```bash\n   make -C doc html\n```\n\nThis generates the HTML version of the docs, which you may find in the following directory:\n\n```bash\n   cd doc/_build/html\n```\n\nYou can also clean the build directory by running the following command:\n\n```bash\n   make -C doc clean\n```\n\n## Running the tests\n\nIn case you were interested in running the tests locally, you need to clone the repository and\ninstall the test requirements first:\n\n```bash\n   git clone https://github.com/pyansys/pyansys-tools-report.git\n   cd pyansys-tools-report\n   pip install -e .[test]\n```\n\nOnce you have the requirements, run the tests by running the following:\n\n```bash\n   pytest\n```\n\nThe ``pyproject.toml`` file already contains some default configuration for running the tests. Please,\ntake a look at it if you may want to run it with your own configuration.\n\n\n## Requirements\n\nThis Python package does not contain specific requirements files. Instead, its requirements may\nbe found within the ``pyproject.toml`` file which defines the package. Thus, when the package is\ninstalled it automatically detects the dependencies needed and installs them.\n',
    'author': 'ANSYS, Inc.',
    'author_email': 'pyansys.support@ansys.com',
    'maintainer': 'PyAnsys developers',
    'maintainer_email': 'pyansys.maintainers@ansys.com',
    'url': 'https://report.tools.docs.pyansys.com/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
