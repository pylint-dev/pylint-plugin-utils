import pickle

import pylint
from pylint.checkers.typecheck import TypeChecker

from pylint_plugin_utils import augment_visit, suppress_message


def fake_augmentation_func(*args, **kwargs):
    ...


def fake_suppress_func(*args, **kwargs):
    ...


def test_linter_should_be_pickleable(linter):
    # after pylint>=2.13, dill is used in pylint -
    # see discussion https://github.com/PyCQA/pylint-plugin-utils/issues/26
    # therefore we can ignore that test, as the previous reasons for this
    # test no longer exist
    # (reason was https://github.com/PyCQA/pylint-plugin-utils/issues/20)
    if pylint.__version__ >= "2.13":
        return

    # Setup
    linter.register_checker(TypeChecker(linter))
    augment_visit(linter, TypeChecker.visit_attribute, fake_augmentation_func)
    suppress_message(linter, TypeChecker.visit_attribute, "no-member", fake_suppress_func)

    # Act and Assert
    pickle.dumps(linter)
