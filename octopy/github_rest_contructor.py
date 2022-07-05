import requests


class GitHubConstructorRestError(Exception):
    pass


class GitHubRestConstructor:
    def __init__(self, conf):
        self.headers = {"Authorization": f"Bearer {conf['GQL_API_TOKEN']}"}
        self.base_url = "https://" + conf["URL_SLUG"] + "/api/v3/"

    def create_user(self, user):
        url = self.base_url + "admin/users"
        payload = {"login": user["login"], "email": user["email"]}
        response = self._execute(url, payload)
        return print(response.json())

    def _execute(self, url, payload):
        try:
            response = requests.request("POST", url, json=payload, headers=self.headers)
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
