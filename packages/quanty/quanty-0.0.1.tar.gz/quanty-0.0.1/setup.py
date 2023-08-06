#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    name = 'quanty',
    version = '0.0.1',
    author = 'jianjun',
    author_email = '910667956@qq.com',
    url = 'https://github.com/EVA-JianJun/quanty',
    description = u'Python 量化交易框架!',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = ["quanty"],
    install_requires = [
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    package_data={
    },
)