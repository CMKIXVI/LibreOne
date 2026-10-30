from dataclasses import dataclass
from datetime import datetime
from collections.abc import Callable

@dataclass(frozen=True, slots=True)
class ScheduledTask:
    run_at: datetime
    task: Callable[[], object]

class Scheduler:
    def __init__(self) -> None:
        self._tasks: list[ScheduledTask] = []

    def schedule(self, run_at: datetime, task: Callable[[], object]) -> ScheduledTask:
        item = ScheduledTask(run_at, task)
        self._tasks.append(item)
        self._tasks.sort(key=lambda x: x.run_at)
        return item
