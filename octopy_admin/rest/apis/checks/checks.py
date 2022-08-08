"""
Rich interactions with checks run by your integrations.
"""


# pylint: disable=too-many-arguments
class Checks:
    """
    Rich interactions with checks run by your integrations.
    """

    def __init__(self, client):
        """
        Initialize the Checks class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def create_a_check_run(self, owner, repo, params=None, payload=None):
        """
        Create a check run
        https://docs.github.com/rest/reference/checks#create-a-check-run
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_check_run(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Get a check run
        https://docs.github.com/rest/reference/checks#get-a-check-run
        Attributes:
        Path Parameters:
        owner
        repo
        check_run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_check_run(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Update a check run
        https://docs.github.com/rest/reference/checks#update-a-check-run
        Attributes:
        Path Parameters:
        owner
        repo
        check_run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_check_run_annotations(self, owner, repo, check_run_id, params=None, payload=None):
        """
        List check run annotations
        https://docs.github.com/rest/reference/checks#list-check-run-annotations
        Attributes:
        Path Parameters:
        owner
        repo
        check_run_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def rerequest_a_check_run(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Rerequest a check run
        https://docs.github.com/rest/reference/checks#rerequest-a-check-run
        Attributes:
        Path Parameters:
        owner
        repo
        check_run_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_check_suite(self, owner, repo, params=None, payload=None):
        """
        Create a check suite
        https://docs.github.com/rest/reference/checks#create-a-check-suite
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_repository_preferences_for_check_suites(
        self, owner, repo, params=None, payload=None
    ):
        """
        Update repository preferences for check suites
        https://docs.github.com/rest/reference/checks#update-repository-preferences-for-check-suites
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/preferences"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_a_check_suite(self, owner, repo, check_suite_id, params=None, payload=None):
        """
        Get a check suite
        https://docs.github.com/rest/reference/checks#get-a-check-suite
        Attributes:
        Path Parameters:
        owner
        repo
        check_suite_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/{check_suite_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_check_runs_in_a_check_suite(
        self, owner, repo, check_suite_id, params=None, payload=None
    ):
        """
        List check runs in a check suite
        https://docs.github.com/rest/reference/checks#list-check-runs-in-a-check-suite
        Attributes:
        Path Parameters:
        owner
        repo
        check_suite_id
        Payload Parameters:
        check-name
         status
         filter
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def rerequest_a_check_suite(self, owner, repo, check_suite_id, params=None, payload=None):
        """
        Rerequest a check suite
        https://docs.github.com/rest/reference/checks#rerequest-a-check-suite
        Attributes:
        Path Parameters:
        owner
        repo
        check_suite_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_check_runs_for_a_git_reference(self, owner, repo, ref, params=None, payload=None):
        """
        List check runs for a Git reference
        https://docs.github.com/rest/reference/checks#list-check-runs-for-a-git-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:
        check-name
         status
         filter
         per-page
         page
         app_id
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/check-runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_check_suites_for_a_git_reference(self, owner, repo, ref, params=None, payload=None):
        """
        List check suites for a Git reference
        https://docs.github.com/rest/reference/checks#list-check-suites-for-a-git-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:
        app_id
         check-name
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/check-suites"
        response = self._execute("get", url, params=params, payload=payload)
        return response
