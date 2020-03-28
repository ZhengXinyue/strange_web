#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    description='Flaskr for learning flask',
    long_description='xxx',
    author='ZhengXinyue',
    author_email='zhengxinyue@nuaa.edu.cn',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ]
)