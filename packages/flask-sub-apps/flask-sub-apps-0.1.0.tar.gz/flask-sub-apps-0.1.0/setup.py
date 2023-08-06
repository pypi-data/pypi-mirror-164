# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="flask-sub-apps",
    version="0.1.0",
    description="Flask package for auto-loading sub-apps",
    license="MIT",
    author="Damian Ciftci",
    packages=find_packages(),
    install_requires=["flask", "flask-sqlalchemy", "click"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ],
)
