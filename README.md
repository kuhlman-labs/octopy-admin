# OctoPy Admin

OctoPy Admin is a Python library for interacting with the GitHub GraphQL
and REST APIs.

## Installation

### Install with Poetry

OctoPy Admin uses Poetry for dependency management. If you haven't installed
it already please use Poetry's [official docs](https://python-poetry.org/docs/#installation)
for instructions.

Clone the repository locally, change directory to
project root, and run the following command:

```bash
poetry install
```

### Install with pip

```bash
pip install octopy-admin
```

### Set Environment Variables

Creat a `.env` file at the root of the repo and set value for `API_TOKEN`.
If running against GHES, set value for `GHE_HOSTNAME` to determine appropirate
API endpoints, if these values are not set it defaults to the .com endpoints.

#### GitHub Enterprise Example

```bash
GHE_HOSTNAME=github.domain.com
API_TOKEN=ghp_xxx
```

## Usage

### Rest API

To use the OctoPy Admin Rest package, import the `RestClient` class from the
`octopy_admin.rest.rest_client` module and instantiate a new `RestClient` object.

Example:

```python
from dotenv import load_dotenv # Import if you want to use .env file
from octopy_admin.rest.rest_client import RestClient

# Load environment variables from a .env file
load_dotenv()
# Create a new RestClient object
github = RestClient()
# Create a new RestClient object and set the API token and the GHES hostname
# github = RestClient(hostname="ghes.kuhlman-labs.io", api_token="ghp_xxxxx")

# Make a request to the REST API for the current user:
current_user = github.users.get_the_authenticated_user()
# Print response
print(current_user.text)
```

### GraphQL API

To use the OctoPy Admin Rest package, import the `GraphClient` class from the
`octopy_admin.graph.graph_client` module and instantiate a new `GraphClient` object.

Example:

```python
from dotenv import load_dotenv # Import if you want to use .env file
from octopy_admin.graph.graph_client import GraphClient

# Load environment variables from a .env file:
load_dotenv() 
# Create a new GraphClient object:
github = GraphClient()
# Create a new GraphClient object and set the API token and the GHES hostname:
# github = GraphClient(hostname="ghes.kuhlman-labs.io", api_token="ghp_xxxxx")

# Make a request to the Graph API to get an organization's repositories:
repo_query = github.query.get_org_repos(org)
# Get a list of repositories:
repos = github.query.results_to_list(repo_query)
# Print list:
print(repos)
```

Other Examples can be found in the [reports](/reports/) and
[scripts](/scripts/) folders.

## Library Reference

For a complete reference of the library's API, please see the
[API Reference](https://kuhlman-labs.github.io/octopy-admin/reference/).
