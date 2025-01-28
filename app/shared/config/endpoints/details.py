from typing import List

from app.shared.config.endpoints.tags import EndpointTag


class APIEndpointDetail:
    """
    This class contains all the endpoints details for the application. It is
    used to generate the documentation for the API.
    Returns:
    """
    class Endpoint:
        def __init__(self, summary: str, description: str, tags: List[str],
                     path: str):
            """
            Generic implementation for the endpoints details
            Args:
                summary (str): summary of the endpoint
                description (str): detailed description of the endpoint
                tags (List[str]): tags related to the endpoint
                path (str): endpoint path
            """
            self.summary = summary
            self.description = description
            self.tags = tags
            self.path = path

    root = Endpoint(
        summary='Root',
        description='''
        This is root path of the application. When connecting to server, it
        should be used for check whether the server is up and running or not.
        In case if some endpoints are not working properly, then it should be
        checked from root path of the application. If it is working properly,
        then there is no issue with the server.
        ''',
        tags=EndpointTag.root,
        path='/'
    )

    sample_add_v0 = Endpoint(
        summary='Sample Add',
        description='''
        This is sample add endpoint. It is used to add two numbers.
        ''',
        tags=EndpointTag.sample_V0,
        path='/add'
    )

    sample_get_v0 = Endpoint(
        summary='Sample Get',
        description='''
        This is sample get endpoint. It is used to get two numbers.
        ''',
        tags=EndpointTag.sample_V0,
        path='/get'
    )

    sample_update_v0 = Endpoint(
        summary='Sample Update',
        description='''
        This is sample update endpoint. It is used to update two numbers.
        ''',
        tags=EndpointTag.sample_V0,
        path='/update'
    )

    sample_delete_v0 = Endpoint(
        summary='Sample Delete',
        description='''
        This is sample delete endpoint. It is used to delete two numbers.
        ''',
        tags=EndpointTag.sample_V0,
        path='/delete'
    )
