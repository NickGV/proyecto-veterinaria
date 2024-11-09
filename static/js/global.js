function toggleMenu() {
  const navbar = document.querySelector(".navbar");
  navbar.classList.toggle("active");

  document.body.style.overflow = navbar.classList.contains("active")
    ? "hidden"
    : "";
}

function toggleInfo() {
  const info = document.getElementById("info");
  const seccionPerfilU = document.getElementById("inf-user");

  if (info && seccionPerfilU) {
    info.classList.toggle("hidden");
    seccionPerfilU.classList.toggle("hidden");
  }
}

document.querySelectorAll(".nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    const navbar = document.querySelector(".navbar");
    if (navbar.classList.contains("active")) {
      toggleMenu();
    }
  });
});

window.addEventListener("resize", () => {
  const navbar = document.querySelector(".navbar");
  if (window.innerWidth > 768 && navbar.classList.contains("active")) {
    navbar.classList.remove("active");
    document.body.style.overflow = "";
  }
});