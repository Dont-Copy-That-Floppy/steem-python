#!/usr/bin/env python3
from setuptools import setup, find_packages

import sys
if sys.version_info < (3,0):
    sys.exit(
        'Sorry, python2 is not yet supported. ' +
            'Please use python3.'
    )

setup(
    name='steem',
    version='0.18.103',
    description='Official Python Steem Library',
    # long_description = file: README.rst
    keywords=['steem', 'steemit', 'cryptocurrency', 'blockchain'],
    license='MIT',
    url='https://github.com/steemit/steem-python',
    maintainer='steemit_inc',
    maintainer_email='john@steemit.com',
    packages=find_packages(),
    install_requires = [
        'appdirs',
        'certifi',
        'ecdsa',
        'funcy',
        'langdetect',
        'prettytable',
        'pycrypto',
        'scrypt',
        'toolz',
        'urllib3',
        'voluptuous',
        'w3lib',
    ],
    entry_points={
        'console_scripts': ['steempy=steem.cli:legacy'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta']
)
