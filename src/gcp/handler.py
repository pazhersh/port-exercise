from src.gcp.google_service import list_resource
from src.port.entities import create_entities_json
from src.port.client import PortClient
from consts import EXPORTER_NAME, PORT_API_URL
from secret_config import client_id, client_secret
from config import get_config
from itertools import product, chain

CONFIG = get_config('samples/config.json')

def generate_selector_permutations(selectors):
    values_permutations = product(*selectors.values())
    return [{k:v for k, v in zip(selectors.keys(), permutation)} for permutation in values_permutations]

def get_entities(resource):
    service = resource.get('service')
    resource_kind = resource.get('resourceKind')
    resource_selectors = resource.get('selectors')
    selectors_permutations = generate_selector_permutations(resource_selectors)
    resource_mapping = resource.get('portEntityMapping')

    entities = []
    for selectors in selectors_permutations:
        gcp_resources = list_resource(service, resource_kind, **selectors) or {}
        for gcp_resource in gcp_resources.get('items', []):
            entities.extend(create_entities_json(gcp_resource, selector_jq_query=None, jq_mappings=resource_mapping))

    return entities

def export_entities():
    entities = chain.from_iterable(get_entities(resource) for resource in CONFIG.get('resources'))

    port_client = PortClient(client_id, client_secret, EXPORTER_NAME, PORT_API_URL)
    for entity in entities:
        port_client.upsert_entity(entity)
