"""
Interact with and view information about users and also current user.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Users:
    """
    Interact with and view information about users and also current user.
    """

    def __init__(self, client):
        """
        Initializes the Users class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Get the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#get-the-authenticated-user
        """
        url = self._base_url + "/user"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Update the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users/#update-the-authenticated-user
        """
        url = self._base_url + "/user"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_users_blocked_by_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List users blocked by the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-users-blocked-by-the-authenticated-user
        """
        url = self._base_url + "/user/blocks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_is_blocked_by_the_authenticated_user(
        self, username, params=None, payload=None
    ):
        """
        Summary:
        Check if a user is blocked by the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#check-if-a-user-is-blocked-by-the-authenticated-user
        """
        url = self._base_url + f"/user/blocks/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def block_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Block a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#block-a-user
        """
        url = self._base_url + f"/user/blocks/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unblock_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Unblock a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#unblock-a-user
        """
        url = self._base_url + f"/user/blocks/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def set_primary_email_visibility_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Set primary email visibility for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#set-primary-email-visibility-for-the-authenticated-user
        """
        url = self._base_url + "/user/email/visibility"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_email_addresses_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List email addresses for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-email-addresses-for-the-authenticated-user
        """
        url = self._base_url + "/user/emails"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_an_email_address_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Add an email address for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#add-an-email-address-for-the-authenticated-user
        """
        url = self._base_url + "/user/emails"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_an_email_address_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Delete an email address for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#delete-an-email-address-for-the-authenticated-user
        """
        url = self._base_url + "/user/emails"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_followers_of_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List followers of the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-followers-of-the-authenticated-user
        """
        url = self._base_url + "/user/followers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_the_people_the_authenticated_user_follows(self, params=None, payload=None):
        """
        Summary:
        List the people the authenticated user follows
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-the-people-the-authenticated-user-follows
        """
        url = self._base_url + "/user/following"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_person_is_followed_by_the_authenticated_user(
        self, username, params=None, payload=None
    ):
        """
        Summary:
        Check if a person is followed by the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#check-if-a-person-is-followed-by-the-authenticated-user
        """
        url = self._base_url + f"/user/following/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def follow_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Follow a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#follow-a-user
        """
        url = self._base_url + f"/user/following/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unfollow_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Unfollow a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#unfollow-a-user
        """
        url = self._base_url + f"/user/following/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_gpg_keys_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List GPG keys for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-gpg-keys-for-the-authenticated-user
        """
        url = self._base_url + "/user/gpg_keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_gpg_key_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Create a GPG key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#create-a-gpg-key-for-the-authenticated-user
        """
        url = self._base_url + "/user/gpg_keys"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_gpg_key_for_the_authenticated_user(self, gpg_key_id, params=None, payload=None):
        """
        Summary:
        Get a GPG key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#get-a-gpg-key-for-the-authenticated-user
        """
        url = self._base_url + f"/user/gpg_keys/{gpg_key_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_gpg_key_for_the_authenticated_user(self, gpg_key_id, params=None, payload=None):
        """
        Summary:
        Delete a GPG key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#delete-a-gpg-key-for-the-authenticated-user
        """
        url = self._base_url + f"/user/gpg_keys/{gpg_key_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_public_ssh_keys_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List public SSH keys for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-public-ssh-keys-for-the-authenticated-user
        """
        url = self._base_url + "/user/keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_public_ssh_key_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Create a public SSH key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#create-a-public-ssh-key-for-the-authenticated-user
        """
        url = self._base_url + "/user/keys"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_public_ssh_key_for_the_authenticated_user(self, key_id, params=None, payload=None):
        """
        Summary:
        Get a public SSH key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#get-a-public-ssh-key-for-the-authenticated-user
        """
        url = self._base_url + f"/user/keys/{key_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_public_ssh_key_for_the_authenticated_user(self, key_id, params=None, payload=None):
        """
        Summary:
        Delete a public SSH key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#delete-a-public-ssh-key-for-the-authenticated-user
        """
        url = self._base_url + f"/user/keys/{key_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_public_email_addresses_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List public email addresses for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-public-email-addresses-for-the-authenticated-user
        """
        url = self._base_url + "/user/public_emails"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_ssh_signing_keys_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List SSH signing keys for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-public-ssh-signing-keys-for-the-authenticated-user
        """
        url = self._base_url + "/user/ssh_signing_keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_ssh_signing_key_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Create a SSH signing key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#create-an-ssh-signing-key-for-the-authenticated-user
        """
        url = self._base_url + "/user/ssh_signing_keys"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_ssh_signing_key_for_the_authenticated_user(
        self, ssh_signing_key_id, params=None, payload=None
    ):
        """
        Summary:
        Get an SSH signing key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#get-a-ssh-signing-key-for-the-authenticated-user
        """
        url = self._base_url + f"/user/ssh_signing_keys/{ssh_signing_key_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_ssh_signing_key_for_the_authenticated_user(
        self, ssh_signing_key_id, params=None, payload=None
    ):
        """
        Summary:
        Delete an SSH signing key for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#delete-a-ssh-signing-key-for-the-authenticated-user
        """
        url = self._base_url + f"/user/ssh_signing_keys/{ssh_signing_key_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_users(self, params=None, payload=None):
        """
        Summary:
        List users
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-users
        """
        url = self._base_url + "/users"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Get a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#get-a-user
        """
        url = self._base_url + f"/users/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_followers_of_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List followers of a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-followers-of-a-user
        """
        url = self._base_url + f"/users/{username}/followers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_the_people_a_user_follows(self, username, params=None, payload=None):
        """
        Summary:
        List the people a user follows
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-the-people-a-user-follows
        """
        url = self._base_url + f"/users/{username}/following"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_follows_another_user(
        self, username, target_user, params=None, payload=None
    ):
        """
        Summary:
        Check if a user follows another user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#check-if-a-user-follows-another-user
        """
        url = self._base_url + f"/users/{username}/following/{target_user}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_gpg_keys_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List GPG keys for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-gpg-keys-for-a-user
        """
        url = self._base_url + f"/users/{username}/gpg_keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_contextual_information_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        Get contextual information for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#get-contextual-information-for-a-user
        """
        url = self._base_url + f"/users/{username}/hovercard"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_keys_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List public keys for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-public-keys-for-a-user
        """
        url = self._base_url + f"/users/{username}/keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_ssh_signing_keys_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List SSH signing keys for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/users#list-ssh-signing-keys-for-a-user
        """
        url = self._base_url + f"/users/{username}/ssh_signing_keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response
