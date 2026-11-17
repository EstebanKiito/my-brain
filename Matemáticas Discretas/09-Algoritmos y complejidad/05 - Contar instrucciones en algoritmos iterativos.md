---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[04 - Polinomios, logaritmos y órdenes de crecimiento habituales]]"
---

# Contar instrucciones en algoritmos iterativos

Para estimar el tiempo de un algoritmo se define una función $T(n)$ que cuenta las instrucciones ejecutadas según el tamaño $n$ de la entrada, y de ella se busca una notación asintótica (idealmente $\Theta$). No interesa el valor exacto de $T(n)$ sino su orden.

## Método

1. Elegir la **instrucción representativa**: la que refleja el trabajo del problema (en búsqueda y ordenación, las comparaciones; en ciclos anidados, el cuerpo del ciclo interno).
2. Elegir el **parámetro** $n$ respecto del cual se mide (largo del arreglo, valor de un número...).
3. Contar cuántas veces se ejecuta la instrucción en función de $n$ y acotar.

## Ciclos anidados

```
x ← 0
for i = 1 to n:
    for j = 1 to i:
        x ← x + 1
```

La instrucción `x ← x + 1` se ejecuta $i$ veces en la vuelta $i$, luego en total $\sum_{i=1}^{n} i = \tfrac{n(n+1)}{2}$. Como $\tfrac{n^2}{2} \le \tfrac{n(n+1)}{2} \le n^2$, el costo es $\Theta(n^2)$.

Segundo caso, con un ciclo que reduce el tamaño a la mitad:

```
x ← 0;  j ← n
while j ≥ 1:
    for i = 1 to j:  x ← x + 1
    j ← ⌊j/2⌋
```

El cuerpo se ejecuta $n + \lfloor n/2 \rfloor + \lfloor n/4 \rfloor + \dots + 1$ veces. Esa suma es al menos $n$ (primer término) y menor que $n(1 + \tfrac12 + \tfrac14 + \dots) = 2n$, por lo tanto el costo es $\Theta(n)$ y **no** $\Theta(n \log n)$, aunque haya $\log n$ vueltas del `while`. Con $n = 8$ son $8 + 4 + 2 + 1 = 15$ ejecuciones.

> [!warning] Tantas vueltas por tantas operaciones no siempre da el producto
> Multiplicar "número de vueltas del `while`" por "máximo del `for`" sobreestima: aquí el `for` se achica en cada vuelta y la serie es geométrica.

## Mejor y peor caso

El tiempo puede depender del **contenido** de la entrada, no solo de su tamaño. Se distinguen el **peor caso** (la entrada que más tarda para ese $n$) y el **mejor caso** (la que menos tarda).

![Búsqueda lineal en un arreglo](adjuntos/Búsqueda%20lineal%20en%20un%20arreglo.png)

> [!example]- Transcripción de la imagen
> `Búsqueda(A, n, k)` recibe un arreglo $A = [a_0,\dots,a_{n-1}]$, su largo $n > 0$ y un entero $k$; devuelve el índice de $k$ o $-1$. Línea 1: `for i = 0 to n−1`; línea 2: `if a_i = k`; línea 3: `return i`; línea 4: `return −1`.

Se cuentan las comparaciones de la línea 2 (las líneas 3 y 4 se ejecutan a lo más una vez y no representan el trabajo):

- **Mejor caso:** $a_0 = k$. Una comparación: $T(n) \in \Theta(1)$.
- **Peor caso:** $k \notin A$. Se compara con los $n$ elementos: $T(n) \in \Theta(n)$.

Se dice entonces que la búsqueda es lineal en el peor caso y constante en el mejor.

## Ordenamiento por inserción

![Algoritmo InsertionSort](adjuntos/Algoritmo%20InsertionSort.png)

> [!example]- Transcripción de la imagen
> `InsertionSort(A, n)` ordena el arreglo $A$. Línea 1: `for i = 1 to n−1`; línea 2: `j ← i`; línea 3: `while a_{j−1} > a_j ∧ j > 0`; líneas 4 a 6: se intercambian $a_{j-1}$ y $a_j$ con una variable auxiliar `t`; línea 7: `j ← j − 1`.

Para cada $i$, el elemento $a_i$ retrocede mientras sea menor que su antecesor. Se cuentan las comparaciones del `while`:

- **Mejor caso** (arreglo ya ordenado): cada $i$ hace una sola comparación que falla, total $n - 1$: $\Theta(n)$.
- **Peor caso** (orden inverso): $a_i$ retrocede hasta el inicio, con $i$ comparaciones exitosas; total $1 + 2 + \dots + (n-1) = \tfrac{n(n-1)}{2}$: $\Theta(n^2)$.

Con $[4,3,2,1]$ se hacen $6 = \tfrac{4 \cdot 3}{2}$ comparaciones y $6$ intercambios; con $[1,2,3,4]$, solo $3$.

> [!tip] Qué se reporta
> Lo habitual es el **peor caso**, porque es una garantía: dice cuán mal puede portarse el algoritmo. Si encontrar una cota $\Theta$ exacta es difícil, basta una buena cota $O$ para el peor caso, que sigue acotando superiormente el tiempo.

## Preguntas de repaso

> [!question]- ¿Por qué en `Búsqueda` no se cuentan las líneas 3 y 4?
> Porque se ejecutan a lo más una vez por llamada; el crecimiento del tiempo con $n$ lo determina el número de comparaciones de la línea 2.

> [!question]- ¿Por qué el segundo ejemplo de ciclos es $\Theta(n)$ y no $\Theta(n \log n)$?
> Porque el `for` interno recorre $j$ elementos y $j$ se divide a la mitad cada vez; la suma $n + n/2 + n/4 + \dots$ es una serie geométrica menor que $2n$.

> [!question]- ¿Qué entrada produce el peor caso de InsertionSort y por qué?
> El arreglo ordenado al revés: cada elemento debe retroceder hasta la posición $0$, lo que da $\tfrac{n(n-1)}{2}$ comparaciones.

> [!question]- ¿Por qué se prefiere el peor caso al mejor caso?
> Porque el mejor caso puede ocurrir muy rara vez; el peor caso da una cota que vale para toda entrada de tamaño $n$.
