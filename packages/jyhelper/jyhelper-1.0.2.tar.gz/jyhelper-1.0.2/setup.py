#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2023/11/08 18:38 
# @Author : JY

from setuptools import setup

setup(
    name='jyhelper',
    version='1.0.2',
    description='各种实用、常用的小函数、类',
    author='JY',
    author_email='your-email@example.com',
    packages=['jyhelper'],
    install_requires=[
        'pymysql',
    ],
)