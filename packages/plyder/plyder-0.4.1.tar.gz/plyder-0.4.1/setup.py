# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plyder',
 'plyder.download_providers',
 'plyder.routes',
 'plyder.static',
 'plyder.templates']

package_data = \
{'': ['*'], 'plyder.download_providers': ['experimental/*']}

install_requires = \
['Jinja2>=2.11.3,<4.0.0',
 'PyYAML>=5.4.1,<7.0.0',
 'aiofiles>=0.6,<23.2',
 'appdirs>=1.4.4,<2.0.0',
 'fastapi>=0.104.0,<0.105.0',
 'humanize>=3.3,<5.0',
 'jsonschema>=3.2,<5.0',
 'loguru>=0.5.3,<0.7.0',
 'mega.py>=1.0.8,<2.0.0',
 'psutil>=5.8.0,<6.0.0',
 'pydantic>=2,<3',
 'sh>=1.14.1,<3.0.0',
 'uvicorn>=0.13.4,<0.22.0']

entry_points = \
{'console_scripts': ['plyder = plyder:main']}

setup_kwargs = {
    'name': 'plyder',
    'version': '0.4.1',
    'description': 'Download manager with web-interface.',
    'long_description': '# plyder\n\n[![PyPI](https://img.shields.io/pypi/v/plyder.svg?style=flat)](https://pypi.python.org/pypi/plyder)\n[![Tests](https://github.com/kpj/plyder/workflows/Tests/badge.svg)](https://github.com/kpj/plyder/actions)\n\nDownload manager with web-interface.\n\n<img src="gallery/web-interface.png" width="100%">\n\n\n## Installation\n\n```python\n$ pip install plyder\n```\n\n\n## Usage\n\n```bash\n$ plyder\n```\n\n`plyder` works out of the box. Though you might want to adapt the configuration to your taste.\n\n### Custom download scripts\n\nCustom download scripts can be specified in the configuration file:\n\n```yaml\ndownload_handlers:\n    - ./github_downloader.sh\n```\n\n`./github_downloader.sh` needs to be an executable script of the following form:\n\n```bash\n#!/usr/bin/env bash\n# PLYDER_HOST: <host to match>\n\nurl="$1"\noutput_dir="$2"\n\n<custom logic>\n```\n\nSee `plyder/download_providers/` for built-in examples.\n\n### Prometheus integration\n\n`plyder` exposes the `/metric` resource which allows monitoring download counts and system usage using [Prometheus](https://prometheus.io/) and, e.g., [Grafana](https://grafana.com/).',
    'author': 'kpj',
    'author_email': 'kim.philipp.jablonski@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kpj/plyder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
