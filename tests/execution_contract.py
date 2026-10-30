from libreone.system.executor import Executor


def verify_execution_contract() -> bool:
    executor = Executor()
    return executor.execute(lambda: "LibreOne") == "LibreOne"
