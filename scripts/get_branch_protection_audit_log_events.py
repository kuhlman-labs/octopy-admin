import datetime
import json

from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
github = RestClient()


def get_repo_branch_protection_aduit_log_events(enterprise, repo):
    """
    Get the repo's branch protection audit log events
    for the last five minutes. Output is a list of dictionaries.
    """
    try:
        current_time = datetime.datetime.now()
        time_of_event = current_time - datetime.timedelta(minutes=5)
        time_of_event = time_of_event.isoformat("T", "seconds") + "+00:00"
        audit_log_query = github.enterprise_admin.get_the_audit_log_for_an_enterprise(
            enterprise=enterprise,
            params={
                "page": "1",
                "per_page": "100",
                "phrase": f"action:protected_branch repo:{repo} created:>={time_of_event}",
            },
        )
        responses = github.paginate_request(audit_log_query)
        events = []
        for response in responses:
            for event in response:
                events.append(event)
        return events
    except RestClientError as e:
        print(e)


repo_events = get_repo_branch_protection_aduit_log_events(enterprise="", repo="")

with open("branch_protection_audit_log_events.json", "w") as outfile:
    json.dump(repo_events, outfile, indent=4)
