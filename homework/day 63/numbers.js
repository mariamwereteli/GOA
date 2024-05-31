function compareNumbers() {
    var number1 = parseFloat(document.getElementById('number1').value);
    var number2 = parseFloat(document.getElementById('number2').value);

    console.log("Number 1 is greater than Number 2: " + (number1 > number2));
    console.log("Number 1 is less than Number 2: " + (number1 < number2));
    console.log("Number 1 is equal to Number 2: " + (number1 === number2));
    console.log("Number 1 is not equal to Number 2: " + (number1 !== number2));
    console.log("Number 1 is greater than or equal to Number 2: " + (number1 >= number2));
    console.log("Number 1 is less than or equal to Number 2: " + (number1 <= number2));
}

document.getElementById('compareButton').addEventListener('click', compareNumbers);
