from libreone.system.process import Process, ProcessState


def test_stopped_process_can_restart():
    process = Process("worker")
    process.start()
    process.stop()
    process.start()
    assert process.state is ProcessState.RUNNING
