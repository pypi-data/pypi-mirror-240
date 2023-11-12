#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))

try:
    long = open("mcae\\README.md",encoding = "utf-8").read()
except:
    long = ""

setup(
    name='mcae',
    version='0.1.0',
    description='一个用于制作Minecraft原版指令动画的工具',
    author='luoyily',
    url='https://github.com/luoyily/mcae',
    packages=find_packages(),
    install_requires=['aiofiles>=23.2.1', "urllib3>=2.0.4"],
    keywords='a Minecraft command animation tool',
    long_description=long,
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)