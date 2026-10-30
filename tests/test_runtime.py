from libreone.system.runtime import RuntimeTask


def test_runtime_task_is_named():
    task = RuntimeTask("init")
    assert task.name == "init"
