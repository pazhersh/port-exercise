from src.read_from_gcp import read_vm_instances
from src.port.client import PortClient
from consts import PORT_API_URL
from secret_config import client_id, client_secret
from src.port.jqless_entities import create_virtual_machine_instance_entity

vms = read_vm_instances()

port_client = PortClient(client_id, client_secret, 'paz', PORT_API_URL)

port_client.upsert_entity(create_virtual_machine_instance_entity(vms[0]))

pass