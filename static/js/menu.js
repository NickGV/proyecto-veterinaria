let slideIndex = 1; // Inicia en la primera imagen
    showSlides(slideIndex);

    // Función para mover el carrusel
    function moveSlide(n) {
        showSlides(slideIndex += n);
    }

    // Función para mostrar el slide actual
    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    // Función para mostrar los slides según el índice
    function showSlides(n) {
        let slides = document.querySelectorAll('.carrusel-item');
        let dots = document.querySelectorAll('.dot');
        
        // Asegurarse de que el índice esté dentro del rango
        if (n > slides.length) {
            slideIndex = 1;
        }
        if (n < 1) {
            slideIndex = slides.length;
        }
        
        // Ocultar todas las imágenes
        slides.forEach((slide, index) => {
            slide.style.display = 'none';
            dots[index].classList.remove('active');
        });
        
        // Mostrar la imagen correspondiente
        slides[slideIndex - 1].style.display = 'block';
        dots[slideIndex - 1].classList.add('active');
    }

    // Configurar el carrusel para que avance automáticamente
    setInterval(() => {
        moveSlide(1);
    }, 3000); // Avanza cada 5 segundos