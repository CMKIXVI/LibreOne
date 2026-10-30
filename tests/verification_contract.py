from libreone.system.verification import verify_digest


def verify_contract() -> bool:
    value = b"libreone"
    return verify_digest(value, verify_digest.__globals__["hashlib"].sha256(value).hexdigest())
