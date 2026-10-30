import json
from typing import Any


def encode(value: Any) -> str:
    return json.dumps(value, separators=(",", ":"), sort_keys=True)


def decode(value: str | bytes) -> Any:
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    return json.loads(value)
