from libreone.system.memory import MemoryRegion


def test_memory_region_bounds():
    region = MemoryRegion(100, 50)
    assert region.end == 150
    assert region.contains(100)
    assert region.contains(149)
    assert not region.contains(150)
