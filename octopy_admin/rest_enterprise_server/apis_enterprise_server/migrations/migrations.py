"""
Move projects to or from GitHub.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Migrations:
    """
    Move projects to or from GitHub.
    """

    def __init__(self, client):
        """
        Initializes the Migrations class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_migrations(self, org, params=None, payload=None):
        """
        Summary:
        List organization migrations
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#list-organization-migrations
        """
        url = self._base_url + f"/orgs/{org}/migrations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_an_organization_migration(self, org, params=None, payload=None):
        """
        Summary:
        Start an organization migration
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#start-an-organization-migration
        """
        url = self._base_url + f"/orgs/{org}/migrations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_organization_migration_status(self, org, migration_id, params=None, payload=None):
        """
        Summary:
        Get an organization migration status
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#get-an-organization-migration-status
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_user_migrations(self, params=None, payload=None):
        """
        Summary:
        List user migrations
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#list-user-migrations
        """
        url = self._base_url + "/user/migrations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_a_user_migration(self, params=None, payload=None):
        """
        Summary:
        Start a user migration
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#start-a-user-migration
        """
        url = self._base_url + "/user/migrations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def download_a_user_migration_archive(self, migration_id, params=None, payload=None):
        """
        Summary:
        Download a user migration archive
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#download-a-user-migration-archive
        """
        url = self._base_url + f"/user/migrations/{migration_id}/archive"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_for_a_user_migration(self, migration_id, params=None, payload=None):
        """
        Summary:
        List repositories for a user migration
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/migrations#list-repositories-for-a-user-migration
        """
        url = self._base_url + f"/user/migrations/{migration_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response
