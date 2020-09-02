function clearForm(){
    document.getElementById("name").value="";
    document.getElementById("pwd").value="";
}

//Button
var login_btn = document.getElementById("login");

login_btn.addEventListener("click", () => {

    clearForm();
});


//login
function validate(){
    var benutzername = document.getElementById("name").value;
    var password = document.getElementById("pwd").value;

    if (benutzername === "flotschi" && password === "12345"){
        window.location = "./overview.html";
        return false;
    } else {
        alert("Login fehlgeschlagen");
        return false;
    }
}



clearForm();