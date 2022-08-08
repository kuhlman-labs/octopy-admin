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
        audit_log_query = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
            enterprise=enterprise,
            params={"page": "1", "per_page": "100", "phrase": "action:protected_branch"},
        )
        requests = github.paginate_request(audit_log_query)
        return requests
    except RestClientError as err:
        print(err)


def get_last_five_minutes_branch_protection_aduit_log_events(enterprise):
    """
    Get the branch protection audit log events for last five minutes
    for an enterprise and write to json file.
    """
    try:
        responses = get_branch_protection_aduit_log_events(enterprise)
        events = []
        for response in responses:
            for event in response:
                for key, value in event.items():
                    if key == "created_at":
                        current_time = datetime.datetime.utcnow()
                        created_at = datetime.datetime.utcfromtimestamp(value / 1000).strftime(
                            "%Y-%m-%d %H:%M:%S.%f"
                        )
                        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f")
                        if current_time - created_at < datetime.timedelta(minutes=5):
                            events.append(event)
        with open("branch_protection_audit_log_events.json", "w") as outfile:
            json.dump(events, outfile, indent=4)
    except RestClientError as err:
        print(err)
