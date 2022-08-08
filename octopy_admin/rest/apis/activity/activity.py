"""
Activity APIs provide access to notifications, subscriptions, and timelines.
"""


# pylint: disable=too-many-arguments
class Activity:
    # pylint: disable=too-many-public-methods
    """
    Activity APIs provide access to notifications, subscriptions, and timelines.
    """

    def __init__(self, client):
        """
        Initialize the Activity class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_public_events(self, params=None, payload=None):
        """
        List public events
        https://docs.github.com/rest/reference/activity#list-public-events
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_feeds(self, params=None, payload=None):
        """
        Get feeds
        https://docs.github.com/rest/reference/activity#get-feeds
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/feeds"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_events_for_a_network_of_repositories(
        self, owner, repo, params=None, payload=None
    ):
        """
        List public events for a network of repositories
        https://docs.github.com/rest/reference/activity#list-public-events-for-a-network-of-repositories
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/networks/{owner}/{repo}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_notifications_for_the_authenticated_user(self, params=None, payload=None):
        """
        List notifications for the authenticated user
        https://docs.github.com/rest/reference/activity#list-notifications-for-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        all
         participating
         since
         before
         per-page
         page
        """
        url = self._base_url + "/notifications"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def mark_notifications_as_read(self, params=None, payload=None):
        """
        Mark notifications as read
        https://docs.github.com/rest/reference/activity#mark-notifications-as-read
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/notifications"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_a_thread(self, thread_id, params=None, payload=None):
        """
        Get a thread
        https://docs.github.com/rest/reference/activity#get-a-thread
        Attributes:
        Path Parameters:
        thread_id
        Payload Parameters:

        """
        url = self._base_url + f"/notifications/threads/{thread_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def mark_a_thread_as_read(self, thread_id, params=None, payload=None):
        """
        Mark a thread as read
        https://docs.github.com/rest/reference/activity#mark-a-thread-as-read
        Attributes:
        Path Parameters:
        thread_id
        Payload Parameters:

        """
        url = self._base_url + f"/notifications/threads/{thread_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_a_thread_subscription_for_the_authenticated_user(
        self, thread_id, params=None, payload=None
    ):
        """
        Get a thread subscription for the authenticated user
        https://docs.github.com/rest/reference/activity#get-a-thread-subscription-for-the-authenticated-user
        Attributes:
        Path Parameters:
        thread_id
        Payload Parameters:

        """
        url = self._base_url + f"/notifications/threads/{thread_id}/subscription"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_a_thread_subscription(self, thread_id, params=None, payload=None):
        """
        Set a thread subscription
        https://docs.github.com/rest/reference/activity#set-a-thread-subscription
        Attributes:
        Path Parameters:
        thread_id
        Payload Parameters:

        """
        url = self._base_url + f"/notifications/threads/{thread_id}/subscription"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_thread_subscription(self, thread_id, params=None, payload=None):
        """
        Delete a thread subscription
        https://docs.github.com/rest/reference/activity#delete-a-thread-subscription
        Attributes:
        Path Parameters:
        thread_id
        Payload Parameters:

        """
        url = self._base_url + f"/notifications/threads/{thread_id}/subscription"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_public_organization_events(self, org, params=None, payload=None):
        """
        List public organization events
        https://docs.github.com/rest/reference/activity#list-public-organization-events
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_events(self, owner, repo, params=None, payload=None):
        """
        List repository events
        https://docs.github.com/rest/reference/activity#list-repository-events
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_notifications_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        List repository notifications for the authenticated user
        https://docs.github.com/rest/reference/activity#list-repository-notifications-for-the-authenticated-user
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        all
         participating
         since
         before
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/notifications"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def mark_repository_notifications_as_read(self, owner, repo, params=None, payload=None):
        """
        Mark repository notifications as read
        https://docs.github.com/rest/reference/activity#mark-repository-notifications-as-read
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/notifications"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_stargazers(self, owner, repo, params=None, payload=None):
        """
        List stargazers
        https://docs.github.com/rest/reference/activity#list-stargazers
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stargazers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_watchers(self, owner, repo, params=None, payload=None):
        """
        List watchers
        https://docs.github.com/rest/reference/activity#list-watchers
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscribers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_subscription(self, owner, repo, params=None, payload=None):
        """
        Get a repository subscription
        https://docs.github.com/rest/reference/activity#get-a-repository-subscription
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscription"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_a_repository_subscription(self, owner, repo, params=None, payload=None):
        """
        Set a repository subscription
        https://docs.github.com/rest/reference/activity#set-a-repository-subscription
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscription"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_subscription(self, owner, repo, params=None, payload=None):
        """
        Delete a repository subscription
        https://docs.github.com/rest/reference/activity#delete-a-repository-subscription
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscription"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_starred_by_the_authenticated_user(self, params=None, payload=None):
        """
        List repositories starred by the authenticated user
        https://docs.github.com/rest/reference/activity#list-repositories-starred-by-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        sort
         direction
         per-page
         page
        """
        url = self._base_url + "/user/starred"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_repository_is_starred_by_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Check if a repository is starred by the authenticated user
        https://docs.github.com/rest/reference/activity#check-if-a-repository-is-starred-by-the-authenticated-user
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/user/starred/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def star_a_repository_for_the_authenticated_user(self, owner, repo, params=None, payload=None):
        """
        Star a repository for the authenticated user
        https://docs.github.com/rest/reference/activity#star-a-repository-for-the-authenticated-user
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/user/starred/{owner}/{repo}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unstar_a_repository_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Unstar a repository for the authenticated user
        https://docs.github.com/rest/reference/activity#unstar-a-repository-for-the-authenticated-user
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/user/starred/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_watched_by_the_authenticated_user(self, params=None, payload=None):
        """
        List repositories watched by the authenticated user
        https://docs.github.com/rest/reference/activity#list-repositories-watched-by-the-authenticated-user
        Attributes:
        Path Parameters:

        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + "/user/subscriptions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_events_for_the_authenticated_user(self, username, params=None, payload=None):
        """
        List events for the authenticated user
        https://docs.github.com/rest/reference/activity#list-events-for-the-authenticated-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_events_for_the_authenticated_user(
        self, username, org, params=None, payload=None
    ):
        """
        List organization events for the authenticated user
        https://docs.github.com/rest/reference/activity#list-organization-events-for-the-authenticated-user
        Attributes:
        Path Parameters:
        username
        org
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/events/orgs/{org}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_events_for_a_user(self, username, params=None, payload=None):
        """
        List public events for a user
        https://docs.github.com/rest/reference/activity#list-public-events-for-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/events/public"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_events_received_by_the_authenticated_user(self, username, params=None, payload=None):
        """
        List events received by the authenticated user
        https://docs.github.com/rest/reference/activity#list-events-received-by-the-authenticated-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/received_events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_events_received_by_a_user(self, username, params=None, payload=None):
        """
        List public events received by a user
        https://docs.github.com/rest/reference/activity#list-public-events-received-by-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/received_events/public"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_starred_by_a_user(self, username, params=None, payload=None):
        """
        List repositories starred by a user
        https://docs.github.com/rest/reference/activity#list-repositories-starred-by-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        sort
         direction
         per-page
         page
        """
        url = self._base_url + f"/users/{username}/starred"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_watched_by_a_user(self, username, params=None, payload=None):
        """
        List repositories watched by a user
        https://docs.github.com/rest/reference/activity#list-repositories-watched-by-a-user
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/users/{username}/subscriptions"
        response = self._execute("get", url, params=params, payload=payload)
        return response
