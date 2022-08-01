"""
Interact with GitHub Issues.
"""


class Issues:
    # pylint: disable=too-many-public-methods
    """
    Interact with GitHub Issues.
    """

    def __init__(self, client):
        """
        Initialize the Issues class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_issues_assigned_to_the_authenticated_user(self, payload=None):
        """
        List issues assigned to the authenticated user
        https://docs.github.com/rest/reference/issues#list-issues-assigned-to-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        filter
         state
         labels
         sort
         direction
         since
         collab
         orgs
         owned
         pulls
         per-page
         page
        """
        url = self._base_url + "/issues"
        response = self._execute("get", url, payload)
        return response

    def list_organization_issues_assigned_to_the_authenticated_user(self, org, payload=None):
        """
        List organization issues assigned to the authenticated user
        https://docs.github.com/rest/reference/issues#list-organization-issues-assigned-to-the-authenticated-user
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        filter
         state
         labels
         sort
         direction
         since
         per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/issues"
        response = self._execute("get", url, payload)
        return response

    def list_assignees(self, owner, repo, payload=None):
        """
        List assignees
        https://docs.github.com/rest/reference/issues#list-assignees
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/assignees"
        response = self._execute("get", url, payload)
        return response

    def check_if_a_user_can_be_assigned(self, owner, repo, assignee, payload=None):
        """
        Check if a user can be assigned
        https://docs.github.com/rest/reference/issues#check-if-a-user-can-be-assigned
        Attributes:
        Path Parameters:
        owner
        repo
        assignee
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/assignees/{assignee}"
        response = self._execute("get", url, payload)
        return response

    def list_repository_issues(self, owner, repo, payload=None):
        """
        List repository issues
        https://docs.github.com/rest/reference/issues#list-repository-issues
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        milestone
         state
         assignee
         creator
         mentioned
         labels
         sort
         direction
         since
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues"
        response = self._execute("get", url, payload)
        return response

    def create_an_issue(self, owner, repo, payload=None):
        """
        Create an issue
        https://docs.github.com/rest/reference/issues#create-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues"
        response = self._execute("post", url, payload)
        return response

    def list_issue_comments_for_a_repository(self, owner, repo, payload=None):
        """
        List issue comments for a repository
        https://docs.github.com/rest/reference/issues#list-issue-comments-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        sort
         direction
         since
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments"
        response = self._execute("get", url, payload)
        return response

    def get_an_issue_comment(self, owner, repo, comment_id, payload=None):
        """
        Get an issue comment
        https://docs.github.com/rest/reference/issues#get-an-issue-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
        response = self._execute("get", url, payload)
        return response

    def update_an_issue_comment(self, owner, repo, comment_id, payload=None):
        """
        Update an issue comment
        https://docs.github.com/rest/reference/issues#update-an-issue-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
        response = self._execute("patch", url, payload)
        return response

    def delete_an_issue_comment(self, owner, repo, comment_id, payload=None):
        """
        Delete an issue comment
        https://docs.github.com/rest/reference/issues#delete-an-issue-comment
        Attributes:
        Path Parameters:
        owner
        repo
        comment_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
        response = self._execute("delete", url, payload)
        return response

    def list_issue_events_for_a_repository(self, owner, repo, payload=None):
        """
        List issue events for a repository
        https://docs.github.com/rest/reference/issues#list-issue-events-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/events"
        response = self._execute("get", url, payload)
        return response

    def get_an_issue_event(self, owner, repo, event_id, payload=None):
        """
        Get an issue event
        https://docs.github.com/rest/reference/issues#get-an-issue-event
        Attributes:
        Path Parameters:
        owner
        repo
        event_id
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/events/{event_id}"
        response = self._execute("get", url, payload)
        return response

    def get_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Get an issue
        https://docs.github.com/rest/reference/issues#get-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}"
        response = self._execute("get", url, payload)
        return response

    def update_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Update an issue
        https://docs.github.com/rest/reference/issues/#update-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}"
        response = self._execute("patch", url, payload)
        return response

    def add_assignees_to_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Add assignees to an issue
        https://docs.github.com/rest/reference/issues#add-assignees-to-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        response = self._execute("post", url, payload)
        return response

    def remove_assignees_from_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Remove assignees from an issue
        https://docs.github.com/rest/reference/issues#remove-assignees-from-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
        response = self._execute("delete", url, payload)
        return response

    def list_issue_comments(self, owner, repo, issue_number, payload=None):
        """
        List issue comments
        https://docs.github.com/rest/reference/issues#list-issue-comments
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:
        since
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/comments"
        response = self._execute("get", url, payload)
        return response

    def create_an_issue_comment(self, owner, repo, issue_number, payload=None):
        """
        Create an issue comment
        https://docs.github.com/rest/reference/issues#create-an-issue-comment
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/comments"
        response = self._execute("post", url, payload)
        return response

    def list_issue_events(self, owner, repo, issue_number, payload=None):
        """
        List issue events
        https://docs.github.com/rest/reference/issues#list-issue-events
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/events"
        response = self._execute("get", url, payload)
        return response

    def list_labels_for_an_issue(self, owner, repo, issue_number, payload=None):
        """
        List labels for an issue
        https://docs.github.com/rest/reference/issues#list-labels-for-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("get", url, payload)
        return response

    def add_labels_to_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Add labels to an issue
        https://docs.github.com/rest/reference/issues#add-labels-to-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("post", url, payload)
        return response

    def set_labels_for_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Set labels for an issue
        https://docs.github.com/rest/reference/issues#set-labels-for-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("put", url, payload)
        return response

    def remove_all_labels_from_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Remove all labels from an issue
        https://docs.github.com/rest/reference/issues#remove-all-labels-from-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
        response = self._execute("delete", url, payload)
        return response

    def remove_a_label_from_an_issue(self, owner, repo, issue_number, name, payload=None):
        # pylint: disable=too-many-arguments
        """
        Remove a label from an issue
        https://docs.github.com/rest/reference/issues#remove-a-label-from-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}"
        response = self._execute("delete", url, payload)
        return response

    def lock_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Lock an issue
        https://docs.github.com/rest/reference/issues#lock-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/lock"
        response = self._execute("put", url, payload)
        return response

    def unlock_an_issue(self, owner, repo, issue_number, payload=None):
        """
        Unlock an issue
        https://docs.github.com/rest/reference/issues#unlock-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/lock"
        response = self._execute("delete", url, payload)
        return response

    def list_timeline_events_for_an_issue(self, owner, repo, issue_number, payload=None):
        """
        List timeline events for an issue
        https://docs.github.com/rest/reference/issues#list-timeline-events-for-an-issue
        Attributes:
        Path Parameters:
        owner
        repo
        issue_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/issues/{issue_number}/timeline"
        response = self._execute("get", url, payload)
        return response

    def list_labels_for_a_repository(self, owner, repo, payload=None):
        """
        List labels for a repository
        https://docs.github.com/rest/reference/issues#list-labels-for-a-repository
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels"
        response = self._execute("get", url, payload)
        return response

    def create_a_label(self, owner, repo, payload=None):
        """
        Create a label
        https://docs.github.com/rest/reference/issues#create-a-label
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels"
        response = self._execute("post", url, payload)
        return response

    def get_a_label(self, owner, repo, name, payload=None):
        """
        Get a label
        https://docs.github.com/rest/reference/issues#get-a-label
        Attributes:
        Path Parameters:
        owner
        repo
        name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels/{name}"
        response = self._execute("get", url, payload)
        return response

    def update_a_label(self, owner, repo, name, payload=None):
        """
        Update a label
        https://docs.github.com/rest/reference/issues#update-a-label
        Attributes:
        Path Parameters:
        owner
        repo
        name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels/{name}"
        response = self._execute("patch", url, payload)
        return response

    def delete_a_label(self, owner, repo, name, payload=None):
        """
        Delete a label
        https://docs.github.com/rest/reference/issues#delete-a-label
        Attributes:
        Path Parameters:
        owner
        repo
        name
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/labels/{name}"
        response = self._execute("delete", url, payload)
        return response

    def list_milestones(self, owner, repo, payload=None):
        """
        List milestones
        https://docs.github.com/rest/reference/issues#list-milestones
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        state
         sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones"
        response = self._execute("get", url, payload)
        return response

    def create_a_milestone(self, owner, repo, payload=None):
        """
        Create a milestone
        https://docs.github.com/rest/reference/issues#create-a-milestone
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones"
        response = self._execute("post", url, payload)
        return response

    def get_a_milestone(self, owner, repo, milestone_number, payload=None):
        """
        Get a milestone
        https://docs.github.com/rest/reference/issues#get-a-milestone
        Attributes:
        Path Parameters:
        owner
        repo
        milestone_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
        response = self._execute("get", url, payload)
        return response

    def update_a_milestone(self, owner, repo, milestone_number, payload=None):
        """
        Update a milestone
        https://docs.github.com/rest/reference/issues#update-a-milestone
        Attributes:
        Path Parameters:
        owner
        repo
        milestone_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
        response = self._execute("patch", url, payload)
        return response

    def delete_a_milestone(self, owner, repo, milestone_number, payload=None):
        """
        Delete a milestone
        https://docs.github.com/rest/reference/issues#delete-a-milestone
        Attributes:
        Path Parameters:
        owner
        repo
        milestone_number
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
        response = self._execute("delete", url, payload)
        return response

    def list_labels_for_issues_in_a_milestone(self, owner, repo, milestone_number, payload=None):
        """
        List labels for issues in a milestone
        https://docs.github.com/rest/reference/issues#list-labels-for-issues-in-a-milestone
        Attributes:
        Path Parameters:
        owner
        repo
        milestone_number
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/milestones/{milestone_number}/labels"
        response = self._execute("get", url, payload)
        return response

    def list_user_account_issues_assigned_to_the_authenticated_user(self, payload=None):
        """
        List user account issues assigned to the authenticated user
        https://docs.github.com/rest/reference/issues#list-user-account-issues-assigned-to-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        filter
         state
         labels
         sort
         direction
         since
         per-page
         page
        """
        url = self._base_url + "/user/issues"
        response = self._execute("get", url, payload)
        return response
