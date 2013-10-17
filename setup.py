# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages
import time


_version = "0.1.dev%s" % int(time.time())
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "Utilities and helpers for writing Pylint plugins"


setup(
    name='pylint-plugin-utils',
    url='https://github.com/landscapeio/pylint-plugin-utils',
    author='landscape.io',
    author_email='code@landscape.io',
    description=_short_description,
    version=_version,
    install_requires=['pylint', 'astroid'],
    packages=_packages,
    license='GPLv2',
    keywords=('pylint', 'plugin', 'helpers')
)
