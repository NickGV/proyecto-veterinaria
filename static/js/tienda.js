document.addEventListener("DOMContentLoaded", () => {
  const carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  const botones = document.querySelectorAll(".add-to-cart");
  const categoriaSelect = document.getElementById("categoria-select");

  botones.forEach((boton) => {
    boton.addEventListener("click", () => {
      const producto = {
        id: boton.getAttribute("data-id"),
        nombre: boton.getAttribute("data-name"),
        precio: boton.getAttribute("data-price"),
      };

      carrito.push(producto);
      localStorage.setItem("carrito", JSON.stringify(carrito));
      alert(`${producto.nombre} añadido al carrito`);
    });
  });

  categoriaSelect.addEventListener("change", (event) => {
    const categoriaSeleccionada = event.target.value;
    const productos = document.querySelectorAll(".product");

    productos.forEach((producto) => {
      if (
        categoriaSeleccionada === "todas" ||
        producto.getAttribute("data-categoria") === categoriaSeleccionada
      ) {
        producto.style.display = "block";
      } else {
        producto.style.display = "none";
      }
    });
  });
});
