from enum import Enum, unique


@unique
class Operations(Enum):
    """Available calculator operations"""

    ADD: int = 0
    SUB: int = 1
    MUL: int = 2
    DIV: int = 3


def add(x: int, y: int) -> int:
    """Adds two numbers

    Args:
        x (int): Left operand
        y (int): Right operand

    Returns:
        int: The sum of the two operands
    """
    return x + y


def subtract(x: int, y: int) -> int:
    """Subtracts two numbers

    Args:
        x (int): Left operand
        y (int): Right operand

    Returns:
        int: The difference of the two operands
    """
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiplies two numbers

    Args:
        x (int): Left operand
        y (int): Right operand

    Returns:
        int: The product of the two operands
    """
    return x * y


def divide(x: int, y: int) -> float:
    """Divides two numbers

    Args:
        x (int): Left operand
        y (int): Right operand

    Returns:
        int: The division of the two operands
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x * 1.0 / y
