##############################################################################
#
# Copyright (c) 2017 Jonathan Vanasco and Contributors
# Portions Copyright (c) 2008-2013 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################
import os

from setuptools import setup
from setuptools import find_packages

# store version in the init.py
import re

with open(
    os.path.join(os.path.dirname(__file__), "pyramid_csrf_multi_scheme", "__init__.py")
) as v_file:
    VERSION = re.compile(r'.*__VERSION__ = "(.*?)"', re.S).match(v_file.read()).group(1)


requires = [
    "pyramid>=1.10.4",
]
tests_require = [
    "pytest",
    "pyramid_debugtoolbar>=4.0.0",
]
testing_extras = tests_require + []

setup(
    name="pyramid_csrf_multi_scheme",
    version=VERSION,
    description="provides for creating independent csrf tokens for the http and https schemes",
    long_description="""This package enables two separate cookie tokens on each request, bound to the scheme:

* a secure HTTPS-only cookie
* a mixed-use INSECURE http token
""",
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: Repoze Public License",
    ],
    keywords="web pyramid csrf",
    packages=[
        "pyramid_csrf_multi_scheme",
    ],
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    url="https://github.com/jvanasco/pyramid_csrf_multi_scheme",
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    include_package_data=True,
    zip_safe=False,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
    test_suite="tests",
)
