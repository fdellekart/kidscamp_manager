function clearForm(){
    document.getElementById("name").value="";
    document.getElementById("pwd").value="";
}

//Button
var login_btn = document.getElementById("login");

login_btn.addEventListener("click", () => {
    clearForm();
});




// xhttp.onreadystatechange = function () {
//     if (this.readyState == 1 && this.status == 200){
//         alert(this.responseText);
//     } else if (this.readyState == 1) {
//         alert("Log in fehlgeschlagen "+ this.status);
//     }
// }
function sendRequest(){
    var benutzername = document.getElementById("name").value;
    var password = document.getElementById("pwd").value;
    var xhttp = new XMLHttpRequest();

    xhttp.open("POST", "http://142.93.98.32:80/auth/token",  false);
    xhttp.setRequestHeader("Content-type", application/x-www-form-urlencoded);
    xhttp.send(benutzername & password);
    alert(xhttp.responseText)
}



clearForm();