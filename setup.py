#!./venv/bin/python3
'''
Created on 20220926
Update on 20220926
@author: Eduardo Pagotto
'''

from setuptools import setup, find_packages

from SimplestRpcApi.__init__ import __version__ as VERSION

PACKAGE = "SimplestRpcApi"

# listar os packages
#python -c "from setuptools import setup, find_packages; print(find_packages())"

setup(
    name="SimplestRpcApi",
    version=VERSION,
    author="Eduardo Pagotto",
    author_email="edupagotto@gmail.com",
    description="RPC Classes",
    long_description="Classes to build simplest RPC's",#long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EduardoPagotto/SimplestRpcApi.git",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['setuptools',
                      'typing_extensions',
                      'wheel'])
