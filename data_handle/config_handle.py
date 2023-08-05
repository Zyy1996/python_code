import json

def cfg_load(file_path):
    try:
        with open(file_path, 'r') as f:
            config_json = json.load(f)
        return config_json
    except FileNotFoundError:
        return None