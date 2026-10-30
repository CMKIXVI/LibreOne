from pathlib import Path

from libreone.system.storage import Storage


def test_storage_can_create_parent_directories(tmp_path: Path):
    storage = Storage(tmp_path)
    target = storage.resolve("nested/value.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("LibreOne", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == "LibreOne"
