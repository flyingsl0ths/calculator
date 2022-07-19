from api import calculator
from typing import Callable, Union
from flask import Flask, request
from os import environ

app = Flask(__name__.split(".")[0])


OPS: dict[calculator.Operations, Callable[[int, int], Union[float, int]]] = {
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
    factors: list[int] = []

    x: int = request.json.get("x")  # type: ignore
    y: int = request.json.get("y")  # type: ignore

    if x and y:
        factors.append(int(x))
        factors.append(int(y))
    else:
        return 0

    return solve(method, factors)


def solve(
    method: calculator.Operations,
    factors: list[int],
) -> Union[float, int]:
    return OPS[method](factors[0], factors[1])


def get_port() -> int:
    port_number = environ.get("PORT")
    return int(port_number) if port_number else 8080


app.run(host="0.0.0.0", port=get_port())
