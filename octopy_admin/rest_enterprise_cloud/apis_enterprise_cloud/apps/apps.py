"""
Information for integrations and installations.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Apps:
    """
    Information for integrations and installations.
    """

    def __init__(self, client):
        """
        Initializes the Apps class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_the_authenticated_app(self, params=None, payload=None):
        """
        Summary:
        Get the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-the-authenticated-app
        """
        url = self._base_url + "/app"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_github_app_from_a_manifest(self, code, params=None, payload=None):
        """
        Summary:
        Create a GitHub App from a manifest
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#create-a-github-app-from-a-manifest
        """
        url = self._base_url + f"/app-manifests/{code}/conversions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_webhook_configuration_for_an_app(self, params=None, payload=None):
        """
        Summary:
        Get a webhook configuration for an app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-a-webhook-configuration-for-an-app
        """
        url = self._base_url + "/app/hook/config"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_webhook_configuration_for_an_app(self, params=None, payload=None):
        """
        Summary:
        Update a webhook configuration for an app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#update-a-webhook-configuration-for-an-app
        """
        url = self._base_url + "/app/hook/config"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_deliveries_for_an_app_webhook(self, params=None, payload=None):
        """
        Summary:
        List deliveries for an app webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-deliveries-for-an-app-webhook
        """
        url = self._base_url + "/app/hook/deliveries"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_delivery_for_an_app_webhook(self, delivery_id, params=None, payload=None):
        """
        Summary:
        Get a delivery for an app webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-a-delivery-for-an-app-webhook
        """
        url = self._base_url + f"/app/hook/deliveries/{delivery_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def redeliver_a_delivery_for_an_app_webhook(self, delivery_id, params=None, payload=None):
        """
        Summary:
        Redeliver a delivery for an app webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#redeliver-a-delivery-for-an-app-webhook
        """
        url = self._base_url + f"/app/hook/deliveries/{delivery_id}/attempts"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_installations_for_the_authenticated_app(self, params=None, payload=None):
        """
        Summary:
        List installations for the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-installations-for-the-authenticated-app
        """
        url = self._base_url + "/app/installations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_installation_for_the_authenticated_app(
        self, installation_id, params=None, payload=None
    ):
        """
        Summary:
        Get an installation for the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-an-installation-for-the-authenticated-app
        """
        url = self._base_url + f"/app/installations/{installation_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_installation_for_the_authenticated_app(
        self, installation_id, params=None, payload=None
    ):
        """
        Summary:
        Delete an installation for the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#delete-an-installation-for-the-authenticated-app
        """
        url = self._base_url + f"/app/installations/{installation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_an_installation_access_token_for_an_app(
        self, installation_id, params=None, payload=None
    ):
        """
        Summary:
        Create an installation access token for an app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps/#create-an-installation-access-token-for-an-app
        """
        url = self._base_url + f"/app/installations/{installation_id}/access_tokens"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def suspend_an_app_installation(self, installation_id, params=None, payload=None):
        """
        Summary:
        Suspend an app installation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#suspend-an-app-installation
        """
        url = self._base_url + f"/app/installations/{installation_id}/suspended"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unsuspend_an_app_installation(self, installation_id, params=None, payload=None):
        """
        Summary:
        Unsuspend an app installation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#unsuspend-an-app-installation
        """
        url = self._base_url + f"/app/installations/{installation_id}/suspended"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def delete_an_app_authorization(self, client_id, params=None, payload=None):
        """
        Summary:
        Delete an app authorization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#delete-an-app-authorization
        """
        url = self._base_url + f"/applications/{client_id}/grant"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def check_a_token(self, client_id, params=None, payload=None):
        """
        Summary:
        Check a token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#check-a-token
        """
        url = self._base_url + f"/applications/{client_id}/token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def reset_a_token(self, client_id, params=None, payload=None):
        """
        Summary:
        Reset a token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#reset-a-token
        """
        url = self._base_url + f"/applications/{client_id}/token"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_an_app_token(self, client_id, params=None, payload=None):
        """
        Summary:
        Delete an app token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#delete-an-app-token
        """
        url = self._base_url + f"/applications/{client_id}/token"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_scoped_access_token(self, client_id, params=None, payload=None):
        """
        Summary:
        Create a scoped access token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#create-a-scoped-access-token
        """
        url = self._base_url + f"/applications/{client_id}/token/scoped"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_app(self, app_slug, params=None, payload=None):
        """
        Summary:
        Get an app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps/#get-an-app
        """
        url = self._base_url + f"/apps/{app_slug}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_accessible_to_the_app_installation(self, params=None, payload=None):
        """
        Summary:
        List repositories accessible to the app installation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-repositories-accessible-to-the-app-installation
        """
        url = self._base_url + "/installation/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def revoke_an_installation_access_token(self, params=None, payload=None):
        """
        Summary:
        Revoke an installation access token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#revoke-an-installation-access-token
        """
        url = self._base_url + "/installation/token"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_subscription_plan_for_an_account(self, account_id, params=None, payload=None):
        """
        Summary:
        Get a subscription plan for an account
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-a-subscription-plan-for-an-account
        """
        url = self._base_url + f"/marketplace_listing/accounts/{account_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_plans(self, params=None, payload=None):
        """
        Summary:
        List plans
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-plans
        """
        url = self._base_url + "/marketplace_listing/plans"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_accounts_for_a_plan(self, plan_id, params=None, payload=None):
        """
        Summary:
        List accounts for a plan
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-accounts-for-a-plan
        """
        url = self._base_url + f"/marketplace_listing/plans/{plan_id}/accounts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_subscription_plan_for_an_account__stubbed(
        self, account_id, params=None, payload=None
    ):
        """
        Summary:
        Get a subscription plan for an account (stubbed)
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-a-subscription-plan-for-an-account-stubbed
        """
        url = self._base_url + f"/marketplace_listing/stubbed/accounts/{account_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_plans__stubbed(self, params=None, payload=None):
        """
        Summary:
        List plans (stubbed)
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-plans-stubbed
        """
        url = self._base_url + "/marketplace_listing/stubbed/plans"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_accounts_for_a_plan__stubbed(self, plan_id, params=None, payload=None):
        """
        Summary:
        List accounts for a plan (stubbed)
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-accounts-for-a-plan-stubbed
        """
        url = self._base_url + f"/marketplace_listing/stubbed/plans/{plan_id}/accounts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_installation_for_the_authenticated_app(
        self, org, params=None, payload=None
    ):
        """
        Summary:
        Get an organization installation for the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-an-organization-installation-for-the-authenticated-app
        """
        url = self._base_url + f"/orgs/{org}/installation"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_installation_for_the_authenticated_app(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Get a repository installation for the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-a-repository-installation-for-the-authenticated-app
        """
        url = self._base_url + f"/repos/{owner}/{repo}/installation"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_app_installations_accessible_to_the_user_access_token(self, params=None, payload=None):
        """
        Summary:
        List app installations accessible to the user access token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-app-installations-accessible-to-the-user-access-token
        """
        url = self._base_url + "/user/installations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_accessible_to_the_user_access_token(
        self, installation_id, params=None, payload=None
    ):
        """
        Summary:
        List repositories accessible to the user access token
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-repositories-accessible-to-the-user-access-token
        """
        url = self._base_url + f"/user/installations/{installation_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_a_repository_to_an_app_installation(
        self, installation_id, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Add a repository to an app installation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#add-a-repository-to-an-app-installation
        """
        url = self._base_url + f"/user/installations/{installation_id}/repositories/{repository_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_from_an_app_installation(
        self, installation_id, repository_id, params=None, payload=None
    ):
        """
        Summary:
        Remove a repository from an app installation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#remove-a-repository-from-an-app-installation
        """
        url = self._base_url + f"/user/installations/{installation_id}/repositories/{repository_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_subscriptions_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List subscriptions for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-subscriptions-for-the-authenticated-user
        """
        url = self._base_url + "/user/marketplace_purchases"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_subscriptions_for_the_authenticated_user__stubbed(self, params=None, payload=None):
        """
        Summary:
        List subscriptions for the authenticated user (stubbed)
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#list-subscriptions-for-the-authenticated-user-stubbed
        """
        url = self._base_url + "/user/marketplace_purchases/stubbed"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_user_installation_for_the_authenticated_app(
        self, username, params=None, payload=None
    ):
        """
        Summary:
        Get a user installation for the authenticated app
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/apps#get-a-user-installation-for-the-authenticated-app
        """
        url = self._base_url + f"/users/{username}/installation"
        response = self._execute("get", url, params=params, payload=payload)
        return response
