from src.gcp.google_service import get_instances
from src.port.entities import create_entities_json
from src.port.client import PortClient
from consts import PORT_API_URL
from secret_config import client_id, client_secret

vms = get_instances()


port_client = PortClient(client_id, client_secret, 'paz', PORT_API_URL)

mock_config = {
  "resources": [
    {
      "kind": "AWS::Lambda::Function",
      "selector": {
        "aws": {
          "regions": ["us-east-1", "us-west-1"]
        }
      },
      "port": {
        "entity": {
          "mappings": [
            {
              "identifier": ".FunctionName",
              "title": ".FunctionName",
              "blueprint": "function",
              "properties": {
                "memory": ".MemorySize",
                "timeout": ".Timeout",
                "runtime": ".Runtime"
              }
            }
          ]
        }
      }
    }
  ]
}

mappings = [{
    "identifier": ".name",
    "title": ".name",
    "blueprint": "vmi",
    "properties": {
        'name': '.name',
        'description': '.description',
        'cpu_platform': '.cpu_platform'
    }
}]

# port_client.upsert_entity(create_virtual_machine_instance_entity(vms[0]))
port_client.upsert_entity(create_entities_json(vms[0], selector_jq_query=None, jq_mappings=mappings))


pass
