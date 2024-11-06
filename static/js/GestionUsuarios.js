// Array para almacenar los usuarios
let usuarios = [];

// Registrar Usuario
document.getElementById("form-usuarios").addEventListener("submit", function(event) {
    event.preventDefault();

    // Obtener datos del formulario
    const nombre = document.getElementById("nombre").value;
    const correo = document.getElementById("correo").value;

    // Crear objeto usuario y agregarlo al array
    const usuario = { nombre, correo, historial: [] };
    usuarios.push(usuario);

    // Actualizar tabla de usuarios
    actualizarTablaUsuarios();

    // Resetear el formulario
    this.reset();
});

// Actualizar tabla de usuarios
function actualizarTablaUsuarios() {
    const tabla = document.getElementById("tabla-usuarios").querySelector("tbody");
    tabla.innerHTML = ""; // Limpiar tabla

    usuarios.forEach((user, index) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td>${user.nombre}</td>
            <td>${user.correo}</td>
            <td>${user.historial.length > 0 ? user.historial.join(", ") : "Sin compras registradas"}</td>
            <td>
                <button onclick="editarUsuario(${index})">Editar</button>
                <button onclick="eliminarUsuario(${index})">Eliminar</button>
            </td>
        `;
        tabla.appendChild(fila);
    });
}

// Editar Usuario
function editarUsuario(index) {
    const usuario = usuarios[index];
    document.getElementById("nombre").value = usuario.nombre;
    document.getElementById("correo").value = usuario.correo;

    // Eliminar usuario temporalmente para actualizar después
    usuarios.splice(index, 1);
    actualizarTablaUsuarios();
}

// Eliminar Usuario
function eliminarUsuario(index) {
    usuarios.splice(index, 1); // Eliminar usuario
    actualizarTablaUsuarios(); // Actualizar tabla
}

// Función para volver al menú principal
function volverAlMenu() {
    window.location.href = "menu_principal.html";
}
