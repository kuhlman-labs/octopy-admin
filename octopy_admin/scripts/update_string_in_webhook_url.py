"""
These scripts are used to update a string in an existing webhook url to a new value.
"""
import os
import sys

from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


CONFIG = load_dotenv()

github = RestClient()


def replace_string_in_org_webhooks_url(org, string_to_replace, new_string):
    """
    Replace a string in an org's webhooks url.
    """
    try:
        webook_org_list = github.orgs.list_organization_webhooks(org)
        for webhook in webook_org_list:
            webhook_url = webhook.get("config").get("url")
            if string_to_replace in webhook_url:
                new_webhook_url = webhook_url.replace(string_to_replace, new_string)
                print(f"Updating webhook url: {webhook_url} -> {new_webhook_url}")
                github.orgs.update_an_organization_webhook(
                    org, webhook.get("id"), payload={"url": new_webhook_url}
                )
    except RestClientError as err:
        print(err)


def replace_string_in_repo_webhooks_url(org, repo, string_to_replace, new_string):
    """
    Replace a string in a repo's webhooks url.
    """
    try:
        webook_repo_list = github.repos.list_repository_webhooks(org, repo)
        for webhook in webook_repo_list:
            webhook_url = webhook.get("config").get("url")
            if string_to_replace in webhook_url:
                new_webhook_url = webhook_url.replace(string_to_replace, new_string)
                print(f"Updating webhook url: {webhook_url} -> {new_webhook_url}")
                github.repos.update_a_repository_webhook(
                    org, repo, webhook.get("id"), payload={"url": new_webhook_url}
                )
    except RestClientError as err:
        print(err)
