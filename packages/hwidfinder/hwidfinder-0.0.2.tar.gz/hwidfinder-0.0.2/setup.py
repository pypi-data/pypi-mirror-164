from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Find your HWID easily.'

# Setting up
setup(
    name="hwidfinder",
    version=VERSION,
    author="Arxify (Daniel Rodriguez)",
    author_email="<arxifybusiness@proton.me>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['colorama'],
    keywords=['python', 'hwid', 'finder', 'find', 'windows', 'tool'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)