import hashlib
import time
import random
import json

from typing import Any


def json_dumps(data: Any, **kwargs) -> str:
    return json.dumps(data, **kwargs)


def json_loads(data: str) -> Any:
    return json.loads(data)


def hash_data(data: Any) -> str:
    """Create a SHA-256 hash from arbitrary (json-serializable) data."""
    if type(data) in (int, float, bool, dict, list):
        data = json_dumps(data)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def create_hash() -> str:
    """Create a pseudo-random hash (used as and access token)."""
    return hash_data([time.time(), random.random()])
