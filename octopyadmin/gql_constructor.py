from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError
import os


class GitHubGQLConstructorError(Exception):
    pass


class GitHubGQLConstructor:
    def __init__(self):
        headers = {"Authorization": f"Bearer {os.environ['API_TOKEN']}"}
        transport = AIOHTTPTransport(url=os.environ["GQL_API_URL"], headers=headers)
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def _load_query(self, path):
        absolute_path = os.path.dirname(__file__)
        relative_path = path
        full_path = os.path.join(absolute_path, relative_path)
        with open(full_path) as f:
            return gql(f.read())

    def _execute(self, query, params):
        try:
            return self._client.execute(query, variable_values=params)
        except TransportQueryError as err:
            raise GitHubGQLConstructorError(err.errors[0]["message"])

    def add_enterprise_org(self, organization):
        params = {"organization": organization}
        query = self._load_query(os.path.abspath("gql_queries/create-enterprise-org.gql"))
        result = self._execute(query, params)
        return print(result)

    def add_repository(self, repository):
        params = {"repository": repository}
        query = self._load_query("gql_queries/create-repository.gql")
        result = self._execute(query, params)
        return print(result)
