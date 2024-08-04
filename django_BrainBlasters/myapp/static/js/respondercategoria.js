function skipQuestion() {
    // Lógica para saltar la pregunta
}

// Lógica del cronómetro
let timerBar = document.getElementById('timer-bar');
let width = 100;
let interval = setInterval(function() {
    if (width <= 0) {
        clearInterval(interval);
        // Lógica cuando el tiempo se acaba
    } else {
        width--;
        timerBar.style.width = width + '%';
    }
}, 100);