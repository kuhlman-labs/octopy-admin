import datetime
import json

from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def get_branch_protection_aduit_log_events(enterprise):
    """
    Get all the branch protection audit log events for an enterprise.
    """
    try:
        results = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
            enterprise=enterprise,
            params={"page": "1", "per_page": "100", "phrase": "action:protected_branch"},
        )
        if results.links.get("next") is None and results:
            yield results.json()
        while results.links.get("next"):
            next_page = int(
                results.links.get("next").get("url").split("page=")[1].replace("&per_", "")
            )
            results = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
                enterprise=enterprise,
                params={
                    "page": str(next_page),
                    "per_page": "100",
                    "phrase": "action:protected_branch",
                },
            )
            yield results.json()
    except RestClientError as err:
        print(err)


def get_last_five_minutes_branch_protection_aduit_log_events(enterprise):
    """
    Get the branch protection audit log events for last five minutes
    for an enterprise and write to json file.
    """
    try:
        results = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
            enterprise=enterprise,
            params={"page": "1", "per_page": "100", "phrase": "action:protected_branch"},
        )
        results = results.json()
        events = []
        for result in results:
            for key, value in result.items():
                if key == "created_at":
                    current_time = datetime.datetime.utcnow()
                    created_at = datetime.datetime.utcfromtimestamp(value / 1000).strftime(
                        "%Y-%m-%d %H:%M:%S.%f"
                    )
                    created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f")
                    if current_time - created_at < datetime.timedelta(minutes=5):
                        events.append(result)
        with open("branch_protection_audit_log_events.json", "w") as outfile:
            json.dump(events, outfile, indent=4)
    except RestClientError as err:
        print(err)
