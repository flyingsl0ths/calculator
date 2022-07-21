const CalculatorController = {
    callApi(endPoint, json, { onSuccess, onError }) {
        const req = {
            method: "POST",
            headers: {
                Accept: "text/html",
                "Content-Type": "application/json"
            },

            body: json
        };

        const onOk = res => {
            res.json().then(onSuccess).catch(onError);
        };

        fetch(endPoint, req).then(onOk).catch(onError);
    },

    toDisplayNumber(number) {
        const parsedNumber = number.toString();
        const [ints, decimals = false] = parsedNumber.split(".");

        const integerDigits = parseFloat(ints);

        let integerDisplay = ints;
        let parserError = false;
        if (isNaN(integerDigits)) {
            integerDisplay = parsedNumber;
            if (parsedNumber.length > 0) {
                parserError = true;
            }
        }

        return {
            result:
                parserError || !decimals
                    ? integerDisplay
                    : `${integerDisplay}.${decimals}`,
            hadParserError: parserError
        };
    }
};

export default CalculatorController;
