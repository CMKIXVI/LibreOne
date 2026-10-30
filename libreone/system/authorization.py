from .policy import Policy


class Authorizer:
    def __init__(self, policies: tuple[Policy, ...] | list[Policy] = ()) -> None:
        self._policies = tuple(policies)

    def allowed(self) -> bool:
        return all(policy.permits() for policy in self._policies)

    def authorize(self, resource: str | None = None) -> bool:
        return all(policy.permits(resource) for policy in self._policies)
