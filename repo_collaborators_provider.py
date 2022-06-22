from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError


class RepoCollaboratorsProviderError(Exception):
    pass


class RepoCollaboratorsProvider:
    def __init__(SELF, CONF):
        HEADERS = {"Authorization": f"Bearer {CONF['DEST_TOKEN']}"}
        TRANSPORT = AIOHTTPTransport(url=CONF["DEST_URL"], headers=HEADERS)
        SELF._client = Client(transport=TRANSPORT)
        SELF._sku_query = SELF._load_query("graphql/get-repo-collaborators.gql")

    def get_repo_collaborators(SELF, ORG, REPO):
        COLLAB_CURSOR = None
        while True:
            PARAMS = {"owner": ORG, "name": REPO, "collabcursor": COLLAB_CURSOR}
            RESULT = SELF._execute(SELF._sku_query, PARAMS)
            COLLAB_CURSOR = RESULT["repository"]["collaborators"]["pageInfo"][
                "endCursor"
            ]
            HAS_NEXT_PAGE = RESULT["repository"]["collaborators"]["pageInfo"][
                "hasNextPage"
            ]
            COLLABORATORS = RESULT["repository"]["collaborators"]["edges"]
            for COLLABORATOR in COLLABORATORS:
                yield COLLABORATOR
            if not HAS_NEXT_PAGE:
                return

    def _load_query(SELF, PATH):
        with open(PATH) as F:
            return gql(F.read())

    def _execute(SELF, QUERY, VARIABLE_VALUES):
        try:
            return SELF._client.execute(QUERY, variable_values=VARIABLE_VALUES)
        except TransportQueryError as ERR:
            raise RepoCollaboratorsProviderError(ERR.errors[0]["message"])
