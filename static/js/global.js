document.addEventListener("DOMContentLoaded", () => {
  console.log("click");
  const hamburger = document.querySelector(".hamburger-menu");

  hamburger.addEventListener("click", () => {
    toggleMenu();
  });

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

  const closeBtn = document.querySelector(".close-btn");

  closeBtn.addEventListener("click", () => {
    const info = document.getElementById("info");
    const seccionPerfilU = document.getElementById("inf-user");

    if (info && seccionPerfilU) {
      info.classList.toggle("hidden");
      seccionPerfilU.classList.toggle("hidden");
    }
  });

  window.addEventListener("resize", () => {
    const navbar = document.querySelector(".navbar");
    if (window.innerWidth > 768 && navbar.classList.contains("active")) {
      navbar.classList.remove("active");
      document.body.style.overflow = "";
    }
  });
});
