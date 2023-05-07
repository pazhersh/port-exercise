import base64
import json
import functions_framework
from src.gcp import handler

@functions_framework.cloud_event
def export_resources(cloud_event):
    raw_data = cloud_event.data.get('message').get('data')
    data_string = base64.b64decode(raw_data)
    configuration = json.loads(data_string)
    handler.export_entities(configuration)
