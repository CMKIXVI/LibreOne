class SystemError(Exception):
    """Base error for LibreOne system services."""


class StateError(SystemError):
    """Raised when an operation violates lifecycle state."""


class ResourceError(SystemError):
    """Raised when a required system resource is unavailable."""
