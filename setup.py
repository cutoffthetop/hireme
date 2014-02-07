# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='hireme',
    version='0.1',
    author='Nicolas Drebenstedt',
    author_email='drebenstedt@me.com',
    license='BSD',
    platforms='any',
    test_suite='hireme.tests',
    zip_safe=False,
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
    'setuptools',
    'flask'
    ],
    entry_points="""
    [console_scripts]
    hireme = hireme.server:run_local
    """
)