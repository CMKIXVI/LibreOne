from libreone.system.timeout import Timeout


def test_timeout_value():
    timeout = Timeout(2.5)
    assert timeout.seconds == 2.5
