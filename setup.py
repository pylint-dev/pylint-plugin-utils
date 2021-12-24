# -*- coding: UTF-8 -*-
from setuptools import find_packages, setup

_version = "0.6"
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "Utilities and helpers for writing Pylint plugins"

_classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
]

setup(
    name='pylint-plugin-utils',
    url='https://github.com/PyCQA/pylint-plugin-utils',
    author='Python Code Quality Authority',
    author_email='code-quality@python.org',
    description=_short_description,
    version=_version,
    install_requires=['pylint>=1.7', 'pytest'],
    packages=_packages,
    license='GPLv2',
    classifiers=_classifiers,
    keywords='pylint plugin helpers',
    python_requires='>=3.6.2',
)
