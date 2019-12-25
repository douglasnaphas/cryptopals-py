# cryptopals-python
Solutions to https://cryptopals.com/ in Python.

## Setup

### Get pyenv
Install [pyenv](https://github.com/pyenv/pyenv#installation) to manage your
Python versions.

### Choose your Python version
Do `pyenv install --list` to see available Python versions.

This project has a `pyproject.toml` file that sets a required Python version
range of ^3.7.

To setup, for example, Python 3.8.0, in the current shell, do:

    pyenv install 3.8.0
    pyenv shell 3.8.0

### Create and activate virtualenv

    pip install virtualenv
    virtualenv -p $(which python) venv
    . venv/bin/activate

### Install poetry
Install [poetry](https://pypi.org/project/poetry/) to manage dependencies.

### Install dependencies

    poetry install

## Run tests

    python -m unittest # run all tests
    python -m unittest utils.test.test_utils.TestNby # run a specific class
