import pytest

from libreone.system.process import Process, ProcessState


def test_process_lifecycle():
    process = Process("worker")
    assert process.state is ProcessState.CREATED
    process.start()
    assert process.state is ProcessState.RUNNING
    process.stop()
    assert process.state is ProcessState.STOPPED


def test_process_rejects_invalid_start():
    process = Process("worker")
    process.start()
    with pytest.raises(RuntimeError):
        process.start()


def test_process_rejects_invalid_stop():
    process = Process("worker")
    with pytest.raises(RuntimeError):
        process.stop()
