"""
Manage access of OAuth applications
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class OauthAuthorizations:
    """
    Manage access of OAuth applications
    """

    def __init__(self, client):
        """
        Initializes the OauthAuthorizations class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_your_grants(self, params=None, payload=None):
        """
        Summary:
        List your grants
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#list-your-grants
        """
        url = self._base_url + "/applications/grants"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_single_grant(self, grant_id, params=None, payload=None):
        """
        Summary:
        Get a single grant
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#get-a-single-grant
        """
        url = self._base_url + f"/applications/grants/{grant_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_grant(self, grant_id, params=None, payload=None):
        """
        Summary:
        Delete a grant
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#delete-a-grant
        """
        url = self._base_url + f"/applications/grants/{grant_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_your_authorizations(self, params=None, payload=None):
        """
        Summary:
        List your authorizations
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#list-your-authorizations
        """
        url = self._base_url + "/authorizations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_new_authorization(self, params=None, payload=None):
        """
        Summary:
        Create a new authorization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#create-a-new-authorization
        """
        url = self._base_url + "/authorizations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_or_create_an_authorization_for_a_specific_app(self, params=None, payload=None):
        """
        Summary:
        Get-or-create an authorization for a specific app
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#get-or-create-an-authorization-for-a-specific-app
        """
        url = self._base_url + "/authorizations/clients/{client_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_or_create_an_authorization_for_a_specific_app_and_fingerprint(
        self, client_id, fingerprint, params=None, payload=None
    ):
        """
        Summary:
        Get-or-create an authorization for a specific app and fingerprint
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#get-or-create-an-authorization-for-a-specific-app-and-fingerprint
        """
        url = self._base_url + f"/authorizations/clients/{client_id}/{fingerprint}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_a_single_authorization(self, authorization_id, params=None, payload=None):
        """
        Summary:
        Get a single authorization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#get-a-single-authorization
        """
        url = self._base_url + f"/authorizations/{authorization_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_existing_authorization(self, authorization_id, params=None, payload=None):
        """
        Summary:
        Update an existing authorization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#update-an-existing-authorization
        """
        url = self._base_url + f"/authorizations/{authorization_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_an_authorization(self, authorization_id, params=None, payload=None):
        """
        Summary:
        Delete an authorization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/oauth-authorizations#delete-an-authorization
        """
        url = self._base_url + f"/authorizations/{authorization_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response
