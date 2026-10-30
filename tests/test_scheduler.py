from libreone.system.scheduler import Scheduler


def test_scheduler_runs_submitted_callable():
    scheduler = Scheduler()
    result = []
    scheduler.submit(lambda: result.append(1))
    scheduler.run_once()
    assert result == [1]
    assert scheduler.pending == 0
