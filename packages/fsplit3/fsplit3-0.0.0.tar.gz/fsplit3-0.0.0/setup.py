#!/usr/bin/env python2

##
# fsplit
# https://github.com/leosartaj/fsplit.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from fsplit import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = 'fsplit3',
    version = __version__,
    author = 'shantanu kumar',
    author_email = 'shantanu020198@gmail.com',
    description = ('Split files into small portable chunks'),
    long_description = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    license = 'MIT',
    keywords = 'files chunk split parts portable join tar',
    url = 'https://github.com/shantanuk98/fsplit2',
    packages=find_packages(),
    scripts=['bin/fsplit', 'bin/fjoin'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Natural Language :: English',
    ],
)

