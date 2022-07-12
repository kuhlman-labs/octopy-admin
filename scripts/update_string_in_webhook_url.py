import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from dotenv import load_dotenv

from octopy.rest_query import RestGetProvider, RestPatchProducer, RestRequestError

config = load_dotenv()
restpatch = RestPatchProducer()
restget = RestGetProvider()


def replace_string_in_org_webhooks_url(org, string_to_replace, new_string):
    try:
        webook_org_list = restget.get_org_webhook_list(org)
        for webhook in webook_org_list:
            webhook_url = webhook.get("config").get("url")
            if string_to_replace in webhook_url:
                new_webhook_url = webhook_url.replace(string_to_replace, new_string)
                print(f"Updating webhook url: {webhook_url} -> {new_webhook_url}")
                restpatch.update_org_webhook_url(org, webhook["id"], new_webhook_url)
    except RestRequestError as err:
        print(err)
