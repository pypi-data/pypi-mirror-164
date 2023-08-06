# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datapipes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'datapipes',
    'version': '0.0.2',
    'description': 'DataPipes for open data',
    'long_description': '# DataPipes\n\nDataPipes for open data\n\n\n\n## Installation\n\n```bash\npip install datapipes\n```\n\n\n\n## Quick Start\n\n```python\nimport datapipes\n```\n\n\n\n## Contributing\n\n\n\n## License\n\nDataPipes has an BSD-3-Clause license, as found in the [LICENSE](https://github.com/opencovid19data/opendata/blob/main/LICENSE) file.\n',
    'author': 'OpenCOVID-19',
    'author_email': 'contact.opencovid19@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/opencovid19data/opendata/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
