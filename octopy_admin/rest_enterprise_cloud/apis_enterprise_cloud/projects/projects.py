"""
Interact with GitHub Projects.
"""
# pylint: disable=too-many-arguments, too-many-public-methods, too-many-lines, duplicate-code, line-too-long


class Projects:
    """
    Interact with GitHub Projects.
    """

    def __init__(self, client):
        """
        Initializes the Projects class.
        """
        self._base_url = client._base_url
        self._execute = client._execute

    def list_organization_projects(self, org, params=None, payload=None):
        """
        Summary:
        List organization projects
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#list-organization-projects
        """
        url = self._base_url + f"/orgs/{org}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_an_organization_project(self, org, params=None, payload=None):
        """
        Summary:
        Create an organization project
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#create-an-organization-project
        """
        url = self._base_url + f"/orgs/{org}/projects"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_project_card(self, card_id, params=None, payload=None):
        """
        Summary:
        Get a project card
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#get-a-project-card
        """
        url = self._base_url + f"/projects/columns/cards/{card_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_existing_project_card(self, card_id, params=None, payload=None):
        """
        Summary:
        Update an existing project card
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#update-a-project-card
        """
        url = self._base_url + f"/projects/columns/cards/{card_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_project_card(self, card_id, params=None, payload=None):
        """
        Summary:
        Delete a project card
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#delete-a-project-card
        """
        url = self._base_url + f"/projects/columns/cards/{card_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def move_a_project_card(self, card_id, params=None, payload=None):
        """
        Summary:
        Move a project card
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#move-a-project-card
        """
        url = self._base_url + f"/projects/columns/cards/{card_id}/moves"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_project_column(self, column_id, params=None, payload=None):
        """
        Summary:
        Get a project column
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#get-a-project-column
        """
        url = self._base_url + f"/projects/columns/{column_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_an_existing_project_column(self, column_id, params=None, payload=None):
        """
        Summary:
        Update an existing project column
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#update-a-project-column
        """
        url = self._base_url + f"/projects/columns/{column_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_project_column(self, column_id, params=None, payload=None):
        """
        Summary:
        Delete a project column
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#delete-a-project-column
        """
        url = self._base_url + f"/projects/columns/{column_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_project_cards(self, column_id, params=None, payload=None):
        """
        Summary:
        List project cards
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#list-project-cards
        """
        url = self._base_url + f"/projects/columns/{column_id}/cards"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_project_card(self, column_id, params=None, payload=None):
        """
        Summary:
        Create a project card
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#create-a-project-card
        """
        url = self._base_url + f"/projects/columns/{column_id}/cards"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def move_a_project_column(self, column_id, params=None, payload=None):
        """
        Summary:
        Move a project column
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#move-a-project-column
        """
        url = self._base_url + f"/projects/columns/{column_id}/moves"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def get_a_project(self, project_id, params=None, payload=None):
        """
        Summary:
        Get a project
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#get-a-project
        """
        url = self._base_url + f"/projects/{project_id}"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def update_a_project(self, project_id, params=None, payload=None):
        """
        Summary:
        Update a project
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#update-a-project
        """
        url = self._base_url + f"/projects/{project_id}"
        response = self._execute("patch", url, params=params, payload=payload)
        return response

    def delete_a_project(self, project_id, params=None, payload=None):
        """
        Summary:
        Delete a project
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#delete-a-project
        """
        url = self._base_url + f"/projects/{project_id}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def list_project_collaborators(self, project_id, params=None, payload=None):
        """
        Summary:
        List project collaborators
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#list-project-collaborators
        """
        url = self._base_url + f"/projects/{project_id}/collaborators"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def add_project_collaborator(self, project_id, username, params=None, payload=None):
        """
        Summary:
        Add project collaborator
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#add-project-collaborator
        """
        url = self._base_url + f"/projects/{project_id}/collaborators/{username}"
        response = self._execute("put", url, params=params, payload=payload)
        return response

    def remove_user_as_a_collaborator(self, project_id, username, params=None, payload=None):
        """
        Summary:
        Remove user as a collaborator
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#remove-project-collaborator
        """
        url = self._base_url + f"/projects/{project_id}/collaborators/{username}"
        response = self._execute("delete", url, params=params, payload=payload)
        return response

    def get_project_permission_for_a_user(self, project_id, username, params=None, payload=None):
        """
        Summary:
        Get project permission for a user
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#get-project-permission-for-a-user
        """
        url = self._base_url + f"/projects/{project_id}/collaborators/{username}/permission"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def list_project_columns(self, project_id, params=None, payload=None):
        """
        Summary:
        List project columns
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#list-project-columns
        """
        url = self._base_url + f"/projects/{project_id}/columns"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_project_column(self, project_id, params=None, payload=None):
        """
        Summary:
        Create a project column
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#create-a-project-column
        """
        url = self._base_url + f"/projects/{project_id}/columns"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_repository_projects(self, owner, repo, params=None, payload=None):
        """
        Summary:
        List repository projects
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#list-repository-projects
        """
        url = self._base_url + f"/repos/{owner}/{repo}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response

    def create_a_repository_project(self, owner, repo, params=None, payload=None):
        """
        Summary:
        Create a repository project
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#create-a-repository-project
        """
        url = self._base_url + f"/repos/{owner}/{repo}/projects"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def create_a_user_project(self, params=None, payload=None):
        """
        Summary:
        Create a user project
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#create-a-user-project
        """
        url = self._base_url + "/user/projects"
        response = self._execute("post", url, params=params, payload=payload)
        return response

    def list_user_projects(self, username, params=None, payload=None):
        """
        Summary:
        List user projects
        Docs:
        https://docs.github.com/enterprise-cloud@latest//rest/reference/projects#list-user-projects
        """
        url = self._base_url + f"/users/{username}/projects"
        response = self._execute("get", url, params=params, payload=payload)
        return response
