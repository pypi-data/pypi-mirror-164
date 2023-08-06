# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['modified_xicor']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'modified-xicor',
    'version': '0.3.0',
    'description': 'New correlation function on the block!',
    'long_description': "# Xi Correlation by Chatterjee, modified\n\nIt detects non-linear correlations including parabolas and waves. The longer the series, the better the results.\n\nHere's the paper I used. https://arxiv.org/pdf/1909.10140.pdf\nHere's the github gist: https://gist.github.com/mandrewstuart/e1c584a36ca5394cc934542731b4d8c2\n\nI modified the unordered equation because the boundaries weren't working I expected. They are now 'unordered': 1 + (len(Y)*numerator)/(4*denominator)\n\n\nUsage:\n\n\n>> import modified_xicor as mx\n\n>> x = [1, 2, 3, 4, 5]\n\n>> y = [1, 3, 5, 7, 9]\n\n>> mx.xicor(x, y)\n\n{'ordered': float, 'unordered': float, 'len': int}\n",
    'author': 'Andrew Matte',
    'author_email': 'andrew.matte@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
