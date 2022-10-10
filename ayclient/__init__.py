__all__ = [
    "api",
    "config",
    "dispatch_event",
    "json_loads",
    "json_dumps",
    "hash_data",
    "create_hash"
]

from ayclient.api import api
from ayclient.config import config
from ayclient.events import dispatch_event

from ayclient.utils import json_loads, json_dumps, hash_data, create_hash


def addon_settings(addon_name: str = None, addon_version: str = None):
    if addon_name is None:
        addon_name = config.addon_name
        addon_version = config.addon_version
    endpoint = f"addons/{addon_name}/{addon_version}/settings"
    print(endpoint)
    response = api.get(endpoint)
    print(response)
    return response.json()
