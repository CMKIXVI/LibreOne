import json
from typing import Any


def encode(value: Any) -> str:
    """Encode JSON using a deterministic, standards-compliant representation."""
    return json.dumps(
        value,
        separators=(",", ":"),
        sort_keys=True,
        allow_nan=False,
    )


def decode(value: str | bytes) -> Any:
    """Decode UTF-8 JSON and reject unsupported input types explicitly."""
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    elif not isinstance(value, str):
        raise TypeError("serialized value must be str or bytes")
    return json.loads(value)
