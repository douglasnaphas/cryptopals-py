# cryptopals-python
Solutions to https://cryptopals.com/ in Python.

## Usage

### Get pyenv
Install [pyenv](https://github.com/pyenv/pyenv#installation) to manage your
Python versions.

### Choose your Python version
Do `pyenv install --list` to see available Python versions.

This project has a `pyproject.toml` file that sets a required Python version
range of ^3.9.

To setup, for example, Python 3.9.0, in the current shell, do:

    pyenv install 3.9.0
    pyenv shell 3.9.0

### Run tests

    make clean && make install && make test
