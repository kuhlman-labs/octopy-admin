import requests

class GitHubConstructorRestError(Exception):
    pass

class GitHubRestConstructor:
    def __init__(SELF, CONF):
        SELF.HEADERS = {"Authorization": f"Bearer {CONF['GQL_API_TOKEN']}"}
        SELF.BASE_URL = "https://"+ CONF["URL_SLUG"] + "/api/v3/"
    
    def create_user(SELF, USER):
        URL = SELF.BASE_URL + "admin/users"
        PAYLOAD = {
            "login": USER["login"],
            "email": USER["email"]
        }
        RESPONSE = SELF._execute(URL, PAYLOAD)
        return print(RESPONSE.json())

    def _execute(SELF, URL, PAYLOAD):
        try:
            RESPONSE = requests.request("POST", URL, json=PAYLOAD, headers=SELF.HEADERS)
            RESPONSE.raise_for_status()
            return RESPONSE                   
        except requests.exceptions.Timeout as ERRTIMEOUT:
                raise GitHubConstructorRestError(ERRTIMEOUT)
        except requests.exceptions.HTTPError as ERRHTTP:
                raise GitHubConstructorRestError(ERRHTTP)
        except requests.exceptions.TooManyRedirects as ERRREDIRECT:
                raise GitHubConstructorRestError(ERRREDIRECT)
        except requests.exceptions.RequestException as ERR:
                raise GitHubConstructorRestError(ERR)
