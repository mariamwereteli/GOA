function sumEvenNumbers(start, end) {
    let total = 0;
    for (let num = start; num <= end; num++) {
        if (num % 2 === 0) {
            total += num;
        }
    }
    return total;
}
let start = 1;
let end = 10;
let result = sumEvenNumbers(start, end);
console.log("Sum of even numbers between", start, "and", end, "is:", result);