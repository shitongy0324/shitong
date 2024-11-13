let dognames = []
for (i = 0;i<5;i++){
    names = prompt(`${i+1},enter the dog's name`);
    dognames.push(names);
};
dognames.sort().reverse();
let doglist = document.getElementById("dogeslist")
dognames.forEach(name=>{
    let listItem = document.createElement('li');
    listItem.textContent = name;
    doglist.appendChild(listItem);
})
