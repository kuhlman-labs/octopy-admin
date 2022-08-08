"""
Retrieve code scanning alerts from a repository.
"""


# pylint: disable=too-many-arguments
class CodeScanning:
    """
    Retrieve code scanning alerts from a repository.
    """

    def __init__(self, client):
        """
        Initialize the CodeScanning class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_code_scanning_alerts_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        List code scanning alerts for an enterprise
        https://docs.github.com/rest/reference/code-scanning#list-code-scanning-alerts-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        tool-name
         tool-guid
         pagination-before
         pagination-after
         page
         per-page
         direction
         state
         sort
        """
        url = self._base_url + f"/enterprises/{enterprise}/code-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_code_scanning_alerts_for_an_organization(self, org, params=None, payload=None):
        """
        List code scanning alerts for an organization
        https://docs.github.com/rest/reference/code-scanning#list-code-scanning-alerts-by-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        tool-name
         tool-guid
         pagination-before
         pagination-after
         page
         per-page
         direction
         state
         sort
        """
        url = self._base_url + f"/orgs/{org}/code-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_code_scanning_alerts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List code scanning alerts for a repository
        https://docs.github.com/rest/reference/code-scanning#list-code-scanning-alerts-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        tool-name
         tool-guid
         page
         per-page
         git-ref
         direction
         sort
         state
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_code_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Get a code scanning alert
        https://docs.github.com/rest/reference/code-scanning#get-a-code-scanning-alert
        Attributes:
        Path Parameters:
        owner
        repo
        alert_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_code_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Update a code scanning alert
        https://docs.github.com/rest/reference/code-scanning#update-a-code-scanning-alert
        Attributes:
        Path Parameters:
        owner
        repo
        alert_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_instances_of_a_code_scanning_alert(
        self, owner, repo, alert_number, params=None, payload=None
    ):
        """
        List instances of a code scanning alert
        https://docs.github.com/rest/reference/code-scanning#list-instances-of-a-code-scanning-alert
        Attributes:
        Path Parameters:
        owner
        repo
        alert_number
        Payload Parameters:
        page
         per-page
         git-ref
        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_code_scanning_analyses_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List code scanning analyses for a repository
        https://docs.github.com/rest/reference/code-scanning#list-code-scanning-analyses-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        tool-name
         tool-guid
         page
         per-page
         ref
         sarif_id
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/analyses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_code_scanning_analysis_for_a_repository(
        self, owner, repo, analysis_id, params=None, payload=None
    ):
        """
        Get a code scanning analysis for a repository
        https://docs.github.com/rest/reference/code-scanning#get-a-code-scanning-analysis-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        analysis_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_code_scanning_analysis_from_a_repository(
        self, owner, repo, analysis_id, params=None, payload=None
    ):
        """
        Delete a code scanning analysis from a repository
        https://docs.github.com/rest/reference/code-scanning#delete-a-code-scanning-analysis-from-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        analysis_id
        Payload Parameters:
        confirm_delete
        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def run_codeql_queries_against_one_or_more_repositories(
        self, owner, repo, params=None, payload=None
    ):
        """
        Run CodeQL queries against one or more repositories
        https://docs.github.com/rest/reference/code-scanning#run-codeql-queries-against-one-or-more-repositories
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/codeql/queries"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def put_a_summary_status_report_for_building_a_codeql_database(
        self, owner, repo, params=None, payload=None
    ):
        """
        Put a summary status report for building a CodeQL database
        N/A
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/codeql/status"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def upload_an_analysis_as_sarif_data(self, owner, repo, params=None, payload=None):
        """
        Upload an analysis as SARIF data
        https://docs.github.com/rest/reference/code-scanning#upload-a-sarif-file
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/sarifs"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_information_about_a_sarif_upload(
        self, owner, repo, sarif_id, params=None, payload=None
    ):
        """
        Get information about a SARIF upload
        https://docs.github.com/rest/reference/code-scanning#list-recent-code-scanning-analyses-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        sarif_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response
