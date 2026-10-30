from libreone.system.state import SystemPhase


def test_system_phase_values_are_unique():
    values = [phase.value for phase in SystemPhase]
    assert len(values) == len(set(values))
