from libreone.system.interrupts import InterruptTable


def test_interrupt_dispatch():
    table = InterruptTable()
    seen = []
    table.register(7, lambda value: seen.append(value))
    table.dispatch(7, "ok")
    assert seen == ["ok"]
