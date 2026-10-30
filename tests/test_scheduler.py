import pytest

from libreone.system.scheduler import Scheduler


def test_scheduler_runs_submitted_callable():
    scheduler = Scheduler()
    result = []
    task_id = scheduler.submit(lambda: result.append(1))
    assert task_id == 1
    scheduler.run_once()
    assert result == [1]
    assert scheduler.pending == 0


def test_scheduler_preserves_fifo_order_and_ids():
    scheduler = Scheduler()
    result = []
    first = scheduler.submit(lambda: result.append(1))
    second = scheduler.submit(lambda: result.append(2))
    assert (first, second) == (1, 2)
    scheduler.run_once()
    scheduler.run_once()
    assert result == [1, 2]


def test_scheduler_can_cancel_pending_task():
    scheduler = Scheduler()
    result = []
    first = scheduler.submit(lambda: result.append(1))
    scheduler.submit(lambda: result.append(2))
    assert scheduler.cancel(first) is True
    assert scheduler.cancel(first) is False
    scheduler.run_once()
    assert result == [2]


def test_scheduler_rejects_invalid_or_full_queue():
    with pytest.raises(TypeError):
        Scheduler(max_pending=True)
    with pytest.raises(ValueError):
        Scheduler(max_pending=0)

    scheduler = Scheduler(max_pending=1)
    scheduler.submit(lambda: None)
    with pytest.raises(RuntimeError, match="queue is full"):
        scheduler.submit(lambda: None)


def test_scheduler_cancel_validates_task_id():
    scheduler = Scheduler()
    with pytest.raises(TypeError):
        scheduler.cancel(True)


def test_scheduler_rejects_non_callable_tasks():
    scheduler = Scheduler()
    with pytest.raises(TypeError):
        scheduler.submit(123)
