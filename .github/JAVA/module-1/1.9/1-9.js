function checkPrimeNumber() {
    const number = parseInt(prompt("Enter an integer:"), 10);

    if (isNaN(number) || number <= 1) {
        document.getElementById("primeResult").textContent = "Please enter a valid integer greater than 1.";
        return;
    }

    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }

    const resultContainer = document.getElementById("primeResult");
    if (isPrime) {
        resultContainer.textContent = `${number} is a prime number.`;
    } else {
        resultContainer.textContent = `${number} is not a prime number.`;
    }
}
window.onload = function() {
    checkPrimeNumber();
};