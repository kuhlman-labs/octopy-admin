from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class GitHubConstructorError(Exception):
    pass


class GitHubConstructor:
    def __init__(SELF, CONF):
        HEADERS = {"Authorization": f"Bearer {CONF['GQL_API_TOKEN']}"}
        TRANSPORT = AIOHTTPTransport(url=CONF["GQL_API_URL"], headers=HEADERS)
        SELF._client = Client(transport=TRANSPORT)

    def _load_query(SELF, PATH):
        with open(PATH) as F:
            return gql(F.read())

    def _execute(SELF, QUERY, PARAMS):
        try:
            return SELF._client.execute(QUERY, variable_values=PARAMS)
        except TransportQueryError as ERR:
            raise GitHubConstructorError(ERR.errors[0]["message"])

    def add_enterprise_org(SELF, ORGANIZATION):
        PARAMS = {"organization": ORGANIZATION}
        QUERY = SELF._load_query("graphql/create-enterprise-org.gql")
        RESULT = SELF._execute(QUERY, PARAMS)
        return print(RESULT)

    def remove_enterprise_org():
        pass
