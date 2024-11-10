const number_1 = parseInt(prompt('enter the first number'))
const number_2 = parseInt(prompt('enter the second number'))
const number_3 = parseInt(prompt('enter the third munber'))

const sum = number_1 + number_2 + number_3
const product = number_1 * number_2 * number_3
const average = sum / 3
document.querySelector('#target').innerHTML = `The sum of three numbers is ${sum}\nThe product of three numbers is ${product}\nThe average of three number is ${average}`