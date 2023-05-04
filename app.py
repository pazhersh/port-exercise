from src.gcp.google_service import list_resource
from src.port.entities import create_entities_json
from src.port.client import PortClient
from consts import PORT_API_URL
from secret_config import client_id, client_secret

vms = list_resource('compute', 'instances', zone='us-west4-b', project='plenary-ridge-385508')
port_client = PortClient(client_id, client_secret, 'paz', PORT_API_URL)

mappings = [
    {
        'identifier': '.name',
        'title': '.name',
        'blueprint': '"vmi"',
        'properties': {
            'name': '.name',
            'description': '.description',
            'cpu_platform': '.cpuPlatform'
        }
    }
]

entities = [entity for vm in vms.get('items', []) for entity in create_entities_json(vm, selector_jq_query=None, jq_mappings=mappings)]

for entity in entities:
    port_client.upsert_entity(entity)
