# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrepository']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyrepository',
    'version': '0.0.1',
    'description': 'PyRepository',
    'long_description': '# PyRepository\n\n\n\n## Installation\n\n```bash\npip install pyrepository\n```\n\n\n\n## Quick Start\n\n```python\nimport pyrepository\n```\n\n\n\n## Contributing\n\n\n\n## License\n\nPyRepository has an BSD-3-Clause license, as found in the [LICENSE](https://github.com/imyizhang/pyrepository/blob/main/LICENSE) file.',
    'author': 'Yi Zhang',
    'author_email': 'yizhang.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/imyizhang/pyrepository/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
