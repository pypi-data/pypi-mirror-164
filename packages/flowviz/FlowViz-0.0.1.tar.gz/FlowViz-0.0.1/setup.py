# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flowviz']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'flowviz',
    'version': '0.0.1',
    'description': 'Visualization for flow cytometry data.',
    'long_description': '# FlowViz\n\nVisualization for flow cytometry data.\n\n\n\n## Installation\n\n```bash\npip install flowviz\n```\n\n\n\n## Quick Start\n\n```python\nimport flowviz\n```\n\n\n\n## Contributing\n\n\n\n## License\n\nFlowViz has an BSD-3-Clause license, as found in the [LICENSE](https://github.com/imyizhang/flowviz/blob/main/LICENSE) file.',
    'author': 'Yi Zhang',
    'author_email': 'yizhang.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/imyizhang/flowviz/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
