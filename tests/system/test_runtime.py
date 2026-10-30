from libreone.system.resources import ResourceLimits
from libreone.system.runtime import RuntimeTask


def test_runtime_task_defaults():
    task = RuntimeTask("ai")
    assert task.name == "ai"
    assert isinstance(task.limits, ResourceLimits)
