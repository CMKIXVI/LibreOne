from libreone.system.policy import Decision, Policy


def verify_policy_contract() -> bool:
    policy = Policy("read", Decision.ALLOW)
    return policy.permits("read")
