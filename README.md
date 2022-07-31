# OctoPy Admin

OctoPy Admin is a python library for interacting with the GitHub API.

## Installation

OctoPy Admin uses Poetry for dependency management. If you haven't installed
it already please use Poetry's [official docs](https://python-poetry.org/docs/#installation)
for instructions.

### Install project depenencies

```bash
poetry install
```

### Install pre-commit hooks

```bash
poetry run pre-commit install
```

### Set Environment Variables

Creat a `.env` file at the root of the repo and set value for `API_TOKEN`.
If running against GHES, set values for `GQL_API_URL` and `REST_API_URL` endpoints,
if these values are not set it defaults to the .com endpoints.

#### GitHub Enterprise Example

```bash
GRAPH_API_URL=https://{hostname}/api/graphql
REST_API_URL=https://{hostname}/api/v3
API_TOKEN=ghp_xxx
```

You are ready to rock!
