import os

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError, TransportServerError


class GraphRequest:
    def __init__(self):
        if os.environ.get("API_TOKEN") is None:
            raise GraphRequestError("API_TOKEN environment variable is not set")
        headers = {"Authorization": f"Bearer {os.environ.get('API_TOKEN')}"}
        transport = AIOHTTPTransport(
            url=os.environ.get("GQL_API_URL", r"https://api.github.com/graphql"), headers=headers
        )
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
        except TransportQueryError as errquery:
            raise GraphRequestError(errquery.errors[0].get("message"))
        except TransportServerError as errserver:
            raise GraphRequestError(f"Server responded with a {str(errserver.code)} status code")


class GraphRequestError(Exception):
    pass


class GraphQueryProvider(GraphRequest):
    def __init__(self):
        super().__init__()

    def _get_page_info(self, results):
        if results.get("pageInfo") is None:
            for key, item in results.items():
                if isinstance(item, dict):
                    if item.get("pageInfo") is None:
                        results = item
                        return self._get_page_info(results)
                    else:
                        return item.get("pageInfo")
        else:
            return results.get("pageInfo")

    def _paginate_results(self, query, params):
        cursor = None
        while True:
            params["cursor"] = cursor
            results = self._execute(query, params)
            page_info = self._get_page_info(results)
            next_page = page_info.get("hasNextPage")
            cursor = page_info.get("endCursor")
            yield results
            if not next_page:
                return

    def get_enterprise_orgs(self, enterprise):
        query = self._load_query("gql_files/get-enterprise-orgs.gql")
        params = {"slug": enterprise, "cursor": None}
        return self._paginate_results(query, params)

    def get_org_repos(self, org):
        query = self._load_query("gql_files/get-org-repos.gql")
        params = {"organization": org, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_collaborators(self, org, repo):
        query = self._load_query("gql_files/get-repo-collaborators.gql")
        params = {"owner": org, "name": repo, "cursor": None}
        return self._paginate_results(query, params)


class GraphMutationProducer(GraphRequest):
    def __init__(self):
        super().__init__()

    def add_enterprise_org(self, organization):
        params = {"organization": organization}
        query = self._load_query("gql_files/create-enterprise-org.gql")
        result = self._execute(query, params)
        return print(result)

    def add_repository(self, repository):
        params = {"repository": repository}
        query = self._load_query("gql_files/create-repository.gql")
        result = self._execute(query, params)
        return print(result)


class GraphQueryResponseTransmuter(GraphQueryProvider):
    def __init__(self):
        super().__init__()

    def get_org_list(self, enterprise):
        org_list = list()
        try:
            org_results = self.get_enterprise_orgs(enterprise)
            for organizations in org_results:
                for org in organizations.get("enterprise").get("organizations").get("nodes"):
                    org_list.append(org.get("name"))
        except GraphRequestError as err:
            print(err)
        return org_list

    def get_repo_list(self, org):
        repo_list = list()
        try:
            repo_results = self.get_org_repos(org)
            for repositories in repo_results:
                for repo in repositories.get("organization").get("repositories").get("edges"):
                    repo_list.append(repo.get("node").get("name"))
        except GraphRequestError as err:
            print(err)
        return repo_list

    def get_collaborators_permission_list(self, org, repo):
        collaborator_list = list()
        try:
            collaborator_results = self.get_repo_collaborators(org, repo)
            for collaborators in collaborator_results:
                for collaborator in collaborators.get("repository").get("collaborators").get("edges"):
                    collaborator_list.append((collaborator.get("node").get("login"), collaborator.get("permission")))
        except GraphRequestError as err:
            print(err)
        return collaborator_list
