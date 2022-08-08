"""
Endpoints to access Dependency Graph features.
"""


# pylint: disable=too-many-arguments
class DependencyGraph:
    """
    Endpoints to access Dependency Graph features.
    """

    def __init__(self, client):
        """
        Initialize the DependencyGraph class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_a_diff_of_the_dependencies_between_commits(
        self, owner, repo, basehead, params=None, payload=None
    ):
        """
        Get a diff of the dependencies between commits
        https://docs.github.com/rest/reference/dependency-graph#get-a-diff-of-the-dependencies-between-commits
        Attributes:
        Path Parameters:
        owner
        repo
        basehead
        Payload Parameters:
        manifest-path
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_snapshot_dependencies_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Get snapshot dependencies for a repository
        https://docs.github.com/rest/reference/repos#dependency-graph/get-snapshot-dependencies-for-repo
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependency-graph/dependencies"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_snapshot_of_dependencies_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Create a snapshot of dependencies for a repository
        https://docs.github.com/rest/reference/dependency-graph#create-a-snapshot-of-dependencies-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependency-graph/snapshots"
        response = self._execute("post", url, params=params, payload=payload)
        return response
