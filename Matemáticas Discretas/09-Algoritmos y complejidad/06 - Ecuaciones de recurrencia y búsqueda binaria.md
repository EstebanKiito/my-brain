---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[05 - Contar instrucciones en algoritmos iterativos]]"
  - "[[03 - Inducción fuerte]]"
---

# Ecuaciones de recurrencia y búsqueda binaria

En un algoritmo recursivo el tiempo se escribe en términos del tiempo de las llamadas recursivas, y eso produce una **ecuación de recurrencia**. Resolverla (hallar una fórmula que no use $T$) y acotarla asintóticamente es el análogo recursivo de contar iteraciones.

## Plantear la recurrencia: búsqueda binaria

![Algoritmo BinarySearch](adjuntos/Algoritmo%20BinarySearch.png)

> [!example]- Transcripción de la imagen
> `BinarySearch(A, x, i, f)` recibe un arreglo ordenado $A[0..n-1]$, un elemento $x$ y los índices $i, f$; devuelve un índice en $\{0,\dots,n-1\}$ o $-1$. Si $i > f$ devuelve $-1$; si $i = f$, devuelve $i$ cuando $A[i]$ es el buscado y $-1$ si no (la lámina escribe `a` por `x`); en otro caso calcula $m = \lfloor (i+f)/2 \rfloor$ y: si $A[m] < x$ llama con $(m+1, f)$; si $A[m] > x$ llama con $(i, m-1)$; si no, devuelve $m$.

Se cuentan las comparaciones, y el peor caso es que el elemento no esté (o aparezca solo al final). Para $n = 1$ se ejecutan las comparaciones de las líneas 1, 3 y 4: $3$. Para $n > 1$ se hacen las de las líneas 1, 3, 10 y 12 (cuatro) y se entra a una sola llamada recursiva sobre a lo más $\lfloor n/2 \rfloor$ elementos:

$$T(n) = \begin{cases} 3 & n = 1 \\ T(\lfloor n/2 \rfloor) + 4 & n > 1 \end{cases}$$

## Resolver por sustitución

Con $n = 2^k$ la recurrencia queda $T(2^k) = T(2^{k-1}) + 4$, y expandiendo:

$$T(2^k) = T(2^{k-1}) + 4 = T(2^{k-2}) + 8 = \dots = T(2^{k-i}) + 4i.$$

Con $i = k$: $T(2^k) = T(1) + 4k = 4k + 3$, o sea, como $k = \log_2 n$,

$$T(n) = 4 \log_2 n + 3 \quad (n \text{ potencia de } 2).$$

Comprobado por cálculo: $T(1), T(2), T(4), T(8) = 3, 7, 11, 15$, que coinciden con $4k + 3$ para $k = 0, 1, 2, 3$.

## Notación condicional

La fórmula solo vale para potencias de 2. Se formaliza con $P \subseteq \mathbb{N}$:

$$O(f \mid P) = \{\, g \mid \exists c\ \exists n_0\ \forall n \ge n_0:\ (n \in P \to g(n) \le c \cdot f(n)) \,\}$$

(y análogamente $\Omega(f \mid P)$ y $\Theta(f \mid P)$). Con $\text{POTENCIA}_2 = \{2^i \mid i \in \mathbb{N}\}$ se concluye $T \in \Theta(\log_2 n \mid \text{POTENCIA}_2)$. El objetivo es pasar a $T \in O(\log n)$ sin restricción.

## Generalizar con inducción

Se quiere $\exists c\ \exists n_0\ \forall n \ge n_0:\ T(n) \le c \log_2 n$. Se estiman las constantes con los primeros valores: $T(1) = 3 > 7 \log_2 1 = 0$, pero $T(2) = T(3) = 7 \le 7\log_2 n$. Se prueba entonces, por **inducción fuerte**, que $T(n) \le 7 \log_2 n$ para $n \ge 2$.

- **Casos base:** $n = 2$ ($7 = 7 \log_2 2$) y $n = 3$ ($7 < 7 \log_2 3$); $n = 3$ es base porque depende de $T(1)$, que está fuera del rango probado.
- **Paso** ($n \ge 4$, $\lfloor n/2 \rfloor \ge 2$): por HI y por monotonía del logaritmo,
$$T(n) = T(\lfloor n/2 \rfloor) + 4 \le 7 \log_2 \lfloor n/2 \rfloor + 4 \le 7(\log_2 n - 1) + 4 = 7 \log_2 n - 3 < 7 \log_2 n.$$

Se concluye $T \in O(\log n)$. Esta demostración sirve, pero exige adivinar $c$ y $n_0$; la nota siguiente da un atajo.

> [!warning] Los casos base de la inducción fuerte dependen de la recurrencia
> Si el paso usa $T(\lfloor n/2 \rfloor)$ y el resultado solo vale desde $n \ge 2$, hay que verificar a mano todos los $n$ cuya mitad cae fuera del rango (aquí $n = 2$ y $n = 3$).

## Preguntas de repaso

> [!question]- ¿Por qué la recurrencia de BinarySearch tiene una sola llamada recursiva?
> Porque cada paso descarta la mitad del arreglo: según la comparación con $A[m]$ se continúa solo con una de las dos mitades.

> [!question]- ¿Por qué la solución $4\log_2 n + 3$ no basta para concluir sobre todo $n$?
> Porque se dedujo con $n = 2^k$; para $n$ arbitrario ($n = 3, 5, \dots$) el piso cambia la recurrencia y hay que justificar la extensión.

> [!question]- ¿Cómo se eligen $c$ y $n_0$ en la inducción?
> Tabulando los primeros valores de $T$ y comparándolos con la cota propuesta: aquí $n_0 = 2$ y $c = 7$ funcionan, porque $T(2) = 7$.

> [!question]- ¿Cuántas comparaciones hace la búsqueda binaria en un arreglo de $1024$ elementos, según el modelo?
> $T(1024) = 4 \cdot 10 + 3 = 43$, frente a las $1024$ de la búsqueda lineal en el peor caso.
