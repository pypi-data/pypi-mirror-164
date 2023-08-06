# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['joblibgcs']

package_data = \
{'': ['*']}

install_requires = \
['gcsfs>=2022.7.1,<2023.0.0', 'joblib>=1.1.0,<2.0.0']

extras_require = \
{'book': ['ipykernel>=6.15.1,<7.0.0']}

setup_kwargs = {
    'name': 'joblibgcs',
    'version': '0.2.0',
    'description': 'a google cloud storage memory backend for joblib',
    'long_description': '# joblibgcs\n\nA google cloud storage memory backend for joblib\n\n- inspired by and closely following [joblib-s3](https://github.com/aabadie/joblib-s3)\n\n- relies heavily on [gcsfs](https://github.com/fsspec/gcsfs)\n\n```py\nimport numpy as np\nfrom joblib import Memory, register_store_backend\nfrom joblibgcs.gcs_backend import GCSFSStoreBackend\n\nregister_store_backend("gcs", GCSFSStoreBackend)\n\nmem = Memory(\n    "cache-location",\n    backend="gcs",\n    verbose=100,\n    backend_options={"project": "project-name"},\n)\n\nmultiply = mem.cache(np.multiply)\narray1 = np.arange(10000)\narray2 = np.arange(10000)\n\nresult = multiply(array1, array2)\nprint(result)\n\nresult2 = multiply(array1, array2)\nprint(result2)\n```',
    'author': 'Gautam Sisodia',
    'author_email': 'gautam.sisodia@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/gautas/joblibgcs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
