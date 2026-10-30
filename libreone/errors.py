"""Stable LibreOne exception hierarchy."""

class LibreOneError(Exception):
    """Base exception for expected LibreOne failures."""

class ConfigurationError(LibreOneError):
    """Invalid or incomplete configuration."""

class ValidationError(LibreOneError):
    """Input or state failed validation."""

class CapabilityError(LibreOneError):
    """A requested capability cannot execute."""
