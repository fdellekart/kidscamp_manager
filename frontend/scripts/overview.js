function checkAuth() {
    token = sessionStorage.getItem("kc_manager_token");
    if(token == null) {
        window.location.assign("http://anmeldung.kidscamp.at/login/");
    }
}

function getAllKidsData() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://anmeldung.kidscamp.at/allapplications/");
    xhttp.onreadystatechange = function () {
        if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 200) {
            console.log(xhttp.response)
            return JSON.parse(xhttp.response)
        } else if (xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 401) {
            console.log("Not authorized!")
            window.location.assign("http://anmeldung.kidscamp.at/login/")
        }
    }
    xhttp.setRequestHeader("authorization", "Bearer " + sessionStorage.getItem("kc_manager_token"))
    xhttp.send()
}

checkAuth()
getAllKidsData()
