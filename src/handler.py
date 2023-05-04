from src.gcp.google_service import list_resource
from src.port.entities import create_entities_json
from src.port.client import PortClient
from consts import PORT_API_URL
from secret_config import client_id, client_secret
from config import get_config
from itertools import product

CONFIG = get_config()

def generate_selector_permutations(selectors):
    values_permutations = product(*selectors.values())
    return [{k:v for k, v in zip(selectors.keys(), permutation)} for permutation in values_permutations]

def export_entities():
    for resource in CONFIG.get('resources'):
        service = resource.get('service')
        resource_kind = resource.get('resourceKind')
        resource_selectors = resource.get('selectors')
        selectors_permutations = generate_selector_permutations(resource_selectors)
        resource_mapping = resource.get('portEntityMapping')

        for selectors in selectors_permutations:
            vms = list_resource(service, resource_kind, **selectors)
            port_client = PortClient(client_id, client_secret, 'paz', PORT_API_URL)

            entities = [entity for vm in vms.get('items', []) for entity in create_entities_json(vm, selector_jq_query=None, jq_mappings=resource_mapping)]

            for entity in entities:
                port_client.upsert_entity(entity)
