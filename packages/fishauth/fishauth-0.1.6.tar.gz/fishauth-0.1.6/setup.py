from __future__ import print_function

import io
import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
this_directory = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(this_directory, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()


install_requires = ["SQLAlchemy==2.0.22", "typing_extensions==4.8.0"]
setup(
    name="fishauth",
    version="0.1.6",
    author="Johan Rujano",
    author_email="johanrujano@gmail.com",
    description="Libraries that have models and methods to handle user authentication",
    license="https://www.apache.org/licenses/LICENSE-2.0",
    url="https://github.com/jrujano/fishauth-library",
    packages=["fishauth", "fishauth.models"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
    ],
    keywords="tools authentication login auth session",
)
