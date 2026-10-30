from pathlib import Path
from libreone.system.storage import Storage


def verify_storage_contract(root: Path) -> bool:
    storage = Storage(root)
    return storage.resolve("libreone.data").parent == root
