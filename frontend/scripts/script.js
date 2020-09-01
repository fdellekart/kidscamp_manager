function clearForm(){
    document.getElementById("name").value="";
    document.getElementById("pwd").value="";
}

//Button
var login_btn = document.getElementById("login");

login_btn.addEventListener("click", () => {
    clearForm();
});



clearForm();