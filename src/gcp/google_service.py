from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_resource_api(service, resource_path):
    api = service
    for path_argument in resource_path:
        api_builder = getattr(api, path_argument)
        api = api_builder()
    return api

def list_resource(service_name, resource_path, service_version = 'v1', **request_kwargs):
    try:
        service = build(service_name, service_version)
        resource_api = get_resource_api(service, resource_path)
        resource_list = resource_api.list(**request_kwargs).execute()
        return resource_list
    except HttpError as err:
        print(err)
