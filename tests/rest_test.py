from dotenv import load_dotenv

from octopy_admin.rest_public.rest_public_client import RestPublicClient

load_dotenv()


class TestRestPublicClient:

    rest_client = RestPublicClient()

    def test_get_authenticated_user(self):
        response = self.rest_client.users.get_the_authenticated_user()
        assert response.status_code == 200
        assert response.json().get("login") is not None
