from libreone.system.executor import Executor

def test_executor_returns_operation_result():
    assert Executor().execute(lambda: 42) == 42
