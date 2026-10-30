from pathlib import Path

import pytest

from libreone.system.storage import Storage


def test_storage_resolves_confined_path(tmp_path: Path):
    storage = Storage(tmp_path)
    assert storage.resolve("data.txt") == tmp_path / "data.txt"


def test_storage_rejects_path_escape(tmp_path: Path):
    storage = Storage(tmp_path)
    with pytest.raises(ValueError):
        storage.resolve("../outside.txt")
