// Evento para el botón de cancelar en recuperar.html
document.getElementById("cancelarButton").addEventListener("click", function() {
    alert("Regresando a la página de login...");
    window.location.href = "http://127.0.0.1:3000/Login/login.html";
});
