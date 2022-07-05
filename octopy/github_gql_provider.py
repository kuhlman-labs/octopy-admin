from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class GitHubGQLProviderError(Exception):
    pass


class GitHubGQLProvider:
    def __init__(self, conf):
        headers = {"Authorization": f"Bearer {conf['GQL_API_TOKEN']}"}
        transport = AIOHTTPTransport(url=conf["GQL_API_URL"], headers=headers)
        self._client = Client(transport=transport)

    def get_enterprise_orgs(self, enterprise):
        query = self._load_query("graphql/get-enterprise-orgs.gql")
        cursor = None
        while True:
            params = {"slug": enterprise, "orgcursor": cursor}
            result = self._execute(query, params)
            cursor = result["enterprise"]["organizations"]["pageInfo"]["endCursor"]
            next_page = result["enterprise"]["organizations"]["pageInfo"]["hasNextPage"]
            orgs = result["enterprise"]["organizations"]["edges"]
            for org in orgs:
                yield org["node"]
            if not next_page:
                return

    def get_org_repos(self, org):
        query = self._load_query("graphql/get-org-repos.gql")
        cursor = None
        while True:
            params = {"organization": org, "repocursor": cursor}
            result = self._execute(query, params)
            cursor = result["organization"]["repositories"]["pageInfo"]["endCursor"]
            next_page = result["organization"]["repositories"]["pageInfo"]["hasNextPage"]
            repos = result["organization"]["repositories"]["edges"]
            for repo in repos:
                yield repo["node"]
            if not next_page:
                return

    def get_repo_collaborators(self, org, repo):
        query = self._load_query("graphql/get-repo-collaborators.gql")
        cursor = None
        while True:
            params = {"owner": org, "name": repo, "collabcursor": cursor}
            result = self._execute(query, params)
            cursor = result["repository"]["collaborators"]["pageInfo"]["endCursor"]
            next_page = result["repository"]["collaborators"]["pageInfo"]["hasNextPage"]
            collaborators = result["repository"]["collaborators"]["edges"]
            for collaborator in collaborators:
                yield collaborator
            if not next_page:
                return

    def test_get_enterprise_orgs(self, enterprise):
        query = self._load_query("graphql/get-enterprise-orgs.gql")
        params = {"slug": enterprise, "cursor": None}
        return self._paginate_results(query, params)

    def _get_page_info(self, results):
        if not results.get("pageInfo"):
            for key, item in results.items():
                if isinstance(item, dict):
                    if not item.get("pageInfo"):
                        results = item
                        return self._get_page_info(results)
                    else:
                        return item["pageInfo"]
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

    def _load_query(self, path):
        with open(path) as f:
            return gql(f.read())

    def _execute(self, query, params):
        try:
            return self._client.execute(query, variable_values=params)
        except TransportQueryError as err:
            raise GitHubGQLProviderError(err.errors[0]["message"])
