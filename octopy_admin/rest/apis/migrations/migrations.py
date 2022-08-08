"""
Move projects to or from GitHub.
"""


# pylint: disable=too-many-arguments
class Migrations:
    # pylint: disable=too-many-public-methods
    """
    Move projects to or from GitHub.
    """

    def __init__(self, client):
        """
        Initialize the Migrations class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_migrations(self, org, params=None, payload=None):
        """
        List organization migrations
        https://docs.github.com/rest/reference/migrations#list-organization-migrations
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
         exclude
        """
        url = self._base_url + f"/orgs/{org}/migrations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_an_organization_migration(self, org, params=None, payload=None):
        """
        Start an organization migration
        https://docs.github.com/rest/reference/migrations#start-an-organization-migration
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/migrations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_organization_migration_status(self, org, migration_id, params=None, payload=None):
        """
        Get an organization migration status
        https://docs.github.com/rest/reference/migrations#get-an-organization-migration-status
        Attributes:
        Path Parameters:
        org
        migration_id
        Payload Parameters:
        exclude
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_an_organization_migration_archive(
        self, org, migration_id, params=None, payload=None
    ):
        """
        Download an organization migration archive
        https://docs.github.com/rest/reference/migrations#download-an-organization-migration-archive
        Attributes:
        Path Parameters:
        org
        migration_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/archive"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_organization_migration_archive(
        self, org, migration_id, params=None, payload=None
    ):
        """
        Delete an organization migration archive
        https://docs.github.com/rest/reference/migrations#delete-an-organization-migration-archive
        Attributes:
        Path Parameters:
        org
        migration_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/archive"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def unlock_an_organization_repository(
        self, org, migration_id, repo_name, params=None, payload=None
    ):
        """
        Unlock an organization repository
        https://docs.github.com/rest/reference/migrations#unlock-an-organization-repository
        Attributes:
        Path Parameters:
        org
        migration_id
        repo_name
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_in_an_organization_migration(
        self, org, migration_id, params=None, payload=None
    ):
        """
        List repositories in an organization migration
        https://docs.github.com/rest/reference/migrations#list-repositories-in-an-organization-migration
        Attributes:
        Path Parameters:
        org
        migration_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/migrations/{migration_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_import_status(self, owner, repo, params=None, payload=None):
        """
        Get an import status
        https://docs.github.com/rest/reference/migrations#get-an-import-status
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_an_import(self, owner, repo, params=None, payload=None):
        """
        Start an import
        https://docs.github.com/rest/reference/migrations#start-an-import
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def update_an_import(self, owner, repo, params=None, payload=None):
        """
        Update an import
        https://docs.github.com/rest/reference/migrations#update-an-import
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def cancel_an_import(self, owner, repo, params=None, payload=None):
        """
        Cancel an import
        https://docs.github.com/rest/reference/migrations#cancel-an-import
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_commit_authors(self, owner, repo, params=None, payload=None):
        """
        Get commit authors
        https://docs.github.com/rest/reference/migrations#get-commit-authors
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        since-user
        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/authors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def map_a_commit_author(self, owner, repo, author_id, params=None, payload=None):
        """
        Map a commit author
        https://docs.github.com/rest/reference/migrations#map-a-commit-author
        Attributes:
        Path Parameters:
        owner
        repo
        author_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/authors/{author_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_large_files(self, owner, repo, params=None, payload=None):
        """
        Get large files
        https://docs.github.com/rest/reference/migrations#get-large-files
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/large_files"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_git_lfs_preference(self, owner, repo, params=None, payload=None):
        """
        Update Git LFS preference
        https://docs.github.com/rest/reference/migrations#update-git-lfs-preference
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/import/lfs"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_user_migrations(self, params=None, payload=None):
        """
        List user migrations
        https://docs.github.com/rest/reference/migrations#list-user-migrations
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/migrations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def start_a_user_migration(self, params=None, payload=None):
        """
        Start a user migration
        https://docs.github.com/rest/reference/migrations#start-a-user-migration
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/migrations"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_user_migration_status(self, migration_id, params=None, payload=None):
        """
        Get a user migration status
        https://docs.github.com/rest/reference/migrations#get-a-user-migration-status
        Attributes:
        Path Parameters:
        migration_id
        Payload Parameters:
        exclude
        """
        url = self._base_url + f"/user/migrations/{migration_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def download_a_user_migration_archive(self, migration_id, params=None, payload=None):
        """
        Download a user migration archive
        https://docs.github.com/rest/reference/migrations#download-a-user-migration-archive
        Attributes:
        Path Parameters:
        migration_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/migrations/{migration_id}/archive"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_user_migration_archive(self, migration_id, params=None, payload=None):
        """
        Delete a user migration archive
        https://docs.github.com/rest/reference/migrations#delete-a-user-migration-archive
        Attributes:
        Path Parameters:
        migration_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/migrations/{migration_id}/archive"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def unlock_a_user_repository(self, migration_id, repo_name, params=None, payload=None):
        """
        Unlock a user repository
        https://docs.github.com/rest/reference/migrations#unlock-a-user-repository
        Attributes:
        Path Parameters:
        migration_id
        repo_name
        Payload Parameters:

        """
        url = self._base_url + f"/user/migrations/{migration_id}/repos/{repo_name}/lock"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_for_a_user_migration(self, migration_id, params=None, payload=None):
        """
        List repositories for a user migration
        https://docs.github.com/rest/reference/migrations#list-repositories-for-a-user-migration
        Attributes:
        Path Parameters:
        migration_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/user/migrations/{migration_id}/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response
