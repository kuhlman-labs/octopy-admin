"""
Endpoints to manage Dependabot.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Dependabot:
    """
    Endpoints to manage Dependabot.
    """

    def __init__(self, client):
        """
        Initializes the Dependabot class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_secrets(self, org, params=None, payload=None):
        """
        Summary:
        List organization secrets
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#list-organization-secrets
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_public_key(self, org, params=None, payload=None):
        """
        Summary:
        Get an organization public key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#get-an-organization-public-key
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Get an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#get-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Create or update an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#create-or-update-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_organization_secret(self, org, secret_name, params=None, payload=None):
        """
        Summary:
        Delete an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#delete-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Summary:
        List selected repositories for an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#list-selected-repositories-for-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_selected_repositories_for_an_organization_secret(
        self, org, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Set selected repositories for an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#set-selected-repositories-for-an-organization-secret
        """
        url = self._base_url + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def add_selected_repository_to_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Add selected repository to an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#add-selected-repository-to-an-organization-secret
        """
        url = (
            self._base_url
            + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_selected_repository_from_an_organization_secret(
        self, org, secret_name, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Remove selected repository from an organization secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#remove-selected-repository-from-an-organization-secret
        """
        url = (
            self._base_url
            + f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_dependabot_alerts_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List Dependabot alerts for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#list-dependabot-alerts-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_dependabot_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Summary:
        Get a Dependabot alert
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#get-a-dependabot-alert
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_dependabot_alert(self, owner, repo, alert_number, params=None, payload=None):
        """
        Summary:
        Update a Dependabot alert
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#update-a-dependabot-alert
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_repository_secrets(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository secrets
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#list-repository-secrets
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_public_key(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a repository public key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#get-a-repository-public-key
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/public-key"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Summary:
        Get a repository secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#get-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_a_repository_secret(
        self, owner, repo, secret_name, params=None, payload=None
    ):
        """
        Summary:
        Create or update a repository secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#create-or-update-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_secret(self, owner, repo, secret_name, params=None, payload=None):
        """
        Summary:
        Delete a repository secret
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/dependabot#delete-a-repository-secret
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
