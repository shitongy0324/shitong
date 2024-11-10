let answer = confirm('Should I calculate the square root?');
if (answer === true){
    const number = Number(prompt('enter a positive number '))
    if ((isNaN(number) || (number<0))){
        alert('enter a positive number ')
    } 
    else{
        const root = Math.sqrt(number)
        document.querySelector('#root').innerHTML=`it square root is ${root}`
    }
}
else{
    document.querySelector('#root').innerHTML='The square root is not calculated.'
}