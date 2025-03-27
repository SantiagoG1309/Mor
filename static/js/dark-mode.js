// Script para manejar el modo oscuro
document.addEventListener('DOMContentLoaded', function() {
    // Verificar si hay una preferencia guardada en localStorage
    const darkModeEnabled = localStorage.getItem('darkMode') === 'enabled';
    
    // Aplicar el modo oscuro si estaba habilitado previamente
    if (darkModeEnabled) {
        document.body.classList.add('dark-mode');
        updateDarkModeButton();
    }
    
    // Obtener el botón de modo oscuro
    const darkModeButton = document.querySelector('.btn-mode');
    
    // Si existe el botón, añadir el evento click
    if (darkModeButton) {
        darkModeButton.addEventListener('click', function(e) {
            e.preventDefault(); // Prevenir la navegación por defecto
            
            // Alternar la clase dark-mode en el body
            document.body.classList.toggle('dark-mode');
            
            // Guardar la preferencia en localStorage
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('darkMode', 'enabled');
            } else {
                localStorage.setItem('darkMode', 'disabled');
            }
            
            // Actualizar el texto del botón
            updateDarkModeButton();
        });
    }
    
    // Función para actualizar el texto del botón según el modo actual
    function updateDarkModeButton() {
        const darkModeButton = document.querySelector('.btn-mode');
        if (darkModeButton) {
            const icon = darkModeButton.querySelector('i');
            
            if (document.body.classList.contains('dark-mode')) {
                // Cambiar a icono de sol y texto para modo claro
                if (icon) icon.className = 'fas fa-sun';
                darkModeButton.innerHTML = darkModeButton.innerHTML.replace('Modo Oscuro', 'Modo Claro');
            } else {
                // Cambiar a icono de luna y texto para modo oscuro
                if (icon) icon.className = 'fas fa-moon';
                darkModeButton.innerHTML = darkModeButton.innerHTML.replace('Modo Claro', 'Modo Oscuro');
            }
        }
    }
});