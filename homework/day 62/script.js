function performOperations() {
    let num1 = parseFloat(prompt("Enter the first number:"));

    let num2 = parseFloat(prompt("Enter the second number:"));

    if (isNaN(num1) || isNaN(num2)) {
        console.log("Please enter valid numbers.");
        return;
    }

    let addition = num1 + num2;
    let subtraction = num1 - num2;
    let multiplication = num1 * num2;
    let division = num1 / num2;

    console.log("The addition of " + num1 + " and " + num2 + " is: " + addition);
    console.log("The subtraction of " + num1 + " from " + num2 + " is: " + subtraction);
    console.log("The multiplication of " + num1 + " and " + num2 + " is: " + multiplication);
    console.log("The division of " + num1 + " by " + num2 + " is: " + division);
}
performOperations();
