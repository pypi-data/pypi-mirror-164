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
    'version': '0.1.2',
    'description': '🖼️ An image select component for Streamlit',
    'long_description': '# streamlit-image-select 🖼️\n\n[![Badge](https://img.shields.io/badge/add%20one-badge-blue)](https://shields.io/)\n\nAn image select component for Streamlit\n\n# Sample project &nbsp;👻\n\n[![Badge](https://img.shields.io/badge/add%20one-badge-blue)](https://shields.io/)\n\n**This one sentence explains your project in simple words.**\n\nAdd some more description of your project here. Try to keep it short but explain most features. Two to four lines of text are usually good. Link to frameworks and tools that you integrate. Some more text and more text and more text and more text and more text and more text and more text and more text and more text. \n\n<sup>If needed: Alpha/Beta version, use with care.</sup>\n\n---\n\n<h3 align="center">\n  🎉 <a href="https://github.com/jrieke/readme-template">Try it out</a> 🎉\n</h3>\n\n---\n\n<p align="center">\n    <a href="https://github.com/jrieke/readme-template"><img src="demo.gif" width=600></a>\n</p>\n\n\n## Installation\n\n```bash\npip install sample-package\n```\n\nYou can add some more detailed instructions here. Don\'t forget to mention any special dependencies.\n\n\n## How to use it\n\n```python\nimport sample_package\n\nsample_package.do_something()\nsample_package.do_something_else()\n```\n\nAdd some description of what will happen. Or an image. Or the terminal output of the command above. One to three paragraphs of text is a good guideline here. Ideally, the user should be able to run a simple example with this instruction. Anything more advanced can go to the section below. \n\n\n## More options\n\n- Here\'s something else you can do:\n\n  ```python\n  sample_package.super_advanced_func()\n  ```\n\n- Also, there\'s feature X. \n\n- If you already have a lot of features, you can split this up into several sections.\n\n\n## TODOs\n\nPRs are welcome! If you want to work on any of these things, please open an issue to coordinate.\n\n- [ ] List a few things you want to do\n- [ ] The idea is to let people know where you are headed, so they can see if they want to help you\n- [x] ~~If you\'re working on an item, you can strike it through, so people know they shouldn\'t start working on it~~\n',
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
