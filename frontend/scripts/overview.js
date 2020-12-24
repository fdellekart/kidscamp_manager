function checkAuthToken() {
    token = sessionStorage.getItem("kc_manager_token");
    if(token == null) {
        window.location.assign("http://localhost:80/login/");
    }
}

const app = new Vue({
    el: "#app",
    data: {
        kids: []
    },
    created: function () {
            checkAuthToken();
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "http://localhost:80/allapplications/");
            xhttp.onreadystatechange = function () {
                if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 200) {
                    console.log(xhttp.response);
                    app.kids = JSON.parse(xhttp.response);
                } else if (xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 401) {
                    console.log("Not authorized!")
                    window.location.assign("http://localhost:80/login/")
                }
            }
            xhttp.setRequestHeader("authorization", "Bearer " + sessionStorage.getItem("kc_manager_token"))
            xhttp.send()
        }
    },
)
