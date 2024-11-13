function handleForm(event){
    event.preventDefault();
    let form = event.target;
    let rating = form.serviceRating.value;
    rating = "poor";
    let feedback = document.getElementById("serviceRatingFeedback");
    console.log(rating);
    if(rating==="poor" || rating === "good" || rating === "excellent"){
        feedback.innerText="";
    } else{
        feedback.innerText = "Feedback should be poor, good or excellent";
        feedback.style = "color:red";
    }
    
    
    // Calculations for tip
    let costBefore = form.billTotal.value;
    let numPeople = form.numPaying.value;
    let costDisplay = document.getElementById("totalWithTip");
    let perPerson = document.getElementById("perPerson");
    let poorTip = costBefore;
    let goodTip = costBefore*1.1;
    let excellentTip = costBefore*1.2;
    console.log(costBefore);
    console.log(rating);
    console.log(poorTip);
    console.log(goodTip);
    console.log(rating + "1");
    if(rating === "poor"){
        costDisplay.innerText = poorTip.toFixed(2);
        console.log("rating poor");
        perPerson.innerText = poorTip.toFixed(2)/numPeople;
    } else if(rating==="good"){
        costDisplay.innerText = goodTip.toFixed(2);
        perPerson.innerText = goodTip.toFixed(2)/numPeople;
    } else if(rating === "excellent"){
        costDisplay.innerText = excellentTip.toFixed(2);
        perPerson.innerText = excellentTip.toFixed(2)/numPeople;
    } else{
        costDisplay.innerText = "";
    }
    console.log(rating + "2")
}

function tester(){  

    let rating = "poor";
    let costDisplay = {};
    let perPerson = {};
    let poorTip = 100;
    let numPeople = 2;

    if(rating === "poor"){
        costDisplay.innerText = poorTip.toFixed(2);
        console.log("rating poor");
        perPerson.innerText = poorTip.toFixed(2)/numPeople;
    } 
    console.log(rating + "2")
}

tester()
