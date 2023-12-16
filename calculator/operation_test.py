# pytest
# coverage run -m pytest
# coverage report -m
from operation import add, minus, multiply


def test_add():
    assert add(1, 2) == 3, "Should be 3"
    assert add(1, 1) == 2, "Should be 2"


def test_minus():
    assert minus(1, 1) == 0, "Should be 0"


def test_multiply():
    assert multiply(0, 1) == 0, "Should be 0"
    assert multiply(1, 1) == 1, "Should be 1"
