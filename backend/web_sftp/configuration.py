import os
import json

cwd = os.getcwd()


def read_from_config():
    with open(f'{cwd}/config.json') as f:
        return json.load(f)['servers'][0]
