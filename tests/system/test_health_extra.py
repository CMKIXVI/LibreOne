from libreone.system.health import Health


def test_health_states_are_distinct():
    assert len(set(Health)) == 3
