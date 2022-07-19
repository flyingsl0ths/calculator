from api import calculator
from typing import Callable, Union
from flask import Flask, request
from os import environ

app = Flask(__name__.split(".")[0])


OPS: dict[
    calculator.Operations,
    Callable[[Union[float, int], Union[float, int]], Union[float, int]],
] = {
    calculator.Operations.ADD: calculator.add,
    calculator.Operations.SUB: calculator.subtract,
    calculator.Operations.MUL: calculator.multiply,
    calculator.Operations.DIV: calculator.divide,
}


@app.route("/api/add", methods=["POST"])
def add() -> str:
    return str(operation(calculator.Operations.ADD))


@app.route("/api/subtract", methods=["POST"])
def subtract() -> str:
    return str(operation(calculator.Operations.SUB))


@app.route("/api/multiply", methods=["POST"])
def multiply() -> str:
    return str(operation(calculator.Operations.MUL))


@app.route("/api/divide", methods=["POST"])
def divide() -> str:
    return str(operation(calculator.Operations.DIV))


def operation(
    method: calculator.Operations,
) -> Union[float, int]:
    factors: tuple[Union[float, int], Union[float, int]]

    x = request.json.get("x")  # type: ignore
    y = request.json.get("y")  # type: ignore

    if x and y:
        factors = (float(x), float(y))
    else:
        return 0.0

    return solve(method, factors)


def solve(
    method: calculator.Operations,
    factors: tuple[Union[float, int], Union[float, int]],
) -> Union[float, int]:
    return OPS[method](factors[0], factors[1])


def get_port() -> int:
    port_number = environ.get("PORT")
    return int(port_number) if port_number else 5000


app.run(host="0.0.0.0", port=get_port())
