# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_analytics', 'simple_analytics.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.14,<4.0.0']

setup_kwargs = {
    'name': 'django-simple-analytics',
    'version': '0.1.2',
    'description': 'A simple django packages to track requests on the site',
    'long_description': '# Django Simple Analytics\n\n⚠️ This package is still in beta. Do not use for production ⚠️\n\nSimple analytics is a very simple package to track requests done to the website and store them in database.\n\n\n## Installation\n\nFrom PYPi using `pip`:\n```\npip install django-simple-analytics\n```\n\n## Usage\n\nIn order to install the package add the following line to `INSTALLED_APPS`\n\n```python\nINSTALLED_APPS = [\n    ...\n    "simple_analytics",\n]\n```\n\nThis will make the model available for you to call and query. To enable the middleware, add this at the bottom of the middleware list:\n\n```python\nMIDDLEWARE = [\n    ...\n    "simple_analytics.middleware.page_counts",\n]\n```\n\nThen, you need to run migrations, finally:\n\n```console\n./manage.py migrate\n```\n\nTo actually create the table in the database.\n\nNow every request done to the django website will be recorded in the database with the following fields:\n\n- Date: The date pf the request.\n- Page: The path of the request.\n- Method: The verb used to request the page.\n- Whether the page exists or not.\n- User: The user who performed the request. If the user is not authenticated, it will show as AnonymousUser.\n- view\\_count: The number of requests to that page, per date and per method used.\n\n## Licence\n\nThis package is distributed under [MIT Licence](./LICENCE).\n',
    'author': 'Ferran Jovell',
    'author_email': 'ferran.jovell+gh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mrswats/django-simple-analytics',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
