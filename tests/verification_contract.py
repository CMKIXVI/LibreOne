from hashlib import sha256

from libreone.system.verification import verify_digest


def verify_contract() -> bool:
    value = b"libreone"
    digest = sha256(value).hexdigest()
    return verify_digest(digest, digest)
