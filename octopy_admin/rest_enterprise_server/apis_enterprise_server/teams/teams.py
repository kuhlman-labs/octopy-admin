"""
Interact with GitHub Teams.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Teams:
    """
    Interact with GitHub Teams.
    """

    def __init__(self, client):
        """
        Initializes the Teams class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_an_external_group(self, org, group_id, params=None, payload=None):
        """
        Summary:
        Get an external group
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#external-idp-group-info-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/external-group/{group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_external_groups_in_an_organization(self, org, params=None, payload=None):
        """
        Summary:
        List external groups in an organization
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-external-idp-groups-for-an-organization
        """
        url = self._base_url + f"/orgs/{org}/external-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_teams(self, org, params=None, payload=None):
        """
        Summary:
        List teams
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-teams
        """
        url = self._base_url + f"/orgs/{org}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_team(self, org, params=None, payload=None):
        """
        Summary:
        Create a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#create-a-team
        """
        url = self._base_url + f"/orgs/{org}/teams"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_team_by_name(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        Get a team by name
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-a-team-by-name
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_team(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        Update a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#update-a-team
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_team(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        Delete a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#delete-a-team
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussions(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        List discussions
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-discussions
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        Create a discussion
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#create-a-discussion
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion(self, org, team_slug, discussion_number, params=None, payload=None):
        """
        Summary:
        Get a discussion
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-a-discussion
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion(self, org, team_slug, discussion_number, params=None, payload=None):
        """
        Summary:
        Update a discussion
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#update-a-discussion
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion(self, org, team_slug, discussion_number, params=None, payload=None):
        """
        Summary:
        Delete a discussion
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#delete-a-discussion
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussion_comments(
        self, org, team_slug, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        List discussion comments
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-discussion-comments
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion_comment(
        self, org, team_slug, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        Create a discussion comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#create-a-discussion-comment
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion_comment(
        self,
        org,
        team_slug,
        discussion_number,
        comment_number,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Get a discussion comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-a-discussion-comment
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion_comment(
        self,
        org,
        team_slug,
        discussion_number,
        comment_number,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Update a discussion comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#update-a-discussion-comment
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion_comment(
        self,
        org,
        team_slug,
        discussion_number,
        comment_number,
        params=None,
        payload=None,
    ):
        """
        Summary:
        Delete a discussion comment
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#delete-a-discussion-comment
        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_a_connection_between_an_external_group_and_a_team(
        self, org, team_slug, params=None, payload=None
    ):
        """
        Summary:
        List a connection between an external group and a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-external-idp-group-team-connection
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/external-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_the_connection_between_an_external_group_and_a_team(
        self, org, team_slug, params=None, payload=None
    ):
        """
        Summary:
        Update the connection between an external group and a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#link-external-idp-group-team-connection
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/external-groups"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_the_connection_between_an_external_group_and_a_team(
        self, org, team_slug, params=None, payload=None
    ):
        """
        Summary:
        Remove the connection between an external group and a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#unlink-external-idp-group-team-connection
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/external-groups"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_members(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        List team members
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-team-members
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_team_membership_for_a_user(self, org, team_slug, username, params=None, payload=None):
        """
        Summary:
        Get team membership for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-team-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_membership_for_a_user(
        self, org, team_slug, username, params=None, payload=None
    ):
        """
        Summary:
        Add or update team membership for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#add-or-update-team-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_membership_for_a_user(
        self, org, team_slug, username, params=None, payload=None
    ):
        """
        Summary:
        Remove team membership for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#remove-team-membership-for-a-user
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_projects(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        List team projects
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-team-projects
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_project(
        self, org, team_slug, project_id, params=None, payload=None
    ):
        """
        Summary:
        Check team permissions for a project
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#check-team-permissions-for-a-project
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects/{project_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_project_permissions(
        self, org, team_slug, project_id, params=None, payload=None
    ):
        """
        Summary:
        Add or update team project permissions
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#add-or-update-team-project-permissions
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects/{project_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_project_from_a_team(self, org, team_slug, project_id, params=None, payload=None):
        """
        Summary:
        Remove a project from a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#remove-a-project-from-a-team
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects/{project_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_repositories(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        List team repositories
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-team-repositories
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_repository(
        self, org, team_slug, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Check team permissions for a repository
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#check-team-permissions-for-a-repository
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_repository_permissions(
        self, org, team_slug, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Add or update team repository permissions
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#add-or-update-team-repository-permissions
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_from_a_team(
        self, org, team_slug, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Remove a repository from a team
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#remove-a-repository-from-a-team
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_child_teams(self, org, team_slug, params=None, payload=None):
        """
        Summary:
        List child teams
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-child-teams
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_team__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        Get a team (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#get-a-team-legacy
        """
        url = self._base_url + f"/teams/{team_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_team__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        Update a team (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#update-a-team-legacy
        """
        url = self._base_url + f"/teams/{team_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_team__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        Delete a team (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#delete-a-team-legacy
        """
        url = self._base_url + f"/teams/{team_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussions__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        List discussions (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-discussions-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        Create a discussion (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#create-a-discussion-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion__legacy(self, team_id, discussion_number, params=None, payload=None):
        """
        Summary:
        Get a discussion (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-a-discussion-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion__legacy(self, team_id, discussion_number, params=None, payload=None):
        """
        Summary:
        Update a discussion (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#update-a-discussion-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion__legacy(self, team_id, discussion_number, params=None, payload=None):
        """
        Summary:
        Delete a discussion (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#delete-a-discussion-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussion_comments__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        List discussion comments (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-discussion-comments-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion_comment__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        Summary:
        Create a discussion comment (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#create-a-discussion-comment-legacy
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Summary:
        Get a discussion comment (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-a-discussion-comment-legacy
        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Summary:
        Update a discussion comment (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#update-a-discussion-comment-legacy
        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Summary:
        Delete a discussion comment (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#delete-a-discussion-comment-legacy
        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_members__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        List team members (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-team-members-legacy
        """
        url = self._base_url + f"/teams/{team_id}/members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_team_member__legacy(self, team_id, username, params=None, payload=None):
        """
        Summary:
        Get team member (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-team-member-legacy
        """
        url = self._base_url + f"/teams/{team_id}/members/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_team_member__legacy(self, team_id, username, params=None, payload=None):
        """
        Summary:
        Add team member (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#add-team-member-legacy
        """
        url = self._base_url + f"/teams/{team_id}/members/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_member__legacy(self, team_id, username, params=None, payload=None):
        """
        Summary:
        Remove team member (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#remove-team-member-legacy
        """
        url = self._base_url + f"/teams/{team_id}/members/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_team_membership_for_a_user__legacy(self, team_id, username, params=None, payload=None):
        """
        Summary:
        Get team membership for a user (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#get-team-membership-for-a-user-legacy
        """
        url = self._base_url + f"/teams/{team_id}/memberships/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_membership_for_a_user__legacy(
        self, team_id, username, params=None, payload=None
    ):
        """
        Summary:
        Add or update team membership for a user (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy
        """
        url = self._base_url + f"/teams/{team_id}/memberships/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_membership_for_a_user__legacy(
        self, team_id, username, params=None, payload=None
    ):
        """
        Summary:
        Remove team membership for a user (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#remove-team-membership-for-a-user-legacy
        """
        url = self._base_url + f"/teams/{team_id}/memberships/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_projects__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        List team projects (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#list-team-projects-legacy
        """
        url = self._base_url + f"/teams/{team_id}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_project__legacy(
        self, team_id, project_id, params=None, payload=None
    ):
        """
        Summary:
        Check team permissions for a project (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#check-team-permissions-for-a-project-legacy
        """
        url = self._base_url + f"/teams/{team_id}/projects/{project_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_project_permissions__legacy(
        self, team_id, project_id, params=None, payload=None
    ):
        """
        Summary:
        Add or update team project permissions (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#add-or-update-team-project-permissions-legacy
        """
        url = self._base_url + f"/teams/{team_id}/projects/{project_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_project_from_a_team__legacy(self, team_id, project_id, params=None, payload=None):
        """
        Summary:
        Remove a project from a team (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#remove-a-project-from-a-team-legacy
        """
        url = self._base_url + f"/teams/{team_id}/projects/{project_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_repositories__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        List team repositories (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#list-team-repositories-legacy
        """
        url = self._base_url + f"/teams/{team_id}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_repository__legacy(
        self, team_id, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Check team permissions for a repository (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#check-team-permissions-for-a-repository-legacy
        """
        url = self._base_url + f"/teams/{team_id}/repos/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_repository_permissions__legacy(
        self, team_id, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Add or update team repository permissions (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#add-or-update-team-repository-permissions-legacy
        """
        url = self._base_url + f"/teams/{team_id}/repos/{owner}/{repo}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_from_a_team__legacy(
        self, team_id, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Remove a repository from a team (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#remove-a-repository-from-a-team-legacy
        """
        url = self._base_url + f"/teams/{team_id}/repos/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_child_teams__legacy(self, team_id, params=None, payload=None):
        """
        Summary:
        List child teams (Legacy)
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams/#list-child-teams-legacy
        """
        url = self._base_url + f"/teams/{team_id}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_teams_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List teams for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/teams#list-teams-for-the-authenticated-user
        """
        url = self._base_url + "/user/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response
