from gql import Client, gql
from gql.dsl import DSLQuery, DSLSchema, dsl_gql, DSLVariableDefinitions
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError, TransportServerError


class GitHubGQLProviderError(Exception):
    pass


class GitHubGQLProvider:
    def __init__(self, conf):
        headers = {"Authorization": f"Bearer {conf['GQL_API_TOKEN']}"}
        transport = AIOHTTPTransport(url=conf["GQL_API_URL"], headers=headers)
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def get_enterprise_orgs(self, enterprise):
        query = self._load_query("graphql/get-enterprise-orgs.gql")
        params = {"slug": enterprise, "cursor": None}
        return self._paginate_results(query, params)
    
    def test(self, enterprise):
        params = {"slug": enterprise, "cursor": None}
        ds = DSLSchema(self._client.schema)
        var= DSLVariableDefinitions()        
        op = DSLQuery(
                ds.Query.enterprise.args(slug=var.slug).select(
                    ds.Enterprise.name,
                    ds.Enterprise.organizations.args(first=1, after=var.cursor).select(
                        ds.OrganizationConnection.pageInfo.select(
                            ds.PageInfo.hasNextPage,
                            ds.PageInfo.endCursor
                        ),
                        ds.OrganizationConnection.nodes.select(
                            ds.Organization.name,
                    )  
                )
            )
        )
        op.variable_definitions = var
        query = dsl_gql(op)       
        return self._paginate_results(query, params)

    def get_org_repos(self, org):
        query = self._load_query("graphql/get-org-repos.gql")
        params = {"organization": org, "cursor": None}
        return self._paginate_results(query, params)

    def get_repo_collaborators(self, org, repo):
        query = self._load_query("graphql/get-repo-collaborators.gql")
        params = {"owner": org, "name": repo, "cursor": None}
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
            next_page = page_info["hasNextPage"]
            cursor = page_info["endCursor"]
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
        except TransportServerError as errserver:
            raise GitHubGQLProviderError("Server responded with a " + str(errserver.code) + " status code")
