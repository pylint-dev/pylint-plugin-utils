# pylint: disable=redefined-outer-name
from pathlib import Path

import pytest
from pylint.lint import PyLinter


@pytest.fixture()
def tests_directory():
    return Path(__file__).parent


@pytest.fixture
def linter():
    _linter = PyLinter()
    return _linter
