# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['processpy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'processpy',
    'version': '0.1.0',
    'description': 'Python Process or Thread Manager',
    'long_description': '# Python Process Manager (processpy)\n\n\nprocesspy is simple process manager for python.\nIf you want to run multiple process for the same function, this tool is for you.\n\n* You can run multiple process of the same function concurrently.\n* You can choose to kill previous running process before running a new process of the same function.\n* You can choose to ignore new process of the same function if it\'s already running.\n\n\n## Installation\n\n```bash\npip install processpy\n```\n\n## Example (No concurrency and no previous kill)\n\n```python\nfrom processpy import ProcessManager\nimport time\n\ndef sum(a, b):\n    time.sleep(30)\n    print(a+b)\n\nsum_process = ProcessManager(sum, kill_previous=False, concurrent_running=False)\nsum_process.run({\'a\': 10, \'b\': 20})\ntime.sleep(5)\n\n"""\nThe following will not run. Because concurrent run is false and kill previous is also false. So, it will simply return with doing nothing and let the previous run.\n"""\nsum_process.run({\'a\': 10, \'b\': 20}) \n\n```\n\n## Example (No concurrency but with previous kill)\n```python\nfrom processpy import ProcessManager\nimport time\n\ndef sum(a, b):\n    time.sleep(30)\n    print(a+b)\n\nsum_process = ProcessManager(sum, kill_previous=True, concurrent_running=False)\nsum_process.run({\'a\': 10, \'b\': 20})\ntime.sleep(5)\n\n"""\nThe following will kill the previous unfinished process and run. Because concurrent run is false and kill previous is True. So, it will simply kill the previous unfinished process. If previous one is already finished, nothing to kill. \n"""\nsum_process.run({\'a\': 10, \'b\': 20}) \n```\n\n## Example (with concurrency)\n```python\nfrom processpy import ProcessManager\nimport time\n\ndef sum(a, b):\n    time.sleep(30)\n    print(a+b)\n\nsum_process = ProcessManager(sum, concurrent_running=True)\nsum_process.run({\'a\': 10, \'b\': 20})\ntime.sleep(5)\n\n"""\nThe following will run alongside of the previous process. \n"""\nsum_process.run({\'a\': 10, \'b\': 20}) \n```\n\n## You can also kill the running process (if concurrent_running=False )\n```python\nsub_process.kill()\n```',
    'author': 'Nazmul Hasan',
    'author_email': 'edufornazmul@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nazmulnnb/processpy',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
