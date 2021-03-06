#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='telephus',
    version='1.0.0~beta1',
    description=('connection pooled, low-level client API for Cassandra in '
                 'Twisted (Python)'),
    author='brandon@faltering.com',
    url='http://github.com/driftx/Telephus',
    packages=['telephus',
              'telephus.cassandra']
)
