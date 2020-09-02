function clearForm(){
    document.getElementById("name").value="";
    document.getElementById("pwd").value="";
}

//Button
var login_btn = document.getElementById("login");

login_btn.addEventListener("click", () => {
    clearForm();
});




var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
    if (this.readyState == 1 && this.status == 200){
        alert(this.responseText);
    } else if (this.readyState == 1) {
        alert("Log in fehlgeschlagen "+ this.readyState);
    }
}
function sendRequest(){
    var benutzername = document.getElementById("name").value;
    var password = document.getElementById("pwd").value;

    xhttp.open("POST", "http://142.93.98.32:80/auth/token",  true);
    xhttp.setRequestHeader("Content-type", application/x-www-form-urlencoded);
    xhttp.send(benutzername & password);
}



clearForm();