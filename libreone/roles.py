from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Role:
    name: str
    permissions: frozenset[str]

def can(role: Role, permission: str) -> bool:
    return permission in role.permissions
