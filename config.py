import json

def get_config(config_file = 'config.json'):
    return json.load(open(config_file, 'r'))