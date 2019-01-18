let result = 0.0;
let operand = "";
let operator = "";

function resetCalculator() {
    operand = "";
    operator = "";
    display(operand);
    log();
}

function display(value) {
    var resultBox = document.getElementById("result-box");
    resultBox.childNodes.forEach(
        function (node, key, parent) {
            node.remove();
        }
    );
    var text = document.createTextNode(value);
    resultBox.appendChild(text);
}

function appendDigit(digit) {
    operand += digit;
    display(operand);
    log();
}

function appendOperation(newOperator) {
    if (operator == "") {
    result = parseFloat(operand);
    } else   if (operator == "+"){
            result = result + parseFloat(operand);
    } else   if (operator == "-"){
            result = result - parseFloat(operand);
    } else   if (operator == "*"){
            result = result * parseFloat(operand);
    } else   if (operator == "/"){
            result = result / parseFloat(operand);
            }

    operator = newOperator;
    operand = "";
    display(result);
    log();
}

function appendDecimalPeriod() {     
    operand += ".";
    display(operand);
    log();
}

function equal() {
    appendOperation("");
}

function log() {
    console.log("Operand: " + operand);
    console.log("Operator: " + operator);
    console.log("Result: " + result);
}