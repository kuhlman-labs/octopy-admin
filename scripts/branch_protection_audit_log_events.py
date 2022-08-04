from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def get_branch_protection_aduit_log_events(enterprise):
    """
    Get the branch protection audit log events for an enterprise.
    """
    try:
        results = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
            enterprise=enterprise,
            params={"page": "1", "per_page": "1", "phrase": "action:protected_branch"},
        )
        if results.links.get("next") is None:
            yield results.json()
        while results.links.get("next"):
            next_page = int(results.links.get("next").get("url").split("page=")[1][0])
            results = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
                enterprise=enterprise,
                params={
                    "page": str(next_page),
                    "per_page": "10",
                    "phrase": "action:protected_branch",
                },
            )
            yield results.json()
    except RestClientError as err:
        print(err)
