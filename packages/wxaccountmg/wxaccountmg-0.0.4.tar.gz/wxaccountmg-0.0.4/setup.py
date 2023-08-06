# -*- coding:utf-8 -*-
# _author: Damion.zeng
# Email: Damion.zeng@akmmv.com
# date: 2022/8/25
# @desc:

from setuptools import setup,find_packages

with open("README.md",'r',encoding='utf-8') as fh:
    long_description =fh.read()

setup(
    name="wxaccountmg",
    version="0.0.4",
    license="MIT Licence",
    packages=find_packages(),
    install_requires=["zhdate>=0.1","xmltodict>=0.13.0","requests"]
)