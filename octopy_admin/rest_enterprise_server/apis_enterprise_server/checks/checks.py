"""
Rich interactions with checks run by your integrations.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Checks:
    """
    Rich interactions with checks run by your integrations.
    """

    def __init__(self, client):
        """
        Initializes the Checks class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def create_a_check_run(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a check run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#create-a-check-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_check_run(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Summary:
        Get a check run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#get-a-check-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_check_run(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Summary:
        Update a check run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#update-a-check-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_check_run_annotations(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Summary:
        List check run annotations
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#list-check-run-annotations
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def rerequest_a_check_run(self, owner, repo, check_run_id, params=None, payload=None):
        """
        Summary:
        Rerequest a check run
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#rerequest-a-check-run
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_check_suite(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a check suite
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#create-a-check-suite
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_repository_preferences_for_check_suites(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Update repository preferences for check suites
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#update-repository-preferences-for-check-suites
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/preferences"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_a_check_suite(self, owner, repo, check_suite_id, params=None, payload=None):
        """
        Summary:
        Get a check suite
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#get-a-check-suite
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/{check_suite_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_check_runs_in_a_check_suite(
        self, owner, repo, check_suite_id, params=None, payload=None
    ):
        """
        Summary:
        List check runs in a check suite
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#list-check-runs-in-a-check-suite
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def rerequest_a_check_suite(self, owner, repo, check_suite_id, params=None, payload=None):
        """
        Summary:
        Rerequest a check suite
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#rerequest-a-check-suite
        """
        url = self._base_url + f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_check_runs_for_a_git_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        List check runs for a Git reference
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#list-check-runs-for-a-git-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/check-runs"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_check_suites_for_a_git_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        List check suites for a Git reference
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/checks#list-check-suites-for-a-git-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/check-suites"
        response = self._execute("get", url, params=params, payload=payload)
        return response
