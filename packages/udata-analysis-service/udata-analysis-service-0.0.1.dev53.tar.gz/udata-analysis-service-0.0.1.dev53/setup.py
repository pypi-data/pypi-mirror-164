# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['udata_analysis_service', 'udata_analysis_service.utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.21.21,<1.22.0',
 'celery>=5.2.3,<5.3.0',
 'click>=8.0.4,<8.1.0',
 'csv-detective>=0.4.5,<0.5.0',
 'flake8>=4.0.1,<4.1.0',
 'flit>=3.6.0,<3.7.0',
 'kafka-python>=2.0.2,<2.1.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'redis>=4.1.4,<4.2.0',
 'requests>=2.27.1,<2.28.0',
 'udata_event_service>=0.0.8,<0.1.0']

entry_points = \
{'console_scripts': ['udata-analysis-service = udata_analysis_service.cli:cli']}

setup_kwargs = {
    'name': 'udata-analysis-service',
    'version': '0.0.1.dev53',
    'description': '',
    'long_description': None,
    'author': 'Etalab',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
