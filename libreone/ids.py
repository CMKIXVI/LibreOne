"""Identifier helpers with explicit string serialization."""
from __future__ import annotations
from uuid import UUID, uuid4

def new_id() -> UUID:
    return uuid4()

def id_text(value: UUID) -> str:
    return str(value)
