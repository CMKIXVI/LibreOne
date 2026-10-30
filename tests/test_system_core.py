from libreone.system.boot_manifest import BootManifest
from libreone.system.bootstrap import Bootstrap
from libreone.system.cancellation import CancellationToken
from libreone.system.checksum import sha256_file
from libreone.system.config import SystemConfig
from libreone.system.identity import Identity
from libreone.system.policy import Decision, Policy
from libreone.system.process import Process, ProcessState
from libreone.system.serialization import decode, encode
from libreone.system.state import StateError, SystemPhase, SystemState
from libreone.system.storage import Storage


def test_state_transitions_are_explicit():
    state = SystemState()
    state.transition(SystemPhase.BOOTING)
    state.transition(SystemPhase.INITIALIZING)
    state.transition(SystemPhase.RUNNING)
    assert state.phase is SystemPhase.RUNNING


def test_invalid_state_transition_is_rejected():
    state = SystemState()
    try:
        state.transition(SystemPhase.RUNNING)
    except StateError:
        return
    raise AssertionError("invalid transition was accepted")


def test_process_lifecycle():
    process = Process("init")
    assert process.state is ProcessState.CREATED
    process.start()
    assert process.state is ProcessState.RUNNING
    process.stop()
    assert process.state is ProcessState.STOPPED


def test_identity_ids_are_unique():
    assert Identity().id != Identity().id


def test_policy_permission():
    assert Policy("read", Decision.ALLOW).permits("read")
    assert not Policy("read", Decision.DENY).permits("read")


def test_storage_confines_paths(tmp_path):
    storage = Storage(tmp_path)
    target = storage.resolve("nested/data.txt")
    target.parent.mkdir(parents=True)
    target.write_text("ok", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == "ok"


def test_serialization_is_round_trip():
    value = {"name": "LibreOne", "version": 1}
    assert decode(encode(value)) == value


def test_cancellation_token():
    token = CancellationToken()
    assert not token.cancelled
    token.cancel()
    assert token.cancelled


def test_boot_manifest_validation():
    manifest = BootManifest("1", "x86_64", "libreone", "a" * 64)
    assert manifest.architecture == "x86_64"


def test_bootstrap_reaches_running(tmp_path):
    config = SystemConfig(environment="test", data_dir=tmp_path)
    state = Bootstrap().initialize(config)
    assert state.phase is SystemPhase.RUNNING


def test_checksum(tmp_path):
    path = tmp_path / "data"
    path.write_bytes(b"LibreOne")
    digest = sha256_file(path)
    assert len(digest) == 64
