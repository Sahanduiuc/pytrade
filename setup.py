#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyTrade: Pythonic Trading Framework
# https://pytrade.io
#
# Copyright 2019-2020 Ran Aroussi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup, find_packages
from codecs import open
from os import path
import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytrade',
    url="http://pytrade.io",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Pythonic Trading Framework',
    author='Ran Aroussi.',
    author_email='ran@aroussi.com',
    license='Apache 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',

        'Natural Language :: English',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',

        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    platforms=['any'],
    keywords='qtpylib algotrading algo trading quant backtest backtester',
    packages=find_packages(exclude=[
        'contrib', 'docs', 'tests', 'demo', 'demos', 'examples']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pytrade=pytrade:main',
        ],
    },
    # include_package_data=True,
    # package_data={},
)
