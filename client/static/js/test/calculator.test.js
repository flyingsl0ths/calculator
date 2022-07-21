import Calculator from "../CalculatorView.js";

import { describe, test } from "mocha";
import assert from "assert";

describe("Calculator", () => {
    test("calculator clears", () => {
        const calculator = new Calculator();
        calculator.clear();

        assert.strictEqual(calculator.currentOperand, "");
        assert.strictEqual(calculator.previousOperand, "");
        assert.strictEqual(calculator.operation, "");
        assert.strictEqual(calculator.validOperand, true);
    });

    test("calculator can input numbers", () => {
        const calculator = new Calculator();
        calculator.appendNumber(1);
        assert.strictEqual(calculator.currentOperand, "1");

        calculator.appendNumber(2);
        assert(calculator.currentOperand, "12");
    });

    test("calculator can delete", () => {
        const calculator = new Calculator();
        calculator.appendNumber(1);
        assert.strictEqual(calculator.currentOperand, "1");

        calculator.appendNumber(2);
        assert(calculator.currentOperand, "12");

        calculator.delete();
        assert.strictEqual(calculator.currentOperand, "1");
    });
});
