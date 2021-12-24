# pylint-plugin-utils

## Status

[![Build Status](https://travis-ci.org/PyCQA/pylint-plugin-utils.svg?branch=master)](https://travis-ci.org/PyCQA/pylint-plugin-utils)
[![Code Health](https://landscape.io/github/PyCQA/pylint-plugin-utils/master/landscape.svg?style=flat)](https://landscape.io/github/PyCQA/pylint-plugin-utils/master)
[![Coverage Status](https://coveralls.io/repos/github/PyCQA/pylint-plugin-utils/badge.svg?branch=master)](https://coveralls.io/github/PyCQA/pylint-plugin-utils?branch=master)

# About

Utilities and helpers for writing Pylint plugins. This is not a direct Pylint plugin, but rather a set of tools and functions used by other plugins such as [pylint-django](https://github.com/PyCQA/pylint-django) and [pylint-celery](https://github.com/PyCQA/pylint-celery).

# Testing
We use [tox](https://tox.readthedocs.io/en/latest/) and [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/index.html) for running the test suite. You should be able to install it with:
```bash
pip install tox pytest pytest-benchmark
```

To run the test suite for a particular Python version, you can do:
```bash
tox -e py37
```

To run individual tests with ``tox``, you can do::
```bash
tox -e py37 -- -k name_of_the_test
```

We use pytest_ for testing ``pylint``, which you can use without using ``tox`` for a faster development cycle.

If you want to run tests on a specific portion of the code with [pytest](https://docs.pytest.org/en/latest/), [pytest-cov](https://pypi.org/project/pytest-cov/) and your local python version::
```bash
pip install pytest-cov
# Everything:
python3 -m pytest tests/ --cov=pylint_plugin_utils
coverage html
```



# License

`pylint-plugin-utils` is available under the GPLv2 License.
