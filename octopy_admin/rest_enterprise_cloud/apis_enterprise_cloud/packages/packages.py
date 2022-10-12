"""
Manage packages for authenticated users and organizations.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Packages:
    """
    Manage packages for authenticated users and organizations.
    """

    def __init__(self, client):
        """
        Initializes the Packages class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_packages_for_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List packages for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#list-packages-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/packages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_package_for_an_organization(
        self, package_type, package_name, org, params=None, payload=None
    ):
        """
        Summary:
        Get a package for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#get-a-package-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_package_for_an_organization(
        self, package_type, package_name, org, params=None, payload=None
    ):
        """
        Summary:
        Delete a package for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#delete-a-package-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def restore_a_package_for_an_organization(
        self, package_type, package_name, org, params=None, payload=None
    ):
        """
        Summary:
        Restore a package for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#restore-a-package-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}/restore"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_package_versions_for_a_package_owned_by_an_organization(
        self, package_type, package_name, org, params=None, payload=None
    ):
        """
        Summary:
        List package versions for a package owned by an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/packages#get-all-package-versions-for-a-package-owned-by-an-organization
        """
        url = self._base_url + f"/orgs/{org}/packages/{package_type}/{package_name}/versions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_package_version_for_an_organization(
        self,
        package_type,
        package_name,
        org,
        package_version_id,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Get a package version for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#get-a-package-version-for-an-organization
        """
        url = (
            self._base_url
            + f"/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_package_version_for_an_organization(
        self,
        package_type,
        package_name,
        org,
        package_version_id,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Delete package version for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#delete-a-package-version-for-an-organization
        """
        url = (
            self._base_url
            + f"/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def restore_package_version_for_an_organization(
        self,
        package_type,
        package_name,
        org,
        package_version_id,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Restore package version for an organization
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#restore-a-package-version-for-an-organization
        """
        url = (
            self._base_url
            + f"/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_packages_for_the_authenticated_users_namespace(self, params=None, payload=None):
        """
        Summary:
        List packages for the authenticated user's namespace
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#list-packages-for-the-authenticated-user
        """
        url = self._base_url + "/user/packages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_package_for_the_authenticated_user(
        self, package_type, package_name, params=None, payload=None
    ):
        """
        Summary:
        Get a package for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#get-a-package-for-the-authenticated-user
        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_package_for_the_authenticated_user(
        self, package_type, package_name, params=None, payload=None
    ):
        """
        Summary:
        Delete a package for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#delete-a-package-for-the-authenticated-user
        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def restore_a_package_for_the_authenticated_user(
        self, package_type, package_name, params=None, payload=None
    ):
        """
        Summary:
        Restore a package for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#restore-a-package-for-the-authenticated-user
        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}/restore"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_package_versions_for_a_package_owned_by_the_authenticated_user(
        self, package_type, package_name, params=None, payload=None
    ):
        """
        Summary:
        List package versions for a package owned by the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/packages#get-all-package-versions-for-a-package-owned-by-the-authenticated-user
        """
        url = self._base_url + f"/user/packages/{package_type}/{package_name}/versions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_package_version_for_the_authenticated_user(
        self, package_type, package_name, package_version_id, params=None, payload=None
    ):
        """
        Summary:
        Get a package version for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#get-a-package-version-for-the-authenticated-user
        """
        url = (
            self._base_url
            + f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_package_version_for_the_authenticated_user(
        self, package_type, package_name, package_version_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a package version for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#delete-a-package-version-for-the-authenticated-user
        """
        url = (
            self._base_url
            + f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def restore_a_package_version_for_the_authenticated_user(
        self, package_type, package_name, package_version_id, params=None, payload=None
    ):
        """
        Summary:
        Restore a package version for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#restore-a-package-version-for-the-authenticated-user
        """
        url = (
            self._base_url
            + f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_packages_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List packages for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#list-packages-for-user
        """
        url = self._base_url + f"/users/{username}/packages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_package_for_a_user(
        self, package_type, package_name, username, params=None, payload=None
    ):
        """
        Summary:
        Get a package for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#get-a-package-for-a-user
        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_package_for_a_user(
        self, package_type, package_name, username, params=None, payload=None
    ):
        """
        Summary:
        Delete a package for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#delete-a-package-for-a-user
        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def restore_a_package_for_a_user(
        self, package_type, package_name, username, params=None, payload=None
    ):
        """
        Summary:
        Restore a package for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#restore-a-package-for-a-user
        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}/restore"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_package_versions_for_a_package_owned_by_a_user(
        self, package_type, package_name, username, params=None, payload=None
    ):
        """
        Summary:
        List package versions for a package owned by a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/packages#get-all-package-versions-for-a-package-owned-by-a-user
        """
        url = self._base_url + f"/users/{username}/packages/{package_type}/{package_name}/versions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_package_version_for_a_user(
        self,
        package_type,
        package_name,
        package_version_id,
        username,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Get a package version for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#get-a-package-version-for-a-user
        """
        url = (
            self._base_url
            + f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_package_version_for_a_user(
        self,
        package_type,
        package_name,
        username,
        package_version_id,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Delete package version for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#delete-a-package-version-for-a-user
        """
        url = (
            self._base_url
            + f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def restore_package_version_for_a_user(
        self,
        package_type,
        package_name,
        username,
        package_version_id,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Restore package version for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/packages#restore-a-package-version-for-a-user
        """
        url = (
            self._base_url
            + f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response
