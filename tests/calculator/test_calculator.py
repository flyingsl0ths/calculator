from pytest import raises
from api import calculator


def test_add():
    assert calculator.add(1, 2) == 3.0
    assert calculator.add(1.0, 2.0) == 3.0
    assert calculator.add(0, 2.0) == 2.0
    assert calculator.add(2.0, 0) == 2.0
    assert calculator.add(-4, 2.0) == -2.0


def test_subtract():
    assert calculator.subtract(1, 2) == -1.0
    assert calculator.subtract(2, 1) == 1.0
    assert calculator.subtract(1.0, 2.0) == -1.0
    assert calculator.subtract(0, 2.0) == -2.0
    assert calculator.subtract(2.0, 0.0) == 2.0
    assert calculator.subtract(-4, 2.0) == -6.0


def test_multiply():
    assert calculator.multiply(1, 2) == 2.0
    assert calculator.multiply(1.0, 2.0) == 2.0
    assert calculator.multiply(0, 2.0) == 0.0
    assert calculator.multiply(2.0, 0.0) == 0.0
    assert calculator.multiply(-4, 2.0) == -8.0


def test_divide():
    assert calculator.divide(1, 2) == 0.5
    assert calculator.divide(1.0, 2.0) == 0.5
    assert calculator.divide(0, 2.0) == 0
    assert calculator.divide(-4, 2.0) == -2.0


def test_division_by_zero() -> None:
    with raises(ZeroDivisionError):
        calculator.divide(10, 0)
