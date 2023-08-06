# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['filterbox', 'filterbox.concurrent', 'filterbox.frozen', 'filterbox.mutable']

package_data = \
{'': ['*']}

install_requires = \
['cykhash>=2.0.0,<3.0.0',
 'numpy>=1.14,<2.0',
 'readerwriterlock>=1.0.9,<2.0.0',
 'sortednp>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'filterbox',
    'version': '1.0.0',
    'description': 'Container for finding Python objects using database-like indexes.',
    'long_description': "[![tests Actions Status](https://github.com/manimino/filterbox/workflows/tests/badge.svg)](https://github.com/manimino/filterbox/actions)\n[![Coverage - 100%](https://img.shields.io/static/v1?label=Coverage&message=100%&color=2ea44f)](test/cov.txt)\n[![license - MIT](https://img.shields.io/static/v1?label=license&message=MIT&color=2ea44f)](/LICENSE)\n![python - 3.7+](https://img.shields.io/static/v1?label=python&message=3.7%2B&color=2ea44f)\n\n# FilterBox\n\nContainer that stores objects in database-like indexes for fast lookup.\n\n#### Install: \n\n```\npip install filterbox\n```\n\n#### Usage:\n```\nfrom filterbox import FilterBox\n\nobjects = [{'x': 4, 'y': 1}, {'x': 6, 'y': 2}, {'x': 8, 'y': 5}]\n\n# create a FilterBox containing objects, indexed on x and y\nfb = FilterBox(objects, ['x', 'y'])  \n\n# find the ones you want\nfb[{\n    'x': {'>': 5, '<': 10},     # find objects where x is between 5 and 10\n    'y': {'in': [1, 2, 3]}      # and y is 1, 2, or 3\n}]\n# result: [{'x': 6, 'y': 2}]\n```\n\nValid operators are ==, !=, <, <=, >, >=, in, not in. \n\n#### Is FilterBox a database?\n\nNo. But like a database, FilterBox builds B-tree indexes and uses them to find results very quickly. It does\nnot any do other database things like SQL, tables, etc. This keeps FilterBox simple, light, and performant.\n\n#### Is FilterBox fast?\n\nYes. Here's how FilterBox compares to other object-finders on an example task.\n\n![Example benchmark](docs/perf_bench.png)\n\n[Benchmark code](examples/perf_demo.ipynb)\n\nThe closest thing to a FilterBox is an in-memory SQLite. While SQLite is a fantastic database, it requires\nmore overhead. As such, FilterBox is generally faster.\n\n### Class APIs\n\nThere are three containers.\n - [FilterBox](https://filterbox.readthedocs.io/en/latest/filterbox.mutable.html#filterbox.mutable.main.FilterBox): \nCan `add`, `remove`, and `update` objects after creation.\n - [ConcurrentFilterBox](https://filterbox.readthedocs.io/en/latest/filterbox.concurrent.html#filterbox.concurrent.main.ConcurrentFilterBox): \nSame as FilterBox, but thread-safe.\n - [FrozenFilterBox](https://filterbox.readthedocs.io/en/latest/filterbox.frozen.html#filterbox.frozen.main.FrozenFilterBox):\nCannot be changed after creation, it's read-only. But it's super fast, and of course thread-safe.\n\nAll three can be pickled using the special functions `filterbox.save()` / `filterbox.load()`. \n\n### Part 2\n\n[Readme Part 2](/README_part_2.md) has lots more examples, including handling of nested data and missing attributes.\n",
    'author': 'Theo Walker',
    'author_email': 'theo.ca.walker@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/manimino/filterbox/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
