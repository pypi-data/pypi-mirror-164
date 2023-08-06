# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflownz', 'airflownz.hooks', 'airflownz.operators']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow-providers-common-sql>=1.1.0,<2.0.0',
 'apache-airflow>=2.2.0,<3.0.0',
 'nzpy>=1.13.2,<2.0.0']

entry_points = \
{'apache_airflow_provider': ['provider_info = '
                             'airflownz.provider_info:get_provider_info']}

setup_kwargs = {
    'name': 'airflownz',
    'version': '1.0.1',
    'description': 'Airflow Hook for Netezza',
    'long_description': '# Airflow Hook for Netezza\n\nInstall this package in the python environment with Airflow to use the Netezza Hook.\n\nInstallation: `pip install airflownz`\n\n\nMore about creating your own provider packages - https://airflow.apache.org/docs/apache-airflow-providers/index.html#how-to-create-your-own-provider\n',
    'author': 'Sanjay Renduchintala',
    'author_email': 'san8055@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
