import hashlib
from libreone.system.verification import verify_digest

def test_digest_verification_uses_exact_value():
    value = "libreone"
    digest = hashlib.sha256(value.encode()).hexdigest()
    assert verify_digest(digest, digest)
    assert not verify_digest(digest, "0" * 64)
