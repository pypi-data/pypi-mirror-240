# coding=utf-8

import re
from pathlib import Path
from setuptools import setup, find_packages

# The directory containing this file
root_dir = Path(__file__).parent
project_name = root_dir.name
# exe_name = project_name.replace("pypi_", "")


# The text of the README file
# with open("README.md", "r") as fh:
#   readme = fh.read()
# README = (root_dir / "README.md").read_text(encoding='utf-8')
readme = root_dir.joinpath('README.md').read_text(encoding='utf-8')
changelog = root_dir.joinpath('CHANGELOG.txt').read_text(encoding='utf-8')

package_init = root_dir.joinpath(project_name, '__init__.py').read_text(encoding='utf-8')
# loc1 = package_init.find('__version__') + len('__version__')
# loc2 = package_init[loc1:].find("'") + 1
# loc3 = package_init[loc1+loc2:].find("'")
# VERSION = package_init[loc1+loc2:loc1+loc2+loc3]
version = re.findall("__version__ = .*", package_init)[0].replace("__version__ =", "").replace("'", "")
description = re.findall("__description__ = ", package_init)[0].replace("__description__ =", "")
author = re.findall("__author__ = ", package_init)[0].replace("__author__ =", "")
author_email = re.findall("__author_email__ = ", package_init)[0].replace("__author_email__ =", "")
url = re.findall("__url__ = ", package_init)[0].replace("__url__ =", "")
license = re.findall("__license__ = ", package_init)[0].replace("__license__ =", "")
# print(f"version is {version}")

# This call to setup() does all the work
setup(
    name=project_name,
    version=version,
    description=description,
    long_description=(readme + '\n\n' + changelog),
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    classifiers=[ # see https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=project_name.split("_"), 
    # package_dir={},
    packages=find_packages(),
    # packages=[project_name],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            f"{project_name}={project_name}.__main__:main",
        ]
    },
)
