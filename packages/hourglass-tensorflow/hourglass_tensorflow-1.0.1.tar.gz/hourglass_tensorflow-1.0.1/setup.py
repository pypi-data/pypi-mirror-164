# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hourglass_tensorflow',
 'hourglass_tensorflow.handlers',
 'hourglass_tensorflow.layers',
 'hourglass_tensorflow.losses',
 'hourglass_tensorflow.metrics',
 'hourglass_tensorflow.models',
 'hourglass_tensorflow.types',
 'hourglass_tensorflow.types.config',
 'hourglass_tensorflow.utils',
 'hourglass_tensorflow.utils.parsers',
 'hourglass_tensorflow.utils.sets']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pydantic>=1.9.2,<2.0.0',
 'scipy>=1.9.0,<2.0.0']

entry_points = \
{'console_scripts': ['htf = cli.__init__:cli']}

setup_kwargs = {
    'name': 'hourglass-tensorflow',
    'version': '1.0.1',
    'description': 'Tensorflow implementation of Stacked Hourglass Networks for Human Pose Estimation',
    'long_description': None,
    'author': 'wbenbihi',
    'author_email': 'waligoo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
