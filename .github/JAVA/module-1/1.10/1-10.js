function simulateDiceProbability() {
    const numDice = parseInt(prompt("Enter the number of dice:"), 10);
    const targetSum = parseInt(prompt("Enter the sum of the eyes you are interested in:"), 10);

    if (isNaN(numDice) || isNaN(targetSum) || numDice <= 0 || targetSum <= 0) {
        document.getElementById("diceResult").textContent = "Please enter valid positive numbers for dice and sum.";
        return;
    }

    let successfulOutcomes = 0;
    const simulations = 10000;

    for (let i = 0; i < simulations; i++) {
        let sum = 0;
        for (let j = 0; j < numDice; j++) {
            sum += Math.floor(Math.random() * 6) + 1; // Rolling a dice (1-6)
        }
        if (sum === targetSum) {
            successfulOutcomes++;
        }
    }

    const probability = (successfulOutcomes / simulations) * 100;
    document.getElementById("diceResult").textContent = `The probability of getting the sum ${targetSum} with ${numDice} dice is approximately ${probability.toFixed(2)}%.`;
}
window.onload = function() {
    simulateDiceProbability();
};