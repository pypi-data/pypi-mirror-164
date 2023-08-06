# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     setup
   Description :   
   Author :       lth
   date：          2022/8/26
-------------------------------------------------
   Change Activity:
                   2022/8/26 3:11: create this script
-------------------------------------------------
"""
__author__ = 'lth'

import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lth_develop_tools",
    version="0.0.0", # first 0 means test
    author="lth",
    author_email="673567903@qq.com",
    description="this package is used for author only",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "lth_tools"},
    packages=setuptools.find_packages(where="lth_tools"),
    python_requires=">=3.6",

)
