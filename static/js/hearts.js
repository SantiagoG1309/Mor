// Animación de corazones flotantes
document.addEventListener('DOMContentLoaded', function() {
    const heartsContainer = document.querySelector('.hearts-bg');
    
    // Crear corazones flotantes
    function createHearts() {
        const heart = document.createElement('div');
        heart.classList.add('heart');
        
        // Tamaño aleatorio
        const size = Math.random() * 20 + 10;
        heart.style.width = `${size}px`;
        heart.style.height = `${size}px`;
        
        // Posición inicial aleatoria
        const startPos = Math.random() * 100;
        heart.style.left = `${startPos}%`;
        
        // Color aleatorio (tonos de rosa y rojo)
        const colors = ['#ff6b6b', '#ff8e8e', '#ffb3b3', '#ff9999', '#e91e63', '#f48fb1'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        heart.style.backgroundColor = randomColor;
        
        // Añadir al contenedor
        heartsContainer.appendChild(heart);
        
        // Animación
        const duration = Math.random() * 5 + 5; // Entre 5 y 10 segundos
        heart.style.animation = `float ${duration}s linear forwards`;
        
        // Eliminar después de la animación
        setTimeout(() => {
            heart.remove();
        }, duration * 1000);
    }
    
    // Crear corazones periódicamente
    setInterval(createHearts, 300);
    
    // Crear algunos corazones iniciales
    for (let i = 0; i < 15; i++) {
        setTimeout(createHearts, 100 * i);
    }
    
    // Añadir estilos CSS para la animación
    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0% {
                bottom: -20px;
                transform: translateX(0) rotate(0deg) scale(1);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                bottom: 100%;
                transform: translateX(${Math.random() > 0.5 ? '+' : '-'}100px) rotate(${Math.random() * 360}deg) scale(0.5);
                opacity: 0;
            }
        }
        
        .heart {
            position: fixed;
            bottom: -20px;
            background-color: #ff6b6b;
            display: inline-block;
            height: 20px;
            width: 20px;
            transform: rotate(-45deg);
            z-index: 0;
        }
        
        .heart:before,
        .heart:after {
            content: '';
            background-color: inherit;
            border-radius: 50%;
            height: 100%;
            width: 100%;
            position: absolute;
        }
        
        .heart:before {
            top: -50%;
            left: 0;
        }
        
        .heart:after {
            top: 0;
            right: -50%;
        }
    `;
    document.head.appendChild(style);
});