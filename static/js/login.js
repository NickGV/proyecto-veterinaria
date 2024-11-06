document.getElementById("ingresarButton").addEventListener("click", function() {
    const dni = document.getElementById("dni").value;
    const password = document.getElementById("password").value;

    if (dni && password) {
        alert("Ingreso exitoso");
    } else {
        alert("Por favor, ingrese su DNI y contraseña.");
    }
});

document.getElementById("registrarButton").addEventListener("click", function() {
    window.location.href = "file:///C:/Users/Usuario/OneDrive/Documentos/Proyecto%20Pagina%20Web/Registro/registro.html";
    alert("Redirigiendo a la página de registro...");
});

document.getElementById("recuperarButton").addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:3000/RecuperarContrasena/recuperar.html";
    alert("Redirigiendo a la página de recuperación de contraseña...");
    redirectToRecover();
});
