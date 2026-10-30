from libreone.system.runtime import RuntimeTask


def verify_runtime_contract() -> bool:
    task = RuntimeTask("bootstrap")
    task.validate()
    return task.name == "bootstrap"
