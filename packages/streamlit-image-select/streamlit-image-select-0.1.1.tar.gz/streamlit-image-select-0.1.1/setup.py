# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['streamlit_image_select']

package_data = \
{'': ['*'],
 'streamlit_image_select': ['frontend/*',
                            'frontend/build/*',
                            'frontend/build/static/js/*',
                            'frontend/public/*',
                            'frontend/src/*']}

install_requires = \
['streamlit>=1.12.0,<2.0.0']

setup_kwargs = {
    'name': 'streamlit-image-select',
    'version': '0.1.1',
    'description': '🖼️ An image select component for Streamlit',
    'long_description': None,
    'author': 'Johannes Rieke',
    'author_email': 'johannes.rieke@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
