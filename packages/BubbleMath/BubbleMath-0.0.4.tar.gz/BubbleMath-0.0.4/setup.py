from setuptools import setup, find_packages
import codecs
import os

# If we get stuck, check out this tutorial: https://www.youtube.com/watch?v=tEFkHEKypLI

### To upload to PyPi ###
# pip install wheel --upgrade
# python setup.py sdist bdist_wheel
# pip install twine --upgrade
# twine upload dist/*
### Use your PyPi credentials when prompted ###
# Username: __token__
# Password: {API_KEY}

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

PACKAGE_NAME = "BubbleMath"
VERSION = '0.0.4'
AUTHOR = "SoapDoesCode"
AUTHOR_EMAIL = ""
DESCRIPTION = ''

# Setting up
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['gmpy2'], # required packages
    keywords=['python', 'math', 'calculations', 'calculator', 'bubble math'],
    classifiers=[
        "Development Status :: 1 - Planning", # https://pypi.org/classifiers/
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)