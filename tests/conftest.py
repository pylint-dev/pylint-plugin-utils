# pylint: disable=redefined-outer-name
import os
from pathlib import Path

import pytest

from pylint import checkers
from pylint.lint import PyLinter
from pylint.testutils import MinimalTestReporter


@pytest.fixture()
def tests_directory():
    return Path(__file__).parent


@pytest.fixture
def linter():
    _linter = PyLinter()
    return _linter

