#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
AUTHOR_RE = re.compile(r'__author__\s*=\s*["\'](.+?)["\']')
PACKAGE_RE = re.compile(r'__package__\s*=\s*["\'](.+?)["\']')


def get_version():
    init = open(os.path.join(ROOT, 'boto3_handlers', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)

def get_author():
    init = open(os.path.join(ROOT, 'boto3_handlers', '__init__.py')).read()
    return AUTHOR_RE.search(init).group(1)

def get_package():
    init = open(os.path.join(ROOT, 'boto3_handlers', '__init__.py')).read()
    return PACKAGE_RE.search(init).group(1)

setup(
    name=get_package(),
    version=get_version(),
    description='Python Boto3 Dynamo DB Handler',
    long_description=open('README.md').read(),
    url='https://github.com/alexsmithx6-0z1nm/boto3_handlers',
    author=get_author(),
    author_email='alexsmithx6@0z1nm.onmicrosoft.com',
    license='MIT',
    packages=[get_package()],
    install_requires=['boto3'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
    
    project_urls={
        'Documentation': 'https://boto3.amazonaws.com/v1/documentation/api/latest/index.html',
        'Source': 'https://github.com/alexsmithx6-0z1nm/boto3_handlers',
    },
)