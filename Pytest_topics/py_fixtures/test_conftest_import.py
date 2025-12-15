import pytest

def test_len(block01, block02):
    assert len(pytest.weekdays1 + block02) == len(block01 + pytest.weekdays2)