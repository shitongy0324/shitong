const rolls = parseInt(prompt("Enter the number of dice rolls"), 10);

if (isNaN(rolls) || rolls <= 0) {
    document.querySelector('#result').innerHTML = "Please enter a valid number of rolls.";
} else {
    let sum = 0;

    for (let i = 0; i < rolls; i++) {
        const roll = Math.floor(Math.random() * 6) + 1;
        sum += roll; 
    }

    document.querySelector('#result').innerHTML = `The total sum of ${rolls} dice rolls is ${sum}.`;
}