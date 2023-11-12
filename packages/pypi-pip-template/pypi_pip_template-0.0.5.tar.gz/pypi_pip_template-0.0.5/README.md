# pypi_pip_template
a template for build python package to upload pypi repository bu using pip

https://pypi.org/project/pypi-pip-template/


## Create a project with the following structure
```bash
pypi_pip_template
├── .gitignore
├── LICENSE
├── CHANGELOG.txt
├── README.md
├── setup.py
├── pypi_pip_template
│       ├── __init__.py
│       └── __main__.py
│       ├── gui
│           └── __init__.py
│       ├── utils
│           └── __init__.py
└── tests
    └── test.py
```

### windows
```powershell

$package="pypi_pip_template"
New-Item CHANGELOG.txt -type file
New-Item setup.py -type file
New-Item LICENSE -type file
New-Item README.md -type file
New-Item .gitignore -type file
New-Item -Force -Path $package/gui -ItemType Directory
New-Item -Force -Path $package/utils -ItemType Directory
New-Item $package/__init__.py -type file
New-Item $package/__main__.py -type file
New-Item $package/gui/__init__.py -type file
New-Item $package/utils/__init__.py -type file
New-Item -Force -Path tests -ItemType Directory
New-Item tests/test.py -type file


```

### linux
```bash

package="pypi_pip_template"
touch CHANGELOG.txt
touch setup.py
touch LICENSE
touch README.md
touch .gitignore
mkdir -p ${package}/gui
mkdir -p ${package}/utils
touch ${package}/__init__.py
touch ${package}/__main__.py
touch ${package}/gui/__init__.py
touch ${package}/utils/__init__.py
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
python -m pip install --upgrade build setuptools wheel twine

pip freeze >requirements.txt 

```

linux
```bash

python3 -m venv .venv
./.venv/Scripts/activate 

pip list

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build setuptools wheel twine

pip freeze >requirements.txt 

```

### Create the build
windows
```powershell
Remove-Item -LiteralPath "dist" -Force -Recurse
python setup.py sdist bdist_wheel

```
linux
```bash
rm -rf dist
python3 setup.py sdist bdist_wheel

```

### publish package to pypi
windows
```powershell

# python -m twine upload --repository testpypi dist/*
python -m twine upload --repository pypi dist/*

```

linux
```bash
# python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload --repository pypi dist/*


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
python3 -m pip install --index-url https://pypi.org/simple/ --no-deps pypi-pip-template==0.0.1
python3 -m pip install pypi-pip-template==0.0.1
pip install pypi-pip-template==0.0.1
pip install -i https://pypi.org/simple pypi-pip-template==0.0.1 ((recomend))

```






### References
- https://www.youtube.com/watch?v=v4bkJef4W94
- https://packaging.python.org/tutorials/packaging-projects/
- 
