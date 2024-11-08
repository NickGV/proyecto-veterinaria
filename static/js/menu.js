// Función para mostrar y ocultar la barra lateral
function toggleSidebar() {
  const sidebar = document.querySelector(".sidebar");
  const body = document.querySelector("body");
  const closeBtn = document.querySelector(".toggle-btn");
  closeBtn.classList.toggle("close");

  // Verificamos el estado actual de la barra lateral
  if (sidebar.style.right === "0px") {
    sidebar.style.right = "-250px"; // Ocultar la barra lateral
    body.style.marginRight = "0"; // Volver el contenido principal a su posición inicial
    closeBtn.textContent = "☰";
  } else {
    sidebar.style.right = "0"; // Mostrar la barra lateral
    body.style.marginRight = "250px"; // Desplazar el contenido principal
    closeBtn.textContent = "X";
  }
}
function toggleInfo() {
  const info = document.getElementById("info");
  const seccionPerfilU = document.getElementById("inf-user");
  info.classList.toggle("hidden");
  seccionPerfilU.classList.toggle("hidden");
}
