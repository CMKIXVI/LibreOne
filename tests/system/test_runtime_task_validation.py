import pytest

from libreone.system.runtime import RuntimeTask


def test_runtime_task_rejects_empty_name():
    with pytest.raises(ValueError):
        RuntimeTask("")
