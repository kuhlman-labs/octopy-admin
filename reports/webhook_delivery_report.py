"""
This module contains functions for generating reports on webhook deliveries.
"""


import csv

from dotenv import load_dotenv

from octopy_admin.rest.rest_client import RestClient, RestClientError

load_dotenv()
restclient = RestClient()

# list of webhooks for a repository
def get_webhook_events(org, repo):
    """
    This function gets the list of webhooks  for a repository.
    """
    try:
        print(f"Getting webhooks for the {org}/{repo} repository.")
        webhooks = restclient.repos.list_repository_webhooks(org, repo)
        webhooks = webhooks.json()
        webhooks = [webhook for webhook in webhooks if webhook["active"]]
        print(f"Got {len(webhooks)} webhooks for {repo}.")
        return webhooks
    except RestClientError as err:
        print(err)
        return None


# list of webhooks for an organization
def get_org_webhook_events(org):
    """
    This function gets the list of webhooks for an organization.
    """
    try:
        print(f"Getting webhooks for the {org} organization.")
        webhooks = restclient.orgs.list_organization_webhooks(org)
        webhooks = webhooks.json()
        webhooks = [webhook for webhook in webhooks if webhook["active"]]
        print(f"Got {len(webhooks)} webhooks.")
        return webhooks
    except RestClientError as err:
        print(err)
        return None


# get repo webhook deliveries for a webhook
def get_repo_webhook_deliveries(org, repo, webhook_id):
    """
    This function gets the list of webhook deliveries for a webhook.
    """
    try:
        print(f"Getting webhook deliveries for the {org}/{repo} repository.")
        webhook_deliveries = restclient.repos.list_deliveries_for_a_repository_webhook(
            org, repo, webhook_id
        )
        webhook_deliveries = webhook_deliveries.json()
        print(f"Got {len(webhook_deliveries)} webhook deliveries.")
        return webhook_deliveries
    except RestClientError as err:
        print(err)
        return None


# get org webhook deliveries for a webhook
def get_org_webhook_deliveries(org, webhook_id):
    """
    This function gets the list of webhook deliveries for a webhook.
    """
    try:
        print(f"Getting webhook deliveries for the {org} organization.")
        webhook_deliveries = restclient.orgs.list_deliveries_for_an_organization_webhook(
            org, webhook_id
        )
        webhook_deliveries = webhook_deliveries.json()
        print(f"Got {len(webhook_deliveries)} webhook deliveries.")
        return webhook_deliveries
    except RestClientError as err:
        print(err)
        return None


# create webhook delivery report for a repository
def create_webhook_delivery_report(org, repo):
    """
    This function creates a webhook delivery report for a repository.
    """
    webhooks = get_webhook_events(org, repo)
    if webhooks:
        for webhook in webhooks:
            webhook_id = webhook["id"]
            webhook_deliveries = get_repo_webhook_deliveries(org, repo, webhook_id)
            if webhook_deliveries:
                with open(f"{org}_{repo}_webhook_delivery_report.csv", "w", newline="") as csvfile:
                    fieldnames = [
                        "id",
                        "guid",
                        "delivered_at",
                        "redelivery",
                        "duration",
                        "status",
                        "status_code",
                        "event",
                        "action",
                        "installation_id",
                        "repository_id",
                        "url",
                    ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for webhook_delivery in webhook_deliveries:
                        writer.writerow(webhook_delivery)


# create webhook delivery report for an organization
def create_org_webhook_delivery_report(org):
    """
    This function creates a webhook delivery report for an organization.
    """
    webhooks = get_org_webhook_events(org)
    if webhooks:
        for webhook in webhooks:
            webhook_id = webhook["id"]
            webhook_deliveries = get_org_webhook_deliveries(org, webhook_id)
            if webhook_deliveries:
                with open(f"{org}_webhook_delivery_report.csv", "w", newline="") as csvfile:
                    fieldnames = [
                        "id",
                        "guid",
                        "delivered_at",
                        "redelivery",
                        "duration",
                        "status",
                        "status_code",
                        "event",
                        "action",
                        "installation_id",
                        "repository_id",
                        "url",
                    ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for webhook_delivery in webhook_deliveries:
                        writer.writerow(webhook_delivery)


# example of creating a webhook delivery report for a repository
# create_webhook_delivery_report("engineering", "platform")

# example of creating a webhook delivery report for an organization
create_org_webhook_delivery_report("engineering")
