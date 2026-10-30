from libreone.system.executor import Executor


def test_executor_returns_callable_result():
    assert Executor().execute(lambda: "LibreOne") == "LibreOne"
