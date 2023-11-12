from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2.1'
DESCRIPTION = 'A smarter print and profile for Python execution checks.'

with open("README.md", "r") as _:
	readme = _.readlines()

LONG_DESCRIPTION = readme

# Setting up
setup(
    name="pychek",
    version=VERSION,
    author="xbais (Aakash Singh Bais)",
    author_email="<aakash@aioniaepochi.org>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['setuptools', 'argparse', 'tqdm', 'colorama', 'psutil', 'pyfiglet'],
    keywords=['python', 'print', 'profiler'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
