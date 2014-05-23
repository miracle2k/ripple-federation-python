#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
    name="ripple-federation",
    description="Map email to Ripple addresses using the Federation protocol",
    author='Michael Elsdörfer',
    author_email='michael@elsdoerfer.com',
    version="1.1.3",
    url="https://github.com/miracle2k/ripple-federation-python",
    license='BSD',
    py_modules=['ripple_federation'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
    ]
)
