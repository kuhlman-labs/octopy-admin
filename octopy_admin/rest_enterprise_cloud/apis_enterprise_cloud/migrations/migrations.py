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
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#list-organization-migrations
        """
        url = self._base_url + f"/orgs/{org}/migrations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_an_organization_migration(self, org, params=None, payload=None):
        """
        Summary:
        Start an organization migration
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#start-an-organization-migration
        """
        url = self._base_url + f"/orgs/{org}/migrations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_organization_migration_status(self, org, migration_id, params=None, payload=None):
        """
        Summary:
        Get an organization migration status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#get-an-organization-migration-status
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_an_organization_migration_archive(
        self, org, migration_id, params=None, payload=None
    ):
        """
        Summary:
        Download an organization migration archive
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#download-an-organization-migration-archive
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/archive"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_organization_migration_archive(
        self, org, migration_id, params=None, payload=None
    ):
        """
        Summary:
        Delete an organization migration archive
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#delete-an-organization-migration-archive
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/archive"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def unlock_an_organization_repository(
        self, org, migration_id, repo_name, params=None, payload=None
    ):
        """
        Summary:
        Unlock an organization repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#unlock-an-organization-repository
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_in_an_organization_migration(
        self, org, migration_id, params=None, payload=None
    ):
        """
        Summary:
        List repositories in an organization migration
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#list-repositories-in-an-organization-migration
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_import_status(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get an import status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#get-an-import-status
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_an_import(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Start an import
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#start-an-import
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_import(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Update an import
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#update-an-import
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def cancel_an_import(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Cancel an import
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#cancel-an-import
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_commit_authors(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get commit authors
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#get-commit-authors
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/authors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def map_a_commit_author(self, owner, repo, author_id, params=None, payload=None):
        """
        Summary:
        Map a commit author
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#map-a-commit-author
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/authors/{author_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_large_files(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get large files
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#get-large-files
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/large_files"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_git_lfs_preference(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Update Git LFS preference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#update-git-lfs-preference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/lfs"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_user_migrations(self, params=None, payload=None):
        """
        Summary:
        List user migrations
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#list-user-migrations
        """
        url = self._base_url + "/user/migrations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_a_user_migration(self, params=None, payload=None):
        """
        Summary:
        Start a user migration
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#start-a-user-migration
        """
        url = self._base_url + "/user/migrations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_user_migration_status(self, migration_id, params=None, payload=None):
        """
        Summary:
        Get a user migration status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#get-a-user-migration-status
        """
        url = self._base_url + f"/user/migrations/{migration_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_a_user_migration_archive(self, migration_id, params=None, payload=None):
        """
        Summary:
        Download a user migration archive
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#download-a-user-migration-archive
        """
        url = self._base_url + f"/user/migrations/{migration_id}/archive"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_user_migration_archive(self, migration_id, params=None, payload=None):
        """
        Summary:
        Delete a user migration archive
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#delete-a-user-migration-archive
        """
        url = self._base_url + f"/user/migrations/{migration_id}/archive"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def unlock_a_user_repository(self, migration_id, repo_name, params=None, payload=None):
        """
        Summary:
        Unlock a user repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#unlock-a-user-repository
        """
        url = self._base_url + f"/user/migrations/{migration_id}/repos/{repo_name}/lock"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_for_a_user_migration(self, migration_id, params=None, payload=None):
        """
        Summary:
        List repositories for a user migration
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/migrations#list-repositories-for-a-user-migration
        """
        url = self._base_url + f"/user/migrations/{migration_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response
