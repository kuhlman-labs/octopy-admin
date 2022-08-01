"""
Monitor charges and usage from Actions and Packages.
"""


class Billing:
    """
    Monitor charges and usage from Actions and Packages.
    """

    def __init__(self, client):
        """
        Initialize the Billing class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_github_actions_billing_for_an_enterprise(self, enterprise, payload=None):
        """
        Get GitHub Actions billing for an enterprise
        https://docs.github.com/rest/reference/billing#get-github-actions-billing-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/settings/billing/actions"
        response = self._execute("get", url, payload)
        return response

    def get_github_advanced_security_active_committers_for_an_enterprise(
        self, enterprise, payload=None
    ):
        """
        Get GitHub Advanced Security active committers for an enterprise
        https://docs.github.com/rest/reference/billing#export-advanced-security-active-committers-data-for-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/enterprises/{enterprise}/settings/billing/advanced-security"
        response = self._execute("get", url, payload)
        return response

    def get_github_packages_billing_for_an_enterprise(self, enterprise, payload=None):
        """
        Get GitHub Packages billing for an enterprise
        https://docs.github.com/rest/reference/billing#get-github-packages-billing-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/settings/billing/packages"
        response = self._execute("get", url, payload)
        return response

    def get_shared_storage_billing_for_an_enterprise(self, enterprise, payload=None):
        """
        Get shared storage billing for an enterprise
        https://docs.github.com/rest/reference/billing#get-shared-storage-billing-for-an-enterprise
        Attributes:
        Path Parameters:
        enterprise
        Payload Parameters:

        """
        url = self._base_url + f"/enterprises/{enterprise}/settings/billing/shared-storage"
        response = self._execute("get", url, payload)
        return response

    def get_github_actions_billing_for_an_organization(self, org, payload=None):
        """
        Get GitHub Actions billing for an organization
        https://docs.github.com/rest/reference/billing#get-github-actions-billing-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/settings/billing/actions"
        response = self._execute("get", url, payload)
        return response

    def get_github_advanced_security_active_committers_for_an_organization(self, org, payload=None):
        """
        Get GitHub Advanced Security active committers for an organization
        https://docs.github.com/rest/reference/billing#get-github-advanced-security-active-committers-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/settings/billing/advanced-security"
        response = self._execute("get", url, payload)
        return response

    def get_github_packages_billing_for_an_organization(self, org, payload=None):
        """
        Get GitHub Packages billing for an organization
        https://docs.github.com/rest/reference/billing#get-github-packages-billing-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/settings/billing/packages"
        response = self._execute("get", url, payload)
        return response

    def get_shared_storage_billing_for_an_organization(self, org, payload=None):
        """
        Get shared storage billing for an organization
        https://docs.github.com/rest/reference/billing#get-shared-storage-billing-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/settings/billing/shared-storage"
        response = self._execute("get", url, payload)
        return response

    def get_github_actions_billing_for_a_user(self, username, payload=None):
        """
        Get GitHub Actions billing for a user
        https://docs.github.com/rest/reference/billing#get-github-actions-billing-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/settings/billing/actions"
        response = self._execute("get", url, payload)
        return response

    def get_github_packages_billing_for_a_user(self, username, payload=None):
        """
        Get GitHub Packages billing for a user
        https://docs.github.com/rest/reference/billing#get-github-packages-billing-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/settings/billing/packages"
        response = self._execute("get", url, payload)
        return response

    def get_shared_storage_billing_for_a_user(self, username, payload=None):
        """
        Get shared storage billing for a user
        https://docs.github.com/rest/reference/billing#get-shared-storage-billing-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/settings/billing/shared-storage"
        response = self._execute("get", url, payload)
        return response
