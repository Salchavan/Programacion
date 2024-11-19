const sum = (num1, num2) => {
    result = parseInt(num1) + parseInt(num2);
    return result;
}
const subtract = (num1, num2) => {
    result = parseInt(num1) - parseInt(num2);
    return result;
}
const division = (num1, num2) => {
    result = parseInt(num1) / parseInt(num2);
    return result;
}
const multiplication = (num1, num2) => {
    result = parseInt(num1) * parseInt(num2);
    return result;
}
while (true) {
    alert("What operation you want to perform");
    let election = prompt("1-Sum | 2-Subtract | 3-Division | 4-Multiplication");
    if (election == 1) {
        result = sum(prompt("Enter the number 1"), prompt("Enter the number 2"))
        alert("The result is " + result);
    }
    else if (election == 2) {
        result = subtract(prompt("Enter the number 1"), prompt("Enter the number 2"))
        alert("The result is " + result);
    }
    else if (election == 3) {  
        result = division(prompt("Enter the number 1"), prompt("Enter the number 2"))
        alert("The result is " + result);
    }
    else if (election == 4) {  
        result = multiplication(prompt("Enter the number 1"), prompt("Enter the number 2"))
        alert("The result is " + result);
    }
}