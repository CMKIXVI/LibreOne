"""Stable minimal intermediate representation for execution plans."""
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Operation:
    opcode: str
    operands: tuple[str, ...] = ()

@dataclass(frozen=True, slots=True)
class Program:
    operations: tuple[Operation, ...] = field(default_factory=tuple)
