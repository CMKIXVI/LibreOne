from libreone.system.process import ProcessState


def test_process_state_values_are_unique():
    values = [state.value for state in ProcessState]
    assert len(values) == len(set(values))
