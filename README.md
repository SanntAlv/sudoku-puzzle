sudoku-puzzle:

La idea principal de este proyecto es que, se inicia la aplicacion y lo primero que se pide es un nombre de usuario (en caso de no existir lo crea en el momento), luego lo reedirige a la pagina principal donde se puede seleccionar la dificultad y en base a esta se genera un sudoku para resolver. Una vez resuelto por el usuario se compara con la solucion real y en caso de que sean las mismas entonces se le asigna una x cantidad de puntos al usuario.
La cantidad de puntos depende directamente de la dificultad del sudoku y del tiempo tardado
Cuando quiera, el usuario puede ser redirigido a una pagina donde se muestra una ranking de todos los jugadores y de los puntos de cada uno.

tabla: usuarios
-id
-nombre usuario
-puntuacion

tabla: puntuaciones
-id
-id_usuarios
-dificultad
-tiempo
-puntos
