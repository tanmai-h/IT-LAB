function validate() {
    email = document.getElementById("email").value;
    pass =  document.getElementById("pass").value;
    error = document.getElementById("form-error");
    
    if(email == "" || pass == "" || email == "" || pass == "") {
        error.innerHTML = "Both fields required";
        return false;
    }
    if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        error.innerHTML = "Invalid email";
        return false;
    }
    else {
        error.innerHTML = "";
        alert("Welcome");
        return true;
    }
}

function signup() {
    email = document.getElementById("email").value;
    name = document.getElementById("name").value;
    phone = document.getElementById("phone").value;
    pass =  document.getElementById("pass").value;
    confpass =  document.getElementById("confpass").value;
    
    error = document.getElementById("form-error");
    
    if(email == "" || pass == "" || name == "" || phone == "" || confpass == "") {
        error.innerHTML = "All fields required";
        return false;
    }
    else if(!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        error.innerHTML = "Invalid email";
        return false;
    }
    else if(!phone.match( /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/)) {
        error.innerHTML = "Invalid Mobile Num";
        return false;
    }
    else if(pass != confpass) {
        error.innerHTML = "Passwords must match";
        return false;
    }
    else if(pass.length < 6) {
        error.innerHTML = "Passwords must be atleast 6 characters long";
        return false;
    }
    else {
        error.innerHTML = "";
        alert("Welcome " + name + ", you have been registered");
        return true;
    }
}

function amount() {
    time = document.getElementById("time").value;
    money = document.getElementById("money");

    if(time == 0) {
        money.innerHTML = "Please select a duration for you recharge pack";
    }
    else if(time == 1) {
        money.innerHTML = "&#8377 120";
    }
    else if(time == 3) {
        money.innerHTML = "&#8377 328";
    }
    else if(time == 5) {
        money.innerHTML = "&#8377 578";
    }
}
function recharge() {
    email = document.getElementById("email").value;
    phone = document.getElementById("phone").value;
    time = document.getElementById("time").value;
    error = document.getElementById("form-error");
    money = document.getElementById("money").innerHTML;

    if(email == "" || phone == "" || time == 0) {
        error.innerHTML = "All fields required";
        return false;
    }
    else if(!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        error.innerHTML = "Invalid email";
        return false;
    }
    else if(!phone.match( /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/)) {
        error.innerHTML = "Invalid Mobile Num";
        return false;
    }
    
    else {
        error.innerHTML = "";
        alert("Thank you for selecting the " + money + " pack. We will redirect you shortly to the payment gateway");

        return true;
    }
}