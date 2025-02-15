#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WARNING:
    Direct invocation of setup.py is deprecated.
    Please use "pip install ." or "python -m build" (with a proper pyproject.toml)
    to build and install this package.
"""

import io
import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

# Read the long description from the README file (if available)
try:
    with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Official python steem library."

setuptools.setup(
    name="steem",
    version="1.0.2",
    author="Steemit",
    author_email="john@steemit.com",
    description="Official python steem library.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/steemit/steem-python",
    packages=setuptools.find_packages(exclude=("tests", "scripts")),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.5",
    install_requires=[
        "appdirs",
        "certifi",
        "ecdsa>=0.13",
        "funcy",
        'futures; python_version < "3.0.0"',
        "future",
        "langdetect",
        "prettytable",
        "pycryptodome>=3.20.0",
        "pylibscrypt>=1.6.1",
        "scrypt>=0.8.0",
        "toolz",
        "ujson",
        "urllib3",
        "voluptuous",
        "w3lib",
    ],
    entry_points={
        "console_scripts": [
            "piston=steem.cli:legacyentry",
            "steempy=steem.cli:legacyentry",
            "steemtail=steem.cli:steemtailentry",
        ],
    },
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "autopep8",
            "yapf",
            "twine",
            "pypandoc",
            "recommonmark",
            "wheel",
            "setuptools",
            "sphinx",
            "sphinx_rtd_theme",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "autopep8",
            "yapf",
        ],
    },
)
