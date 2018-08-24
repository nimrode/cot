from django.db import models
from enum import Enum

import json

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)


class PropertyTypes(ChoiceEnum):
    JSON = 'application/json'
    BINARY = 'application/octet-stream'
    PLAINTEXT = 'text/plain'

def serialize_content_data(type, value):
    if type == PropertyTypes.JSON.value and isinstance(value, dict):
        return json.dumps(value).encode()
    elif type == PropertyTypes.PLAINTEXT.value and isinstance(value, str):
        return value.encode()
    elif type == PropertyTypes.BINARY.value:
        return str(value).encode()
    else:
        raise TypeError("Illegal <type> and <content> representation")


def deserialize_content_data(type, value):
    if type == PropertyTypes.JSON.value:
        return json.loads(value.decode())
    elif type == PropertyTypes.PLAINTEXT.value:
        return value.decode()
    else:    # PropertyTypes.BINARY
        return value