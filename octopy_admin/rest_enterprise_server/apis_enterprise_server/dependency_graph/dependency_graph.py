"""
Endpoints to access Dependency Graph features.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, too-few-public-methods


class DependencyGraph:
    """
    Endpoints to access Dependency Graph features.
    """

    def __init__(self, client):
        """
        Initializes the DependencyGraph class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_a_diff_of_the_dependencies_between_commits(
        self, owner, repo, basehead, params=None, payload=None
    ):
        """
        Summary:
        Get a diff of the dependencies between commits
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/dependency-graph#get-a-diff-of-the-dependencies-between-commits
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
