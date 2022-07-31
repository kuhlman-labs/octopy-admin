# OctoPy Admin Reference

## Graph Package

::: octopy_admin.graph.graph_request.GraphRequest
    handler: python
    options:
      members:
        - __init__
        - _load_query
      show_root_heading: true
      show_source: false

::: octopy_admin.graph.graph_query.GraphQuery
    handler: python
    options:
      members:
        - get_enterprise_orgs
        - get_org_repos
        - get_repo_collaborators
      show_root_heading: true
      show_source: false

::: octopy_admin.graph.graph_mutation.GraphMutation
    handler: python
    options:
      members:
        - add_enterprise_org
        - add_repository
      show_root_heading: true
      show_source: false

::: octopy_admin.graph.graph_query_converter.GraphQueryConverter
    handler: python
    options:
      members:
        - get_org_list
        - get_repo_list
        - get_collaborators_permission_list
      show_root_heading: true
      show_source: false

## Rest Package

::: octopy_admin.rest.rest_client
    handler: python
    options:
      members:
        - __init__
        - _execute
