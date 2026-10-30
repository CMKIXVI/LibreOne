from .policy import Policy


class Authorizer:
    def __init__(self, policies: tuple[Policy, ...] = ()) -> None:
        self._policies = policies

    def allowed(self) -> bool:
        return all(policy.permits() for policy in self._policies)
