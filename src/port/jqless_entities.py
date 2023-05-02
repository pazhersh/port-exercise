def create_virtual_machine_instance_entity(vmi):
    return {
    'blueprint': 'vmi',
    'identifier': vmi.name,
    'title': vmi.name,
    'properties': {
        'name': vmi.name,
        'description': vmi.description,
        'cpu_platform': vmi.cpu_platform
    }
}


post_entity_stracture = {
    'identifier': 'string',
    'title': 'string',
    'icon': 'string',
    'team': 'string',
    'properties': {},
    'relations': {
        'property1': 'string',
        'property2': 'string'
    }
}
