function findLeapYears() {
    const startYear = parseInt(prompt("Enter the start year:"), 10);
    const endYear = parseInt(prompt("Enter the end year:"), 10);

    if (isNaN(startYear) || isNaN(endYear) || startYear > endYear) {
        alert("Please enter valid years with the start year less than or equal to the end year.");
        return;
    }

    const leapYears = [];
    for (let year = startYear; year <= endYear; year++) {
        if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
            leapYears.push(year);
        }
    }

    const resultContainer = document.getElementById("leapYears");
    resultContainer.innerHTML = "";
    if (leapYears.length > 0) {
        const ul = document.createElement("ul");
        leapYears.forEach(year => {
            const li = document.createElement("li");
            li.textContent = year;
            ul.appendChild(li);
        });
        resultContainer.appendChild(ul);
    } else {
        resultContainer.textContent = "No leap years found in the given range.";
    }
}

window.onload = function() {
    findLeapYears();
};