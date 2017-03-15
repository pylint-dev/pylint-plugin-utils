# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages

_version = "0.2.6"
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "Utilities and helpers for writing Pylint plugins"

_classifiers = (
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
)

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
    classifiers=_classifiers,
    keywords='pylint plugin helpers'
)
