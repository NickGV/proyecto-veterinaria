document.getElementById("ingresarButton").addEventListener("click", function() {
    const dni = document.getElementById("dni").value;
    const password = document.getElementById("password").value;

    if (dni && password) {
        alert("Ingreso exitoso");
    } else {
        alert("Por favor, ingrese su DNI y contraseña.");
    }
});

