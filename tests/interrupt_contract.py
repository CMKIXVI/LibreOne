from libreone.system.interrupts import InterruptTable


def verify_interrupt_contract() -> bool:
    table = InterruptTable()
    seen = []
    table.register(1, lambda: seen.append(1))
    table.dispatch(1)
    return seen == [1]
