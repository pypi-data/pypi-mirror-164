# -*- coding: utf-8 -*-
# @Time     : 2022/8/26 13:19
# @author   : yone
# @FileName : setup.py

import setuptools

setuptools.setup(
    name="yb-wishes",
    version="0.0.2",
    author="yone",
    author_email="931932073@qq.com",
    description="A small example package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)