import pytest
from api import calculator


class TestCalculator:
    x: int = 10
    y: int = 20

    def test_add(self) -> None:
        assert calculator.add(self.x, self.y) == 30

    def test_subtraction(self) -> None:
        assert calculator.subtract(self.y, self.x) == 10

    def test_multiplication(self) -> None:
        assert calculator.multiply(self.y, self.x) == 200

    def test_division(self) -> None:
        assert calculator.divide(self.y, self.x) == 2.0

    def test_division_by_zero(self) -> None:
        with pytest.raises(ZeroDivisionError):
            calculator.divide(self.x, 0)
