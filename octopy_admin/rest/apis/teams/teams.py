"""
Interact with GitHub Teams.
"""
# pylint: disable=too-many-lines


# pylint: disable=too-many-arguments
class Teams:
    # pylint: disable=too-many-public-methods
    """
    Interact with GitHub Teams.
    """

    def __init__(self, client):
        """
        Initialize the Teams class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def get_an_external_group(self, org, group_id, params=None, payload=None):
        """
        Get an external group
        https://docs.github.com/rest/reference/teams#external-idp-group-info-for-an-organization
        Attributes:
        Path Parameters:
        org
        group_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/external-group/{group_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_external_groups_in_an_organization(self, org, params=None, payload=None):
        """
        List external groups in an organization
        https://docs.github.com/rest/reference/teams#list-external-idp-groups-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
         display_name
        """
        url = self._base_url + f"/orgs/{org}/external-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_idp_groups_for_an_organization(self, org, params=None, payload=None):
        """
        List IdP groups for an organization
        https://docs.github.com/rest/reference/teams#list-idp-groups-for-an-organization
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/team-sync/groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_teams(self, org, params=None, payload=None):
        """
        List teams
        https://docs.github.com/rest/reference/teams#list-teams
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_team(self, org, params=None, payload=None):
        """
        Create a team
        https://docs.github.com/rest/reference/teams#create-a-team
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_team_by_name(self, org, team_slug, params=None, payload=None):
        """
        Get a team by name
        https://docs.github.com/rest/reference/teams#get-a-team-by-name
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_team(self, org, team_slug, params=None, payload=None):
        """
        Update a team
        https://docs.github.com/rest/reference/teams#update-a-team
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_team(self, org, team_slug, params=None, payload=None):
        """
        Delete a team
        https://docs.github.com/rest/reference/teams#delete-a-team
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussions(self, org, team_slug, params=None, payload=None):
        """
        List discussions
        https://docs.github.com/rest/reference/teams#list-discussions
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:
        direction
         per-page
         page
         pinned
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion(self, org, team_slug, params=None, payload=None):
        """
        Create a discussion
        https://docs.github.com/rest/reference/teams#create-a-discussion
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion(self, org, team_slug, discussion_number, params=None, payload=None):
        """
        Get a discussion
        https://docs.github.com/rest/reference/teams#get-a-discussion
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion(self, org, team_slug, discussion_number, params=None, payload=None):
        """
        Update a discussion
        https://docs.github.com/rest/reference/teams#update-a-discussion
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion(self, org, team_slug, discussion_number, params=None, payload=None):
        """
        Delete a discussion
        https://docs.github.com/rest/reference/teams#delete-a-discussion
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussion_comments(
        self, org, team_slug, discussion_number, params=None, payload=None
    ):
        """
        List discussion comments
        https://docs.github.com/rest/reference/teams#list-discussion-comments
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:
        direction
         per-page
         page
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
        Create a discussion comment
        https://docs.github.com/rest/reference/teams#create-a-discussion-comment
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments"
        )
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion_comment(
        self, org, team_slug, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Get a discussion comment
        https://docs.github.com/rest/reference/teams#get-a-discussion-comment
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        comment_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion_comment(
        self, org, team_slug, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Update a discussion comment
        https://docs.github.com/rest/reference/teams#update-a-discussion-comment
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        comment_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion_comment(
        self, org, team_slug, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Delete a discussion comment
        https://docs.github.com/rest/reference/teams#delete-a-discussion-comment
        Attributes:
        Path Parameters:
        org
        team_slug
        discussion_number
        comment_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}"  # pylint: disable=line-too-long # noqa: E501
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_a_connection_between_an_external_group_and_a_team(
        self, org, team_slug, params=None, payload=None
    ):
        """
        List a connection between an external group and a team
        https://docs.github.com/rest/reference/teams#list-external-idp-group-team-connection
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/external-groups"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_the_connection_between_an_external_group_and_a_team(
        self, org, team_slug, params=None, payload=None
    ):
        """
        Update the connection between an external group and a team
        https://docs.github.com/rest/reference/teams#link-external-idp-group-team-connection
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/external-groups"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def remove_the_connection_between_an_external_group_and_a_team(
        self, org, team_slug, params=None, payload=None
    ):
        """
        Remove the connection between an external group and a team
        https://docs.github.com/rest/reference/teams#unlink-external-idp-group-team-connection
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/external-groups"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_pending_team_invitations(self, org, team_slug, params=None, payload=None):
        """
        List pending team invitations
        https://docs.github.com/rest/reference/teams#list-pending-team-invitations
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_team_members(self, org, team_slug, params=None, payload=None):
        """
        List team members
        https://docs.github.com/rest/reference/teams#list-team-members
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:
        role
         per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_team_membership_for_a_user(self, org, team_slug, username, params=None, payload=None):
        """
        Get team membership for a user
        https://docs.github.com/rest/reference/teams#get-team-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        team_slug
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_membership_for_a_user(
        self, org, team_slug, username, params=None, payload=None
    ):
        """
        Add or update team membership for a user
        https://docs.github.com/rest/reference/teams#add-or-update-team-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        team_slug
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_membership_for_a_user(
        self, org, team_slug, username, params=None, payload=None
    ):
        """
        Remove team membership for a user
        https://docs.github.com/rest/reference/teams#remove-team-membership-for-a-user
        Attributes:
        Path Parameters:
        org
        team_slug
        username
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/memberships/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_projects(self, org, team_slug, params=None, payload=None):
        """
        List team projects
        https://docs.github.com/rest/reference/teams#list-team-projects
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_project(
        self, org, team_slug, project_id, params=None, payload=None
    ):
        """
        Check team permissions for a project
        https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-project
        Attributes:
        Path Parameters:
        org
        team_slug
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects/{project_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_project_permissions(
        self, org, team_slug, project_id, params=None, payload=None
    ):
        """
        Add or update team project permissions
        https://docs.github.com/rest/reference/teams#add-or-update-team-project-permissions
        Attributes:
        Path Parameters:
        org
        team_slug
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects/{project_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_project_from_a_team(self, org, team_slug, project_id, params=None, payload=None):
        """
        Remove a project from a team
        https://docs.github.com/rest/reference/teams#remove-a-project-from-a-team
        Attributes:
        Path Parameters:
        org
        team_slug
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/projects/{project_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_repositories(self, org, team_slug, params=None, payload=None):
        """
        List team repositories
        https://docs.github.com/rest/reference/teams#list-team-repositories
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_repository(
        self, org, team_slug, owner, repo, params=None, payload=None
    ):
        """
        Check team permissions for a repository
        https://docs.github.com/rest/reference/teams/#check-team-permissions-for-a-repository
        Attributes:
        Path Parameters:
        org
        team_slug
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_repository_permissions(
        self, org, team_slug, owner, repo, params=None, payload=None
    ):
        """
        Add or update team repository permissions
        https://docs.github.com/rest/reference/teams/#add-or-update-team-repository-permissions
        Attributes:
        Path Parameters:
        org
        team_slug
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_from_a_team(
        self, org, team_slug, owner, repo, params=None, payload=None
    ):
        """
        Remove a repository from a team
        https://docs.github.com/rest/reference/teams/#remove-a-repository-from-a-team
        Attributes:
        Path Parameters:
        org
        team_slug
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_idp_groups_for_a_team(self, org, team_slug, params=None, payload=None):
        """
        List IdP groups for a team
        https://docs.github.com/rest/reference/teams#list-idp-groups-for-a-team
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/team-sync/group-mappings"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_idp_group_connections(self, org, team_slug, params=None, payload=None):
        """
        Create or update IdP group connections
        https://docs.github.com/rest/reference/teams#create-or-update-idp-group-connections
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/team-sync/group-mappings"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_child_teams(self, org, team_slug, params=None, payload=None):
        """
        List child teams
        https://docs.github.com/rest/reference/teams#list-child-teams
        Attributes:
        Path Parameters:
        org
        team_slug
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/teams/{team_slug}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_team__legacy(self, team_id, params=None, payload=None):
        """
        Get a team (Legacy)
        https://docs.github.com/rest/reference/teams/#get-a-team-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_team__legacy(self, team_id, params=None, payload=None):
        """
        Update a team (Legacy)
        https://docs.github.com/rest/reference/teams/#update-a-team-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_team__legacy(self, team_id, params=None, payload=None):
        """
        Delete a team (Legacy)
        https://docs.github.com/rest/reference/teams/#delete-a-team-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussions__legacy(self, team_id, params=None, payload=None):
        """
        List discussions (Legacy)
        https://docs.github.com/rest/reference/teams#list-discussions-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:
        direction
         per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/discussions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion__legacy(self, team_id, params=None, payload=None):
        """
        Create a discussion (Legacy)
        https://docs.github.com/rest/reference/teams#create-a-discussion-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/discussions"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion__legacy(self, team_id, discussion_number, params=None, payload=None):
        """
        Get a discussion (Legacy)
        https://docs.github.com/rest/reference/teams#get-a-discussion-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_discussion__legacy(self, team_id, discussion_number, params=None, payload=None):
        """
        Update a discussion (Legacy)
        https://docs.github.com/rest/reference/teams#update-a-discussion-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_discussion__legacy(self, team_id, discussion_number, params=None, payload=None):
        """
        Delete a discussion (Legacy)
        https://docs.github.com/rest/reference/teams#delete-a-discussion-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_discussion_comments__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        List discussion comments (Legacy)
        https://docs.github.com/rest/reference/teams#list-discussion-comments-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:
        direction
         per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/comments"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_discussion_comment__legacy(
        self, team_id, discussion_number, params=None, payload=None
    ):
        """
        Create a discussion comment (Legacy)
        https://docs.github.com/rest/reference/teams#create-a-discussion-comment-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/discussions/{discussion_number}/comments"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_discussion_comment__legacy(
        self, team_id, discussion_number, comment_number, params=None, payload=None
    ):
        """
        Get a discussion comment (Legacy)
        https://docs.github.com/rest/reference/teams#get-a-discussion-comment-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        comment_number
        Payload Parameters:

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
        Update a discussion comment (Legacy)
        https://docs.github.com/rest/reference/teams#update-a-discussion-comment-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        comment_number
        Payload Parameters:

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
        Delete a discussion comment (Legacy)
        https://docs.github.com/rest/reference/teams#delete-a-discussion-comment-legacy
        Attributes:
        Path Parameters:
        team_id
        discussion_number
        comment_number
        Payload Parameters:

        """
        url = (
            self._base_url
            + f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}"
        )
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_pending_team_invitations__legacy(self, team_id, params=None, payload=None):
        """
        List pending team invitations (Legacy)
        https://docs.github.com/rest/reference/teams#list-pending-team-invitations-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/invitations"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_team_members__legacy(self, team_id, params=None, payload=None):
        """
        List team members (Legacy)
        https://docs.github.com/rest/reference/teams#list-team-members-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:
        role
         per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/members"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_team_member__legacy(self, team_id, username, params=None, payload=None):
        """
        Get team member (Legacy)
        https://docs.github.com/rest/reference/teams#get-team-member-legacy
        Attributes:
        Path Parameters:
        team_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/members/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_team_member__legacy(self, team_id, username, params=None, payload=None):
        """
        Add team member (Legacy)
        https://docs.github.com/rest/reference/teams#add-team-member-legacy
        Attributes:
        Path Parameters:
        team_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/members/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_member__legacy(self, team_id, username, params=None, payload=None):
        """
        Remove team member (Legacy)
        https://docs.github.com/rest/reference/teams#remove-team-member-legacy
        Attributes:
        Path Parameters:
        team_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/members/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_team_membership_for_a_user__legacy(self, team_id, username, params=None, payload=None):
        """
        Get team membership for a user (Legacy)
        https://docs.github.com/rest/reference/teams#get-team-membership-for-a-user-legacy
        Attributes:
        Path Parameters:
        team_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/memberships/{username}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_membership_for_a_user__legacy(
        self, team_id, username, params=None, payload=None
    ):
        """
        Add or update team membership for a user (Legacy)
        https://docs.github.com/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy
        Attributes:
        Path Parameters:
        team_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/memberships/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_team_membership_for_a_user__legacy(
        self, team_id, username, params=None, payload=None
    ):
        """
        Remove team membership for a user (Legacy)
        https://docs.github.com/rest/reference/teams#remove-team-membership-for-a-user-legacy
        Attributes:
        Path Parameters:
        team_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/memberships/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_projects__legacy(self, team_id, params=None, payload=None):
        """
        List team projects (Legacy)
        https://docs.github.com/rest/reference/teams/#list-team-projects-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_project__legacy(
        self, team_id, project_id, params=None, payload=None
    ):
        """
        Check team permissions for a project (Legacy)
        https://docs.github.com/rest/reference/teams/#check-team-permissions-for-a-project-legacy
        Attributes:
        Path Parameters:
        team_id
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/projects/{project_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_project_permissions__legacy(
        self, team_id, project_id, params=None, payload=None
    ):
        """
        Add or update team project permissions (Legacy)
        https://docs.github.com/rest/reference/teams/#add-or-update-team-project-permissions-legacy
        Attributes:
        Path Parameters:
        team_id
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/projects/{project_id}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_project_from_a_team__legacy(self, team_id, project_id, params=None, payload=None):
        """
        Remove a project from a team (Legacy)
        https://docs.github.com/rest/reference/teams/#remove-a-project-from-a-team-legacy
        Attributes:
        Path Parameters:
        team_id
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/projects/{project_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_team_repositories__legacy(self, team_id, params=None, payload=None):
        """
        List team repositories (Legacy)
        https://docs.github.com/rest/reference/teams/#list-team-repositories-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/repos"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_team_permissions_for_a_repository__legacy(
        self, team_id, owner, repo, params=None, payload=None
    ):
        """
        Check team permissions for a repository (Legacy)
        https://docs.github.com/rest/reference/teams/#check-team-permissions-for-a-repository-legacy
        Attributes:
        Path Parameters:
        team_id
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/repos/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_or_update_team_repository_permissions__legacy(
        self, team_id, owner, repo, params=None, payload=None
    ):
        """
        Add or update team repository permissions (Legacy)
        https://docs.github.com/rest/reference/teams/#add-or-update-team-repository-permissions-legacy
        Attributes:
        Path Parameters:
        team_id
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/repos/{owner}/{repo}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_a_repository_from_a_team__legacy(
        self, team_id, owner, repo, params=None, payload=None
    ):
        """
        Remove a repository from a team (Legacy)
        https://docs.github.com/rest/reference/teams/#remove-a-repository-from-a-team-legacy
        Attributes:
        Path Parameters:
        team_id
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/repos/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_idp_groups_for_a_team__legacy(self, team_id, params=None, payload=None):
        """
        List IdP groups for a team (Legacy)
        https://docs.github.com/rest/reference/teams#list-idp-groups-for-a-team-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/team-sync/group-mappings"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_or_update_idp_group_connections__legacy(self, team_id, params=None, payload=None):
        """
        Create or update IdP group connections (Legacy)
        https://docs.github.com/rest/reference/teams#create-or-update-idp-group-connections-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:

        """
        url = self._base_url + f"/teams/{team_id}/team-sync/group-mappings"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def list_child_teams__legacy(self, team_id, params=None, payload=None):
        """
        List child teams (Legacy)
        https://docs.github.com/rest/reference/teams/#list-child-teams-legacy
        Attributes:
        Path Parameters:
        team_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/teams/{team_id}/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_teams_for_the_authenticated_user(self, params=None, payload=None):
        """
        List teams for the authenticated user
        https://docs.github.com/rest/reference/teams#list-teams-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/teams"
        response = self._execute("get", url, params=params, payload=payload)
        return response
