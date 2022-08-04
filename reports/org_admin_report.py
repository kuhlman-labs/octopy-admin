from dotenv import load_dotenv

from octopy_admin.graph.graph_client import GraphClient, GraphClientError

load_dotenv()
github = GraphClient()


def get_org_admins(org):
    """
    Get the org admins for an org.
    """
    try:
        org_admins = []
        results = github.query.get_org_members(org)
        results = github.query.results_to_list(results)
        for result in results:
            if result.get("role") == "ADMIN":
                org_admins.append(result.get("node").get("login"))
        return org_admins
    except GraphClientError as err:
        print(err)
