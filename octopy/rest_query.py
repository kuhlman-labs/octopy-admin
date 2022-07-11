import requests
import os

class RestQueryError(Exception):
    pass


class RestQuery:
    def __init__(self):
        if os.environ.get("API_TOKEN") is None:
            raise RestQueryError("API_TOKEN environment variable is not set")
        self._headers = {"Authorization": f"Bearer {os.environ.get('API_TOKEN')}"}
        self._base_url = os.environ.get('REST_API_URL', r'https://api.github.com')

    def _execute(self,method, url, payload):
        try:
            response = requests.request(method=method, url=url, json=payload, headers=self._headers)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as errtimeout:
            raise RestQueryError(errtimeout)
        except requests.exceptions.HTTPError as errhttp:
            raise RestQueryError(errhttp)
        except requests.exceptions.TooManyRedirects as errredirect:
            raise RestQueryError(errredirect)
        except requests.exceptions.RequestException as errexcept:
            raise RestQueryError(errexcept)

class RestQueryContructor(RestQuery):
    def __init__(self):
        super().__init__()
        self._method = "Post"
    
    def create_user(self, user):
        url = self._base_url + "/admin/users"
        payload = {"login": user.get("login"), "email": user.get("email")}
        response = self._execute(self._method,url, payload)
        return print(response.json())

