import json
from yaml import load, SafeLoader


def parse_file(path):
    if get_format(path) == 'json':
        data = json.load(open(path))
        return data
    with open(path) as f:
        data = load(f, Loader=SafeLoader)
        return data


def get_format(path):
    parts = path.split('.')
    return parts[-1]
