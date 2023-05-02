from google.cloud import compute

def read_vm_instances():
    # TODO: get zones and projects dynamicly and collect vm-instances from all
    client = compute.InstancesClient()
    return client.list(zone='us-west4-b', project='plenary-ridge-385508')