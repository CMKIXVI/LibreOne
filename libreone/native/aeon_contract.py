"""LibreOne-owned contracts for AEON-derived native capabilities.

The contracts intentionally avoid depending on AEON implementation details.
They define the integration points that native implementations must satisfy.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class NativeBuffer:
    """A bounded native memory region owned by the runtime."""

    size: int
    alignment: int = 1

    def __post_init__(self) -> None:
        if not isinstance(self.size, int) or isinstance(self.size, bool) or self.size < 0:
            raise ValueError("size must be a non-negative integer")
        if not isinstance(self.alignment, int) or isinstance(self.alignment, bool) or self.alignment <= 0:
            raise ValueError("alignment must be a positive integer")


@dataclass(frozen=True)
class TensorDescriptor:
    """Stable metadata contract for native tensors."""

    dtype: str
    shape: tuple[int, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.dtype, str) or not self.dtype.strip():
            raise ValueError("dtype cannot be empty")
        if any(not isinstance(dim, int) or isinstance(dim, bool) or dim < 0 for dim in self.shape):
            raise ValueError("tensor dimensions must be non-negative integers")


class NativeMemory(Protocol):
    def allocate(self, size: int, alignment: int = 1) -> NativeBuffer: ...
    def release(self, buffer: NativeBuffer) -> None: ...


class NativeTensorRuntime(Protocol):
    def create(self, descriptor: TensorDescriptor) -> object: ...
    def release(self, tensor: object) -> None: ...


class NativeModelRuntime(Protocol):
    def load(self, model_id: str) -> object: ...
    def unload(self, model: object) -> None: ...
