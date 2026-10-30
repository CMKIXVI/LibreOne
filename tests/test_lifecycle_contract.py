from libreone.system.lifecycle import LifecycleState
from libreone.system.lifecycle_contract import lifecycle_contract


def test_lifecycle_contract_reports_running_then_stopped():
    running, stopped = lifecycle_contract()
    assert running is LifecycleState.RUNNING
    assert stopped is LifecycleState.STOPPED
