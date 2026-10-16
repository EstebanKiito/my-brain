---
ramo: "Estructuras de Datos"
tema: "Programación dinámica"
tags:
  - edd
  - programacion-dinamica
  - memoizacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Subproblemas solapados y subestructura óptima]]"
---

# Memoización y versión iterativa

Una vez que se tiene la [[01 - Subproblemas solapados y subestructura óptima|recurrencia]], hay que implementarla sin repetir cálculos. Una traducción directa a código recursivo es correcta, pero **exponencial**, porque recalcula los mismos subproblemas una y otra vez. Hay dos plantillas para evitarlo: la **recursiva con memoización** y la **iterativa**. Ambas son lineales en el ejemplo de las charlas.

## La recursión ingenua es exponencial

![Algoritmo recursivo Opt](adjuntos/Algoritmo%20recursivo%20Opt.png)

> [!example]- Transcripción de la imagen
> "La ecuación (★) permite plantear el siguiente algoritmo recursivo". input: natural $0 \le j \le n$; output: ganancia óptima. `Opt(j)`: `if j = 0: return 0`; `else: return max{v_j + Opt(b(j)), Opt(j − 1)}`. Opt requiere tener las charlas ordenadas por hora de término, conocer $b(j)$ y suponer que `Opt(0) = 0`.

Al calcular `Opt(6)` se llama a `Opt(3)` y a `Opt(5)`; `Opt(5)` vuelve a llamar a `Opt(3)`, y cada uno de ellos a `Opt(1)` y `Opt(2)`… Los mismos valores se recalculan muchas veces y, en el peor caso, el costo es $O(2^n)$. En la instancia de 6 charlas, la recursión ingenua hace 31 llamadas.

## Memoización: recordar cada $opt(j)$

![Algoritmo RecOpt con memoización](adjuntos/Algoritmo%20RecOpt%20con%20memoizaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Agregaremos un arreglo global $M$ donde almacenaremos cada `Opt(j)` la primera vez que lo calculamos". `RecOpt(j)`: `if j = 0: return 0`; `else: if M[j] ≠ ∅: return M[j]`; `else: M[j] ← max{v_j + RecOpt(b(j)), RecOpt(j − 1)}; return M[j]`.

![Árbol de llamadas de RecOpt](adjuntos/%C3%81rbol%20de%20llamadas%20de%20RecOpt.png)

> [!example]- Transcripción de la imagen
> Árbol de llamadas de `Opt(6)` con las charlas y sus $b(i)$. `Opt(6)` = 8 llama a `Opt(3)` (+1) = 6 y a `Opt(5)` (+0) = 8; `Opt(3)` llama a `Opt(1)` (+4) = 2 y a `Opt(2)` (+0) = 4; `Opt(5)` llama a `Opt(3)` (+2) = 6 y a `Opt(4)` (+0) = 7; `Opt(4)` llama a `Opt(0)` (+7) = 0 y a `Opt(3)` = 6. En azul, el valor de cada llamada; las ramas repetidas ya están en $M$.

Cada `M[j]` se calcula **una sola vez**, y después se lee en $O(1)$. Como hay $n$ subproblemas y cada uno hace trabajo constante, **RecOpt toma tiempo $O(n)$**, suponiendo las charlas ya ordenadas y los $b(j)$ calculados.

## Reconstruir la solución

![Matriz M y reconstrucción de la asignación](adjuntos/Matriz%20M%20y%20reconstrucci%C3%B3n%20de%20la%20asignaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Utilizando RecOpt, obtenemos la matriz de ganancias" $M = [0, 2, 4, 6, 7, 8, 8]$ (índices 0 a 6). "Podemos **deducir la asignación** a partir de $M$, suponiendo que cada $v_j > 0$": como $M[6] = M[6-1]$, no se incluye la charla 6; como $M[5] = v_5 + M[b(5)]$, se incluye la 5; como $M[3] = v_3 + M[b(3)]$, se incluye la 3; como $M[1] = v_1 + M[b(1)]$, se incluye la 1. "Con esto, las charlas asignadas son $\{1, 3, 5\}$".

$M$ guarda los **valores** óptimos. Para saber **qué** charlas elegir, se recorre $M$ desde el final: si $M[j] = M[j-1]$, la charla $j$ no se usó y se pasa a $j - 1$; si no, se usó y se salta a $b(j)$.

## Versión iterativa

![Algoritmo iterativo ItOpt](adjuntos/Algoritmo%20iterativo%20ItOpt.png)

> [!example]- Transcripción de la imagen
> "También podemos plantear una solución **iterativa** para este problema, computando los subproblemas en orden de tamaño". `ItOpt`: `M[0] ← 0`; `for j = 1...n: M[j] ← max{v_j + M[b(j)], M[j−1]}`. Al terminar, ItOpt deja en $M$ las ganancias óptimas. "El algoritmo ItOpt también toma tiempo $\mathcal{O}(n)$".

```python
v = [0, 2, 4, 4, 7, 2, 1]                  # v[1..6]
b = [0, 0, 0, 1, 0, 3, 3]                  # b[1..6]

def it_opt(n):
    M = [0] * (n + 1)
    for j in range(1, n + 1):              # subproblemas de menor a mayor
        M[j] = max(v[j] + M[b[j]], M[j - 1])
    return M

def reconstruir(M, j):
    sol = []
    while j > 0:
        if v[j] + M[b[j]] >= M[j - 1]: sol.append(j); j = b[j]
        else: j -= 1
    return sorted(sol)

M = it_opt(6); print(M, reconstruir(M, 6))   # [0, 2, 4, 6, 7, 8, 8] [1, 3, 5]
```

> [!tip] ¿Recursiva o iterativa?
> La **recursiva con memoización** sigue la recurrencia al pie de la letra: es más fácil de entender y de demostrar correcta. La **iterativa** calcula los subproblemas en orden de tamaño, sin recursión (que tiene su costo), y suele ser más eficiente, aunque con ciclos anidados es más difícil de leer.

## Preguntas de repaso

> [!question]- ¿Por qué la versión recursiva directa de $opt$ es exponencial?
> Porque cada llamada abre dos llamadas, y los mismos subproblemas aparecen en muchas ramas del árbol de recursión. Sin recordarlos, se recalculan una y otra vez.

> [!question]- ¿Qué cambia la memoización y cuál es el nuevo costo?
> Guarda cada $opt(j)$ en un arreglo la primera vez que se calcula y lo reutiliza después. Hay $n$ subproblemas de costo $O(1)$ cada uno, así que el total es $O(n)$.

> [!question]- ¿Cómo se obtiene qué charlas elegir a partir del arreglo $M$?
> Recorriendo desde $j = n$: si $M[j] = M[j-1]$, la charla $j$ no está y se pasa a $j-1$; si no, está, y se salta a $b(j)$.

> [!question]- ¿En qué orden calcula la versión iterativa los subproblemas y por qué?
> De $j = 1$ a $n$, de menor a mayor tamaño, porque $M[j]$ depende de $M[j-1]$ y de $M[b(j)]$, que son índices menores y ya están calculados.
