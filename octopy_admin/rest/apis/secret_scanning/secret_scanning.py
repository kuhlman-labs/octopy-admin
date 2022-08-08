"""
Retrieve secret scanning alerts from a repository.
"""


# pylint: disable=too-many-arguments
class SecretScanning:
    """
    Retrieve secret scanning alerts from a repository.
    """

    def __init__(self, client):
        """
        Initialize the SecretScanning class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_secret_scanning_alerts_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        List secret scanning alerts for an enterprise
        https://docs.github.com/rest/reference/secret-scanning#list-secret-scanning-alerts-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        secret-scanning-alert-state
         secret-scanning-alert-secret-type
         secret-scanning-alert-resolution
         secret-scanning-alert-sort
         direction
         per-page
         pagination-before
         pagination-after
        """
        url = self._base_url + f"/enterprises/{enterprise}/secret-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_secret_scanning_alerts_for_an_organization(self, org, params=None, payload=None):
        """
        List secret scanning alerts for an organization
        https://docs.github.com/rest/reference/secret-scanning#list-secret-scanning-alerts-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        secret-scanning-alert-state
         secret-scanning-alert-secret-type
         secret-scanning-alert-resolution
         secret-scanning-alert-sort
         direction
         page
         per-page
         secret-scanning-pagination-before-org-repo
         secret-scanning-pagination-after-org-repo
        """
        url = self._base_url + f"/orgs/{org}/secret-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_secret_scanning_alerts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List secret scanning alerts for a repository
        https://docs.github.com/rest/reference/secret-scanning#list-secret-scanning-alerts-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        secret-scanning-alert-state
         secret-scanning-alert-secret-type
         secret-scanning-alert-resolution
         secret-scanning-alert-sort
         direction
         page
         per-page
         secret-scanning-pagination-before-org-repo
         secret-scanning-pagination-after-org-repo
        """
        url = self._base_url + f"/repos/{owner}/{repo}/secret-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_secret_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Get a secret scanning alert
        https://docs.github.com/rest/reference/secret-scanning#get-a-secret-scanning-alert
        Attributes:
        Path Parameters:
        owner
        repo
        alert_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_secret_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Update a secret scanning alert
        https://docs.github.com/rest/reference/secret-scanning#update-a-secret-scanning-alert
        Attributes:
        Path Parameters:
        owner
        repo
        alert_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_locations_for_a_secret_scanning_alert(
        self, owner, repo, alert_number, params=None, payload=None
    ):
        """
        List locations for a secret scanning alert
        https://docs.github.com/rest/reference/secret-scanning#list-locations-for-a-secret-scanning-alert
        Attributes:
        Path Parameters:
        owner
        repo
        alert_number
        Payload Parameters:
        page
         per-page
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response
