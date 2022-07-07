# Octopy Admin

Octopy Admin is a python library for interacting with the GitHub API.

## Installation

Octopy Admin uses Poetry for dependency management. If you haven't installed it already please use Poetry's [official docs](https://python-poetry.org/docs/#installation) for instructions.

1.Install project depenencies.

```bash
poetry install
```

2. Install pre-commit hooks

```bash
poetry run pre-commit install
```

You are ready to rock.

## Usage

TBD

```python
import toml
APP_CONFIG = toml.load("pyproject.toml")["app"]

app_name = APP_CONFIG['APP_NAME']
```

Also you can add app secrets directly to the `.env` file and read it anywhere from your project with the help of Python's built in `os` module.

```python
import os
secret = os.environ['APP_SECRET']
```

This is possible because we've loaded the env file from our `main.py` module. If you are replacing this module, be sure to load it again.