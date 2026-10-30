import pytest
from libreone.system.process import Process


def test_process_cannot_stop_before_start():
    with pytest.raises(RuntimeError):
        Process("init").stop()
