document.addEventListener('DOMContentLoaded', function () {
    let slideIndex = 1; // Inicia en la primera imagen
    showSlides(slideIndex);

    // Función para mover el carrusel (avance o retroceso)
    function moveSlide(n) {
        showSlides(slideIndex += n);
    }

    // Función para mostrar el slide actual
    function showSlides(n) {
        let slides = document.querySelectorAll('.carrusel-item'); // Selecciona todas las imágenes
        let totalSlides = slides.length; // Número total de imágenes

        // Asegurarse de que el índice esté dentro del rango
        if (n > totalSlides) {
            slideIndex = 1; // Si el índice es mayor que el número total de imágenes, vuelve a la primera
        }
        if (n < 1) {
            slideIndex = totalSlides; // Si el índice es menor que 1, va a la última imagen
        }

        // Ocultar todas las imágenes
        slides.forEach((slide) => {
            slide.style.display = 'none'; // Ocultar cada imagen
        });

        // Mostrar la imagen correspondiente
        slides[slideIndex - 1].style.display = 'block'; // Mostrar la imagen actual
    }

    // Configurar el carrusel para que avance automáticamente cada 5 segundos
    setInterval(() => {
        moveSlide(1); // Avanza una imagen cada 5 segundos
    }, 3000);

    // Función para el botón "anterior"
    const prevButton = document.querySelector('.prev');
    prevButton.addEventListener('click', () => {
        moveSlide(-1); // Retrocede una imagen
    });

    // Función para el botón "siguiente"
    const nextButton = document.querySelector('.next');
    nextButton.addEventListener('click', () => {
        moveSlide(1); // Avanza una imagen
    });
});
