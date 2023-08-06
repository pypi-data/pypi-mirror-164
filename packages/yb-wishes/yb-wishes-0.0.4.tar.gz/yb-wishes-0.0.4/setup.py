# -*- coding: utf-8 -*-
# @Time     : 2022/8/26 13:19
# @author   : yone
# @FileName : setup.py

import setuptools

setuptools.setup(
    name="yb-wishes",
    version="0.0.4",
    author="yone",
    author_email="1242925780@qq.com",
    description="wishes",
    packages=setuptools.find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    py_modules=['yb-wishes']
)