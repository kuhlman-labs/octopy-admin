"""
Interact with GitHub Repos.
"""


# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines
class Repos:
    # pylint: disable=too-many-public-methods
    """
    Interact with GitHub Repos.
    """

    def __init__(self, client):
        """
        Initialize the Repos class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_repositories(self, org, params=None, payload=None):
        """
        List organization repositories
        https://docs.github.com/rest/reference/repos#list-organization-repositories
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        type
         sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_repository(self, org, params=None, payload=None):
        """
        Create an organization repository
        https://docs.github.com/rest/reference/repos#create-an-organization-repository
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/repos"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_repository(self, owner, repo, params=None, payload=None):
        """
        Get a repository
        https://docs.github.com/rest/reference/repos#get-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_repository(self, owner, repo, params=None, payload=None):
        """
        Update a repository
        https://docs.github.com/rest/reference/repos/#update-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_repository(self, owner, repo, params=None, payload=None):
        """
        Delete a repository
        https://docs.github.com/rest/reference/repos#delete-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_all_autolinks_of_a_repository(self, owner, repo, params=None, payload=None):
        """
        List all autolinks of a repository
        https://docs.github.com/v3/repos#list-autolinks
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_autolink_reference_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Create an autolink reference for a repository
        https://docs.github.com/v3/repos#create-an-autolink
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_autolink_reference_of_a_repository(
        self, owner, repo, autolink_id, params=None, payload=None
    ):
        """
        Get an autolink reference of a repository
        https://docs.github.com/v3/repos#get-autolink
        Attributes:
        Path Parameters:
        owner
        repo
        autolink_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks/{autolink_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_autolink_reference_from_a_repository(
        self, owner, repo, autolink_id, params=None, payload=None
    ):
        """
        Delete an autolink reference from a repository
        https://docs.github.com/v3/repos#delete-autolink
        Attributes:
        Path Parameters:
        owner
        repo
        autolink_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks/{autolink_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def enable_automated_security_fixes(self, owner, repo, params=None, payload=None):
        """
        Enable automated security fixes
        https://docs.github.com/rest/reference/repos#enable-automated-security-fixes
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/automated-security-fixes"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_automated_security_fixes(self, owner, repo, params=None, payload=None):
        """
        Disable automated security fixes
        https://docs.github.com/rest/reference/repos#disable-automated-security-fixes
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/automated-security-fixes"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_branches(self, owner, repo, params=None, payload=None):
        """
        List branches
        https://docs.github.com/rest/reference/repos#list-branches
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        protected
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_branch(self, owner, repo, branch, params=None, payload=None):
        """
        Get a branch
        https://docs.github.com/rest/reference/repos#get-a-branch
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Get branch protection
        https://docs.github.com/rest/reference/repos#get-branch-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Update branch protection
        https://docs.github.com/rest/reference/repos#update-branch-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Delete branch protection
        https://docs.github.com/rest/reference/repos#delete-branch-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_admin_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Get admin branch protection
        https://docs.github.com/rest/reference/repos#get-admin-branch-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_admin_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Set admin branch protection
        https://docs.github.com/rest/reference/repos#set-admin-branch-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_admin_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Delete admin branch protection
        https://docs.github.com/rest/reference/repos#delete-admin-branch-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_pull_request_review_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Get pull request review protection
        https://docs.github.com/rest/reference/repos#get-pull-request-review-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_pull_request_review_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Update pull request review protection
        https://docs.github.com/rest/reference/repos#update-pull-request-review-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_pull_request_review_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Delete pull request review protection
        https://docs.github.com/rest/reference/repos#delete-pull-request-review-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_commit_signature_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Get commit signature protection
        https://docs.github.com/rest/reference/repos#get-commit-signature-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_commit_signature_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Create commit signature protection
        https://docs.github.com/rest/reference/repos#create-commit-signature-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_commit_signature_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Delete commit signature protection
        https://docs.github.com/rest/reference/repos#delete-commit-signature-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_status_checks_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Get status checks protection
        https://docs.github.com/rest/reference/repos#get-status-checks-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_status_check_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Update status check protection
        https://docs.github.com/rest/reference/repos#update-status-check-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_status_check_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Remove status check protection
        https://docs.github.com/rest/reference/repos#remove-status-check-protection
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_all_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Get all status check contexts
        https://docs.github.com/rest/reference/repos#get-all-status-check-contexts
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Add status check contexts
        https://docs.github.com/rest/reference/repos#add-status-check-contexts
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Set status check contexts
        https://docs.github.com/rest/reference/repos#set-status-check-contexts
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Remove status check contexts
        https://docs.github.com/rest/reference/repos#remove-status-check-contexts
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Get access restrictions
        https://docs.github.com/rest/reference/repos#get-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Delete access restrictions
        https://docs.github.com/rest/reference/repos#delete-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_apps_with_access_to_the_protected_branch(
        self, owner, repo, branch, params=None, payload=None
    ):
        """
        Get apps with access to the protected branch
        https://docs.github.com/rest/reference/repos#list-apps-with-access-to-the-protected-branch
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_app_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Add app access restrictions
        https://docs.github.com/rest/reference/repos#add-app-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_app_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Set app access restrictions
        https://docs.github.com/rest/reference/repos#set-app-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_app_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Remove app access restrictions
        https://docs.github.com/rest/reference/repos#remove-app-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_teams_with_access_to_the_protected_branch(
        self, owner, repo, branch, params=None, payload=None
    ):
        """
        Get teams with access to the protected branch
        https://docs.github.com/rest/reference/repos#list-teams-with-access-to-the-protected-branch
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_team_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Add team access restrictions
        https://docs.github.com/rest/reference/repos#add-team-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_team_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Set team access restrictions
        https://docs.github.com/rest/reference/repos#set-team-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Remove team access restrictions
        https://docs.github.com/rest/reference/repos#remove-team-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_users_with_access_to_the_protected_branch(
        self, owner, repo, branch, params=None, payload=None
    ):
        """
        Get users with access to the protected branch
        https://docs.github.com/rest/reference/repos#list-users-with-access-to-the-protected-branch
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_user_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Add user access restrictions
        https://docs.github.com/rest/reference/repos#add-user-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_user_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Set user access restrictions
        https://docs.github.com/rest/reference/repos#set-user-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_user_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Remove user access restrictions
        https://docs.github.com/rest/reference/repos#remove-user-access-restrictions
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def rename_a_branch(self, owner, repo, branch, params=None, payload=None):
        """
        Rename a branch
        https://docs.github.com/rest/reference/repos#rename-a-branch
        Attributes:
        Path Parameters:
        owner
        repo
        branch
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/rename"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_codeowners_errors(self, owner, repo, params=None, payload=None):
        """
        List CODEOWNERS errors
        https://docs.github.com/rest/reference/repos#list-codeowners-errors
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        ref
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codeowners/errors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_collaborators(self, owner, repo, params=None, payload=None):
        """
        List repository collaborators
        https://docs.github.com/rest/reference/repos#list-repository-collaborators
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        affiliation
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_is_a_repository_collaborator(
        self, owner, repo, username, params=None, payload=None
    ):
        """
        Check if a user is a repository collaborator
        https://docs.github.com/rest/reference/repos#check-if-a-user-is-a-repository-collaborator
        Attributes:
        Path Parameters:
        owner
        repo
        username
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_a_repository_collaborator(self, owner, repo, username, params=None, payload=None):
        """
        Add a repository collaborator
        https://docs.github.com/rest/reference/repos#add-a-repository-collaborator
        Attributes:
        Path Parameters:
        owner
        repo
        username
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_collaborator(self, owner, repo, username, params=None, payload=None):
        """
        Remove a repository collaborator
        https://docs.github.com/rest/reference/repos#remove-a-repository-collaborator
        Attributes:
        Path Parameters:
        owner
        repo
        username
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_repository_permissions_for_a_user(
        self, owner, repo, username, params=None, payload=None
    ):
        """
        Get repository permissions for a user
        https://docs.github.com/rest/reference/repos#get-repository-permissions-for-a-user
        Attributes:
        Path Parameters:
        owner
        repo
        username
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}/permission"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_commit_comments_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List commit comments for a repository
        https://docs.github.com/rest/reference/repos#list-commit-comments-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_commit_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Get a commit comment
        https://docs.github.com/rest/reference/repos#get-a-commit-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_commit_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Update a commit comment
        https://docs.github.com/rest/reference/repos#update-a-commit-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_commit_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Delete a commit comment
        https://docs.github.com/rest/reference/repos#delete-a-commit-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_commits(self, owner, repo, params=None, payload=None):
        """
        List commits
        https://docs.github.com/rest/reference/repos#list-commits
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        sha
         path
         author
         since
         until
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_branches_for_head_commit(self, owner, repo, commit_sha, params=None, payload=None):
        """
        List branches for HEAD commit
        https://docs.github.com/rest/reference/repos#list-branches-for-head-commit
        Attributes:
        Path Parameters:
        owner
        repo
        commit_sha
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_commit_comments(self, owner, repo, commit_sha, params=None, payload=None):
        """
        List commit comments
        https://docs.github.com/rest/reference/repos#list-commit-comments
        Attributes:
        Path Parameters:
        owner
        repo
        commit_sha
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_commit_comment(self, owner, repo, commit_sha, params=None, payload=None):
        """
        Create a commit comment
        https://docs.github.com/rest/reference/repos#create-a-commit-comment
        Attributes:
        Path Parameters:
        owner
        repo
        commit_sha
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_pull_requests_associated_with_a_commit(
        self, owner, repo, commit_sha, params=None, payload=None
    ):
        """
        List pull requests associated with a commit
        https://docs.github.com/rest/reference/repos#list-pull-requests-associated-with-a-commit
        Attributes:
        Path Parameters:
        owner
        repo
        commit_sha
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_commit(self, owner, repo, ref, params=None, payload=None):
        """
        Get a commit
        https://docs.github.com/rest/reference/repos#get-a-commit
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:
        page
         per-page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_combined_status_for_a_specific_reference(
        self, owner, repo, ref, params=None, payload=None
    ):
        """
        Get the combined status for a specific reference
        https://docs.github.com/rest/reference/repos#get-the-combined-status-for-a-specific-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/status"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_commit_statuses_for_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        List commit statuses for a reference
        https://docs.github.com/rest/reference/repos#list-commit-statuses-for-a-reference
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/statuses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_community_profile_metrics(self, owner, repo, params=None, payload=None):
        """
        Get community profile metrics
        https://docs.github.com/rest/reference/repos#get-community-profile-metrics
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/community/profile"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def compare_two_commits(self, owner, repo, basehead, params=None, payload=None):
        """
        Compare two commits
        https://docs.github.com/rest/reference/repos#compare-two-commits
        Attributes:
        Path Parameters:
        owner
        repo
        basehead
        Payload Parameters:
        page
         per-page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/compare/{basehead}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_repository_content(self, owner, repo, path, params=None, payload=None):
        """
        Get repository content
        https://docs.github.com/rest/reference/repos#get-repository-content
        Attributes:
        Path Parameters:
        owner
        repo
        path
        Payload Parameters:
        ref
        """
        url = self._base_url + f"/repos/{owner}/{repo}/contents/{path}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_file_contents(self, owner, repo, path, params=None, payload=None):
        """
        Create or update file contents
        https://docs.github.com/rest/reference/repos#create-or-update-file-contents
        Attributes:
        Path Parameters:
        owner
        repo
        path
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/contents/{path}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_file(self, owner, repo, path, params=None, payload=None):
        """
        Delete a file
        https://docs.github.com/rest/reference/repos#delete-a-file
        Attributes:
        Path Parameters:
        owner
        repo
        path
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/contents/{path}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_contributors(self, owner, repo, params=None, payload=None):
        """
        List repository contributors
        https://docs.github.com/rest/reference/repos#list-repository-contributors
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        anon
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/contributors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_deployments(self, owner, repo, params=None, payload=None):
        """
        List deployments
        https://docs.github.com/rest/reference/repos#list-deployments
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        sha
         ref
         task
         environment
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deployment(self, owner, repo, params=None, payload=None):
        """
        Create a deployment
        https://docs.github.com/rest/reference/repos#create-a-deployment
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deployment(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Get a deployment
        https://docs.github.com/rest/reference/repos#get-a-deployment
        Attributes:
        Path Parameters:
        owner
        repo
        deployment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_deployment(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Delete a deployment
        https://docs.github.com/rest/reference/repos#delete-a-deployment
        Attributes:
        Path Parameters:
        owner
        repo
        deployment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_deployment_statuses(self, owner, repo, deployment_id, params=None, payload=None):
        """
        List deployment statuses
        https://docs.github.com/rest/reference/repos#list-deployment-statuses
        Attributes:
        Path Parameters:
        owner
        repo
        deployment_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deployment_status(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Create a deployment status
        https://docs.github.com/rest/reference/repos#create-a-deployment-status
        Attributes:
        Path Parameters:
        owner
        repo
        deployment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deployment_status(
        self, owner, repo, deployment_id, status_id, params=None, payload=None
    ):
        """
        Get a deployment status
        https://docs.github.com/rest/reference/repos#get-a-deployment-status
        Attributes:
        Path Parameters:
        owner
        repo
        deployment_id
        status_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_dispatch_event(self, owner, repo, params=None, payload=None):
        """
        Create a repository dispatch event
        https://docs.github.com/rest/reference/repos#create-a-repository-dispatch-event
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/dispatches"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_all_environments(self, owner, repo, params=None, payload=None):
        """
        Get all environments
        https://docs.github.com/rest/reference/repos#get-all-environments
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_environment(self, owner, repo, environment_name, params=None, payload=None):
        """
        Get an environment
        https://docs.github.com/rest/reference/repos#get-an-environment
        Attributes:
        Path Parameters:
        owner
        repo
        environment_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments/{environment_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_environment(
        self, owner, repo, environment_name, params=None, payload=None
    ):
        """
        Create or update an environment
        https://docs.github.com/rest/reference/repos#create-or-update-an-environment
        Attributes:
        Path Parameters:
        owner
        repo
        environment_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments/{environment_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_environment(self, owner, repo, environment_name, params=None, payload=None):
        """
        Delete an environment
        https://docs.github.com/rest/reference/repos#delete-an-environment
        Attributes:
        Path Parameters:
        owner
        repo
        environment_name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments/{environment_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_forks(self, owner, repo, params=None, payload=None):
        """
        List forks
        https://docs.github.com/rest/reference/repos#list-forks
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        sort
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/forks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_fork(self, owner, repo, params=None, payload=None):
        """
        Create a fork
        https://docs.github.com/rest/reference/repos#create-a-fork
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/forks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_webhooks(self, owner, repo, params=None, payload=None):
        """
        List repository webhooks
        https://docs.github.com/rest/reference/repos#list-repository-webhooks
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_webhook(self, owner, repo, params=None, payload=None):
        """
        Create a repository webhook
        https://docs.github.com/rest/reference/repos#create-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Get a repository webhook
        https://docs.github.com/rest/reference/repos#get-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Update a repository webhook
        https://docs.github.com/rest/reference/repos#update-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Delete a repository webhook
        https://docs.github.com/rest/reference/repos#delete-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_webhook_configuration_for_a_repository(
        self, owner, repo, hook_id, params=None, payload=None
    ):
        """
        Get a webhook configuration for a repository
        https://docs.github.com/rest/reference/repos#get-a-webhook-configuration-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/config"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_webhook_configuration_for_a_repository(
        self, owner, repo, hook_id, params=None, payload=None
    ):
        """
        Update a webhook configuration for a repository
        https://docs.github.com/rest/reference/repos#update-a-webhook-configuration-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/config"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_deliveries_for_a_repository_webhook(
        self, owner, repo, hook_id, params=None, payload=None
    ):
        """
        List deliveries for a repository webhook
        https://docs.github.com/rest/reference/repos#list-deliveries-for-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:
        per-page
         cursor
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_delivery_for_a_repository_webhook(
        self, owner, repo, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Get a delivery for a repository webhook
        https://docs.github.com/rest/reference/repos#get-a-delivery-for-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        delivery_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def redeliver_a_delivery_for_a_repository_webhook(
        self, owner, repo, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Redeliver a delivery for a repository webhook
        https://docs.github.com/rest/reference/repos#redeliver-a-delivery-for-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        delivery_id
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def ping_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Ping a repository webhook
        https://docs.github.com/rest/reference/repos#ping-a-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/pings"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def test_the_push_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Test the push repository webhook
        https://docs.github.com/rest/reference/repos#test-the-push-repository-webhook
        Attributes:
        Path Parameters:
        owner
        repo
        hook_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/tests"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_invitations(self, owner, repo, params=None, payload=None):
        """
        List repository invitations
        https://docs.github.com/rest/reference/repos#list-repository-invitations
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_repository_invitation(self, owner, repo, invitation_id, params=None, payload=None):
        """
        Update a repository invitation
        https://docs.github.com/rest/reference/repos#update-a-repository-invitation
        Attributes:
        Path Parameters:
        owner
        repo
        invitation_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/invitations/{invitation_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_repository_invitation(self, owner, repo, invitation_id, params=None, payload=None):
        """
        Delete a repository invitation
        https://docs.github.com/rest/reference/repos#delete-a-repository-invitation
        Attributes:
        Path Parameters:
        owner
        repo
        invitation_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/invitations/{invitation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_deploy_keys(self, owner, repo, params=None, payload=None):
        """
        List deploy keys
        https://docs.github.com/rest/reference/repos#list-deploy-keys
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deploy_key(self, owner, repo, params=None, payload=None):
        """
        Create a deploy key
        https://docs.github.com/rest/reference/repos#create-a-deploy-key
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deploy_key(self, owner, repo, key_id, params=None, payload=None):
        """
        Get a deploy key
        https://docs.github.com/rest/reference/repos#get-a-deploy-key
        Attributes:
        Path Parameters:
        owner
        repo
        key_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys/{key_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_deploy_key(self, owner, repo, key_id, params=None, payload=None):
        """
        Delete a deploy key
        https://docs.github.com/rest/reference/repos#delete-a-deploy-key
        Attributes:
        Path Parameters:
        owner
        repo
        key_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys/{key_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_languages(self, owner, repo, params=None, payload=None):
        """
        List repository languages
        https://docs.github.com/rest/reference/repos#list-repository-languages
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/languages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def enable_git_lfs_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Enable Git LFS for a repository
        https://docs.github.com/rest/reference/repos#enable-git-lfs-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/lfs"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_git_lfs_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Disable Git LFS for a repository
        https://docs.github.com/rest/reference/repos#disable-git-lfs-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/lfs"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def sync_a_fork_branch_with_the_upstream_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Sync a fork branch with the upstream repository
        https://docs.github.com/rest/reference/repos#sync-a-fork-branch-with-the-upstream-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/merge-upstream"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def merge_a_branch(self, owner, repo, params=None, payload=None):
        """
        Merge a branch
        https://docs.github.com/rest/reference/repos#merge-a-branch
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/merges"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_github_pages_site(self, owner, repo, params=None, payload=None):
        """
        Get a GitHub Pages site
        https://docs.github.com/rest/reference/repos#get-a-github-pages-site
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_github_pages_site(self, owner, repo, params=None, payload=None):
        """
        Create a GitHub Pages site
        https://docs.github.com/rest/reference/repos#create-a-github-pages-site
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_information_about_a_github_pages_site(self, owner, repo, params=None, payload=None):
        """
        Update information about a GitHub Pages site
        https://docs.github.com/rest/reference/repos#update-information-about-a-github-pages-site
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_github_pages_site(self, owner, repo, params=None, payload=None):
        """
        Delete a GitHub Pages site
        https://docs.github.com/rest/reference/repos#delete-a-github-pages-site
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_github_pages_builds(self, owner, repo, params=None, payload=None):
        """
        List GitHub Pages builds
        https://docs.github.com/rest/reference/repos#list-github-pages-builds
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def request_a_github_pages_build(self, owner, repo, params=None, payload=None):
        """
        Request a GitHub Pages build
        https://docs.github.com/rest/reference/repos#request-a-github-pages-build
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_latest_pages_build(self, owner, repo, params=None, payload=None):
        """
        Get latest Pages build
        https://docs.github.com/rest/reference/repos#get-latest-pages-build
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds/latest"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_pages_build(self, owner, repo, build_id, params=None, payload=None):
        """
        Get GitHub Pages build
        https://docs.github.com/rest/reference/repos#get-github-pages-build
        Attributes:
        Path Parameters:
        owner
        repo
        build_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds/{build_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_github_pages_deployment(self, owner, repo, params=None, payload=None):
        """
        Create a GitHub Pages deployment
        https://docs.github.com/rest/reference/repos#create-a-github-pages-deployment
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/deployment"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_dns_health_check_for_github_pages(self, owner, repo, params=None, payload=None):
        """
        Get a DNS health check for GitHub Pages
        https://docs.github.com/rest/reference/repos#get-a-dns-health-check-for-github-pages
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/health"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_readme(self, owner, repo, params=None, payload=None):
        """
        Get a repository README
        https://docs.github.com/rest/reference/repos#get-a-repository-readme
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        ref
        """
        url = self._base_url + f"/repos/{owner}/{repo}/readme"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_readme_for_a_directory(
        self, owner, repo, directory, params=None, payload=None
    ):
        """
        Get a repository README for a directory
        https://docs.github.com/rest/reference/repos#get-a-repository-directory-readme
        Attributes:
        Path Parameters:
        owner
        repo
        directory
        Payload Parameters:
        ref
        """
        url = self._base_url + f"/repos/{owner}/{repo}/readme/{directory}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_releases(self, owner, repo, params=None, payload=None):
        """
        List releases
        https://docs.github.com/rest/reference/repos#list-releases
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_release(self, owner, repo, params=None, payload=None):
        """
        Create a release
        https://docs.github.com/rest/reference/repos#create-a-release
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_release_asset(self, owner, repo, asset_id, params=None, payload=None):
        """
        Get a release asset
        https://docs.github.com/rest/reference/repos#get-a-release-asset
        Attributes:
        Path Parameters:
        owner
        repo
        asset_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_release_asset(self, owner, repo, asset_id, params=None, payload=None):
        """
        Update a release asset
        https://docs.github.com/rest/reference/repos#update-a-release-asset
        Attributes:
        Path Parameters:
        owner
        repo
        asset_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_release_asset(self, owner, repo, asset_id, params=None, payload=None):
        """
        Delete a release asset
        https://docs.github.com/rest/reference/repos#delete-a-release-asset
        Attributes:
        Path Parameters:
        owner
        repo
        asset_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def generate_release_notes_content_for_a_release(self, owner, repo, params=None, payload=None):
        """
        Generate release notes content for a release
        https://docs.github.com/rest/reference/repos#generate-release-notes
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/generate-notes"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_latest_release(self, owner, repo, params=None, payload=None):
        """
        Get the latest release
        https://docs.github.com/rest/reference/repos#get-the-latest-release
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/latest"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_release_by_tag_name(self, owner, repo, tag, params=None, payload=None):
        """
        Get a release by tag name
        https://docs.github.com/rest/reference/repos#get-a-release-by-tag-name
        Attributes:
        Path Parameters:
        owner
        repo
        tag
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/tags/{tag}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Get a release
        https://docs.github.com/rest/reference/repos#get-a-release
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Update a release
        https://docs.github.com/rest/reference/repos#update-a-release
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Delete a release
        https://docs.github.com/rest/reference/repos#delete-a-release
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_release_assets(self, owner, repo, release_id, params=None, payload=None):
        """
        List release assets
        https://docs.github.com/rest/reference/repos#list-release-assets
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/assets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def upload_a_release_asset(self, owner, repo, release_id, params=None, payload=None):
        """
        Upload a release asset
        https://docs.github.com/rest/reference/repos#upload-a-release-asset
        Attributes:
        Path Parameters:
        owner
        repo
        release_id
        Payload Parameters:
        name
         label
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/assets"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_weekly_commit_activity(self, owner, repo, params=None, payload=None):
        """
        Get the weekly commit activity
        https://docs.github.com/rest/reference/repos#get-the-weekly-commit-activity
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/code_frequency"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_last_year_of_commit_activity(self, owner, repo, params=None, payload=None):
        """
        Get the last year of commit activity
        https://docs.github.com/rest/reference/repos#get-the-last-year-of-commit-activity
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/commit_activity"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_all_contributor_commit_activity(self, owner, repo, params=None, payload=None):
        """
        Get all contributor commit activity
        https://docs.github.com/rest/reference/repos#get-all-contributor-commit-activity
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/contributors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_weekly_commit_count(self, owner, repo, params=None, payload=None):
        """
        Get the weekly commit count
        https://docs.github.com/rest/reference/repos#get-the-weekly-commit-count
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/participation"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_hourly_commit_count_for_each_day(self, owner, repo, params=None, payload=None):
        """
        Get the hourly commit count for each day
        https://docs.github.com/rest/reference/repos#get-the-hourly-commit-count-for-each-day
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/punch_card"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_commit_status(self, owner, repo, sha, params=None, payload=None):
        """
        Create a commit status
        https://docs.github.com/rest/reference/repos#create-a-commit-status
        Attributes:
        Path Parameters:
        owner
        repo
        sha
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/statuses/{sha}"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_tags(self, owner, repo, params=None, payload=None):
        """
        List repository tags
        https://docs.github.com/rest/reference/repos#list-repository-tags
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_tag_protection_states_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        List tag protection states for a repository
        https://docs.github.com/rest/reference/repos#list-tag-protection-state-of-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags/protection"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_tag_protection_state_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Create a tag protection state for a repository
        https://docs.github.com/rest/reference/repos#create-tag-protection-state-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags/protection"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_tag_protection_state_for_a_repository(
        self, owner, repo, tag_protection_id, params=None, payload=None
    ):
        """
        Delete a tag protection state for a repository
        https://docs.github.com/rest/reference/repos#delete-tag-protection-state-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        tag_protection_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags/protection/{tag_protection_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def download_a_repository_archive__tar(self, owner, repo, ref, params=None, payload=None):
        """
        Download a repository archive (tar)
        https://docs.github.com/rest/reference/repos#download-a-repository-archive
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/tarball/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_teams(self, owner, repo, params=None, payload=None):
        """
        List repository teams
        https://docs.github.com/rest/reference/repos#list-repository-teams
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_all_repository_topics(self, owner, repo, params=None, payload=None):
        """
        Get all repository topics
        https://docs.github.com/rest/reference/repos#get-all-repository-topics
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        page
         per-page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/topics"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def replace_all_repository_topics(self, owner, repo, params=None, payload=None):
        """
        Replace all repository topics
        https://docs.github.com/rest/reference/repos#replace-all-repository-topics
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/topics"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_repository_clones(self, owner, repo, params=None, payload=None):
        """
        Get repository clones
        https://docs.github.com/rest/reference/repos#get-repository-clones
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per
        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/clones"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_top_referral_paths(self, owner, repo, params=None, payload=None):
        """
        Get top referral paths
        https://docs.github.com/rest/reference/repos#get-top-referral-paths
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/popular/paths"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_top_referral_sources(self, owner, repo, params=None, payload=None):
        """
        Get top referral sources
        https://docs.github.com/rest/reference/repos#get-top-referral-sources
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/popular/referrers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_page_views(self, owner, repo, params=None, payload=None):
        """
        Get page views
        https://docs.github.com/rest/reference/repos#get-page-views
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per
        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/views"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def transfer_a_repository(self, owner, repo, params=None, payload=None):
        """
        Transfer a repository
        https://docs.github.com/rest/reference/repos#transfer-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/transfer"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def check_if_vulnerability_alerts_are_enabled_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Check if vulnerability alerts are enabled for a repository
        https://docs.github.com/rest/reference/repos#check-if-vulnerability-alerts-are-enabled-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/vulnerability-alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def enable_vulnerability_alerts(self, owner, repo, params=None, payload=None):
        """
        Enable vulnerability alerts
        https://docs.github.com/rest/reference/repos#enable-vulnerability-alerts
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/vulnerability-alerts"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_vulnerability_alerts(self, owner, repo, params=None, payload=None):
        """
        Disable vulnerability alerts
        https://docs.github.com/rest/reference/repos#disable-vulnerability-alerts
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/vulnerability-alerts"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def download_a_repository_archive__zip(self, owner, repo, ref, params=None, payload=None):
        """
        Download a repository archive (zip)
        https://docs.github.com/rest/reference/repos#download-a-repository-archive
        Attributes:
        Path Parameters:
        owner
        repo
        ref
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/zipball/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_using_a_template(
        self, template_owner, template_repo, params=None, payload=None
    ):
        """
        Create a repository using a template
        https://docs.github.com/rest/reference/repos#create-a-repository-using-a-template
        Attributes:
        Path Parameters:
        template_owner
        template_repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{template_owner}/{template_repo}/generate"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_public_repositories(self, params=None, payload=None):
        """
        List public repositories
        https://docs.github.com/rest/reference/repos#list-public-repositories
        Attributes:
        Path Parameters:

        Payload Parameters:
        since-repo
        """
        url = self._base_url + "/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def report_telemetry_back_to_datadog(self, repository_id, params=None, payload=None):
        """
        Report telemetry back to datadog
        https://docs.github.com/rest/reference/repos#report-telemetry-back-to-datadog
        Attributes:
        Path Parameters:
        repository_id
        Payload Parameters:

        """
        url = self._base_url + f"/repositories/{repository_id}/pages/telemetry"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repositories_for_the_authenticated_user(self, params=None, payload=None):
        """
        List repositories for the authenticated user
        https://docs.github.com/rest/reference/repos#list-repositories-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        visibility
         affiliation
         type
         sort
         direction
         per-page
         page
         since
         before
        """
        url = self._base_url + "/user/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_for_the_authenticated_user(self, params=None, payload=None):
        """
        Create a repository for the authenticated user
        https://docs.github.com/rest/reference/repos#create-a-repository-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/repos"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_invitations_for_the_authenticated_user(self, params=None, payload=None):
        """
        List repository invitations for the authenticated user
        https://docs.github.com/rest/reference/repos#list-repository-invitations-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/repository_invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def accept_a_repository_invitation(self, invitation_id, params=None, payload=None):
        """
        Accept a repository invitation
        https://docs.github.com/rest/reference/repos#accept-a-repository-invitation
        Attributes:
        Path Parameters:
        invitation_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/repository_invitations/{invitation_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def decline_a_repository_invitation(self, invitation_id, params=None, payload=None):
        """
        Decline a repository invitation
        https://docs.github.com/rest/reference/repos#decline-a-repository-invitation
        Attributes:
        Path Parameters:
        invitation_id
        Payload Parameters:

        """
        url = self._base_url + f"/user/repository_invitations/{invitation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_for_a_user(self, username, params=None, payload=None):
        """
        List repositories for a user
        https://docs.github.com/rest/reference/repos#list-repositories-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        type
         sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/users/{username}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response
