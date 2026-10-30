from libreone.system.ipc import Channel


def verify_ipc_contract() -> bool:
    channel = Channel.create()
    channel.send("hello")
    return channel.receive() == "hello"
