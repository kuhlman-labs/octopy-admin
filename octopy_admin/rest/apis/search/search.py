"""
Look for stuff on GitHub.
"""


# pylint: disable=too-many-arguments
class Search:
    """
    Look for stuff on GitHub.
    """

    def __init__(self, client):
        """
        Initialize the Search class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_resources_accessible_to_the_access_tokens_session(self, params=None, payload=None):
        """
        List resources accessible to the access_token's session
        https://docs.github.com/rest/reference/blackbird#list-resources-accessible-to-the-current-access-tokens-session
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/internal/blackbird/accessible_resources"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def generate_a_signed_access_token_for_use_with_blackbird_fe(self, params=None, payload=None):
        """
        Generate a signed access token for use with blackbird-fe
        https://docs.github.com/rest/reference/blackbird#generate-a-signed-access-token-for-use-with-blackbird-fe
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/internal/blackbird/authorize"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def search_code(self, params=None, payload=None):
        """
        Search code
        https://docs.github.com/rest/reference/search#search-code
        Attributes:
        Path Parameters:

        Payload Parameters:
        q
         sort
         order
         per-page
         page
        """
        url = self._base_url + "/search/code"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_commits(self, params=None, payload=None):
        """
        Search commits
        https://docs.github.com/rest/reference/search#search-commits
        Attributes:
        Path Parameters:

        Payload Parameters:
        q
         sort
         order
         per-page
         page
        """
        url = self._base_url + "/search/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_issues_and_pull_requests(self, params=None, payload=None):
        """
        Search issues and pull requests
        https://docs.github.com/rest/reference/search#search-issues-and-pull-requests
        Attributes:
        Path Parameters:

        Payload Parameters:
        q
         sort
         order
         per-page
         page
        """
        url = self._base_url + "/search/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_labels(self, params=None, payload=None):
        """
        Search labels
        https://docs.github.com/rest/reference/search#search-labels
        Attributes:
        Path Parameters:

        Payload Parameters:
        repository_id
         q
         sort
         order
         per-page
         page
        """
        url = self._base_url + "/search/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_repositories(self, params=None, payload=None):
        """
        Search repositories
        https://docs.github.com/rest/reference/search#search-repositories
        Attributes:
        Path Parameters:

        Payload Parameters:
        q
         sort
         order
         per-page
         page
        """
        url = self._base_url + "/search/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_topics(self, params=None, payload=None):
        """
        Search topics
        https://docs.github.com/rest/reference/search#search-topics
        Attributes:
        Path Parameters:

        Payload Parameters:
        q
         per-page
         page
        """
        url = self._base_url + "/search/topics"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_users(self, params=None, payload=None):
        """
        Search users
        https://docs.github.com/rest/reference/search#search-users
        Attributes:
        Path Parameters:

        Payload Parameters:
        q
         sort
         order
         per-page
         page
        """
        url = self._base_url + "/search/users"
        response = self._execute("get", url, params=params, payload=payload)
        return response
