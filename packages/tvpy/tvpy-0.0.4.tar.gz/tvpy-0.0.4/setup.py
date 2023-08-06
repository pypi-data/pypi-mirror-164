# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tvpy']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'requests>=2.28.1,<3.0.0', 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['tv-html = tvpy.main:tv_html',
                     'tv-json = tvpy.main:tv_json']}

setup_kwargs = {
    'name': 'tvpy',
    'version': '0.0.4',
    'description': '📺 TvPy',
    'long_description': '# 📺 TvPy \nGenerate html from folder names.\n\n## Installation\npip install tvpy\n\n## Usage\n```shell\n> mkdir Carnival.Row Resident.Alien Liar Under.the.Banner.of.Heaven\n> tv-json . && tv-html\n```\n',
    'author': 'Gilad Kutiel',
    'author_email': 'gilad.kutiel@gmail.com',
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
