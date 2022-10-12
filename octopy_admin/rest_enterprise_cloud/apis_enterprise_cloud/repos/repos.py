"""
Interact with GitHub Repos.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long, W0622


class Repos:
    """
    Interact with GitHub Repos.
    """

    def __init__(self, client):
        """
        Initializes the Repos class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_repositories(self, org, params=None, payload=None):
        """
        Summary:
        List organization repositories
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-organization-repositories
        """
        url = self._base_url + f"/orgs/{org}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_repository(self, org, params=None, payload=None):
        """
        Summary:
        Create an organization repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-an-organization-repository
        """
        url = self._base_url + f"/orgs/{org}/repos"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Update a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos/#update-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Delete a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_all_autolinks_of_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List all autolinks of a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//v3/repos#list-autolinks
        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_autolink_reference_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create an autolink reference for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//v3/repos#create-an-autolink
        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_an_autolink_reference_of_a_repository(
        self, owner, repo, autolink_id, params=None, payload=None
    ):
        """
        Summary:
        Get an autolink reference of a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//v3/repos#get-autolink
        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks/{autolink_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_an_autolink_reference_from_a_repository(
        self, owner, repo, autolink_id, params=None, payload=None
    ):
        """
        Summary:
        Delete an autolink reference from a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//v3/repos#delete-autolink
        """
        url = self._base_url + f"/repos/{owner}/{repo}/autolinks/{autolink_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def enable_automated_security_fixes(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Enable automated security fixes
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#enable-automated-security-fixes
        """
        url = self._base_url + f"/repos/{owner}/{repo}/automated-security-fixes"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_automated_security_fixes(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Disable automated security fixes
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#disable-automated-security-fixes
        """
        url = self._base_url + f"/repos/{owner}/{repo}/automated-security-fixes"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_branches(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List branches
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-branches
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_branch(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get a branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-branch
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get branch protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-branch-protection
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Update branch protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#update-branch-protection
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Delete branch protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-branch-protection
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_admin_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get admin branch protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-admin-branch-protection
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_admin_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Set admin branch protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#set-admin-branch-protection
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_admin_branch_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Delete admin branch protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-admin-branch-protection
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_pull_request_review_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get pull request review protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-pull-request-review-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_pull_request_review_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Update pull request review protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#update-pull-request-review-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_pull_request_review_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Delete pull request review protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-pull-request-review-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_commit_signature_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get commit signature protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-commit-signature-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_commit_signature_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Create commit signature protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-commit-signature-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_commit_signature_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Delete commit signature protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-commit-signature-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_status_checks_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get status checks protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-status-checks-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_status_check_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Update status check protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#update-status-check-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_status_check_protection(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Remove status check protection
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#remove-status-check-protection
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_all_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get all status check contexts
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-all-status-check-contexts
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Add status check contexts
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#add-status-check-contexts
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Set status check contexts
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#set-status-check-contexts
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_status_check_contexts(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Remove status check contexts
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#remove-status-check-contexts
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Get access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-access-restrictions
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Delete access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-access-restrictions
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_apps_with_access_to_the_protected_branch(
        self, owner, repo, branch, params=None, payload=None
    ):
        """
        Summary:
        Get apps with access to the protected branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-apps-with-access-to-the-protected-branch
        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_app_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Add app access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#add-app-access-restrictions
        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_app_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Set app access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#set-app-access-restrictions
        """
        url = (
            self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_app_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Remove app access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#remove-app-access-restrictions
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
        Summary:
        Get teams with access to the protected branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-teams-with-access-to-the-protected-branch
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_team_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Add team access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#add-team-access-restrictions
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_team_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Set team access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#set-team-access-restrictions
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Remove team access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#remove-team-access-restrictions
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
        Summary:
        Get users with access to the protected branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-users-with-access-to-the-protected-branch
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_user_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Add user access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#add-user-access-restrictions
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def set_user_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Set user access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#set-user-access-restrictions
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_user_access_restrictions(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Remove user access restrictions
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#remove-user-access-restrictions
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def rename_a_branch(self, owner, repo, branch, params=None, payload=None):
        """
        Summary:
        Rename a branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#rename-a-branch
        """
        url = self._base_url + f"/repos/{owner}/{repo}/branches/{branch}/rename"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_codeowners_errors(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List CODEOWNERS errors
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-codeowners-errors
        """
        url = self._base_url + f"/repos/{owner}/{repo}/codeowners/errors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_collaborators(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository collaborators
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/collaborators#list-repository-collaborators
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_user_is_a_repository_collaborator(
        self, owner, repo, username, params=None, payload=None
    ):
        """
        Summary:
        Check if a user is a repository collaborator
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/collaborators#check-if-a-user-is-a-repository-collaborator
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_a_repository_collaborator(self, owner, repo, username, params=None, payload=None):
        """
        Summary:
        Add a repository collaborator
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/collaborators#add-a-repository-collaborator
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_collaborator(self, owner, repo, username, params=None, payload=None):
        """
        Summary:
        Remove a repository collaborator
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/collaborators#remove-a-repository-collaborator
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_repository_permissions_for_a_user(
        self, owner, repo, username, params=None, payload=None
    ):
        """
        Summary:
        Get repository permissions for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/collaborators#get-repository-permissions-for-a-user
        """
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{username}/permission"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_commit_comments_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List commit comments for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/comments#list-commit-comments-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_commit_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Summary:
        Get a commit comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/comments#get-a-commit-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_commit_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Summary:
        Update a commit comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/comments#update-a-commit-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_commit_comment(self, owner, repo, comment_id, params=None, payload=None):
        """
        Summary:
        Delete a commit comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/comments#delete-a-commit-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/comments/{comment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_commits(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List commits
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/commits#list-commits
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_branches_for_head_commit(self, owner, repo, commit_sha, params=None, payload=None):
        """
        Summary:
        List branches for HEAD commit
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/commits#list-branches-for-head-commit
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_commit_comments(self, owner, repo, commit_sha, params=None, payload=None):
        """
        Summary:
        List commit comments
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/comments#list-commit-comments
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_commit_comment(self, owner, repo, commit_sha, params=None, payload=None):
        """
        Summary:
        Create a commit comment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/comments#create-a-commit-comment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_pull_requests_associated_with_a_commit(
        self, owner, repo, commit_sha, params=None, payload=None
    ):
        """
        Summary:
        List pull requests associated with a commit
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/commits#list-pull-requests-associated-with-a-commit
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_commit(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        Get a commit
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/commits#get-a-commit
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_combined_status_for_a_specific_reference(
        self, owner, repo, ref, params=None, payload=None
    ):
        """
        Summary:
        Get the combined status for a specific reference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/statuses#get-the-combined-status-for-a-specific-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/status"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_commit_statuses_for_a_reference(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        List commit statuses for a reference
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/statuses#list-commit-statuses-for-a-reference
        """
        url = self._base_url + f"/repos/{owner}/{repo}/commits/{ref}/statuses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_community_profile_metrics(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get community profile metrics
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/community#get-community-profile-metrics
        """
        url = self._base_url + f"/repos/{owner}/{repo}/community/profile"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def compare_two_commits(self, owner, repo, basehead, params=None, payload=None):
        """
        Summary:
        Compare two commits
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/commits#compare-two-commits
        """
        url = self._base_url + f"/repos/{owner}/{repo}/compare/{basehead}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_repository_content(self, owner, repo, path, params=None, payload=None):
        """
        Summary:
        Get repository content
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-repository-content
        """
        url = self._base_url + f"/repos/{owner}/{repo}/contents/{path}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_file_contents(self, owner, repo, path, params=None, payload=None):
        """
        Summary:
        Create or update file contents
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-or-update-file-contents
        """
        url = self._base_url + f"/repos/{owner}/{repo}/contents/{path}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_file(self, owner, repo, path, params=None, payload=None):
        """
        Summary:
        Delete a file
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-a-file
        """
        url = self._base_url + f"/repos/{owner}/{repo}/contents/{path}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_contributors(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository contributors
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-repository-contributors
        """
        url = self._base_url + f"/repos/{owner}/{repo}/contributors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_deployments(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List deployments
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-deployments
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deployment(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a deployment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-deployment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deployment(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Summary:
        Get a deployment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-deployment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_deployment(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Summary:
        Delete a deployment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-a-deployment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_deployment_statuses(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Summary:
        List deployment statuses
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-deployment-statuses
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deployment_status(self, owner, repo, deployment_id, params=None, payload=None):
        """
        Summary:
        Create a deployment status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-deployment-status
        """
        url = self._base_url + f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deployment_status(
        self, owner, repo, deployment_id, status_id, params=None, payload=None
    ):
        """
        Summary:
        Get a deployment status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-deployment-status
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_dispatch_event(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a repository dispatch event
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-repository-dispatch-event
        """
        url = self._base_url + f"/repos/{owner}/{repo}/dispatches"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_environments(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List environments
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/deployments/environments#list-environments
        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_an_environment(self, owner, repo, environment_name, params=None, payload=None):
        """
        Summary:
        Get an environment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-an-environment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments/{environment_name}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_an_environment(
        self, owner, repo, environment_name, params=None, payload=None
    ):
        """
        Summary:
        Create or update an environment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-or-update-an-environment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments/{environment_name}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_an_environment(self, owner, repo, environment_name, params=None, payload=None):
        """
        Summary:
        Delete an environment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-an-environment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/environments/{environment_name}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_deployment_branch_policies(
        self, owner, repo, environment_name, params=None, payload=None
    ):
        """
        Summary:
        List deployment branch policies
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/deployments/branch-policies#list-deployment-branch-policies
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deployment_branch_policy(
        self, owner, repo, environment_name, params=None, payload=None
    ):
        """
        Summary:
        Create a deployment branch policy
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/deployments/branch-policies#create-deployment-branch-policy
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deployment_branch_policy(
        self, owner, repo, environment_name, branch_policy_id, params=None, payload=None
    ):
        """
        Summary:
        Get a deployment branch policy
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/deployments/branch-policies#get-deployment-branch-policy
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_deployment_branch_policy(
        self, owner, repo, environment_name, branch_policy_id, params=None, payload=None
    ):
        """
        Summary:
        Update a deployment branch policy
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/deployments/branch-policies#update-deployment-branch-policy
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}"
        )
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_deployment_branch_policy(
        self, owner, repo, environment_name, branch_policy_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a deployment branch policy
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/deployments/branch-policies#delete-deployment-branch-policy
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_forks(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List forks
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-forks
        """
        url = self._base_url + f"/repos/{owner}/{repo}/forks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_fork(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a fork
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-fork
        """
        url = self._base_url + f"/repos/{owner}/{repo}/forks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_webhooks(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository webhooks
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#list-repository-webhooks
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_webhook(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#create-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Summary:
        Get a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#get-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Summary:
        Update a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#update-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Summary:
        Delete a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#delete-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_a_webhook_configuration_for_a_repository(
        self, owner, repo, hook_id, params=None, payload=None
    ):
        """
        Summary:
        Get a webhook configuration for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/config"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_webhook_configuration_for_a_repository(
        self, owner, repo, hook_id, params=None, payload=None
    ):
        """
        Summary:
        Update a webhook configuration for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repo-config#update-a-webhook-configuration-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/config"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_deliveries_for_a_repository_webhook(
        self, owner, repo, hook_id, params=None, payload=None
    ):
        """
        Summary:
        List deliveries for a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repo-deliveries#list-deliveries-for-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_delivery_for_a_repository_webhook(
        self, owner, repo, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Summary:
        Get a delivery for a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repo-deliveries#get-a-delivery-for-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def redeliver_a_delivery_for_a_repository_webhook(
        self, owner, repo, hook_id, delivery_id, params=None, payload=None
    ):
        """
        Summary:
        Redeliver a delivery for a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repo-deliveries#redeliver-a-delivery-for-a-repository-webhook
        """
        url = (
            self._base_url
            + f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def ping_a_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Summary:
        Ping a repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#ping-a-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/pings"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def test_the_push_repository_webhook(self, owner, repo, hook_id, params=None, payload=None):
        """
        Summary:
        Test the push repository webhook
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/webhooks/repos#test-the-push-repository-webhook
        """
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/tests"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_invitations(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository invitations
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/invitations#list-repository-invitations
        """
        url = self._base_url + f"/repos/{owner}/{repo}/invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_repository_invitation(self, owner, repo, invitation_id, params=None, payload=None):
        """
        Summary:
        Update a repository invitation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/invitations#update-a-repository-invitation
        """
        url = self._base_url + f"/repos/{owner}/{repo}/invitations/{invitation_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_repository_invitation(self, owner, repo, invitation_id, params=None, payload=None):
        """
        Summary:
        Delete a repository invitation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/invitations#delete-a-repository-invitation
        """
        url = self._base_url + f"/repos/{owner}/{repo}/invitations/{invitation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_deploy_keys(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List deploy keys
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-deploy-keys
        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_deploy_key(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a deploy key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-deploy-key
        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_deploy_key(self, owner, repo, key_id, params=None, payload=None):
        """
        Summary:
        Get a deploy key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-deploy-key
        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys/{key_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def delete_a_deploy_key(self, owner, repo, key_id, params=None, payload=None):
        """
        Summary:
        Delete a deploy key
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-a-deploy-key
        """
        url = self._base_url + f"/repos/{owner}/{repo}/keys/{key_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repository_languages(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository languages
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-repository-languages
        """
        url = self._base_url + f"/repos/{owner}/{repo}/languages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def enable_git_lfs_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Enable Git LFS for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#enable-git-lfs-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/lfs"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_git_lfs_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Disable Git LFS for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#disable-git-lfs-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/lfs"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def sync_a_fork_branch_with_the_upstream_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Sync a fork branch with the upstream repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#sync-a-fork-branch-with-the-upstream-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/merge-upstream"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def merge_a_branch(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Merge a branch
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#merge-a-branch
        """
        url = self._base_url + f"/repos/{owner}/{repo}/merges"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_github_enterprise_cloud_pages_site(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a GitHub Enterprise Cloud Pages site
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#get-a-github-pages-site
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_github_enterprise_cloud_pages_site(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a GitHub Enterprise Cloud Pages site
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#create-a-github-pages-site
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def update_information_about_a_github_enterprise_cloud_pages_site(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Update information about a GitHub Enterprise Cloud Pages site
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#update-information-about-a-github-pages-site
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_github_enterprise_cloud_pages_site(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Delete a GitHub Enterprise Cloud Pages site
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#delete-a-github-pages-site
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_github_enterprise_cloud_pages_builds(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List GitHub Enterprise Cloud Pages builds
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#list-github-pages-builds
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def request_a_github_enterprise_cloud_pages_build(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Request a GitHub Enterprise Cloud Pages build
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#request-a-github-pages-build
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_latest_pages_build(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get latest Pages build
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#get-latest-pages-build
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds/latest"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_github_enterprise_cloud_pages_build(
        self, owner, repo, build_id, params=None, payload=None
    ):
        """
        Summary:
        Get GitHub Enterprise Cloud Pages build
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#get-github-pages-build
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/builds/{build_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_github_pages_deployment(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a GitHub Pages deployment
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#create-a-github-pages-deployment
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/deployment"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_dns_health_check_for_github_pages(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a DNS health check for GitHub Pages
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/pages#get-a-dns-health-check-for-github-pages
        """
        url = self._base_url + f"/repos/{owner}/{repo}/pages/health"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_readme(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a repository README
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-repository-readme
        """
        url = self._base_url + f"/repos/{owner}/{repo}/readme"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_readme_for_a_directory(self, owner, repo, dir, params=None, payload=None):
        """
        Summary:
        Get a repository README for a directory
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-repository-directory-readme
        """
        url = self._base_url + f"/repos/{owner}/{repo}/readme/{dir}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_releases(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List releases
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-releases
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_release(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a release
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_release_asset(self, owner, repo, asset_id, params=None, payload=None):
        """
        Summary:
        Get a release asset
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-release-asset
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_release_asset(self, owner, repo, asset_id, params=None, payload=None):
        """
        Summary:
        Update a release asset
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#update-a-release-asset
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_release_asset(self, owner, repo, asset_id, params=None, payload=None):
        """
        Summary:
        Delete a release asset
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-a-release-asset
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/assets/{asset_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def generate_release_notes_content_for_a_release(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Generate release notes content for a release
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#generate-release-notes
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/generate-notes"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_latest_release(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get the latest release
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-the-latest-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/latest"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_release_by_tag_name(self, owner, repo, tag, params=None, payload=None):
        """
        Summary:
        Get a release by tag name
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-release-by-tag-name
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/tags/{tag}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        Get a release
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-a-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        Update a release
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#update-a-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_release(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        Delete a release
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-a-release
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_release_assets(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        List release assets
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-release-assets
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/assets"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def upload_a_release_asset(self, owner, repo, release_id, params=None, payload=None):
        """
        Summary:
        Upload a release asset
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#upload-a-release-asset
        """
        url = self._base_url + f"/repos/{owner}/{repo}/releases/{release_id}/assets"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_the_weekly_commit_activity(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get the weekly commit activity
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/statistics#get-the-weekly-commit-activity
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/code_frequency"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_last_year_of_commit_activity(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get the last year of commit activity
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/statistics#get-the-last-year-of-commit-activity
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/commit_activity"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_all_contributor_commit_activity(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get all contributor commit activity
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/statistics#get-all-contributor-commit-activity
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/contributors"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_weekly_commit_count(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get the weekly commit count
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/statistics#get-the-weekly-commit-count
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/participation"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_the_hourly_commit_count_for_each_day(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get the hourly commit count for each day
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/statistics/repos#get-the-hourly-commit-count-for-each-day
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stats/punch_card"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_commit_status(self, owner, repo, sha, params=None, payload=None):
        """
        Summary:
        Create a commit status
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/commits/statuses#create-a-commit-status
        """
        url = self._base_url + f"/repos/{owner}/{repo}/statuses/{sha}"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_tags(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository tags
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-repository-tags
        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_tag_protection_states_for_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List tag protection states for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-tag-protection-state-of-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags/protection"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_tag_protection_state_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Create a tag protection state for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-tag-protection-state-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags/protection"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def delete_a_tag_protection_state_for_a_repository(
        self, owner, repo, tag_protection_id, params=None, payload=None
    ):
        """
        Summary:
        Delete a tag protection state for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#delete-tag-protection-state-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/tags/protection/{tag_protection_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def download_a_repository_archive__tar(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        Download a repository archive (tar)
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#download-a-repository-archive
        """
        url = self._base_url + f"/repos/{owner}/{repo}/tarball/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_teams(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository teams
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-repository-teams
        """
        url = self._base_url + f"/repos/{owner}/{repo}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_all_repository_topics(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get all repository topics
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#get-all-repository-topics
        """
        url = self._base_url + f"/repos/{owner}/{repo}/topics"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def replace_all_repository_topics(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Replace all repository topics
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#replace-all-repository-topics
        """
        url = self._base_url + f"/repos/{owner}/{repo}/topics"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_repository_clones(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get repository clones
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/traffic#get-repository-clones
        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/clones"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_top_referral_paths(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get top referral paths
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/traffic#get-top-referral-paths
        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/popular/paths"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_top_referral_sources(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get top referral sources
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/traffic#get-top-referral-sources
        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/popular/referrers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_page_views(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get page views
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/metrics/traffic#get-page-views
        """
        url = self._base_url + f"/repos/{owner}/{repo}/traffic/views"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def transfer_a_repository(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Transfer a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#transfer-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/transfer"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def check_if_vulnerability_alerts_are_enabled_for_a_repository(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Check if vulnerability alerts are enabled for a repository
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#check-if-vulnerability-alerts-are-enabled-for-a-repository
        """
        url = self._base_url + f"/repos/{owner}/{repo}/vulnerability-alerts"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def enable_vulnerability_alerts(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Enable vulnerability alerts
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#enable-vulnerability-alerts
        """
        url = self._base_url + f"/repos/{owner}/{repo}/vulnerability-alerts"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def disable_vulnerability_alerts(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Disable vulnerability alerts
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#disable-vulnerability-alerts
        """
        url = self._base_url + f"/repos/{owner}/{repo}/vulnerability-alerts"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def download_a_repository_archive__zip(self, owner, repo, ref, params=None, payload=None):
        """
        Summary:
        Download a repository archive (zip)
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#download-a-repository-archive
        """
        url = self._base_url + f"/repos/{owner}/{repo}/zipball/{ref}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_using_a_template(
        self, template_owner, template_repo, params=None, payload=None
    ):
        """
        Summary:
        Create a repository using a template
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-repository-using-a-template
        """
        url = self._base_url + f"/repos/{template_owner}/{template_repo}/generate"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_public_repositories(self, params=None, payload=None):
        """
        Summary:
        List public repositories
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-public-repositories
        """
        url = self._base_url + "/repositories"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List repositories for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-repositories-for-the-authenticated-user
        """
        url = self._base_url + "/user/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        Create a repository for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#create-a-repository-for-the-authenticated-user
        """
        url = self._base_url + "/user/repos"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_invitations_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List repository invitations for the authenticated user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/invitations#list-repository-invitations-for-the-authenticated-user
        """
        url = self._base_url + "/user/repository_invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def accept_a_repository_invitation(self, invitation_id, params=None, payload=None):
        """
        Summary:
        Accept a repository invitation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/invitations#accept-a-repository-invitation
        """
        url = self._base_url + f"/user/repository_invitations/{invitation_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def decline_a_repository_invitation(self, invitation_id, params=None, payload=None):
        """
        Summary:
        Decline a repository invitation
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/collaborators/invitations#decline-a-repository-invitation
        """
        url = self._base_url + f"/user/repository_invitations/{invitation_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List repositories for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/repos#list-repositories-for-a-user
        """
        url = self._base_url + f"/users/{username}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response
