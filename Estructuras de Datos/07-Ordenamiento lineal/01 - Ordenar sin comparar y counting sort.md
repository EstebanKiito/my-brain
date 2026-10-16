---
ramo: "Estructuras de Datos"
tema: "Ordenamiento lineal"
tags:
  - edd
  - ordenamiento
  - counting-sort
  - orden-lineal
  - origen/complemento
prerrequisitos:
  - "[[05 - Complejidad y mejoras de quicksort]]"
  - "[[04 - Propiedades de los algoritmos de ordenación]]"
---

# Ordenar sin comparar y counting sort

Todos los algoritmos vistos hasta ahora ordenan **comparando** pares de elementos, y ninguno baja de $O(n \log n)$. No es casualidad: cualquier algoritmo que solo compara necesita $\Omega(n \log n)$ comparaciones en el peor caso. Debe distinguir entre las $n!$ permutaciones posibles, cada comparación divide las opciones a lo más en dos y $\log_2 n! \in \Theta(n \log n)$. Para ordenar en **$O(n)$** hay que dejar de comparar, y eso solo se puede si se **sabe algo de los datos**.

> [!tip] La condición
> Si los datos solo pueden tomar **pocos valores distintos** (por ejemplo, enteros entre $0$ y $k$, o los colores de una bolsa de M&M), se pueden **categorizar** en vez de comparar: contar cuántos hay de cada categoría y ubicarlos directamente. Ya no se corrigen inversiones de a una.

## Counting sort

Se cuenta cuántas veces aparece cada valor. Después, con sumas acumuladas, se sabe en qué posición termina cada categoría, y cada elemento se coloca en su lugar.

![Pseudocódigo de counting sort](adjuntos/Pseudoc%C3%B3digo%20de%20counting%20sort.png)

> [!example]- Transcripción de la imagen
> input: arreglo $A[0 \dots n-1]$, natural $k$; output: arreglo $B[0 \dots n-1]$. `CountingSort(A, k)`: 1. $B$ ← arreglo vacío de $n$ celdas; 2. $C[0 \dots k]$ ← arreglo vacío de $k+1$ celdas; 3–4. `for i = 0...k: C[i] ← 0`; 5–6. `for j = 0...n-1: C[A[j]] ← C[A[j]] + 1`; 7–8. `for p = 1...k: C[p] ← C[p] + C[p-1]`; 9–11. `for r = n-1...0: B[C[A[r]] - 1] ← A[r]; C[A[r]] ← C[A[r]] - 1`; 12. `return B`.

Hay tres arreglos: **$A$** (la entrada desordenada, con $k+1$ tipos de valor), **$C$** (las cuentas) y **$B$** (la salida).

```python
def counting_sort(A, k, clave=lambda x: x):
    C = [0] * (k + 1)
    for x in A:
        C[clave(x)] += 1                 # cuenta cada categoría
    for p in range(1, k + 1):
        C[p] += C[p - 1]                 # C[p] = cuántos tienen clave <= p
    B = [None] * len(A)
    for x in reversed(A):                # de atrás hacia adelante: estable
        C[clave(x)] -= 1
        B[C[clave(x)]] = x
    return B

print(counting_sort([3, 0, 2, 3, 1, 0], 3))   # [0, 0, 1, 2, 3, 3]
```

![Animación de counting sort](adjuntos/Animaci%C3%B3n%20de%20counting%20sort.gif)

> [!example]- Transcripción de la imagen
> Tres filas de casillas indexadas: arriba, el arreglo de entrada que se recorre (un círculo marca el elemento actual); al medio, el arreglo de cuentas, de 0 a 30, que se va incrementando; abajo, el arreglo de salida, que se llena colocando cada elemento en la posición indicada por las cuentas acumuladas.

> [!warning] Recorrer al revés no es un detalle
> El último ciclo va de $n-1$ a $0$ y llena cada categoría **desde el final**. Así, entre dos elementos iguales, el que estaba más atrás queda más atrás: **counting sort es estable**. Esa estabilidad es justamente lo que permite usarlo dentro de radix sort.

## Complejidad

![Complejidad de counting sort](adjuntos/Complejidad%20de%20counting%20sort.png)

> [!example]- Transcripción de la imagen
> La complejidad del algoritmo es $\Theta(n + k)$. Si $k \in \mathcal{O}(n)$, entonces `CountingSort()` es $\Theta(n)$.

Contar es $O(n)$, acumular es $O(k)$ y colocar es $O(n)$: en total, $\Theta(n + k)$. Si el rango $k$ es del orden de $n$ o menor (un millón de datos con a lo más un millón de valores distintos), es **lineal**. Si $k$ es mucho mayor que $n$, el arreglo de cuentas domina y deja de convenir. Además, no es in place: usa $O(n + k)$ de memoria.

## Preguntas de repaso

> [!question]- ¿Por qué ningún algoritmo que solo compara puede ordenar en $o(n \log n)$ en el peor caso?
> Porque debe distinguir entre $n!$ órdenes posibles y cada comparación tiene dos resultados. Hacen falta al menos $\log_2 n!$ comparaciones, que es $\Theta(n \log n)$.

> [!question]- ¿Qué información sobre los datos necesita counting sort?
> Que los valores (o claves) sean enteros en un rango conocido y acotado $0 \dots k$, idealmente con $k \in O(n)$.

> [!question]- ¿Por qué counting sort recorre la entrada al revés en el último ciclo?
> Para que, dentro de cada categoría, los elementos queden en el mismo orden relativo que en la entrada. Eso lo hace estable.

> [!question]- ¿Cuándo deja de ser buena idea usar counting sort?
> Cuando el rango $k$ es mucho mayor que $n$ (por ejemplo, ordenar 100 números entre 0 y $10^9$): el costo $O(n + k)$ y la memoria para las cuentas quedan dominados por $k$.
