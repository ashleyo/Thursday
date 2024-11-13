function validateUsername(username) {
    let feedback = document.getElementById("usernameFeedback");

    if (username.length < 8) {
        feedback.innerText = "Username must be at least 8 characters long";
        return false;
    }

    if (username.length > 16) {
        feedback.innerText = "Username must not be more than 16 characters long";
        return false;
    }
    
        feedback.innerText = "";
        return true;
    }
}

