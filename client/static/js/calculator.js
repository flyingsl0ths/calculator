import Calculator from "./CalculatorView.js";

const calculatorContainer = document.querySelector("#calculator");

const previousOperandTextElement = document.querySelector(
    "[data-previous-operand]"
);

const currentOperandTextElement = document.querySelector(
    "[data-current-operand]"
);

const calculator = new Calculator(
    previousOperandTextElement,
    currentOperandTextElement
);

const onCalculationError = () => alert("Unable to perform calculation");

calculatorContainer.addEventListener("click", event => {
    const target = event.target;
    if (target.hasAttribute("data-operation")) {
        calculator.compute(onCalculationError);
        calculator.updateOperation(event.target.innerText);
        calculator.updateDisplay();
    } else if (target.hasAttribute("data-number")) {
        calculator.appendNumber(event.target.innerText);
        calculator.updateDisplay();
    } else if (target.hasAttribute("data-equals")) {
        calculator.compute(onCalculationError);
    } else if (target.hasAttribute("data-all-clear")) {
        calculator.clear();
        calculator.updateDisplay();
    }
});

document.addEventListener("keydown", function (event) {
    const patternForNumbers = /[0-9]/g;
    const patternForOperators = /[+\-*/]/g;

    if (event.key.match(patternForNumbers)) {
        event.preventDefault();
        calculator.appendNumber(event.key);
        calculator.updateDisplay();
    }
    if (event.key === ".") {
        event.preventDefault();
        calculator.appendNumber(event.key);
        calculator.updateDisplay();
    }
    if (event.key.match(patternForOperators)) {
        event.preventDefault();
        calculator.updateOperation(event.key);
        calculator.updateDisplay();
    }
    if (event.key === "Enter" || event.key === "=") {
        event.preventDefault();
        calculator.compute();
    }
});
