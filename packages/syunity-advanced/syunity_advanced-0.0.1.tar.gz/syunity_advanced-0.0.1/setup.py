#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import netservice.DataBus

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="syunity_advanced",
    version="0.0.1",
    author="shenarder",
    author_email="shenarder@163.com",
    description="a template for syunity algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/zhec5hl01/python-games",
    py_modules=['pgzero_template'],
    install_requires=[],
    classifiers=[
        "Topic :: Games/Entertainment ",
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Board Games',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)

