import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from dotenv import load_dotenv

from octopy.rest_get import RestGet

load_dotenv()


restquery = RestGet()


def test_get_repo_list():
    response = restquery.get_repo_list("Outer-Planets-Alliance")
    assert response.status_code == 200


def test_get_repo():
    response = restquery.get_repo("kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200


def test_get_org():
    response = restquery.get_org("Outer-Planets-Alliance")
    assert response.status_code == 200


def test_get_user():
    response = restquery.get_user("kuhlman-labs")
    assert response.status_code == 200


def test_get_collaborators():
    response = restquery.get_collaborators("kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200


def test_get_collaborator_permission():
    response = restquery.get_collaborator_permission("kuhlman-labs", "kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200


def test_get_repo_webhook_list():
    response = restquery.get_repo_webhook_list("kuhlman-labs", "kuhlman-labs")
    assert response.status_code == 200


def test_get_repo_webhook():
    response = restquery.get_repo_webhook("Outer-Planets-Alliance", "test", "368519137")
    assert response.status_code == 200


def test_get_org_webhooks():
    response = restquery.get_org_webhook_list("Outer-Planets-Alliance")
    assert response.status_code == 200


def test_get_org_webhook():
    response = restquery.get_org_webhook("Outer-Planets-Alliance", "340083281")
    assert response.status_code == 200
