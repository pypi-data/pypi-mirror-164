# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['componentes']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pycarol>=2.54.0,<3.0.0',
 'pymongo>=4.1.0,<5.0.0',
 'readme']

setup_kwargs = {
    'name': 'componentes',
    'version': '0.1.5',
    'description': 'Componetes de uso de teste',
    'long_description': None,
    'author': 'Bruno',
    'author_email': 'teste@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
