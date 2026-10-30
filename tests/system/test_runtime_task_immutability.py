from dataclasses import FrozenInstanceError

import pytest

from libreone.system.runtime import RuntimeTask


def test_runtime_task_is_immutable():
    task = RuntimeTask("runtime")
    with pytest.raises(FrozenInstanceError):
        task.name = "other"
