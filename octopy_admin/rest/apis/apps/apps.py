"""
Information for integrations and installations.
"""


# pylint: disable=too-many-arguments
class Apps:
    # pylint: disable=too-many-public-methods
    """
    Information for integrations and installations.
    """

    def __init__(self, client):
        """
        Initialize the Apps class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_the_authenticated_app(self, params=None, payload=None):
        """
        Get the authenticated app
        https://docs.github.com/rest/reference/apps#get-the-authenticated-app
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/app"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_github_app_from_a_manifest(self, code, params=None, payload=None):
        """
        Create a GitHub App from a manifest
        https://docs.github.com/rest/reference/apps#create-a-github-app-from-a-manifest
        Attributes:
        Path Parameters:
        code
        Payload Parameters:

        """
        url = self._base_url + f"/app-manifests/{code}/conversions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_webhook_configuration_for_an_app(self, params=None, payload=None):
        """
        Get a webhook configuration for an app
        https://docs.github.com/rest/reference/apps#get-a-webhook-configuration-for-an-app
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/app/hook/config"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_webhook_configuration_for_an_app(self, params=None, payload=None):
        """
        Update a webhook configuration for an app
        https://docs.github.com/rest/reference/apps#update-a-webhook-configuration-for-an-app
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/app/hook/config"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_deliveries_for_an_app_webhook(self, params=None, payload=None):
        """
        List deliveries for an app webhook
        https://docs.github.com/rest/reference/apps#list-deliveries-for-an-app-webhook
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         cursor
        """
        url = self._base_url + "/app/hook/deliveries"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_delivery_for_an_app_webhook(self, delivery_id, params=None, payload=None):
        """
        Get a delivery for an app webhook
        https://docs.github.com/rest/reference/apps#get-a-delivery-for-an-app-webhook
        Attributes:
        Path Parameters:
        delivery_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/hook/deliveries/{delivery_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def redeliver_a_delivery_for_an_app_webhook(self, delivery_id, params=None, payload=None):
        """
        Redeliver a delivery for an app webhook
        https://docs.github.com/rest/reference/apps#redeliver-a-delivery-for-an-app-webhook
        Attributes:
        Path Parameters:
        delivery_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/hook/deliveries/{delivery_id}/attempts"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_installations_for_the_authenticated_app(self, params=None, payload=None):
        """
        List installations for the authenticated app
        https://docs.github.com/rest/reference/apps#list-installations-for-the-authenticated-app
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
         since
         outdated
        """
        url = self._base_url + "/app/installations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_installation_for_the_authenticated_app(
        self, installation_id, params=None, payload=None
    ):
        """
        Get an installation for the authenticated app
        https://docs.github.com/rest/reference/apps#get-an-installation-for-the-authenticated-app
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/installations/{installation_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_installation_for_the_authenticated_app(
        self, installation_id, params=None, payload=None
    ):
        """
        Delete an installation for the authenticated app
        https://docs.github.com/rest/reference/apps#delete-an-installation-for-the-authenticated-app
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/installations/{installation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_an_installation_access_token_for_an_app(
        self, installation_id, params=None, payload=None
    ):
        """
        Create an installation access token for an app
        https://docs.github.com/rest/reference/apps/#create-an-installation-access-token-for-an-app
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/installations/{installation_id}/access_tokens"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def suspend_an_app_installation(self, installation_id, params=None, payload=None):
        """
        Suspend an app installation
        https://docs.github.com/rest/reference/apps#suspend-an-app-installation
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/installations/{installation_id}/suspended"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unsuspend_an_app_installation(self, installation_id, params=None, payload=None):
        """
        Unsuspend an app installation
        https://docs.github.com/rest/reference/apps#unsuspend-an-app-installation
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:

        """
        url = self._base_url + f"/app/installations/{installation_id}/suspended"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def delete_an_app_authorization(self, client_id, params=None, payload=None):
        """
        Delete an app authorization
        https://docs.github.com/rest/reference/apps#delete-an-app-authorization
        Attributes:
        Path Parameters:
        client_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/{client_id}/grant"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def check_a_token(self, client_id, params=None, payload=None):
        """
        Check a token
        https://docs.github.com/rest/reference/apps#check-a-token
        Attributes:
        Path Parameters:
        client_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/{client_id}/token"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def reset_a_token(self, client_id, params=None, payload=None):
        """
        Reset a token
        https://docs.github.com/rest/reference/apps#reset-a-token
        Attributes:
        Path Parameters:
        client_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/{client_id}/token"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_an_app_token(self, client_id, params=None, payload=None):
        """
        Delete an app token
        https://docs.github.com/rest/reference/apps#delete-an-app-token
        Attributes:
        Path Parameters:
        client_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/{client_id}/token"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def create_a_scoped_access_token(self, client_id, params=None, payload=None):
        """
        Create a scoped access token
        https://docs.github.com/rest/reference/apps#create-a-scoped-access-token
        Attributes:
        Path Parameters:
        client_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/{client_id}/token/scoped"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_app(self, app_slug, params=None, payload=None):
        """
        Get an app
        https://docs.github.com/rest/reference/apps/#get-an-app
        Attributes:
        Path Parameters:
        app_slug
        Payload Parameters:

        """
        url = self._base_url + f"/apps/{app_slug}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_accessible_to_the_app_installation(self, params=None, payload=None):
        """
        List repositories accessible to the app installation
        https://docs.github.com/rest/reference/apps#list-repositories-accessible-to-the-app-installation
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/installation/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def revoke_an_installation_access_token(self, params=None, payload=None):
        """
        Revoke an installation access token
        https://docs.github.com/rest/reference/apps#revoke-an-installation-access-token
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/installation/token"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_subscription_plan_for_an_account(self, account_id, params=None, payload=None):
        """
        Get a subscription plan for an account
        https://docs.github.com/rest/reference/apps#get-a-subscription-plan-for-an-account
        Attributes:
        Path Parameters:
        account_id
        Payload Parameters:

        """
        url = self._base_url + f"/marketplace_listing/accounts/{account_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_plans(self, params=None, payload=None):
        """
        List plans
        https://docs.github.com/rest/reference/apps#list-plans
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/marketplace_listing/plans"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_accounts_for_a_plan(self, plan_id, params=None, payload=None):
        """
        List accounts for a plan
        https://docs.github.com/rest/reference/apps#list-accounts-for-a-plan
        Attributes:
        Path Parameters:
        plan_id
        Payload Parameters:
        sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/marketplace_listing/plans/{plan_id}/accounts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_subscription_plan_for_an_account__stubbed(
        self, account_id, params=None, payload=None
    ):
        """
        Get a subscription plan for an account (stubbed)
        https://docs.github.com/rest/reference/apps#get-a-subscription-plan-for-an-account-stubbed
        Attributes:
        Path Parameters:
        account_id
        Payload Parameters:

        """
        url = self._base_url + f"/marketplace_listing/stubbed/accounts/{account_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_plans__stubbed(self, params=None, payload=None):
        """
        List plans (stubbed)
        https://docs.github.com/rest/reference/apps#list-plans-stubbed
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/marketplace_listing/stubbed/plans"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_accounts_for_a_plan__stubbed(self, plan_id, params=None, payload=None):
        """
        List accounts for a plan (stubbed)
        https://docs.github.com/rest/reference/apps#list-accounts-for-a-plan-stubbed
        Attributes:
        Path Parameters:
        plan_id
        Payload Parameters:
        sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/marketplace_listing/stubbed/plans/{plan_id}/accounts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_organization_installation_for_the_authenticated_app(
        self, org, params=None, payload=None
    ):
        """
        Get an organization installation for the authenticated app
        https://docs.github.com/rest/reference/apps#get-an-organization-installation-for-the-authenticated-app
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/installation"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_installation_for_the_authenticated_app(
        self, owner, repo, params=None, payload=None
    ):
        """
        Get a repository installation for the authenticated app
        https://docs.github.com/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/installation"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_app_installations_accessible_to_the_user_access_token(self, params=None, payload=None):
        """
        List app installations accessible to the user access token
        https://docs.github.com/rest/reference/apps#list-app-installations-accessible-to-the-user-access-token
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/installations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_accessible_to_the_user_access_token(
        self, installation_id, params=None, payload=None
    ):
        """
        List repositories accessible to the user access token
        https://docs.github.com/rest/reference/apps#list-repositories-accessible-to-the-user-access-token
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/user/installations/{installation_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_a_repository_to_an_app_installation(
        self, installation_id, repository_id, params=None, payload=None
    ):
        """
        Add a repository to an app installation
        https://docs.github.com/rest/reference/apps#add-a-repository-to-an-app-installation
        Attributes:
        Path Parameters:
        installation_id
        repository_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/installations/{installation_id}/repositories/{repository_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_from_an_app_installation(
        self, installation_id, repository_id, params=None, payload=None
    ):
        """
        Remove a repository from an app installation
        https://docs.github.com/rest/reference/apps#remove-a-repository-from-an-app-installation
        Attributes:
        Path Parameters:
        installation_id
        repository_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/installations/{installation_id}/repositories/{repository_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def search_user_repositories_related_to_integration_installation(
        self, installation_id, params=None, payload=None
    ):
        """
        Search user repositories related to integration installation
        https://docs.github.com/rest/reference/apps#search-user-repositories-related-to-integration
        Attributes:
        Path Parameters:
        installation_id
        Payload Parameters:
        q
         sort
         order
         per-page
         page
        """
        url = self._base_url + f"/user/installations/{installation_id}/search/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_subscriptions_for_the_authenticated_user(self, params=None, payload=None):
        """
        List subscriptions for the authenticated user
        https://docs.github.com/rest/reference/apps#list-subscriptions-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/marketplace_purchases"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_subscriptions_for_the_authenticated_user__stubbed(self, params=None, payload=None):
        """
        List subscriptions for the authenticated user (stubbed)
        https://docs.github.com/rest/reference/apps#list-subscriptions-for-the-authenticated-user-stubbed
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/marketplace_purchases/stubbed"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_user_installation_for_the_authenticated_app(
        self, username, params=None, payload=None
    ):
        """
        Get a user installation for the authenticated app
        https://docs.github.com/rest/reference/apps#get-a-user-installation-for-the-authenticated-app
        Attributes:
        Path Parameters:
        username
        Payload Parameters:

        """
        url = self._base_url + f"/users/{username}/installation"
        response = self._execute("get", url, params=params, payload=payload)
        return response
