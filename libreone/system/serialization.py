import json
from typing import Any


def encode(value: Any) -> bytes:
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode("utf-8")


def decode(value: bytes) -> Any:
    return json.loads(value.decode("utf-8"))
