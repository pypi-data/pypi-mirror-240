# pypi_pip_template
a template for build python package to upload pypi repository bu using pip

https://pypi.org/project/pypi-pip-template/

# Make sure you have upgraded version of pip
Windows
```
py -m pip install --upgrade pip
```

Linux/MAC OS
```
python3 -m pip install --upgrade pip
```

## Create a project with the following structure
```bash
pypi_pip_template
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src
│   └── pypi_pip_template
│       ├── __init__.py
│       ├── __main__.py
│       └── __version__.py
└── tests
    └── test.py
```

### windows
```powershell

$package="pypi_pip_template"
New-Item pyproject.toml -type file
New-Item setup.cfg -type file
New-Item LICENSE -type file
New-Item README.md -type file
New-Item .gitignore -type file
New-Item -Force -Path src/$package -ItemType Directory
New-Item src/$package/__init__.py -type file
New-Item src/$package/__main__.py -type file
New-Item src/$package/__version__.py -type file
New-Item -Force -Path tests -ItemType Directory
New-Item tests/test.py -type file


```

### linux
```bash

package="pypi_pip_template"
touch pyproject.toml
touch setup.cfg
touch LICENSE
touch README.md
touch .gitignore
mkdir -p src/${package}
touch src/${package}/__init__.py
touch src/${package}/__main__.py
touch src/${package}/__version__.py
mkdir -p tests
touch tests/test.py

```

## create virtualenv environment
windows
```powershell

python -m venv .venv
./.venv/Scripts/activate 

pip list

python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m pip install --upgrade twine

pip freeze >requirements.txt 

```

linux
```bash

python3 -m venv .venv
./.venv/Scripts/activate 

pip list

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine

pip freeze >requirements.txt 

```

## pyproject.toml 

This file tells tools like pip and build how to create your project

```bash
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
build-system.requires gives a list of packages that are needed to build your package. Listing something here will only make it available during the build, not after it is installed.

build-system.build-backend is the name of Python object that will be used to perform the build. If you were to use a different build system, such as flit or poetry, those would go here, and the configuration details would be completely different than the setuptools configuration described below.


# Setup.cfg setup
Using setup.cfg is a best practice, but you could have a dynamic setup file using setup.py

```bash
[metadata]
name = pypi_pip_template
version = 0.0.1
author = lgf4591
author_email = lgf4591@outlook.com
description = a template for build python package to upload pypi repository bu using pip
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/lgf4591/pypi_pip_template
project_urls =
    Bug Tracker = https://github.com/lgf4591/pypi_pip_template/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.8

[options.packages.find]
where = src

```
# Running the build
### Make sure your build tool is up to date
Windows
```powershell

python -m pip install --upgrade build

```
Linux/MAC OS
```bash

python3 -m pip install --upgrade build

```


### Create the build
windows
```powershell
Remove-Item -LiteralPath "dist" -Force -Recurse
python -m build

```
linux
```bash
rm -rf dist
python3 -m build

```

### publish package to pypi
windows
```powershell

# python -m twine upload --repository testpypi dist/*
python -m twine upload --repository pypi dist/*

```

linux
```bash



```

You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.

After the command completes, you should see output similar to this:

```bash
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Uploading example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
Uploading example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?

```



### Installing your newly uploaded package
You can use pip to install your package and verify that it works. Create a virtual environment and install your package from TestPyPI:

```powershell

# python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
python -m pip install --index-url https://pypi.org/simple/ --no-deps pypi-pip-template==0.0.1
python -m pip install pypi-pip-template==0.0.1
pip install pypi-pip-template==0.0.1
pip install -i https://pypi.org/simple pypi-pip-template==0.0.1 (recomend)

```

```bash

# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
python3 -m pip install --index-url https://pypi.org/simple/ --no-deps epypi-pip-template==0.0.1
python3 -m pip install pypi-pip-template==0.0.1
pip install pypi-pip-template==0.0.1
pip install -i https://pypi.org/simple pypi-pip-template==0.0.1 ((recomend))

```






### References
- https://www.youtube.com/watch?v=v4bkJef4W94
- https://packaging.python.org/tutorials/packaging-projects/
