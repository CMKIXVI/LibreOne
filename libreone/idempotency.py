from hashlib import sha256
import json
from typing import Any

def key(operation: str, payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(f"{operation}:{canonical}".encode()).hexdigest()
