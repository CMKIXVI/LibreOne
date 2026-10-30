from libreone.system.process import Process, ProcessState


def test_process_lifecycle():
    process = Process("test")
    assert process.state is ProcessState.CREATED
    process.start()
    assert process.state is ProcessState.RUNNING
    process.stop()
    assert process.state is ProcessState.STOPPED


def test_process_ids_are_unique():
    assert Process("a").id != Process("b").id
