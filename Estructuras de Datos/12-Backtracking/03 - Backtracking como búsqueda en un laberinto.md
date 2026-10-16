---
ramo: "Estructuras de Datos"
tema: "Backtracking"
tags:
  - edd
  - backtracking
  - grafos-implicitos
  - laberinto
  - origen/complemento
prerrequisitos:
  - "[[02 - Algoritmo de backtracking]]"
---

# Backtracking como búsqueda en un laberinto

Cada asignación parcial de un CSP abre caminos hacia nuevas asignaciones. Al conjunto de todas esas alternativas se le llama **grafo implícito**: no está guardado en memoria, sino que se genera a medida que se explora. Backtracking es, entonces, una forma de recorrer ese grafo, y el caso canónico es **salir de un laberinto**.

![Laberinto como grafo implícito](adjuntos/Laberinto%20como%20grafo%20impl%C3%ADcito.png)

> [!example]- Transcripción de la imagen
> Un laberinto cuadrado de muros negros con un símbolo Θ (la posición inicial) en el centro.

![Dibujo del laberinto como grafo de celdas](adjuntos/Dibujo%20del%20laberinto%20como%20grafo%20de%20celdas.jpeg)

> [!example]- Transcripción de la imagen
> Dibujo a mano: círculos (celdas) unidos por líneas cuando se puede pasar de una a otra. El laberinto visto como un grafo.

## Modelo

- **Variable:** la celda en la que se está, es decir, si forma parte de un camino válido.
- **Dominio:** las direcciones en que se puede avanzar: norte, sur, este y oeste.
- **Restricciones:** no atravesar un muro y no volver a una celda **ya visitada**, porque si se pasó por ahí sin éxito, ese camino no lleva a la salida.
- **Éxito:** la celda actual es la salida.

![Recorrido del laberinto con retrocesos](adjuntos/Recorrido%20del%20laberinto%20con%20retrocesos.png)

> [!example]- Transcripción de la imagen
> El laberinto con un recorrido marcado: flechas de colores indican las direcciones probadas desde cada celda, y varias X rojas marcan celdas desde las que no se pudo avanzar (sin salida), donde el algoritmo retrocede a la celda anterior.

Cuando en una celda se agotan las cuatro direcciones sin llegar a la salida, esa celda **no es parte de la solución**: se vuelve a la anterior, que prueba su siguiente dirección. Así hasta encontrar la salida o volver al inicio sin opciones, lo que significa que no hay solución.

![isSolvable para el laberinto](adjuntos/isSolvable%20para%20el%20laberinto.png)

> [!example]- Transcripción de la imagen
> "Le agregamos etiquetas a las posiciones, de modo que sabemos cuáles hemos visitado (*visited*). Todas comienzan como *nonvisited* y la salida se marca como *exit*". `isSolvable(X, x, D, R)`: 1. `if x = exit: return true`; 2. `if x = visited: return false`; 3. `x ← visited`; 4. `for v ∈ {N, E, S, W}:`; 5. `if x + v ≠ wall:`; 6. `x ← x + v`; 7. `if isSolvable(X, x, D, R):`; 8. `return true`; 9. `x ← nonvisited`; 10. `return false`.

```python
L = ["#########",
     "#S..#...#",
     "#.#.#.#.#",
     "#.#...#.#",
     "#.#####.#",
     "#...#..E#",
     "#########"]
M = [list(f) for f in L]

def laberinto(x):
    f, c = x
    if M[f][c] == "E": return True              # salida
    if M[f][c] in "v#": return False            # visitada o muro
    M[f][c] = "v"                               # marcar visitada
    for df, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:   # N, S, E, O
        if laberinto((f + df, c + dc)): return True
    M[f][c] = "."                               # no lleva a la salida: desmarcar
    return False

print(laberinto((1, 1)))                        # True
```

> [!warning] Backtracking no es DFS (aunque se parecen)
> Recorrer un laberinto con backtracking se parece mucho a una búsqueda en profundidad. Pero backtracking es una estrategia general para **CSP**, que puede usarse sobre grafos implícitos. Para grafos explícitos existen algoritmos específicos y más eficientes.

## Variantes típicas

- **Encontrar una solución** (la plantilla tal cual).
- **Encontrar todas las soluciones:** no detenerse en la primera.
- **Encontrar la mejor** (por ejemplo, el camino más corto): hay que comparar todas las soluciones, lo que es caro. Para optimizar suelen convenir otras estrategias.

Otros problemas clásicos que se resuelven así son el recorrido del caballo de ajedrez, la mochila (capacidad frente a ítems), la carga de una barcaza o un camión, el estibado de carga (que ambos lados pesen lo mismo) y el coloreo de mapas.

## Preguntas de repaso

> [!question]- ¿Qué es un grafo implícito?
> El grafo de todas las asignaciones parciales posibles de un problema, en el que cada asignación abre caminos a otras. No se guarda en memoria: se genera a medida que backtracking lo explora.

> [!question]- ¿Para qué se marcan las celdas visitadas en el laberinto?
> Para no volver a explorar una celda desde la que ya se buscó sin éxito y para no caer en ciclos infinitos.

> [!question]- ¿Cómo se modifica el algoritmo del laberinto para encontrar el camino más corto?
> No se detiene en la primera salida: explora todos los caminos, guarda la longitud de cada uno al llegar a la salida y se queda con el menor. Es correcto, pero caro.

> [!question]- Modelar el estibado de carga (que dos lados de un camión pesen lo mismo) para backtracking.
> Variables: cada bulto. Dominio: {izquierda, derecha}. Restricción: al final, la suma de pesos de ambos lados es igual (y se puede podar cuando un lado supera la mitad del total). Retorna verdadero si existe una asignación balanceada.
