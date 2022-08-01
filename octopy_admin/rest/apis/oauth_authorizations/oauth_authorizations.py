"""
Manage access of OAuth applications
"""


class OauthAuthorizations:
    """
    Manage access of OAuth applications
    """

    def __init__(self, client):
        """
        Initialize the OauthAuthorizations class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_your_grants(self, payload=None):
        """
        List your grants
        https://docs.github.com/rest/reference/oauth-authorizations#list-your-grants
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
         client_id
        """
        url = self._base_url + "/applications/grants"
        response = self._execute("get", url, payload)
        return response

    def get_a_single_grant(self, grant_id, payload=None):
        """
        Get a single grant
        https://docs.github.com/rest/reference/oauth-authorizations#get-a-single-grant
        Attributes:
        Path Parameters:
        grant_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/grants/{grant_id}"
        response = self._execute("get", url, payload)
        return response

    def delete_a_grant(self, grant_id, payload=None):
        """
        Delete a grant
        https://docs.github.com/rest/reference/oauth-authorizations#delete-a-grant
        Attributes:
        Path Parameters:
        grant_id
        Payload Parameters:

        """
        url = self._base_url + f"/applications/grants/{grant_id}"
        response = self._execute("delete", url, payload)
        return response

    def list_your_authorizations(self, payload=None):
        """
        List your authorizations
        https://docs.github.com/rest/reference/oauth-authorizations#list-your-authorizations
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
         client_id
        """
        url = self._base_url + "/authorizations"
        response = self._execute("get", url, payload)
        return response

    def create_a_new_authorization(self, payload=None):
        """
        Create a new authorization
        https://docs.github.com/rest/reference/oauth-authorizations#create-a-new-authorization
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/authorizations"
        response = self._execute("post", url, payload)
        return response

    def get_or_create_an_authorization_for_a_specific_app(self, client_id, payload=None):
        """
        Get-or-create an authorization for a specific app
        https://docs.github.com/rest/reference/oauth-authorizations#get-or-create-an-authorization-for-a-specific-app
        Attributes:
        Path Parameters:

        Payload Parameters:
        client_secret
        """
        url = self._base_url + f"/authorizations/clients/{client_id}"
        response = self._execute("put", url, payload)
        return response

    def get_or_create_an_authorization_for_a_specific_app_and_fingerprint(
        self, fingerprint, client_id, payload=None
    ):
        """
        Get-or-create an authorization for a specific app and fingerprint
        https://docs.github.com/rest/reference/oauth-authorizations#get-or-create-an-authorization-for-a-specific-app-and-fingerprint
        Attributes:
        Path Parameters:
        fingerprint
        client_id
        Payload Parameters:
        client_secret
        """
        url = self._base_url + f"/authorizations/clients/{client_id}/{fingerprint}"
        response = self._execute("put", url, payload)
        return response

    def get_a_single_authorization(self, authorization_id, payload=None):
        """
        Get a single authorization
        https://docs.github.com/rest/reference/oauth-authorizations#get-a-single-authorization
        Attributes:
        Path Parameters:
        authorization_id
        Payload Parameters:

        """
        url = self._base_url + f"/authorizations/{authorization_id}"
        response = self._execute("get", url, payload)
        return response

    def update_an_existing_authorization(self, authorization_id, payload=None):
        """
        Update an existing authorization
        https://docs.github.com/rest/reference/oauth-authorizations#update-an-existing-authorization
        Attributes:
        Path Parameters:
        authorization_id
        Payload Parameters:

        """
        url = self._base_url + f"/authorizations/{authorization_id}"
        response = self._execute("patch", url, payload)
        return response

    def delete_an_authorization(self, authorization_id, payload=None):
        """
        Delete an authorization
        https://docs.github.com/rest/reference/oauth-authorizations#delete-an-authorization
        Attributes:
        Path Parameters:
        authorization_id
        Payload Parameters:

        """
        url = self._base_url + f"/authorizations/{authorization_id}"
        response = self._execute("delete", url, payload)
        return response
