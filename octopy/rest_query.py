import os

import requests


class RestRequestError(Exception):
    pass


class RestRequest:
    def __init__(self):
        if os.environ.get("API_TOKEN") is None:
            raise RestRequestError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {os.environ.get('API_TOKEN')}"}
        self._base_url = os.environ.get("REST_API_URL", r"https://api.github.com")

    def _execute(self, method, url, payload):
        try:
            response = requests.request(method=method, url=url, json=payload, headers=self._headers)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise RestRequestError(errtimeout)
        except requests.exceptions.HTTPError as errhttp:
            raise RestRequestError(errhttp)
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestRequestError(errredirect)
        except requests.exceptions.RequestException as errexcept:
            raise RestRequestError(errexcept)


class RestPostProducer(RestRequest):
    def __init__(self):
        super().__init__()
        self._method = "Post"

    def create_user(self, user):
        url = self._base_url + "/admin/users"
        payload = {"login": user.get("login"), "email": user.get("email")}
        response = self._execute(self._method, url, payload)
        return print(response.json())


class RestPatchProducer(RestRequest):
    def __init__(self):
        super().__init__()
        self._method = "Patch"

    def update_repo_webhook_url(self, owner, repo, hook_id, new_url):
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}/config"
        payload = {"url": new_url}
        response = self._execute(self._method, url, payload)
        return print(response.json())

    def update_org_webhook_url(self, owner, hook_id, new_url):
        url = self._base_url + f"/orgs/{owner}/hooks/{hook_id}/config"
        payload = {"url": new_url}
        response = self._execute(self._method, url, payload)
        return print(response.json())


class RestGetProvider(RestRequest):
    def __init__(self):
        super().__init__()
        self._method = "Get"

    def get_user(self, user):
        url = self._base_url + f"/users/{user}"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_org(self, org):
        url = self._base_url + f"/orgs/{org}"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_repo(self, owner, repo):
        url = self._base_url + f"/repos/{owner}/{repo}"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_repo_list(self, owner):
        url = self._base_url + f"/orgs/{owner}/repos"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_collaborators_permission_list(self, owner, repo):
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_collaborator_permission(self, owner, repo, user):
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators/{user}"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_collaborator_permission_list(self, owner, repo):
        url = self._base_url + f"/repos/{owner}/{repo}/collaborators"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_repo_webhook_list(self, owner, repo):
        url = self._base_url + f"/repos/{owner}/{repo}/hooks"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_org_webhook_list(self, org):
        url = self._base_url + f"/orgs/{org}/hooks"
        response = self._execute(self._method, url, None)
        return response.json()

    def get_repo_webhook(self, owner, repo, hook_id):
        url = self._base_url + f"/repos/{owner}/{repo}/hooks/{hook_id}"
        response = self._execute(self._method, url, None)
        return print(response.json())

    def get_org_webhook(self, org, hook_id):
        url = self._base_url + f"/orgs/{org}/hooks/{hook_id}"
        response = self._execute(self._method, url, None)
        return response.json()
