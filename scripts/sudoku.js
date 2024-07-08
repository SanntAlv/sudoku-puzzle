import { getSudoku } from "sudoku-gen";
document.addEventListener("DOMContentLoaded", function() {
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


    function displaySudoku(grid) {
        // Muestra el Sudoku en la página
        let table = document.createElement('table');
        for (let i = 0; i < 9; i++) {
            let row = document.createElement('tr');
            for (let j = 0; j < 9; j++) {
                let cell = document.createElement('td');
                if (grid[i][j] !== 0) {
                    cell.textContent = grid[i][j];
                } else {
                    let input = document.createElement('input');
                    input.setAttribute('type', 'number');
                    input.setAttribute('min', '1');
                    input.setAttribute('max', '9');
                    input.setAttribute('maxlength', '1');
                    cell.appendChild(input);
                }
                row.appendChild(cell);
            }
            table.appendChild(row);
        }
        document.getElementById('sudokuContainer').appendChild(table);
    }

    function getUserSolution() {
        // Obtiene la solución ingresada por el usuario
        let solution = [];
        let rows = document.querySelectorAll('#sudokuContainer tr');
        rows.forEach((row, i) => {
            let cells = row.querySelectorAll('td');
            solution[i] = [];
            cells.forEach((cell, j) => {
                let input = cell.querySelector('input');
                solution[i][j] = input ? parseInt(input.value) || 0 : parseInt(cell.textContent);
            });
        });
        return solution;
    }

});