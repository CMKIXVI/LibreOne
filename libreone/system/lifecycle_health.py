from .health import Health, HealthReport
from .lifecycle import Lifecycle, LifecycleState


def lifecycle_health(lifecycle: Lifecycle) -> HealthReport:
    if lifecycle.state is LifecycleState.RUNNING:
        return HealthReport("lifecycle", Health.OK, "running")
    if lifecycle.state is LifecycleState.FAILED:
        return HealthReport("lifecycle", Health.FAILED, "failed")
    return HealthReport("lifecycle", Health.DEGRADED, lifecycle.state.value)
