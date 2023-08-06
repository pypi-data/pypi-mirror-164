# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sat_downloaders']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sat-downloaders',
    'version': '0.0.2',
    'description': '',
    'long_description': 'None',
    'author': 'Martin Raspaud',
    'author_email': 'martin.raspaud@smhi.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
