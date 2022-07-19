from enum import Enum, unique
from typing import Union


@unique
class Operations(Enum):
    """Available calculator operations"""

    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3


def add(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    """Adds two numbers

    Args:
        x (float|int): Left operand
        y (float|int): Right operand

    Returns:
        float|int: The sum of the two operands
    """
    return x + y


def subtract(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    """Subtracts two numbers

    Args:
        x (float|int): Left operand
        y (float|int): Right operand

    Returns:
        float|int: The difference of the two operands
    """
    return x - y


def multiply(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    """Multiplies two numbers

    Args:
        x (float|int): Left operand
        y (float|int): Right operand

    Returns:
        float|int: The product of the two operands
    """
    return x * y


def divide(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    """Divides two numbers

    Args:
        x (float|int): Left operand
        y (float|int): Right operand

    Returns:
        float|int: The division of the two operands
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x * 1.0 / y
