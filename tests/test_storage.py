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


def test_storage_rejects_non_path_inputs(tmp_path: Path):
    storage = Storage(tmp_path)
    with pytest.raises(TypeError):
        Storage(123)
    with pytest.raises(TypeError):
        storage.resolve(123)


def test_storage_blocks_symlink_escape(tmp_path: Path):
    outside = tmp_path.parent / "libreone-storage-outside"
    outside.mkdir(exist_ok=True)
    link = tmp_path / "escape"
    link.symlink_to(outside, target_is_directory=True)
    try:
        with pytest.raises(ValueError):
            Storage(tmp_path).resolve("escape/file.txt")
    finally:
        link.unlink()
        outside.rmdir()
