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
    'version': '0.1.3',
    'description': '🖼️ An image select component for Streamlit',
    'long_description': '# streamlit-image-select 🖼️\n\n[![Badge](https://img.shields.io/badge/add%20one-badge-blue)](https://shields.io/)\n\n**An image select component for Streamlit.**\n\nThis custom component works just like `st.selectbox` but with images. It\'s a great option\nif you want to let the user select an example image, e.g. for a computer vision app!\n\n---\n\n<h3 align="center">\n  🏃 <a href="https://image-select.streamlitapp.com/">Try out the demo app</a> 🏃\n</h3>\n\n---\n\n<p align="center">\n    <a href="https://image-select.streamlitapp.com/"><img src="demo.gif" width=600></a>\n</p>\n\n\n## Installation\n\n```bash\npip install streamlit-image-select\n```\n\n## Usage\n\n```python\nfrom streamlit_image_select import image_select\nimg = image_select("Label", ["image1.png", "image2.png", "image3.png"])\nst.write(img)\n```\n\nSee [the demo app](https://image-select.streamlitapp.com/) for a detailed guide!\n\n\n## Development\n\nNote: you only need to run these steps if you want to change this component or \ncontribute to its development!\n\n### Setup\n\nFirst, clone the repository:\n\n```bash\ngit clone https://github.com/jrieke/streamlit-image-select.git\ncd streamlit-image-select\n```\n\nInstall the Python dependencies:\n\n```bash\npoetry install --dev\n```\n\nAnd install the frontend dependencies:\n\n```bash\ncd streamlit_image_select/frontend\nnpm install\n```\n\n### Making changes\n\nTo make changes, first go to `streamlit_image_select/__init__.py` and make sure the \nvariable `_RELEASE` is set to `False`. This will make the component use the local \nversion of the frontend code, and not the built project. \n\nThen, start one terminal and run:\n\n```bash\ncd streamlit_image_select/frontend\nnpm start\n```\n\nThis starts the frontend code on port 3001.\n\nOpen another terminal and run:\n\n```bash\npoetry shell\nstreamlit run demo.py\n```\n\nThis starts the demo app. Now you can make changes to the Python or Javascript code in \n`streamlit_image_select` and the demo app should update automatically!\n\n\n### Publishing on PyPI\n\nSwitch the variable `_RELEASE` in `streamlit_image_select/__init__.py` to `True`. \nIncrement the version number in `pyproject.toml`. \n\nBuild the frontend code with:\n\n```bash\ncd streamlit_image_select/frontend\nnpm run build\n```\n\nAfter this has finished, build and upload the package to PyPI:\n\n```bash\ncd ..\npoetry build\npoetry publish\n```\n',
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
