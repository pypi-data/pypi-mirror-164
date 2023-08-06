# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flow_helpers_tps']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy',
 'boto3',
 'botocore',
 'cryptography',
 'facebook-business',
 'flatdict',
 'google',
 'google-api-python-client',
 'httplib2',
 'office365',
 'pandas',
 'pendulum',
 'poetry',
 'pysftp',
 'uuid']

setup_kwargs = {
    'name': 'flow-helpers-tps',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'joshliu3',
    'author_email': 'jliu@theparkingspot.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
