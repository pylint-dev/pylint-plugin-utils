import pytest
from pylint.lint import PyLinter


@pytest.fixture
def linter():
    _linter = PyLinter()
    return _linter
