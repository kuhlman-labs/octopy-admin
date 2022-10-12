"""
Retrieve code scanning alerts from a repository.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class CodeScanning:
    """
    Retrieve code scanning alerts from a repository.
    """

    def __init__(self, client):
        """
        Initializes the CodeScanning class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_code_scanning_alerts_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List code scanning alerts for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#list-code-scanning-alerts-by-organization
        """
        url = self._base_url + f"/orgs/{org}/code-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_code_scanning_alerts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List code scanning alerts for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#list-code-scanning-alerts-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_code_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Summary:
        Get a code scanning alert
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#get-a-code-scanning-alert
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_code_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Summary:
        Update a code scanning alert
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#update-a-code-scanning-alert
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_instances_of_a_code_scanning_alert(
        self, owner, repo, alert_number, params=None, payload=None
    ):
        """
        Summary:
        List instances of a code scanning alert
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#list-instances-of-a-code-scanning-alert
        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_code_scanning_analyses_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List code scanning analyses for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#list-code-scanning-analyses-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/analyses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_code_scanning_analysis_for_a_repository(
        self, owner, repo, analysis_id, params=None, payload=None
    ):
        """
        Summary:
        Get a code scanning analysis for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#get-a-code-scanning-analysis-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_code_scanning_analysis_from_a_repository(
        self, owner, repo, analysis_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a code scanning analysis from a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#delete-a-code-scanning-analysis-from-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def upload_an_analysis_as_sarif_data(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Upload an analysis as SARIF data
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#upload-a-sarif-file
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/sarifs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_information_about_a_sarif_upload(
        self, owner, repo, sarif_id, params=None, payload=None
    ):
        """
        Summary:
        Get information about a SARIF upload
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/code-scanning#list-recent-code-scanning-analyses-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
