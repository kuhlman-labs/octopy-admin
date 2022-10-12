"""
Activity APIs provide access to notifications, subscriptions, and timelines.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Activity:
    """
    Activity APIs provide access to notifications, subscriptions, and timelines.
    """

    def __init__(self, client):
        """
        Initializes the Activity class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_public_events(self, params=None, payload=None):
        """
        Summary:
        List public events
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-public-events
        """
        url = self._base_url + "/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_feeds(self, params=None, payload=None):
        """
        Summary:
        Get feeds
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#get-feeds
        """
        url = self._base_url + "/feeds"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_events_for_a_network_of_repositories(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        List public events for a network of repositories
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-public-events-for-a-network-of-repositories
        """
        url = self._base_url + f"/networks/{owner}/{repo}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_notifications_for_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List notifications for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-notifications-for-the-authenticated-user
        """
        url = self._base_url + "/notifications"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def mark_notifications_as_read(self, params=None, payload=None):
        """
        Summary:
        Mark notifications as read
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#mark-notifications-as-read
        """
        url = self._base_url + "/notifications"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def get_a_thread(self, thread_id, params=None, payload=None):
        """
        Summary:
        Get a thread
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#get-a-thread
        """
        url = self._base_url + f"/notifications/threads/{thread_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def mark_a_thread_as_read(self, thread_id, params=None, payload=None):
        """
        Summary:
        Mark a thread as read
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#mark-a-thread-as-read
        """
        url = self._base_url + f"/notifications/threads/{thread_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def get_a_thread_subscription_for_the_authenticated_user(
        self, thread_id, params=None, payload=None
    ):
        """
        Summary:
        Get a thread subscription for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#get-a-thread-subscription-for-the-authenticated-user
        """
        url = self._base_url + f"/notifications/threads/{thread_id}/subscription"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_a_thread_subscription(self, thread_id, params=None, payload=None):
        """
        Summary:
        Set a thread subscription
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#set-a-thread-subscription
        """
        url = self._base_url + f"/notifications/threads/{thread_id}/subscription"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_thread_subscription(self, thread_id, params=None, payload=None):
        """
        Summary:
        Delete a thread subscription
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#delete-a-thread-subscription
        """
        url = self._base_url + f"/notifications/threads/{thread_id}/subscription"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_public_organization_events(self, org, params=None, payload=None):
        """
        Summary:
        List public organization events
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-public-organization-events
        """
        url = self._base_url + f"/orgs/{org}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_events(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository events
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-repository-events
        """
        url = self._base_url + f"/repos/{owner}/{repo}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repository_notifications_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        List repository notifications for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-repository-notifications-for-the-authenticated-user
        """
        url = self._base_url + f"/repos/{owner}/{repo}/notifications"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def mark_repository_notifications_as_read(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Mark repository notifications as read
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#mark-repository-notifications-as-read
        """
        url = self._base_url + f"/repos/{owner}/{repo}/notifications"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def list_stargazers(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List stargazers
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-stargazers
        """
        url = self._base_url + f"/repos/{owner}/{repo}/stargazers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_watchers(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List watchers
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-watchers
        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscribers"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def get_a_repository_subscription(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Get a repository subscription
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#get-a-repository-subscription
        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscription"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def set_a_repository_subscription(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Set a repository subscription
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#set-a-repository-subscription
        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscription"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def delete_a_repository_subscription(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Delete a repository subscription
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#delete-a-repository-subscription
        """
        url = self._base_url + f"/repos/{owner}/{repo}/subscription"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_starred_by_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List repositories starred by the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-repositories-starred-by-the-authenticated-user
        """
        url = self._base_url + "/user/starred"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def check_if_a_repository_is_starred_by_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Check if a repository is starred by the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#check-if-a-repository-is-starred-by-the-authenticated-user
        """
        url = self._base_url + f"/user/starred/{owner}/{repo}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def star_a_repository_for_the_authenticated_user(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Star a repository for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#star-a-repository-for-the-authenticated-user
        """
        url = self._base_url + f"/user/starred/{owner}/{repo}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def unstar_a_repository_for_the_authenticated_user(
        self, owner, repo, params=None, payload=None
    ):
        """
        Summary:
        Unstar a repository for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#unstar-a-repository-for-the-authenticated-user
        """
        url = self._base_url + f"/user/starred/{owner}/{repo}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_repositories_watched_by_the_authenticated_user(self, params=None, payload=None):
        """
        Summary:
        List repositories watched by the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-repositories-watched-by-the-authenticated-user
        """
        url = self._base_url + "/user/subscriptions"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_events_for_the_authenticated_user(self, username, params=None, payload=None):
        """
        Summary:
        List events for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-events-for-the-authenticated-user
        """
        url = self._base_url + f"/users/{username}/events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_organization_events_for_the_authenticated_user(
        self, username, org, params=None, payload=None
    ):
        """
        Summary:
        List organization events for the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-organization-events-for-the-authenticated-user
        """
        url = self._base_url + f"/users/{username}/events/orgs/{org}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_events_for_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List public events for a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-public-events-for-a-user
        """
        url = self._base_url + f"/users/{username}/events/public"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_events_received_by_the_authenticated_user(self, username, params=None, payload=None):
        """
        Summary:
        List events received by the authenticated user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-events-received-by-the-authenticated-user
        """
        url = self._base_url + f"/users/{username}/received_events"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_public_events_received_by_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List public events received by a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-public-events-received-by-a-user
        """
        url = self._base_url + f"/users/{username}/received_events/public"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_starred_by_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List repositories starred by a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-repositories-starred-by-a-user
        """
        url = self._base_url + f"/users/{username}/starred"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_repositories_watched_by_a_user(self, username, params=None, payload=None):
        """
        Summary:
        List repositories watched by a user
        Docs:
        https://docs.github.com/enterprise-server@3.6/rest/reference/activity#list-repositories-watched-by-a-user
        """
        url = self._base_url + f"/users/{username}/subscriptions"
        response = self._execute("get", url, params=params, payload=payload)
        return response
