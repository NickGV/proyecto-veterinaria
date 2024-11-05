document.addEventListener('DOMContentLoaded', () => {
    const carritoContainer = document.querySelector('.carrito-container');
    const totalPriceElement = document.getElementById('total-price');
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];


    function actualizarCarrito() {
        carritoContainer.innerHTML = ''; 
        let total = 0;

        carrito.forEach((producto, index) => {
           
            const productoHTML = `
                <div class="carrito-item">
                    <h3>${producto.nombre}</h3>
                    <p>Precio: $${producto.precio}</p>
                    <button class="remove-button" data-index="${index}">Eliminar</button>
                </div>
            `;
            carritoContainer.innerHTML += productoHTML;
            total += parseFloat(producto.precio); 
        });

        totalPriceElement.textContent = total.toFixed(2); 
    }

    
    carritoContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('remove-button')) {
            const index = e.target.getAttribute('data-index'); 
            carrito.splice(index, 1); 
            localStorage.setItem('carrito', JSON.stringify(carrito)); 
            actualizarCarrito(); 
        }
    });

    
    actualizarCarrito();
});
