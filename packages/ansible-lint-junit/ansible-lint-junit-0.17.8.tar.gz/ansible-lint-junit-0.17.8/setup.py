#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import setuptools

version = {}
with open("src/ansible_lint_junit/version.py") as fp:
    exec(fp.read(), version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ansible-lint-junit',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    version=version['__version__'],
    description='ansible-lint to JUnit converter.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='wasil',
    author_email='piotr.m.boruc@gmail.com',
    url='https://github.com/wasilak/ansible-lint-junit',
    download_url='https://github.com/wasilak/ansible-lint-junit/archive/%s.tar.gz' % (
        version['__version__']),
    keywords=['ansible', 'junit'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ['ansible-lint-junit = ansible_lint_junit.main:main']
    },
    install_requires=[
        'ansible-lint>=5.0.7',
        'defusedxml>=0.7.1',
    ],
    setup_requires=[],
    python_requires=">=3.6",
)
