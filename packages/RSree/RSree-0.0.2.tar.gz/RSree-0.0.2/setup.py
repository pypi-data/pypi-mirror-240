from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'It is basic library that contains some functions related to ML and some Functions that are very useful in codes'

# Setting up
setup(
    name="RSree",
    version=VERSION,
    author="Rahul Sree Manitha",
    author_email="<m.rahulsree1122@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'ml', 'RunOne', 'RunOneTimeinLoop'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)   