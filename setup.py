# -*- coding: utf-8 -*-
import sys
import os

from setuptools import setup, find_packages


def read(relative):
    contents = open(relative, 'r').read()
    return [l for l in contents.split('\n') if l != '']


setup(
    name='pylognorm',
    version='0.3.0',
    description='liblognorm python bindings',
    url='http://github.com/zinic/pylognorm',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Logging',
        'Programming Language :: Python',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3'
    ],
    author='John Hopper',
    author_email='john.hopper@jpserver.net',
    license='Apache 2.0',
    tests_require=read('./tools/test-requires'),
    install_requires=read('./tools/pip-requires'),
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup', '*.tests']),
    ext_modules=ext_modules
)

