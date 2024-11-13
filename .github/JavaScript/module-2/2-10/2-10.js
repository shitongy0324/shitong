let candidates_number = parseInt(prompt(`enter the number of candidates.`),10);
let candidates_name = [];
if (isNaN(candidates_number)){
    alert(`please enter a correct number`);
}
for (let i=0 ; i <candidates_number;i++){
    let names = prompt(`enter the name of candidates ${i+1}`);
    candidates_name.push({name:`${names}`,votes:0});
}
let voter_number = parseInt(prompt(`enter the number of voters`))
if (isNaN(voter_number)){
    alert(`please enter a correct number`);
}
for (let i=0;i<voter_number;i++){
    let votes = prompt(`choose your candidate`)
    if (votes!==""){
        candidates_name.forEach((dict)=>{
            if(dict.name===votes){
                dict.votes = dict.votes+1
            }
        })
    }
}
candidates_name.sort((a, b) => b.votes - a.votes);
const candidates_list = document.getElementById("candidates_list");
candidates_name.forEach((dict,index)=>{
    let listItem = document.createElement("li");
    listItem.innerHTML=`<strong>${index+1}.</strong>Name:${dict.name}<br>Votes:${dict.votes}`
    candidates_list.appendChild(listItem);
})