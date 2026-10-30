from libreone.system.scheduler import Scheduler


def verify_scheduler_contract() -> bool:
    scheduler = Scheduler()
    seen = []
    scheduler.submit(lambda: seen.append("ran"))
    scheduler.run_once()
    return seen == ["ran"] and scheduler.pending() == 0
