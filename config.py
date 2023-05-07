import json
import os

def get_config(config_file = 'config.json'):
    return json.load(open(config_file, 'r'))

def get_from_secret(secret_name):
    secret_value = os.environ.get(secret_name, {})
    return json.loads(secret_value)