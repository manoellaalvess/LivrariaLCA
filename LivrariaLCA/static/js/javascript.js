let userLog = document.getElementById("email");
let senhaLog = document.getElementById("senha");

function loginValidate(){
    if (userLog.value == "user@gmail.com" && senhaLog.value == "123"  ){
    localStorage.setItem("acesso", true);

    window.location.href = "convite.html";
    } else {
        alert('Senha ou usuário incorreto')
    }
}