function validateSigninForm(){
	var x = document.forms["myForm"]["Email"].value;
	if (x == "") {
		alert("Name must be filled out");
		return false;
	}
	var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	if(re.test(String(x).toLowerCase())==false){
		alert("Incorrect Email Format!");
		return false;
	}
	var pswd=document.forms["myForm"]["Password"].value;
	if(pswd==""){
		alert("Password not filled!");
		return false;
	}
	var check = /^[A-Z]*[@#$%&*()]*$/;
	if(check.test(String(pswd))==false){
		alert("Incorrect Password Format!");
		return false;
	}
}

function validateSignupForm(){
	var x = document.forms["signupform"]["Email"].value;
	if (x == "") {
		alert("Name must be filled out");
		return false;
	}
	var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	if(re.test(String(x).toLowerCase())==false){
		alert("Incorrect Email Format!");
		return false;
	}
	// Validating password
	var pswd=document.forms["signupform"]["psw"].value;
	var rpswd=document.forms["signupform"]["psw-repeat"].value;
	if(pswd!=rpswd){
		alert("Passwords don't match!");
		return false;
	}
}