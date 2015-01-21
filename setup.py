# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import peanuts
version = peanuts.__version__

setup(
    name='Peanuts',
    version=version,
    author='',
    author_email='ssbrewster@gmail.com',
    packages=[
        'peanuts',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['peanuts/manage.py'],
)
