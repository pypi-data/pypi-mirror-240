#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Qunfei Wu",
    author_email='wu.qunfei@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    description="An apartment Search engine",
    entry_points={
        'console_scripts': [
            'immogpt=immogpt.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='immogpt',
    name='immogpt',
    packages=find_packages(include=['immogpt', 'immogpt.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wuqunfei/immogpt',
    version='0.1.0',
    zip_safe=False,
)
