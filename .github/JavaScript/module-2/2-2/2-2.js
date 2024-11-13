let number = parseInt(prompt("Enter the number of participants"));
let names = [];

if (!isNaN(number) && number > 0) {
    for (let i = 0; i < number; i++) {
        let name = prompt("Enter the name of participant " + (i + 1));
        names.push(name);
    }
}

names.sort();
let listContainer = document.querySelector(".list");
let ol = document.createElement("ol");  

names.forEach(name => {
    let li = document.createElement("li");
    li.textContent = name;
    ol.appendChild(li);
});

listContainer.appendChild(ol);