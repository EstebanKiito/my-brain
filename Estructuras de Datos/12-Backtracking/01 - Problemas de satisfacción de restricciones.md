---
ramo: "Estructuras de Datos"
tema: "Backtracking"
tags:
  - edd
  - csp
  - backtracking
  - modelamiento
  - origen/complemento
prerrequisitos:
  - "[[01 - Inducción simple, fuerte y estructural]]"
---

# Problemas de satisfacción de restricciones

Muchos problemas consisten en **asignar valores** a un conjunto de variables de modo que se cumplan ciertas reglas: ubicar reinas en un tablero, llenar un sudoku, colorear un mapa, cargar una mochila. Todos comparten la misma forma, llamada **CSP**, y por eso se resuelven con la misma herramienta: **backtracking**. En las interrogaciones, lo primero que se pide suele ser **modelar**: identificar variables, dominios y restricciones.

## El ejemplo clásico: 8 reinas

![Problema de las 8 reinas](adjuntos/Problema%20de%20las%208%20reinas.png)

> [!example]- Transcripción de la imagen
> "Consideremos el problema de posicionar 8 reinas en un tablero de ajedrez de modo que no se ataquen". Las reinas se desplazan por filas, columnas y diagonales; para lograr el objetivo, deben estar en columnas, filas y diagonales diferentes. Abajo, un tablero vacío de 8 × 8.

![Las reinas como vector de columnas](adjuntos/Las%20reinas%20como%20vector%20de%20columnas.png)

> [!example]- Transcripción de la imagen
> Cada fila y columna está en el rango 1…8. Se denota por $x_i$ la columna de la reina en la fila $i$, de modo que las posiciones de las 8 reinas se describen como un vector $(x_1, \dots, x_8)$. "¿Cómo sabemos si $(4, 6, 8, 2, 7, 1, 3, 5)$ es una solución?".

![Tablero con la solución 4 6 8 2 7 1 3 5](adjuntos/Tablero%20con%20la%20soluci%C3%B3n%204%206%208%202%207%201%203%205.png)

> [!example]- Transcripción de la imagen
> Tablero de 8 × 8 con $Q_1$ en la columna 4, $Q_2$ en la 6, $Q_3$ en la 8, $Q_4$ en la 2, $Q_5$ en la 7, $Q_6$ en la 1, $Q_7$ en la 3 y $Q_8$ en la 5: ninguna comparte columna ni diagonal.

> [!tip] Un buen modelo simplifica las restricciones
> Poner **una reina por fila** y que la variable sea su **columna** hace que la restricción de filas se cumpla sola. Solo quedan dos chequeos: columnas distintas ($x_i \ne x_j$) y diagonales distintas, porque dos reinas están en la misma diagonal si la "pendiente" entre ellas vale $\pm 1$: $|x_j - x_i| = |j - i|$.

## Definición

![Definición de CSP](adjuntos/Definici%C3%B3n%20de%20CSP.png)

> [!example]- Transcripción de la imagen
> Un **problema de satisfacción de restricciones** (*constraint satisfaction problem*, CSP) es una tripleta $(X, D, C)$: $X = \{x_1, \dots, x_n\}$ es un conjunto de **variables**, $D = \{D_1, \dots, D_n\}$ el conjunto de sus **dominios** respectivos y $C = \{C_1, \dots, C_m\}$ un conjunto de **restricciones**, donde cada una involucra un subconjunto de variables de $X$. Una **solución** es una asignación de las variables en sus dominios que satisface todas las restricciones. Observaciones: las variables no necesariamente tienen el mismo dominio, y una restricción $C_j$ puede involucrar 1, 2 o más variables.

![Las 8 reinas como CSP](adjuntos/Las%208%20reinas%20como%20CSP.png)

> [!example]- Transcripción de la imagen
> "El problema de las 8 reinas efectivamente es un CSP". Variables: $X = \{x_1, \dots, x_8\}$, donde cada $x_i$ es la columna de la reina en la fila $i$. Dominios: $D = \{B, \dots, B\}$ con $B = \{1, \dots, 8\}$, el mismo para todas. Restricciones: la de filas está implícita en la elección de las variables; para columnas, $i \ne j \to x_i \ne x_j$; para diagonales, la slide escribe $i \ne j \to |(x_j - x_i)/(j - i)| = 1$.

La restricción de diagonales debe exigir que esa pendiente **no** valga 1: $|(x_j - x_i)/(j - i)| \ne 1$.

![Sudoku como CSP](adjuntos/Sudoku%20como%20CSP.png)

> [!example]- Transcripción de la imagen
> Un sudoku de 9 × 9 parcialmente lleno (por ejemplo, 9 en la esquina superior derecha, 7 y 6, 8 en la tercera fila, etc.).

En el **sudoku**, cada celda vacía es una variable con dominio $\{1, \dots, 9\}$, y las restricciones prohíben repetir un número en una fila, en una columna o en un cuadrante de 3 × 3.

> [!warning] Cómo elegir las variables
> Las variables deberían ser **independientes** entre sí. Si unas se deducen de otras, probablemente sobran. Primero hay que entender el problema y después decidir el modelo; casi siempre hay más de una forma válida de hacerlo.

## Preguntas de repaso

> [!question]- ¿Qué tres elementos definen un CSP?
> Las variables $X$, el dominio de valores posibles de cada una ($D$) y las restricciones $C$, que relacionan los valores de una o más variables.

> [!question]- En el modelo de las 8 reinas, ¿por qué no hay que verificar que dos reinas estén en filas distintas?
> Porque cada variable $x_i$ es la columna de la reina de la fila $i$: hay exactamente una reina por fila por construcción. La restricción de filas queda implícita en el modelo.

> [!question]- ¿Cómo se detecta que dos reinas $i$ y $j$ están en la misma diagonal?
> Si $|x_j - x_i| = |j - i|$, es decir, si se desplazan lo mismo en columnas que en filas (pendiente $\pm 1$).

> [!question]- Modelar el coloreo de un mapa como CSP.
> Variables: los países. Dominio: los colores disponibles. Restricciones: dos países vecinos no pueden tener el mismo color (y se pueden agregar otras, como que rojo y verde no queden juntos para no confundir a personas daltónicas).
