import requests
import os

class GitHubConstructorRestError(Exception):
    pass


class GitHubRestConstructor:
    def __init__(self):
        self._headers = {"Authorization": f"Bearer {os.environ.get('API_TOKEN')}"}
        self._base_url = os.environ.get('REST_API_URL')

    def create_user(self, user):
        url = self._base_url + "/admin/users"
        payload = {"login": user.get("login"), "email": user.get("email")}
        response = self._execute(url, payload)
        return print(response.json())

    def _execute(self, url, payload):
        try:
            response = requests.request("POST", url, json=payload, headers=self._headers)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise GitHubConstructorRestError(errtimeout)
        except requests.exceptions.HTTPError as errhttp:
            raise GitHubConstructorRestError(errhttp)
        except requests.exceptions.TooManyRedirects as errredirect:
            raise GitHubConstructorRestError(errredirect)
        except requests.exceptions.RequestException as err:
            raise GitHubConstructorRestError(err)
