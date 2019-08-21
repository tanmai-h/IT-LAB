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
    else {
        error.innerHTML = "";
        alert("Welcome " + name + ", you have been registered");
        return true;
    }
}