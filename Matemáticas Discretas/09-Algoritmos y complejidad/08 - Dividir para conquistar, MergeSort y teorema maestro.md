---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[06 - Ecuaciones de recurrencia y búsqueda binaria]]"
  - "[[07 - Funciones armónicas y notación asintótica condicional]]"
---

# Dividir para conquistar, MergeSort y teorema maestro

Muchos algoritmos usados en la práctica parten la entrada en partes más chicas, las resuelven recursivamente y combinan los resultados. El costo se describe con una recurrencia de forma estándar, y el **teorema maestro** entrega su orden sin resolverla a mano.

## Dividir para conquistar

La entrada de tamaño $n$ se divide por una constante $b$ (aproximando con piso o techo), se hacen $a_1$ llamadas sobre $\lceil n/b \rceil$ y $a_2$ llamadas sobre $\lfloor n/b \rfloor$, y se agrega un trabajo adicional $f(n)$ antes o después de las llamadas (dividir y combinar). A partir de un umbral $n_0$ se usa el caso recursivo; por debajo, se resuelve directamente.

## Ejemplo: MergeSort

**Mezclar** dos listas ordenadas es lineal: se compara el primer elemento de cada una, se pasa el menor a la lista de salida y se avanza; cuando una se agota, se copia lo que queda de la otra. Con $L_1 = [4, 7, 17, 23]$ y $L_2 = [1, 9, 10, 15]$ resulta $[1, 4, 7, 9, 10, 15, 17, 23]$, y en el peor caso se hacen $n - 1$ comparaciones para $n$ elementos en total.

![Algoritmo MergeSort](adjuntos/Algoritmo%20MergeSort.png)

> [!example]- Transcripción de la imagen
> `MergeSort(A, n)` recibe un arreglo $A[0..n-1]$ y devuelve el arreglo ordenado. Línea 1: si $n \le 1$; línea 2: devuelve $A$; si no, línea 4: $m \leftarrow \lfloor n/2 \rfloor$; línea 5: $A_1 \leftarrow$ `MergeSort(A[0…m−1], m)`; línea 6: $A_2 \leftarrow$ `MergeSort(A[m…n−1], n−m)`; línea 7: devuelve `Combinar(A_1, A_2)`.

Contando comparaciones (una por el chequeo de tamaño, $n - 1$ al mezclar en el peor caso, $1 + n - 1 = n$):

$$T(n) = \begin{cases} 1 & n < 2 \\ T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + n & n \ge 2 \end{cases}$$

Para $n = 2^k$ esto da $T(n) = n \log_2 n + n$ (valores $1, 4, 12, 32$ para $n = 1, 2, 4, 8$, comprobados), pero el teorema maestro responde para todo $n$.

## Teorema maestro

![Enunciado del teorema maestro](adjuntos/Enunciado%20del%20teorema%20maestro.png)

> [!example]- Transcripción de la imagen
> Teorema: si $a_1, a_2, b, c, c_0, d \in \mathbb{R}^+$ y $b > 1$, para la recurrencia $T(n) = c_0$ si $0 \le n < n_0$ y $T(n) = a_1 T(\lceil n/b \rceil) + a_2 T(\lfloor n/b \rfloor) + c\,n^d$ si $n \ge n_0$, se cumple: $T(n) \in \Theta(n^d)$ si $a_1 + a_2 < b^d$; $T(n) \in \Theta(n^d \log n)$ si $a_1 + a_2 = b^d$; $T(n) \in \Theta(n^{\log_b(a_1 + a_2)})$ si $a_1 + a_2 > b^d$. Al pie, la pregunta "¿qué valor debe tomar $n_0$?".

El umbral debe garantizar que las llamadas sean más pequeñas que la original: $\lceil n/b \rceil < n$. Como $\lceil n/b \rceil < n/b + 1$, basta $\tfrac{n}{b} + 1 \le n$, es decir $n \ge \tfrac{b}{b-1}$: el umbral $n_0$ solo depende de $b$.

> [!tip] Cómo se usa
> Se calcula $a = a_1 + a_2$ (cuántas llamadas) y se compara con $b^d$ (cuánto se achica el trabajo $n^d$ por nivel). Si el trabajo de combinar domina ($a < b^d$): $\Theta(n^d)$. Si empatan: $\Theta(n^d \log n)$. Si dominan las hojas ($a > b^d$): $\Theta(n^{\log_b a})$.

| Recurrencia | $a_1 + a_2$ | $b^d$ | Caso | Resultado |
|---|---|---|---|---|
| MergeSort: $T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + n$ | $2$ | $2^1 = 2$ | igual | $\Theta(n \log n)$ |
| BinarySearch: $T(\lfloor n/2 \rfloor) + 4$ ($d = 0$) | $1$ | $2^0 = 1$ | igual | $\Theta(\log n)$ |
| $T(n/2) + n$ | $1$ | $2$ | menor | $\Theta(n)$ |
| $3\,T(n/2) + n$ | $3$ | $2$ | mayor | $\Theta(n^{\log_2 3})$ |

Para MergeSort: $a_1 = a_2 = 1$, $b = 2$, $c = d = 1$, $c_0 = 1$ y $a_1 + a_2 = b^d$, luego $T \in \Theta(n \log n)$. La última fila se comprobó numéricamente: $T(n)/n^{\log_2 3}$ tiende a $3$ (con $T(n) = 3T(\lfloor n/2 \rfloor) + n$).

> [!warning] El teorema exige la forma exacta
> Aplica a recurrencias con trabajo $c \cdot n^d$ y llamadas sobre $n/b$. Una recurrencia como $T(n) = T(n-1) + n$ (que da $\tfrac{n(n+1)}{2}$) no tiene esa forma y se resuelve por expansión.

## Preguntas de repaso

> [!question]- ¿Por qué MergeSort y BinarySearch caen en el mismo caso del teorema?
> En ambos $a_1 + a_2 = b^d$: MergeSort duplica las llamadas pero el trabajo de mezclar es $n$, y BinarySearch tiene una llamada con trabajo constante ($d = 0$, $b^0 = 1$).

> [!question]- ¿Qué significa que $a_1 + a_2 > b^d$?
> Que el número de subproblemas crece más rápido de lo que el trabajo por subproblema decrece, de modo que el costo lo dominan los niveles más profundos: $\Theta(n^{\log_b (a_1 + a_2)})$.

> [!question]- ¿Por qué el umbral $n_0$ depende solo de $b$?
> Porque la condición que asegura progreso, $\lceil n/b \rceil < n$, se cumple para todo $n \ge b/(b-1)$ sin importar las constantes de la recurrencia.

> [!question]- ¿Cómo se verifica que MergeSort es correcto?
> Por inducción fuerte sobre $n$: el caso $n \le 1$ devuelve el arreglo; para $n > 1$ las llamadas sobre mitades son correctas por HI y `Combinar` de dos listas ordenadas entrega una lista ordenada.
