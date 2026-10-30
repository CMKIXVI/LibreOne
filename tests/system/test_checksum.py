from pathlib import Path

from libreone.system.checksum import sha256_file
from libreone.system.verification import verify_digest


def test_sha256_and_digest_verification(tmp_path: Path):
    target = tmp_path / "payload"
    target.write_bytes(b"LibreOne")
    digest = sha256_file(target)
    assert len(digest) == 64
    assert verify_digest(digest, digest)
    assert not verify_digest(digest, "0" * 64)
