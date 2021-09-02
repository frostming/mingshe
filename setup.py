# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mingshe', 'mingshe._vendor.pegen']

package_data = \
{'': ['*'], 'mingshe': ['_vendor/*'], 'mingshe._vendor.pegen': ['templates/*']}

entry_points = \
{'console_scripts': ['mingshe = mingshe.commands:main']}

setup_kwargs = {
    'name': 'mingshe',
    'version': '0.3.0',
    'description': '',
    'long_description': '# MíngShé\n\nA better [Python](https://www.python.org/) superset language.\n\n> “鲜山多金玉，无草木，鲜水出焉，而北流注于伊水。其中多鸣蛇，其状如蛇而四翼，其音如磬，见则其邑大旱”——《山海经》\n\n## Install\n\n```\npip install mingshe\n```\n\n## Usage\n\n```bash\nmingshe --help\n```\n\n## Pipe\n\nExample:\n\n```\nrange(10) |> sum |> print\n```\n\nCompile to:\n\n```python\nprint(sum(range(10)))\n```\n\n## Conditional\n\nExample:\n\n```\na ? b : c\n```\n\nCompile to:\n\n```python\nb if a else c\n```\n\n## Partial\n\nExample:\n\n```\nsquare = pow(?, 2)\n```\n\nCompile to:\n\n```python\n(lambda pow: lambda _0, /: pow(_0, 2))(pow)\n```\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/mingshe',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

