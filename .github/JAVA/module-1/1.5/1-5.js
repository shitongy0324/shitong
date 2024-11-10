const year = Number(prompt ('Enter a year'))
if (isNaN(year)){
     alert(`Please enter a valid year.`)
}
else {if ((year % 4 ===0 && year %100 !== 0) || (year % 400 === 0 )){
    document.querySelector('#year').innerHTML=`${year} is a leap year.`}
    else{
        document.querySelector('#year').innerHTML=`${year} is not a leap year.`
    }
}
