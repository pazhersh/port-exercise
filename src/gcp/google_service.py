from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def list_resource(service_name, resource_name, service_version = 'v1', **request_kwargs):
    try:
        service_build = build(service_name, service_version)
        resource_api = getattr(service_build, resource_name)
        resource_list = resource_api().list(**request_kwargs).execute()
        return resource_list
    except HttpError as err:
        print(err)
