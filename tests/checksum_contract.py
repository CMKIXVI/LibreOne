from pathlib import Path
from libreone.system.checksum import sha256_file


def verify_checksum_contract(path: Path) -> bool:
    digest = sha256_file(path)
    return len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
