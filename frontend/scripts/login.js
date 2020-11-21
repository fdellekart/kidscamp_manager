function clearForm(){
    document.getElementById("name").value="";
    document.getElementById("pwd").value="";
}

function sendRequest(){
    var username = document.getElementById("name").value;
    var password = document.getElementById("pwd").value;
    
    var formData = new FormData();

    formData.append("username", username)
    formData.append("password", password)

    var xhttp = new XMLHttpRequest();

    xhttp.open("POST", "http://localhost:8000/auth/token");
    xhttp.onreadystatechange = function () {
        if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 200) {
            response = JSON.parse(xhttp.response)
            // xhttp.response = {"access_token":"test","token_type":"bearer"}
            sessionStorage.setItem("kc_manager_token", response["access_token"])
            window.location.assign("http://localhost:8000/overview/")
        }
    }
    xhttp.send(formData);

}

//Button
var login_btn = document.getElementById("login");

login_btn.addEventListener("click", () => {
    sendRequest();
    clearForm();
});



clearForm();