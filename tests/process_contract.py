from libreone.system.process import Process, ProcessState


def verify_process_contract() -> bool:
    process = Process("contract")
    process.start()
    process.stop()
    return process.state is ProcessState.STOPPED
