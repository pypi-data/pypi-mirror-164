# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chtk']

package_data = \
{'': ['*']}

install_requires = \
['librosa>=0.9.2,<0.10.0', 'numpy>=1.23.2,<2.0.0']

setup_kwargs = {
    'name': 'chtk',
    'version': '0.0.1',
    'description': 'A data science toolkit for working with Clone Hero charts.',
    'long_description': '# chtk\n\n#### Purpose\nchtk is short for "Clone Hero Toolkit." It is a suite of data science tools that are useful for working with Clone Hero data.\n\n### Features\n\n### Getting Started\nchtk can be installed using pip\n```bash\npip install chtk\n```\n\n### Usage\nTODO\n\n### Examples\nTODO\n\n### API\n\n\n### Contribution\nTODO\n\n### Author\nTODO',
    'author': 'Elliott Waissbluth',
    'author_email': 'ewaissbluth@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/elliottwaissbluth/chtk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
