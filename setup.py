# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='hireme',
    version='0.1',
    author='Nicolas Drebenstedt',
    license='BSD',
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
    'setuptools',
    'flask',
    'numpy',
    'nose'
    ],
    entry_points="""
    [console_scripts]
    hireme = hireme.server:run_local
    tests = hireme.testsuite:main
    """
)