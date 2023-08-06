import setuptools
from setuptools import *

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ccdot',
    version='0.1',
    author='n-p3k',
    author_email='nora-p3k@gmail.com',
    description='Utility to manage a block of env variables for multiple dev projects',
    url='https://github.com/n-p3k/ccdot',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False)