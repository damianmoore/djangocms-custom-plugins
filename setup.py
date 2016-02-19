#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='djangocms-custom-plugins',
    version='0.0.1',
    description="""Custom Django CMS plugins""",
    author='Damian Moore',
    url='https://github.com/damianmoore/djangocms-custom-plugins',
    packages=[
        'custom_plugins', 'custom_plugins.migrations'
    ],
    package_data={'custom_plugins': ['templates/*']},
    include_package_data=True
)
