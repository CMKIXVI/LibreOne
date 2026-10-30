class LibreOneError(Exception):
    """Base exception for expected LibreOne failures."""

class ValidationError(LibreOneError):
    """Raised when an input violates a domain invariant."""

class PolicyDenied(LibreOneError):
    """Raised when policy denies an operation."""

class CapabilityUnavailable(LibreOneError):
    """Raised when a requested capability is unavailable."""
