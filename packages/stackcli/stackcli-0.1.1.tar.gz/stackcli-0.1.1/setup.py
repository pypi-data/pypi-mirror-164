# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src',
 'src.comm',
 'src.core',
 'src.dataset',
 'src.storage',
 'src.storage.classes',
 'src.tests',
 'src.user',
 'src.user.database',
 'src.user.license',
 'stack_api']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.60,<2.0.0',
 'fastapi>=0.80.0,<0.81.0',
 'google-cloud-datastore>=2.8.1,<3.0.0',
 'google-cloud-storage>=2.5.0,<3.0.0',
 'maskpass>=0.3.6,<0.4.0',
 'pymongo>=4.2.0,<5.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['stackcli = stack_api.api_cli:app']}

setup_kwargs = {
    'name': 'stackcli',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Stack\n\n\n### Features to implement\n\n#### For stack status\n\n- [] Even  if there are no changes,  it would be great that  `stack status` returns something.\n',
    'author': 'Toni Rosinol',
    'author_email': 'arosinol@getstack.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
