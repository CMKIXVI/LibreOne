from libreone.system.memory import MemoryRegion


def test_memory_region_contains_boundaries():
    region = MemoryRegion(100, 20)
    assert region.contains(100)
    assert region.contains(119)
    assert not region.contains(120)
