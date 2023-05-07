import functions_framework
from src.gcp import handler

@functions_framework.http
def export_resources(request):
    request_json = request.get_json(silent=True)
    handler.export_entities(request_json) # TODO: don't wait for operation to finish before returning result
    return 'finished export resources operation'
