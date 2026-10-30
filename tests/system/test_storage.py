from pathlib import Path

import pytest

from libreone.system.storage import Storage


def test_storage_confines_paths(tmp_path: Path):
    storage = Storage(tmp_path)
    assert storage.resolve("data/file.txt").parent == tmp_path / "data"
    with pytest.raises(ValueError):
        storage.resolve("../outside.txt")
