# Documentation for the `graph_query` module.

::: octopy.graph_query.GraphRequest
    handler: python
    options:
      members:
        - __init__
        - _load_query
        - _execute
      show_root_heading: true
      show_source: false

::: octopy.graph_query.GraphQueryProvider
    handler: python
    options:
      members:
        - get_enterprise_orgs
        - get_org_repos
        - get_repo_collaborators
      show_root_heading: true
      show_source: false

::: octopy.graph_query.GraphMutationProducer
    handler: python
    options:
      members:
        - add_enterprise_org
        - add_repository
      show_root_heading: true
      show_source: false

::: octopy.graph_query.GraphQueryResponseTransmuter
    handler: python
    options:
      members:
        - get_org_list
        - get_repo_list
        - get_collaborators_permission_list
      show_root_heading: true
      show_source: false