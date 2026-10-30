from pathlib import Path

import pytest

from libreone.system.storage import Storage


def test_storage_rejects_absolute_escape(tmp_path: Path):
    storage = Storage(tmp_path)
    with pytest.raises(ValueError):
        storage.resolve("/etc/passwd")
