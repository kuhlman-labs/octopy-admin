"""
This module containst the RestRequest class.
"""

import os

import requests


class RestRequestError(Exception):
    """
    Exception raised when a REST request fails.
    """


class RestRequest:  # pylint: disable=too-few-public-methods
    """
    The following methods are used to form requests to the GitHub REST API.
    """

    def __init__(self, rest_api_url=None, api_token=None):
        """
        Initialize the REST client to make requests to the GitHub API.

        Attributes:
            headers (dict): Headers to be used in the requests.
            base_url (str): Base URL of the GitHub API.
            API_TOKEN (str): GitHub API token.
            REST_API_URL (str): GitHub REST API URL.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
            if os.environ.get("API_TOKEN") is None:
                raise RestRequestError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {api_token}"}
        if rest_api_url is None:
            rest_api_url = os.environ.get("REST_API_URL", r"https://api.github.com")
        self._base_url = rest_api_url

    def _execute(self, method, url, payload):
        """
        Execute a request.

        Attributes:
            method (str): HTTP method.
            url (str): URL.
            payload (dict): Payload.
        """
        try:
            response = requests.request(method=method, url=url, json=payload, headers=self._headers)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise RestRequestError from errtimeout
        except requests.exceptions.HTTPError as errhttp:
            raise RestRequestError from errhttp
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestRequestError from errredirect
        except requests.exceptions.RequestException as errexcept:
            raise RestRequestError from errexcept
