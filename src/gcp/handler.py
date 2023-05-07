from src.gcp.google_service import list_resource
from src.port.entities import create_entities_json
from src.port.client import PortClient
from consts import EXPORTER_NAME, PORT_API_URL
from secret_config import client_id, client_secret
from itertools import product, chain

def generate_selector_permutations(selectors):
    values_permutations = product(*selectors.values())
    return [{k:v for k, v in zip(selectors.keys(), permutation)} for permutation in values_permutations]

def generate_entities(resource):
    service = resource.get('service')
    resource_path = resource.get('resourcePath')
    resource_selectors = resource.get('selectors')
    selectors_permutations = generate_selector_permutations(resource_selectors)
    resource_mapping = resource.get('portEntityMapping')

    entities = []
    for selectors in selectors_permutations:
        gcp_resources = list_resource(service, resource_path, **selectors) or {}
        entities.extend(create_entities_json(gcp_resources, selector_jq_query=None, jq_mappings=resource_mapping))

    return entities

def export_entities(config):
    entities = chain.from_iterable(generate_entities(resource) for resource in config.get('resources'))

    port_client = PortClient(client_id, client_secret, EXPORTER_NAME, PORT_API_URL)
    for entity in entities:
        print('exporting entity:', entity) # TODO: make logs work with GCP
        port_client.upsert_entity(entity)
    
