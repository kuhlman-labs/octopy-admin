"""
These scripts are used to update a string in an existing webhook url to a new value.
"""
import os
import sys

from dotenv import load_dotenv

from octopy_admin.rest_public.rest_public_client import (
    RestPublicClient,
    RestPublicClientError,
)

load_dotenv()
github = RestPublicClient()


def replace_string_in_org_webhooks_url(org, string_to_replace, new_string):
    """
    Replace a string in an org's webhooks url.
    """
    try:
        webhook_org_list = github.orgs.list_organization_webhooks(org)
        webhook_org_list = webhook_org_list.json()
        for webhook in webhook_org_list:
            webhook_url = webhook.get("config").get("url")
            if string_to_replace in webhook_url:
                new_webhook_url = webhook_url.replace(string_to_replace, new_string)
                print(f"Updating webhook url: {webhook_url} -> {new_webhook_url}")
                github.orgs.update_a_webhook_configuration_for_an_organization(
                    org, webhook.get("id"), payload={"url": new_webhook_url}
                )
    except RestPublicClientError as err:
        print(err)


def replace_string_in_repo_webhooks_url(org, repo, string_to_replace, new_string):
    """
    Replace a string in a repo's webhooks url.
    """
    try:
        webook_repo_list = github.repos.list_repository_webhooks(org, repo)
        webook_repo_list = webook_repo_list.json()
        for webhook in webook_repo_list:
            webhook_url = webhook.get("config").get("url")
            if string_to_replace in webhook_url:
                new_webhook_url = webhook_url.replace(string_to_replace, new_string)
                print(f"Updating webhook url: {webhook_url} -> {new_webhook_url}")
                github.repos.update_a_webhook_configuration_for_a_repository(
                    org, repo, webhook.get("id"), payload={"url": new_webhook_url}
                )
    except RestPublicClientError as err:
        print(err)
