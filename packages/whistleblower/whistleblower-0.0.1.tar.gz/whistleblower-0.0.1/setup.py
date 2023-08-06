#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/8/26 14:05
# file: setup.py
# author: Yusheng Wang
# email: yasenwang@bupt.edu.cn
from setuptools import setup, find_packages


setup(
    name="whistleblower",
    version="0.0.1",
    description="This project is used to alarm emergency information to your mobile phone on webhook service",
    long_description="This project is used to alarm emergency information to your mobile phone on webhook service",
    author="Y.S. Wang",
    author_email="yasen@yasenstudio.com",
    url="",
    license="MIT Licence",
    packages=find_packages(),
    install_requires=['requests',
                      ],
)
