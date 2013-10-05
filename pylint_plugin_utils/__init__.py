

class NoSuchChecker(Exception):

    def __init__(self, checker_class):
        self.message = "Checker class %s was not found" % checker_class

    def __repr__(self):
        return self.message


def get_checker(linter, checker_class):
    for checker in linter.get_checkers():
        if isinstance(checker, checker_class):
            return checker
    raise NoSuchChecker(checker_class)


def augment_visit(linter, checker_method, augmentation):
    checker = get_checker(linter, checker_method.im_class)

    old_method = getattr(checker, checker_method.__name__)

    def augment_func(node):
        def chain():
            old_method(node)
        augmentation(chain, node)

    setattr(checker, checker_method.__name__, augment_func)