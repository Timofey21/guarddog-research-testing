import json

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        result = json.load(f)
    return result