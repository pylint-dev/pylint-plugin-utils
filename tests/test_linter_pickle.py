import pickle

from pylint.checkers.typecheck import TypeChecker

from pylint_plugin_utils import augment_visit, suppress_message


def fake_augmentation_func(*args, **kwargs):
    ...


def fake_suppress_func(*args, **kwargs):
    ...


def test_linter_should_be_pickleable(linter):
    # Setup
    linter.register_checker(TypeChecker())
    augment_visit(linter, TypeChecker.visit_attribute, fake_augmentation_func)
    suppress_message(
        linter, TypeChecker.visit_attribute, "no-member", fake_suppress_func
    )

    # Act and Assert
    pickle.dumps(linter)
