import sys
import json
from .client import PurviewClient

class Endpoint:
    def __init__(self):
        self.app = None
        self.method = None
        self.endpoint = None
        self.params = None
        self.payload = None
        self.files = None
        self.headers = {}

def get_data(http_dict):
    client = PurviewClient()
    client.set_region(http_dict['app'])
    client.set_account(http_dict['app'])
    client.set_token(http_dict['app'])
    data = client.http_get(http_dict['app'], http_dict['method'], http_dict['endpoint'], http_dict['params'], http_dict['payload'], http_dict['files'], http_dict['headers'])
    return data

def get_json(args, param):
    response = None
    if args[param] is not None:
        filepath = args[param]
        if '.JSON' in filepath.upper():
            try:
                with open(filepath, encoding='utf-8') as f:
                    response = json.load(f)
            except:
                with open(filepath, encoding='utf-16') as f:
                    response = json.load(f)
        else:
            print('[ERROR] The {0} parameter must contain a valid file path to a JSON document.'.format(param))
            sys.exit()
    return response

def decorator(func):
    def wrapper(self, args):
        func(self, args)
        http_dict = {'app': self.app, 'method': self.method, 'endpoint': self.endpoint, 'params': self.params, 'payload': self.payload, 'files': self.files, 'headers': self.headers}
        data = get_data(http_dict)
        return data
    return wrapper
