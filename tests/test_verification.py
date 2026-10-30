import hashlib

from libreone.system.verification import verify_digest


def test_digest_verification():
    value = b"LibreOne"
    digest = hashlib.sha256(value).hexdigest()
    assert verify_digest(value, digest)
    assert not verify_digest(value, "0" * 64)
