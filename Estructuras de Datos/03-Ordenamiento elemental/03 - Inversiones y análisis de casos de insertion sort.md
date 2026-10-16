---
ramo: "Estructuras de Datos"
tema: "Ordenamiento elemental"
tags:
  - edd
  - ordenamiento
  - insertion-sort
  - inversiones
  - complejidad
  - origen/complemento
prerrequisitos:
  - "[[02 - Insertion sort]]"
---

# Inversiones y análisis de casos de insertion sort

El costo de insertion sort depende de **qué tan desordenados** vienen los datos. Para medir ese desorden con precisión se usa el número de **inversiones**. Con él se calculan exactamente el mejor, el peor y el caso promedio.

> [!tip] Definición
> Un par de índices $(i, j)$ con $i < j$ es una **inversión** si $A[i] > A[j]$: dos elementos que están en el orden equivocado.

## Cada vuelta del `while` corrige una inversión

En la versión in place, el `while` intercambia `A[j]` con `A[j-1]` solo cuando están invertidos, y cada intercambio de vecinos elimina **exactamente una** inversión. Por lo tanto, la cantidad total de vueltas del `while` es el número de inversiones $k$ de la entrada:

$$T(n) = O(n + k)$$

El término $n$ corresponde a la pasada del `for` y el término $k$, a los intercambios.

| Caso | Entrada | Inversiones $k$ | Tiempo |
|---|---|---|---|
| Mejor | Ya ordenada | $0$ | $O(n)$ |
| Peor | Ordenada al revés | $\binom{n}{2} = \frac{n(n-1)}{2}$ | $O(n^2)$ |
| Promedio | Permutación al azar | $\frac{n(n-1)}{4}$ | $O(n^2)$ |

![Peor caso de insertion sort por inversiones](adjuntos/Peor%20caso%20de%20insertion%20sort%20por%20inversiones.png)

> [!example]- Transcripción de la imagen
> "En el peor caso, el arreglo tiene el número máximo de inversiones". El arreglo está ordenado decrecientemente. Al comparar cada índice $i$ con $j > i$ se cuenta una inversión: $k = (n-1) + (n-2) + \dots + 1 = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$. De forma equivalente, $k$ es el número de pares de índices: $\binom{n}{2} = \frac{n!}{2!(n-2)!} = \frac{n(n-1)}{2}$. "La complejidad en el peor caso es $\mathcal{O}(n^2)$". Abajo, el recuadro "¿Qué hay del caso promedio?".

**Caso promedio.** Se calcula como el total de inversiones de todas las permutaciones posibles, dividido por el número de permutaciones. Cada par $(i, j)$ está invertido en exactamente la mitad de las permutaciones, así que el promedio es la mitad de los $\binom{n}{2}$ pares: $\frac{n(n-1)}{4}$. Sigue siendo cuadrático.

```python
from itertools import permutations

def inversiones(A):
    return sum(1 for i in range(len(A)) for j in range(i + 1, len(A)) if A[i] > A[j])

print(inversiones([3, 2, 8, 1, 5]))       # 5: (3,2) (3,1) (2,1) (8,1) (8,5)
n = 6
perms = list(permutations(range(n)))
print(sum(inversiones(p) for p in perms) / len(perms), n * (n - 1) / 4)   # 7.5 7.5
```

> [!tip] Cuándo conviene insertion sort
> Si los datos **ya fueron ordenados antes** y se desordenan poco (por ejemplo, una app que muestra una lista ordenada y de vez en cuando recibe un dato nuevo), hay pocas inversiones e insertion sort trabaja casi en $O(n)$. En ese escenario puede ganarles a los algoritmos $O(n \log n)$, sin recursión ni memoria extra.

## Ejercicio: ordenar sublistas

> [!example] Pregunta de interrogación
> Mostrar que con insertion sort se pueden ordenar $n/k$ sublistas de largo $k$ cada una en tiempo $O(nk)$ en el peor caso.

Ordenar una sublista de largo $k$ cuesta $O(k^2)$. Como son $n/k$ sublistas, el total es $O\!\left(k^2 \cdot \frac{n}{k}\right) = O(nk)$.

![Ejercicio de insertion sort sobre sublistas](adjuntos/Ejercicio%20de%20insertion%20sort%20sobre%20sublistas.png)

> [!example]- Transcripción de la imagen
> "Pregunta 1 - I1–2021-1". Sabemos que insertion sort toma tiempo $O(n^2)$ en arreglos de largo $n$; luego, en un arreglo de largo $k$ toma tiempo $O(k^2)$. Como hay $n/k$ sublistas, correr todos los insertion sort toma $O(k^2 \cdot (n/k)) = O(nk)$.

![Pizarra con n/k sublistas de largo k](adjuntos/Pizarra%20-%20n%20sobre%20k%20sublistas%20de%20largo%20k.jpeg)

> [!example]- Transcripción de la imagen
> Pizarra: tres sublistas de largo $k$ (marcado con una llave arriba), apiladas con puntos suspensivos entre ellas y una llave a la derecha que indica que son $n/k$. Cada una tiene a su izquierda la anotación $O(k^2)$.

![Pizarra con insertion sort por bloques en O(nk)](adjuntos/Pizarra%20-%20insertion%20sort%20por%20bloques%20en%20tiempo%20nk.jpeg)

> [!example]- Transcripción de la imagen
> Pizarra: "Insertion Sort (A(n)) = O(n²)" y una flecha a $O(k^2 \cdot \frac{n}{k})$, que da $O(k \cdot n)$. Debajo, un arreglo dividido en bloques consecutivos marcados con $k$.

## Preguntas de repaso

> [!question]- ¿Por qué el número de intercambios de insertion sort es exactamente el número de inversiones?
> Porque solo intercambia vecinos que están en el orden equivocado, y cada intercambio de ese tipo elimina exactamente una inversión sin crear otra. El algoritmo termina cuando no queda ninguna.

> [!question]- ¿Cuántas inversiones tiene un arreglo de $n$ elementos ordenado al revés?
> Todos los pares están invertidos: $\binom{n}{2} = \frac{n(n-1)}{2}$.

> [!question]- Si un arreglo tiene $O(n)$ inversiones, ¿cuánto demora insertion sort?
> $O(n + k) = O(n + n) = O(n)$: lineal.

> [!question]- ¿Por qué ordenar $n/k$ sublistas de largo $k$ cuesta $O(nk)$ y no $O(n^2)$?
> Porque el costo cuadrático aplica al largo de cada sublista, no a $n$. Son $n/k$ ordenamientos de $O(k^2)$ cada uno: $O(k^2 \cdot n/k) = O(nk)$, que es mucho menor que $n^2$ cuando $k \ll n$.
