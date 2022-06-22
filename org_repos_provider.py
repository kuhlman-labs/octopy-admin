from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class OrgReposProviderError(Exception):
    pass


class OrgReposProvider:
    def __init__(SELF, CONF):
        HEADERS = {"Authorization": f"Bearer {CONF['DEST_TOKEN']}"}
        TRANSPORT = AIOHTTPTransport(url=CONF["DEST_URL"], headers=HEADERS)
        SELF._client = Client(transport=TRANSPORT)
        SELF._sku_query = SELF._load_query("graphql/get-org-repos.gql")

    def get_org_repos(SELF, ORG):
        REPO_CURSOR = None
        while True:
            PARAMS = {"organization": ORG, "repocursor": REPO_CURSOR}
            RESULT = SELF._execute(SELF._sku_query, PARAMS)
            REPO_CURSOR = RESULT["organization"]["repositories"]["pageInfo"][
                "endCursor"
            ]
            HAS_NEXT_PAGE = RESULT["organization"]["repositories"]["pageInfo"][
                "hasNextPage"
            ]
            REPOS = RESULT["organization"]["repositories"]["edges"]
            for REPO in REPOS:
                yield REPO["node"]
            if not HAS_NEXT_PAGE:
                return

    def _load_query(SELF, PATH):
        with open(PATH) as F:
            return gql(F.read())

    def _execute(SELF, QUERY, VARIABLE_VALUES):
        try:
            return SELF._client.execute(QUERY, variable_values=VARIABLE_VALUES)
        except TransportQueryError as ERR:
            raise OrgReposProviderError(ERR.errors[0]["message"])
