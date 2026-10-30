from libreone.system.executor import Executor


def verify_executor_contract() -> bool:
    return Executor().execute(lambda: 42) == 42
