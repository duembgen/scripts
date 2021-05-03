#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
setup.py: 
"""
from setuptools import setup

setup(
    name='scripts',
    version='v0.0.6',
    description='useful system-wide scripts',
    url='http://github.com/duembgen/scripts',
    author='Frederike Duembgen',
    author_email='frederike.duembgen@gmail.com',
    license='CCBY',
    scripts=['remove_output'],
    packages=[],
    zip_safe=False,
    python_requires='>=3',
    install_requires=['nbformat']
)
