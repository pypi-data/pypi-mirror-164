# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spadepp',
 'spadepp.data_source',
 'spadepp.detection',
 'spadepp.detection.signal',
 'spadepp.evaluation',
 'spadepp.labeler',
 'spadepp.models',
 'spadepp.models.features',
 'spadepp.scripts',
 'spadepp.semi_supervised',
 'spadepp.semi_supervised.data_augmentation',
 'spadepp.utils']

package_data = \
{'': ['*']}

install_requires = \
['accelerate>=0.12.0,<0.13.0',
 'click>=8.0.4,<9.0.0',
 'datasets>=1.18.3,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'nltk>=3.7,<4.0',
 'numpy>=1.22.2,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pyspellchecker>=0.6.3,<0.7.0',
 'scikit-activeml>=0.2.5,<0.3.0',
 'scikit-learn>=1.1.2,<2.0.0',
 'sentence-transformers>=2.2.0,<3.0.0',
 'setuptools',
 'spacy>=3.2.2,<4.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'transformers>=4.16.2,<5.0.0',
 'xgboost>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'spadepp',
    'version': '0.1.3',
    'description': '',
    'long_description': 'None',
    'author': 'Minh Pham',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
