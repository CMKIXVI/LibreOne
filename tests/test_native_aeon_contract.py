import pytest

from libreone.native.aeon_contract import NativeBuffer, TensorDescriptor


def test_native_buffer_contract_is_immutable_and_validated():
    buffer = NativeBuffer(size=4096, alignment=64)
    assert buffer.size == 4096
    assert buffer.alignment == 64
    with pytest.raises(Exception):
        buffer.size = 1


def test_native_buffer_rejects_invalid_values():
    with pytest.raises(ValueError):
        NativeBuffer(size=-1)
    with pytest.raises(ValueError):
        NativeBuffer(size=True)
    with pytest.raises(ValueError):
        NativeBuffer(size=1, alignment=0)


def test_tensor_descriptor_contract():
    descriptor = TensorDescriptor(dtype="f32", shape=(1, 8, 16))
    assert descriptor.dtype == "f32"
    assert descriptor.shape == (1, 8, 16)


def test_tensor_descriptor_rejects_invalid_metadata():
    with pytest.raises(ValueError):
        TensorDescriptor(dtype="", shape=(1,))
    with pytest.raises(ValueError):
        TensorDescriptor(dtype="f32", shape=(-1,))
    with pytest.raises(ValueError):
        TensorDescriptor(dtype="f32", shape=(True,))
