"""
Interact with GitHub Projects.
"""


# pylint: disable=too-many-arguments
class Projects:
    # pylint: disable=too-many-public-methods
    """
    Interact with GitHub Projects.
    """

    def __init__(self, client):
        """
        Initialize the Projects class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_projects(self, org, params=None, payload=None):
        """
        List organization projects
        https://docs.github.com/rest/reference/projects#list-organization-projects
        Attributes:
        Path Parameters:
        org
        Payload Parameters:
        state
         per-page
         page
        """
        url = self._base_url + f"/orgs/{org}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_project(self, org, params=None, payload=None):
        """
        Create an organization project
        https://docs.github.com/rest/reference/projects#create-an-organization-project
        Attributes:
        Path Parameters:
        org
        Payload Parameters:

        """
        url = self._base_url + f"/orgs/{org}/projects"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_project_card(self, card_id, params=None, payload=None):
        """
        Get a project card
        https://docs.github.com/rest/reference/projects#get-a-project-card
        Attributes:
        Path Parameters:
        card_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/cards/{card_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_existing_project_card(self, card_id, params=None, payload=None):
        """
        Update an existing project card
        https://docs.github.com/rest/reference/projects#update-a-project-card
        Attributes:
        Path Parameters:
        card_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/cards/{card_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_project_card(self, card_id, params=None, payload=None):
        """
        Delete a project card
        https://docs.github.com/rest/reference/projects#delete-a-project-card
        Attributes:
        Path Parameters:
        card_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/cards/{card_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def move_a_project_card(self, card_id, params=None, payload=None):
        """
        Move a project card
        https://docs.github.com/rest/reference/projects#move-a-project-card
        Attributes:
        Path Parameters:
        card_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/cards/{card_id}/moves"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_project_column(self, column_id, params=None, payload=None):
        """
        Get a project column
        https://docs.github.com/rest/reference/projects#get-a-project-column
        Attributes:
        Path Parameters:
        column_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/{column_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_existing_project_column(self, column_id, params=None, payload=None):
        """
        Update an existing project column
        https://docs.github.com/rest/reference/projects#update-a-project-column
        Attributes:
        Path Parameters:
        column_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/{column_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_project_column(self, column_id, params=None, payload=None):
        """
        Delete a project column
        https://docs.github.com/rest/reference/projects#delete-a-project-column
        Attributes:
        Path Parameters:
        column_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/{column_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_project_cards(self, column_id, params=None, payload=None):
        """
        List project cards
        https://docs.github.com/rest/reference/projects#list-project-cards
        Attributes:
        Path Parameters:
        column_id
        Payload Parameters:
        archived_state
         per-page
         page
        """
        url = self._base_url + f"/projects/columns/{column_id}/cards"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_project_card(self, column_id, params=None, payload=None):
        """
        Create a project card
        https://docs.github.com/rest/reference/projects#create-a-project-card
        Attributes:
        Path Parameters:
        column_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/{column_id}/cards"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def move_a_project_column(self, column_id, params=None, payload=None):
        """
        Move a project column
        https://docs.github.com/rest/reference/projects#move-a-project-column
        Attributes:
        Path Parameters:
        column_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/columns/{column_id}/moves"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_project(self, project_id, params=None, payload=None):
        """
        Get a project
        https://docs.github.com/rest/reference/projects#get-a-project
        Attributes:
        Path Parameters:
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_project(self, project_id, params=None, payload=None):
        """
        Update a project
        https://docs.github.com/rest/reference/projects#update-a-project
        Attributes:
        Path Parameters:
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_project(self, project_id, params=None, payload=None):
        """
        Delete a project
        https://docs.github.com/rest/reference/projects#delete-a-project
        Attributes:
        Path Parameters:
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_project_collaborators(self, project_id, params=None, payload=None):
        """
        List project collaborators
        https://docs.github.com/rest/reference/projects#list-project-collaborators
        Attributes:
        Path Parameters:
        project_id
        Payload Parameters:
        affiliation
         per-page
         page
        """
        url = self._base_url + f"/projects/{project_id}/collaborators"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_project_collaborator(self, project_id, username, params=None, payload=None):
        """
        Add project collaborator
        https://docs.github.com/rest/reference/projects#add-project-collaborator
        Attributes:
        Path Parameters:
        project_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}/collaborators/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_user_as_a_collaborator(self, project_id, username, params=None, payload=None):
        """
        Remove user as a collaborator
        https://docs.github.com/rest/reference/projects#remove-project-collaborator
        Attributes:
        Path Parameters:
        project_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}/collaborators/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_project_permission_for_a_user(self, project_id, username, params=None, payload=None):
        """
        Get project permission for a user
        https://docs.github.com/rest/reference/projects#get-project-permission-for-a-user
        Attributes:
        Path Parameters:
        project_id
        username
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}/collaborators/{username}/permission"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_project_columns(self, project_id, params=None, payload=None):
        """
        List project columns
        https://docs.github.com/rest/reference/projects#list-project-columns
        Attributes:
        Path Parameters:
        project_id
        Payload Parameters:
        per-page
         page
        """
        url = self._base_url + f"/projects/{project_id}/columns"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_project_column(self, project_id, params=None, payload=None):
        """
        Create a project column
        https://docs.github.com/rest/reference/projects#create-a-project-column
        Attributes:
        Path Parameters:
        project_id
        Payload Parameters:

        """
        url = self._base_url + f"/projects/{project_id}/columns"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_projects(self, owner, repo, params=None, payload=None):
        """
        List repository projects
        https://docs.github.com/rest/reference/projects#list-repository-projects
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:
        state
         per-page
         page
        """
        url = self._base_url + f"/repos/{owner}/{repo}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_project(self, owner, repo, params=None, payload=None):
        """
        Create a repository project
        https://docs.github.com/rest/reference/projects#create-a-repository-project
        Attributes:
        Path Parameters:
        owner
        repo
        Payload Parameters:

        """
        url = self._base_url + f"/repos/{owner}/{repo}/projects"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_user_project(self, params=None, payload=None):
        """
        Create a user project
        https://docs.github.com/rest/reference/projects#create-a-user-project
        Attributes:
        Path Parameters:

        Payload Parameters:

        """
        url = self._base_url + "/user/projects"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_user_projects(self, username, params=None, payload=None):
        """
        List user projects
        https://docs.github.com/rest/reference/projects#list-user-projects
        Attributes:
        Path Parameters:
        username
        Payload Parameters:
        state
         per-page
         page
        """
        url = self._base_url + f"/users/{username}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response
