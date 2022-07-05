from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class GitHubGQLConstructorError(Exception):
    pass


class GitHubGQLConstructor:
    def __init__(self, conf):
        headers = {"Authorization": f"Bearer {conf['GQL_API_TOKEN']}"}
        transport = AIOHTTPTransport(url=conf["GQL_API_URL"], headers=headers)
        self._client = Client(transport=transport)

    def _load_query(self, path):
        with open(path) as f:
            return gql(f.read())

    def _execute(self, query, params):
        try:
            return self._client.execute(query, variable_values=params)
        except TransportQueryError as err:
            raise GitHubGQLConstructorError(err.errors[0]["message"])

    def add_enterprise_org(self, organization):
        params = {"organization": organization}
        query = self._load_query("graphql/create-enterprise-org.gql")
        result = self._execute(query, params)
        return print(result)

    def add_repository(self, repository):
        params = {"repository": repository}
        query = self._load_query("graphql/create-repository.gql")
        result = self._execute(query, params)
        return print(result)
