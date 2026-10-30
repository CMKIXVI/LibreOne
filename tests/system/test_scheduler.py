from libreone.system.scheduler import Scheduler


def test_scheduler_executes_fifo():
    scheduler = Scheduler()
    seen = []
    scheduler.submit(lambda: seen.append("a"))
    scheduler.submit(lambda: seen.append("b"))
    assert scheduler.run_once() is None
    assert scheduler.run_once() is None
    assert seen == ["a", "b"]
    assert scheduler.pending == 0
