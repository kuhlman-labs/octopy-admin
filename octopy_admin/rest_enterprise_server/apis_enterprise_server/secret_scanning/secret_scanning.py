"""
Retrieve secret scanning alerts from a repository.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class SecretScanning:
    """
    Retrieve secret scanning alerts from a repository.
    """

    def __init__(self, client):
        """
        Initializes the SecretScanning class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_secret_scanning_alerts_for_an_enterprise(self, enterprise, params=None, payload=None):
        """
        Summary:
        List secret scanning alerts for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/secret-scanning#list-secret-scanning-alerts-for-an-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/secret-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_secret_scanning_alerts_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List secret scanning alerts for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/secret-scanning#list-secret-scanning-alerts-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/secret-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_secret_scanning_alerts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List secret scanning alerts for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/secret-scanning#list-secret-scanning-alerts-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/secret-scanning/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_secret_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Summary:
        Get a secret scanning alert
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/secret-scanning#get-a-secret-scanning-alert
        """
        url = self._base_url + f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_secret_scanning_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Summary:
        Update a secret scanning alert
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/secret-scanning#update-a-secret-scanning-alert
        """
        url = self._base_url + f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_locations_for_a_secret_scanning_alert(
        self, owner, repo, alert_number, params=None, payload=None
    ):
        """
        Summary:
        List locations for a secret scanning alert
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/secret-scanning#list-locations-for-a-secret-scanning-alert
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response
