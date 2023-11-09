#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Meinolf Sellmann",
    author_email='info@insideopt.com',
    python_requires='>=3.8.18',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: MacOS :: MacOS X'
    ],
    description="InsideOpt Seeker Mac Distribution",
    install_requires=requirements,
    long_description=readme, #+ '\n\n' + history,
#    include_package_data=True,
    keywords='insideopt-seeker',
    name='insideopt-seeker',
    test_suite='tests',
#    tests_require=test_requirements,
#    url='https://github.com/audreyr/test_seeker',
    version='0.0.3',
    package_dir = {'': 'seeker'},
    packages=find_packages(include=['insideopt-seeker', 'insideopt-seeker.*']),
    package_data={'insideopt-seeker': ['seeker/*.so']},
    zip_safe=False,
)
