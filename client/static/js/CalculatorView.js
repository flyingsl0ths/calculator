import CalculatorController from "./CalculatorController.js";

export default class Calculator {
    constructor(
        previousOperandTextElement,
        currentOperandTextElement,
        apiURl = "http://localhost:5000/api/"
    ) {
        this.previousOperandTextElement = previousOperandTextElement;
        this.currentOperandTextElement = currentOperandTextElement;
        this.apiURl = apiURl;
        this.clear();
    }

    clear() {
        this.currentOperand = "";
        this.previousOperand = "";
        this.operation = "";
        this.validOperand = true;
    }

    delete() {
        this.currentOperand = this.currentOperand.toString().slice(0, -1);
    }

    appendNumber(number) {
        if (!this.validOperand) {
            return;
        }

        if (number === "." && this.currentOperand.includes(".")) {
            return;
        }

        this.currentOperand = this.currentOperand + number.toString();
    }

    compute(onError) {
        if (!this.validOperand) {
            return;
        } else if (
            this.currentOperand.length === 0 &&
            this.previousOperand.length === 0
        ) {
            return;
        }

        const prev = parseFloat(this.previousOperand);
        const current = parseFloat(this.currentOperand);

        if (isNaN(prev) || isNaN(current)) {
            return;
        }

        let operation;
        switch (this.operation) {
            case "+":
                operation = "add";
                break;
            case "-":
                operation = "subtract";
                break;
            case "*":
                operation = "multiply";
                break;
            case "÷":
                operation = "divide";
                break;
            default:
                return;
        }

        const callbacks = {
            onSuccess: result => {
                this.currentOperand = result;
                this.operation = "";
                this.previousOperand = "";
                this.updateDisplay();
            },
            onError: onError
        };

        CalculatorController.callApi(
            this.apiURl + operation,
            JSON.stringify({
                x: this.previousOperand,
                y: this.currentOperand
            }),
            callbacks
        );
    }

    updateOperation(operation) {
        if (!this.validOperand) {
            return;
        }

        this.operation = operation;
        this.previousOperand = this.currentOperand;
        this.currentOperand = "";
    }

    updateDisplay() {
        const currentOperandResult = CalculatorController.toDisplayNumber(
            this.currentOperand
        );

        if (currentOperandResult.hadParserError) {
            this.validOperand = false;
        }

        this.currentOperandTextElement.innerText = currentOperandResult.result;

        if (this.operation) {
            const previousOperandResult = CalculatorController.toDisplayNumber(
                this.previousOperand
            );

            if (previousOperandResult.hadParserError) {
                this.validOperand = false;
            }

            this.previousOperandTextElement.innerText = `${previousOperandResult.result} ${this.operation}`;
        } else {
            this.previousOperandTextElement.innerText = "";
        }
    }
}
