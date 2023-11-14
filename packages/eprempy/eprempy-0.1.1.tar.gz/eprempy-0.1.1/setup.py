# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['eprempy',
 'eprempy.base',
 'eprempy.dataset',
 'eprempy.measurable',
 'eprempy.measured',
 'eprempy.metric',
 'eprempy.numeric',
 'eprempy.observable',
 'eprempy.observer',
 'eprempy.parameter',
 'eprempy.physical',
 'eprempy.quantity',
 'eprempy.real',
 'eprempy.symbolic']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.0',
 'netCDF4>=1.5.8',
 'numpy>=1.26.0',
 'scipy>=1.7.3',
 'typing-extensions>=4.8.0,<5.0.0']

setup_kwargs = {
    'name': 'eprempy',
    'version': '0.1.1',
    'description': 'Tools for working with EPREM simulation runs',
    'long_description': '# EPREM(py)\n\nTools for working with EPREM simulation runs\n\n## Installation\n\n```bash\n$ pip install eprempy\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`eprempy` was created by Matt Young. It is licensed under the terms of the BSD 3-Clause license.\n\n## Credits\n\n`eprempy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Matt Young',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.13',
}


setup(**setup_kwargs)
