"""
Look for stuff on GitHub.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Search:
    """
    Look for stuff on GitHub.
    """

    def __init__(self, client):
        """
        Initializes the Search class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def search_code(self, params=None, payload=None):
        """
        Summary:
        Search code
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-code
        """
        url = self._base_url + "/search/code"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_commits(self, params=None, payload=None):
        """
        Summary:
        Search commits
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-commits
        """
        url = self._base_url + "/search/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_issues_and_pull_requests(self, params=None, payload=None):
        """
        Summary:
        Search issues and pull requests
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-issues-and-pull-requests
        """
        url = self._base_url + "/search/issues"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_labels(self, params=None, payload=None):
        """
        Summary:
        Search labels
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-labels
        """
        url = self._base_url + "/search/labels"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_repositories(self, params=None, payload=None):
        """
        Summary:
        Search repositories
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-repositories
        """
        url = self._base_url + "/search/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_topics(self, params=None, payload=None):
        """
        Summary:
        Search topics
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-topics
        """
        url = self._base_url + "/search/topics"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def search_users(self, params=None, payload=None):
        """
        Summary:
        Search users
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/search#search-users
        """
        url = self._base_url + "/search/users"
        response = self._execute("get", url, params=params, payload=payload)
        return response
