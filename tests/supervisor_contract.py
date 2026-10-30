from libreone.system.supervisor import Supervisor


def verify_supervisor_contract() -> bool:
    supervisor = Supervisor()
    return hasattr(supervisor, "start_all") and hasattr(supervisor, "stop_all")
