import pytest
from libreone.system.runtime import RuntimeTask

def test_runtime_task_requires_name():
    with pytest.raises(ValueError):
        RuntimeTask(" ").validate()

def test_runtime_task_validates():
    RuntimeTask("boot").validate()
