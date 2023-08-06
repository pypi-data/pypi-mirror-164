#!/usr/bin/env python3
from setuptools import setup, find_packages
import os


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name="purpleair_data_logger",
    version="0.0.7a1",
    license="MIT",
    author="Carlos Santos",
    author_email="27721404+carlkid1499@users.noreply.github.com",
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    packages=['purpleair_data_logger'],
    url="https://github.com/carlkid1499/purpleair_data_logger",
    keywords=["purpleair_data_logger", "purpleair", "data logger"],
    install_requires=[
        "pg8000",
        "requests"
    ],
)
