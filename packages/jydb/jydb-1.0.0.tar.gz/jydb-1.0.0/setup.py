#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2023/11/08 18:38 
# @Author : JY

from setuptools import setup

setup(
    name='jydb',
    version='1.0.0',
    description='基于pymysql的便捷数据库查询',
    author='JY',
    author_email='your-email@example.com',
    packages=['db'],
    install_requires=[
        'pymysql',
    ],
)