# pylint-plugin-utils

## Status

[![Build Status](https://github.com/PyCQA/pylint/actions/workflows/ci.yaml/badge.svg?branch=master)](https://github.com/PyCQA/pylint/actions)
[![Coverage Status](https://coveralls.io/repos/github/PyCQA/pylint-plugin-utils/badge.svg?branch=master)](https://coveralls.io/github/PyCQA/pylint-plugin-utils?branch=master)

# About

Utilities and helpers for writing Pylint plugins. This is not a direct Pylint plugin, but rather a set of tools and functions used by other plugins such as [pylint-django](https://github.com/PyCQA/pylint-django) and [pylint-celery](https://github.com/PyCQA/pylint-celery).

# Testing
Create virtualenv:
```bash
python3.8  -m venv .pylint-plugin-utils
source .pylint-plugin-utils/bin/activate
pip install --upgrade pip setuptools
```

We use [tox](https://tox.readthedocs.io/en/latest/) for running the test suite. You should be able to install it with:
```bash
pip install tox pytest
```

To run the test suite for a particular Python version, you can do:
```bash
tox -e py38
```

To run individual tests with ``tox``, you can do::
```bash
tox -e py38 -- -k test_linter_should_be_pickleable
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
