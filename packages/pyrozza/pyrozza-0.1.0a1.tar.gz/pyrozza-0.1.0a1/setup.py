# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrozza', 'pyrozza.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pyrozza',
    'version': '0.1.0a1',
    'description': 'A Python wrapper for the UK Police API',
    'long_description': '![Build](https://github.com/regoawt/pyrozza/actions/workflows/cicd.yml/badge.svg)\n# pyrozza\nA Python wrapper for the UK Police API\n\n## Usage\nInstantiate the client:\n```python\nclient = pyrozza.Client()\n```\n\nCurrently, the following methods are available:\n```python\nclient.street_level_crimes(\n        lat: float = None,\n        lon: float = None,\n        poly: List[tuple] = None,\n        date: str = None,\n    )\nclient.street_level_outcomes(\n        lat: float = None,\n        lon: float = None,\n        poly: List[tuple] = None,\n        location_id: int = None,\n        date: str = None\n    )\n\nclient.crime_categories(date: str = None)\n```\n\nFor the geo-related kwargs, only one of the following must be provided:\n- `lat` AND `lon`\n- `poly`\n- `location_id`',
    'author': 'Armand Rego',
    'author_email': 'armandrego@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/regoawt/pyrozza',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
