import os
import pickle
from typing import List

import pytest
from pylint.checkers.typecheck import TypeChecker
from pylint.lint import PyLinter
from pylint.testutils import FunctionalTestFile

from pylint_plugin_utils import augment_visit, suppress_message


def get_tests(input_dir: str) -> List[FunctionalTestFile]:
    cwd = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(cwd, input_dir)

    suite = []
    for file_name in os.listdir(input_dir):
        if file_name != '__init__.py' and file_name.endswith('.py'):
            suite.append(FunctionalTestFile(input_dir, file_name))

    return suite


TESTS = get_tests(input_dir='input')
TESTS_NAMES = [t.base for t in TESTS]


def fake_augmentation_func(*args, **kwargs):
    ...


def fake_suppress_func(*args, **kwargs):
    ...


@pytest.mark.parametrize("test_file", TESTS, ids=TESTS_NAMES)
def test_augment_visit_is_pickleable_for_multithreading_as_default_for_py38_or_above(test_file):
    pylinter = PyLinter()
    pylinter.register_checker(TypeChecker())
    augment_visit(pylinter, TypeChecker.visit_attribute, fake_augmentation_func)
    suppress_message(pylinter, TypeChecker.visit_attribute, 'no-member', fake_suppress_func)

    pickle.dumps(pylinter)
