from pathlib import Path

from libreone.system.storage import Storage


def test_storage_root_is_absolute(tmp_path: Path):
    storage = Storage(tmp_path)
    assert storage.root.is_absolute()
