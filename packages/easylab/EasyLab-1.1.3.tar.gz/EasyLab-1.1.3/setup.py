# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easylab']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'easylab',
    'version': '1.1.3',
    'description': 'Offers simple solutions for challenges that can be encountered in the psychology labs.',
    'long_description': '# EasyLab\n\nOffers simple solutions with GUI. From a folder, it can resize images, change their extensions, applies spatial frequencies, and more.\n\n# Purpose of the project\n+ The purpose of the project is to offer a simple solution to solve some of the problems that arise when working with big image datasets. \n+ The project is a work in progress, and it is not finished yet. Since it offers GUI, it is very practical to use it.\n\n# Features\n+ Resize images\n+ Change extension\n+ Apply spatial frequencies\n+ Apply Gaussian blur\n+ Apply gray scale\n+ Rename images\n\n# installation\n+ Install easylab with pip:\n```pip install easylab  ```\n\n# Usage\nit is very simple to use the project.\nFor the open GUI, use the following command:\n```from EasyLab import EasyLab```\nthen open the gui with:\n```EasyLab.easylab()```\n    \n\nIt\'s easy, just select your folder where your images are stored and select extension and size. "Rename" button will change all images\' names like this: "0image", "1image","2image"... and so on...  \nI use this command to standardize the picture names while doing deep learning.\n\n### **Read before the usage!**\nFor unforeseen consequences be sure to copy the original images elsewhere.\n\n## Javascript\nI will also add some javascript to online version.\n# E-prime scripts\nget the trail list (Image names for the E-Prime) or create a jitter:\nhttps://altunenes.github.io/EasyLab/filenames\n\n## Contributing\nContributions are welcome!\n\n##Author\n+   Enes Altun [Main Author](https://altunenes.github.io)',
    'author': 'altunenes',
    'author_email': 'enesaltun2@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/altunenes/EasyLab',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
