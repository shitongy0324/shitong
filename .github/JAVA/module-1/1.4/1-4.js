const name = prompt("Enter your name");
const number = Math.floor(Math.random()*4 + 1);
let class_name;
switch (number) {
    case 1:
        class_name= `Ravenclaw.`
        break
    case 2:
        class_name = `Hufflepuff.`
        break
    case 3:
       class_name=`Slytherin.`
        break
    case 4:
        class_name=`Gryffindor.`
        break
}
document.querySelector('#target').innerHTML = `${name}, your class is ${class_name}`;