document.addEventListener("DOMContentLoaded", function()){
    const { generate, solve } = require('sudoku-gen');

    let difficulty = "easy"; // Puedes cambiar la dificultad a "medium" o "hard"
    let sudoku = generate(difficulty); // Genera un sudoku aleatorio
    let solution = solve(sudoku); // Obtiene la solución del sudoku
    
    displaySudoku(sudoku); // Función que muestra el Sudoku en la página

    document.getElementById("formPuntuacion").addEventListener("submit", function(event) {
        event.preventDefault();
        let userSolution = getUserSolution(); // Función que obtiene la solución del usuario
        let points = calculatePoints(userSolution, solution); // Función que calcula los puntos
        
        document.getElementById("puntos").value = points;
        this.submit();
    });
}