const options = () => {
    document.write("1- Sum 2- Subtract 3- division 4- multiplication 6- Empowerment 6- Square Root 7- Cube Root")
}
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
const empowerment = (num1, num2) => {
    result = parseInt(num1) ** parseInt(num2);
    return result;
}
const quadraticRadiation = (num1) => {
    result = Math.sqrt(parseInt(num1));
    return result;
}
const cubicRadiation = (num1) => {
    result = Math.cbrt(parseInt(num1));
    return result;
}

let election = prompt("What operation you want to perform? 1- Sum 2- Subtract 3- division 4- multiplication 6- Empowerment 6- Square Root 7- Cube Root");

if (election == 1) {
    result = sum(prompt("Enter the number 1"), prompt("Enter the number 2"))
    alert("The result is " + result);
} else if (election == 2) {
    result = subtract(prompt("Enter the number 1"), prompt("Enter the number 2"))
    alert("The result is " + result);
} else if (election == 3) {  
    result = division(prompt("Enter the number 1"), prompt("Enter the number 2"))
    alert("The result is " + result);
} else if (election == 4) {  
    result = multiplication(prompt("Enter the number 1"), prompt("Enter the number 2"))
    alert("The result is " + result);
} else if (election == 5) {  
    result = empowerment(prompt("Enter the number 1"), prompt("Enter the number 2"))
    alert("The result is " + result);
} else if (election == 6) {  
    result = quadraticRadiation(prompt("Enter the number"))
    alert("The result is " + result);
} else if (election == 7) {  
    result = cubicRadiation(prompt("Enter the number"))
    alert("The result is " + result);
} 



