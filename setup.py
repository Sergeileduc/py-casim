#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

# requirements = ['Click>=7.0', 'bs4', 'requests']
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = ['pytest-runner', ]

# test_requirements = ['pytest>=3', 'pytest-datadir>=1.3.1']
with open('requirements_test.txt') as f:
    test_requirements = f.read().splitlines()


setup(
    author="Sergeileduc",
    author_email='sergei.leduc@gmail.com',
    url='https://github.com/Sergeileduc/py-casim',
    project_urls={
        "Documentation": "https://py-casim.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/Sergeileduc/py-casim/issues",
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Upload image",
    entry_points={
        'console_scripts': [
            'py-casim=py_casim.cli:app',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='python casim',
    name='py-casim',
    packages=find_packages(include=['py_casim', 'py_casim.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    version='1.0.0',
    zip_safe=False,
)
