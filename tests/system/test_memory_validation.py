import pytest

from libreone.system.memory import MemoryRegion


def test_memory_region_rejects_negative_start():
    with pytest.raises(ValueError):
        MemoryRegion(-1, 10)


def test_memory_region_rejects_nonpositive_size():
    with pytest.raises(ValueError):
        MemoryRegion(0, 0)
