#!/usr/bin/env python

from distutils.core import setup
import json

with open('fifimon/version.json') as fp:
    _info = json.load(fp)

config = {
    'name': 'fifimon',
    'version': _info['version'],
    'description': 'FIFI-LS Monitor',
    'long_description': 'Program to monitor FIFI-LS data',
    'author': 'Dario Fadda',
    'author_email': 'darioflute@gmail.com',
    'url': 'https://github.com/darioflute/fifimon.git',
    'download_url': 'https://github.com/darioflute/fifimon',
    'license': 'GPLv3+',
    'packages': ['fifimon'],
    'scripts': ['bin/fifimon'],
    'include_package_data':True,
    'package_data':{'obsmaker':['version.json','icons/*.png','copyright.txt','data/CalibrationResults.csv']},
    'install_requires': ['numpy', 'matplotlib', 'astropy'],
    'classifiers':[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPLv3+ License",
            "Operating System :: OS Independent",
            "Intended Audience :: Science/Research", 
            "Development Status :: 4 - Beta",
            "Topic :: Scientific/Engineering :: Visualization",
            ]
}

setup(**config)