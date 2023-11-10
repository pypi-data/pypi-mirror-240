#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension

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
    keywords='insideopt-seeker, seeker, optimization',
    name='insideopt-seeker',
    test_suite='tests',
#    tests_require=test_requirements,
#    url='https://github.com/audreyr/test_seeker',
    version='0.0.6',
#    package_dir={'': '.'},
#    packages=find_packages(include=['seeker', 'seeker.*']),
#    package_data={'seeker': ['*.so', 'seeker.py']},


#    py_modules=["seeker"],
#    package_dir = {'': 'seeker'},
    packages=find_packages(include=['seeker', 'seeker.*', '*.so']),
#    ext_modules=[Extension('seeker', sources=['*.so'], language='c++')],
    package_data={'seeker': ['*.so', 'seeker.py']},
#    packages=find_packages(),
#    package_data={
#        'seeker': ['*.so'],
#    },
    zip_safe=False,
)
