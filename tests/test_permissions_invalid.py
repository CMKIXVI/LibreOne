import pytest
from libreone.system.permissions import Permission


def test_permission_values_are_flags():
    assert Permission.ADMIN
    assert Permission.READ != Permission.WRITE
