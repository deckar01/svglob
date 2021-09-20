#!/usr/bin/env python

from distutils.core import setup
from svglob import glob


setup(
    name='svglob',
    version='1.0.0',
    description=glob.__doc__,
    author='Jared Deckard',
    author_email='jared@shademaps.com',
    url='https://github.com/deckar01/svglob',
    packages=['svglob'],
    requires=[
        'numpy==1.20.3',
        'svgwrite==1.4.1',
        'svgpathtools==1.4.1',
    ],
)
