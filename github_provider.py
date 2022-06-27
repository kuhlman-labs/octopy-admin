from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class GitHubProviderError(Exception):
    pass


class GitHubProvider:
    def __init__(SELF, CONF):
        HEADERS = {"Authorization": f"Bearer {CONF['GQL_API_TOKEN']}"}
        TRANSPORT = AIOHTTPTransport(url=CONF["GQL_API_URL"], headers=HEADERS)
        SELF._client = Client(transport=TRANSPORT)

    def get_enterprise_orgs(SELF, ENTERPRISE):
        QUERY = SELF._load_query("graphql/get-enterprise-orgs.gql")
        CURSOR = None
        while True:
            PARAMS = {"slug": ENTERPRISE, "orgcursor": CURSOR}
            RESULT = SELF._execute(QUERY, PARAMS)
            CURSOR = RESULT["enterprise"]["organizations"]["pageInfo"]["endCursor"]
            NEXT_PAGE = RESULT["enterprise"]["organizations"]["pageInfo"]["hasNextPage"]
            ORGS = RESULT["enterprise"]["organizations"]["edges"]
            for ORG in ORGS:
                yield ORG["node"]
            if not NEXT_PAGE:
                return

    def get_org_repos(SELF, ORG):
        QUERY = SELF._load_query("graphql/get-org-repos.gql")
        CURSOR = None
        while True:
            PARAMS = {"organization": ORG, "repocursor": CURSOR}
            RESULT = SELF._execute(QUERY, PARAMS)
            CURSOR = RESULT["organization"]["repositories"]["pageInfo"]["endCursor"]
            NEXT_PAGE = RESULT["organization"]["repositories"]["pageInfo"][
                "hasNextPage"
            ]
            REPOS = RESULT["organization"]["repositories"]["edges"]
            for REPO in REPOS:
                yield REPO["node"]
            if not NEXT_PAGE:
                return

    def get_repo_collaborators(SELF, ORG, REPO):
        QUERY = SELF._load_query("graphql/get-repo-collaborators.gql")
        CURSOR = None
        while True:
            PARAMS = {"owner": ORG, "name": REPO, "collabcursor": CURSOR}
            RESULT = SELF._execute(QUERY, PARAMS)
            CURSOR = RESULT["repository"]["collaborators"]["pageInfo"]["endCursor"]
            NEXT_PAGE = RESULT["repository"]["collaborators"]["pageInfo"]["hasNextPage"]
            COLLABORATORS = RESULT["repository"]["collaborators"]["edges"]
            for COLLABORATOR in COLLABORATORS:
                yield COLLABORATOR
            if not NEXT_PAGE:
                return

    def _load_query(SELF, PATH):
        with open(PATH) as F:
            return gql(F.read())

    def _execute(SELF, QUERY, PARAMS):
        try:
            return SELF._client.execute(QUERY, variable_values=PARAMS)
        except TransportQueryError as ERR:
            raise GitHubProviderError(ERR.errors[0]["message"])
