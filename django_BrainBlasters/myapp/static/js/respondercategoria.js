function skipQuestion() {
    // Lógica para saltar la pregunta
}

function startCountdown(seconds) {
    let timerBar = document.getElementById('timer-bar');
    let width = 100; // Comienza con 100% de la barra
    let intervalTime = 100; // Tiempo de intervalo en ms
    let decrement = 100 / (seconds * 1000 / intervalTime); // Calcula el decremento por intervalo

    let interval = setInterval(function() {
        if (width <= 0) {
            clearInterval(interval);
            timerBar.style.width = '0%'; // Asegura que la barra se quede vacía
            // Lógica cuando el tiempo se acaba
            console.log('Tiempo terminado');
        } else {
            width -= decrement;
            timerBar.style.width = width + '%';
        }
    }, intervalTime);
}
