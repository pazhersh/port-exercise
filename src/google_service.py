from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.


service = 'compute'
zone = 'us-west4-b'
project = 'plenary-ridge-385508'

request_route = f'{service}/v1/projects/{project}/zones/{zone}/instances'
request_endpoint = f'https://{service}.googleapis.com'
request_url = f'{request_endpoint}/{request_route}'

def service():
    try:
        service_build = build(service, 'v1')
        instances = service_build.instances().list(project=project, zone=zone).execute()
        return instances
    except HttpError as err:
        print(err)
