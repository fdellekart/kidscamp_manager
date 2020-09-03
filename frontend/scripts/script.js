function clearForm(){
    document.getElementById("name").value="";
    document.getElementById("pwd").value="";
}

function sendRequest(){
    var username = document.getElementById("name").value;
    var password = document.getElementById("pwd").value;
    console.log("sendRequest called");

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200){
            document.cookie = "access-token=" + JSON.parse(this.responseText).access_token;
            window.location("http://142.93.98.32:80/overview");
        } else if (this.readyState == 4){
            alert("Log in fehlgeschlagen "+ this.status);
        }
    };

    xhttp.open("POST", "http://142.93.98.32:80/auth/token",  true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.setRequestHeader("accept", "application/json");
    xhttp.send(JSON.stringify({"username" : username, "password" : password}));
}

//Button
var login_btn = document.getElementById("login");

login_btn.addEventListener("click", () => {
    sendRequest();
    clearForm();
});



clearForm();