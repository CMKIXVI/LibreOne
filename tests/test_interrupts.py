from libreone.system.interrupts import InterruptTable


def test_interrupt_dispatch():
    table = InterruptTable()
    seen = []
    table.register(1, lambda: seen.append(1))
    table.dispatch(1)
    assert seen == [1]
