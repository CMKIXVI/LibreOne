from libreone.system.policy import Decision


def test_policy_decision_values_are_unique():
    values = [decision.value for decision in Decision]
    assert len(values) == len(set(values))
