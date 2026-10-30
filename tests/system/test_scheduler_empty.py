from libreone.system.scheduler import Scheduler


def test_empty_scheduler_is_idle():
    scheduler = Scheduler()
    assert scheduler.pending == 0
    assert scheduler.run_once() is None
