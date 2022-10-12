"""
Monitor charges and usage from Actions and Packages.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Billing:
    """
    Monitor charges and usage from Actions and Packages.
    """

    def __init__(self, client):
        """
        Initializes the Billing class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_advanced_security_active_committers_for_an_enterprise(
        self, enterprise, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Advanced Security active committers for an enterprise
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/billing#export-advanced-security-active-committers-data-for-enterprise
        """
        url = self._base_url + f"/enterprises/{enterprise}/settings/billing/advanced-security"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_advanced_security_active_committers_for_an_organization(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Advanced Security active committers for an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/billing#get-github-advanced-security-active-committers-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/settings/billing/advanced-security"
        response = self._execute("get", url, params=params, payload=payload)
        return response
