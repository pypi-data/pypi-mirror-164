# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['siemens']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'siemens',
    'version': '0.1.0',
    'description': 'A placeholder package for Siemens',
    'long_description': '# Siemens\n\nThis is a placeholder package reserved for a potential [PEP 423](https://peps.python.org/pep-0423)\npackaging convention in the future.\n\nFor Siemens Open Source projects, see [opensource.siemens.com](https://opensource.siemens.com) and\n[github.com/siemens](https://github.com/siemens).\n',
    'author': 'Siemens Open Source',
    'author_email': 'opensource@siemens.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://opensource.siemens.com',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
