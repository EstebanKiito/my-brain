---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Contar instrucciones en algoritmos iterativos]]"
  - "[[08 - Dividir para conquistar, MergeSort y teorema maestro]]"
---

# Ejercicios de prueba de algoritmos y complejidad

Las interrogaciones y exámenes repiten cuatro formatos: **demostrar relaciones entre funciones** con la definición de $O$/$\Theta$, **encontrar el orden de un algoritmo** (ciclos, casos según la entrada), **plantear y resolver una recurrencia** (con o sin teorema maestro) y **diseñar un algoritmo de dividir para conquistar**. La pauta puntúa fijar $c$ y $n_0$, usar la definición y no solo el "olfato" del orden. El algoritmo del cerro, que también apareció en la interrogación 2 de 2020-2, está en [[09 - Ejercicios de ayudantías de algoritmos y complejidad]].

## Ejercicios

### 1. Suma de factoriales (examen, 2015-2)
Sean $f(n) = \sum_{i=0}^{n} i!$ y $g(n) = (n+1)!$. ¿Es $f \in O(g)$?

> [!example]- Solución
> Sí. Para $i \le n$, $i! \le n!$, luego $f(n) \le (n+1)\,n! = (n+1)! = g(n)$, con $c = 1$ y $n_0 = 0$.

### 2. $\log(n!) \in \Theta(n \log n)$ (examen, 2017-2)
> [!example]- Solución
> $O$: $n! \le n^n$, así que $\log n! \le n \log n$. $\Omega$: el producto $(n!)^2 = \prod_{i=1}^{n} i\,(n+1-i)$ y cada factor cumple $i(n+1-i) = n + (i-1)(n-i) \ge n$, luego $(n!)^2 \ge n^n$ y $2 \log n! \ge n \log n$. Las dos cotas (con constantes $1$ y $\tfrac12$) dan $\log n! \in \Theta(n \log n)$. (Verificado numéricamente hasta $n = 500$.)

### 3. Tiempo en $\Theta$ y logaritmo de un polinomio (interrogación 3, 2018-1)
(a) Encuentre $f$ tal que `theavengersaredead(n)` sea $\Theta(f)$, con `k ← 1`; `for i = 1 to n: k ← k·n`; `i ← 1`; `while i ≤ k: i ← 2i`; `return i`. (b) Demuestre que $\log(a_k n^k + \dots + a_0) \in O(\log n)$ con $a_i \ge 0$ no todos nulos.

> [!example]- Solución
> **(a)** El `for` hace $n$ pasos y deja $k = n^n$. En el `while`, tras $l$ vueltas $i = 2^l$, y se continúa mientras $2^l \le n^n$, es decir $l \le n \log_2 n$: hay $\lfloor n \log_2 n \rfloor + 1$ vueltas. El tiempo es $T(n) = n + \lfloor n \log_2 n \rfloor + 1 + O(1)$ y, para $n \ge 2$, $n \log_2 n \le T(n) \le 3\, n \log_2 n$ (salvo constantes). Entonces $f(n) = n \log n$.
> **(b)** Con $A = \sum a_i$ y $n \ge 1$: $\log(\sum a_i n^i) \le \log(A\, n^k) = \log A + k \log n$. Para $n \ge 2$ (base $2$) $\log n \ge 1$, así que es $\le (k + \max\{0, \log A\}) \log n$.

### 4. Potencia por dividir para conquistar (examen, 2018-2)
Escriba un algoritmo de dividir para conquistar que calcule $x^n$ con multiplicaciones, cuente cuántas hace y dé su complejidad.

> [!example]- Solución
> ```
> Pow(x, n):  if n = 1: return x
>             h ← Pow(x, ⌊n/2⌋);  p ← h·h
>             if n impar: return p·x  else: return p
> ```
> Por ejemplo $\mathrm{Pow}(2, 7)$: $2^3 = 8$ (dos multiplicaciones), luego $8 \cdot 8 \cdot 2 = 128$ (otras dos): $4$ en total. Las multiplicaciones cumplen $T(1) = 0$ y $T(n) = T(\lfloor n/2 \rfloor) + 1$ ($n$ par) o $+2$ ($n$ impar). Hay $\lfloor \log_2 n \rfloor$ niveles con $1$ o $2$ multiplicaciones cada uno: $\lfloor \log_2 n \rfloor \le T(n) \le 2 \lfloor \log_2 n \rfloor$, es decir $T \in \Theta(\log n)$. La paridad que se pregunta es la de $n$, no la de $x$. (Verificado para $n \le 500$.)

### 5. Casos según la paridad (interrogación 3, 2019-1)
Para el algoritmo de la figura, con tamaño $n = \lvert S \rvert$ y operaciones de costo constante: (a) halle $f$ con $T_A \in \Theta(f)$; (b) pruebe que $T_A \notin \Theta(n^k)$ para todo $k$.

![Algoritmo A con casos según la paridad del tamaño](adjuntos/Algoritmo%20A%20con%20casos%20según%20la%20paridad.png)

> [!example]- Transcripción de la imagen
> Entrada $S = \{a_1,\dots,a_n\}$. Si $\lvert S \rvert$ es par, un `for` con $i$ de $1$ a $\lvert S \rvert$ imprime $a_i$. Si no, dos `for` anidados, $i$ y $j$ de $1$ a $\lvert S \rvert$, imprimen $a_i, a_j$.

> [!example]- Solución
> **(a)** $T_A(n) = c_1 n$ si $n$ es par y $c_2 n^2$ si es impar; luego $f(n) = n$ para $n$ par y $f(n) = n^2$ para $n$ impar.
> **(b)** Si $T_A \in \Theta(n^k)$ habría $C_1, C_2$ con $C_1 n^k \le T_A \le C_2 n^k$ desde algún $n_0$. Para $n$ par, $C_1 n^k \le c_1 n$ obliga a $k \le 1$. Para $n$ impar, $c_2 n^2 \le C_2 n^k$ obliga a $k \ge 2$. Contradicción: ninguna potencia captura ambos regímenes.

### 6. Alcanzabilidad por composición (control 3, 2020-1)
El algoritmo de la figura decide si hay camino de $u$ a $v$. Con $n = \lvert V \rvert$, la línea 7 cuesta $\Theta(n^3)$ y las demás $O(1)$. Halle el orden del mejor y del peor caso.

![Algoritmo de alcanzabilidad por composición de relaciones](adjuntos/Algoritmo%20de%20alcanzabilidad%20por%20composición.png)

> [!example]- Transcripción de la imagen
> Entrada: grafo dirigido $G = (V, E)$ y nodos $u, v$; salida $1$ si hay camino entre $u$ y $v$ y $0$ si no. Líneas: `i = 1`; `M = E`; `while i ≤ |V|`; si $(u,v) \in M$ devuelve $1$; si no, `M = M ∘ E` e `i = i + 1`; al final `return 0`.

> [!example]- Solución
> **Mejor caso:** $(u, v) \in E$. En la primera vuelta se devuelve $1$ con trabajo constante: $\Theta(1)$. **Peor caso:** no hay camino. El `while` corre las $n$ vueltas y cada una gasta entre $C_1 n^3$ y $C_2 n^3$ en la línea 7; el total queda entre $C_1 n^4$ y $n(C' + C_2 n^3)$: $\Theta(n^4)$. En la vuelta $i$, $M$ contiene los pares unidos por caminos de largo exactamente $i$, por eso basta llegar a $n$.

### 7. Algoritmo Mayoría (interrogación 2, 2021-2)
`Mayoría(A, n)` devuelve un elemento que se repite más de $\lfloor n/2 \rfloor$ veces, o $-1$: si $n = 1$ devuelve $A[0]$; si no, con $p = \lfloor n/2 \rfloor$ llama a `Mayoría` sobre cada mitad y usa `Contar` (que recorre $A$ completo: $n$ comparaciones) para verificar cada candidato. (a) Plantee $T(n)$, (b) acote sin teorema maestro, (c) use el teorema maestro.

> [!example]- Solución
> **(a)** $T(1) = 1$ y $T(n) = T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + 2n + 3$ (dos `Contar` de $n$ comparaciones más tres comparaciones de control). **(b)** Con $n = 2^k$, expandiendo: $T(n) = 4n + 2n \log_2 n - 3$ (por ejemplo $T(2) = 9$ y $T(4) = 29$, comprobados). Como $T$ y $n \log n$ son no decrecientes y $n \log n$ es 2-armónica, el teorema de extensión da $T \in O(n \log n)$. **(c)** $a_1 + a_2 = 2 = b^d$ con $b = 2$, $d = 1$: segundo caso, $\Theta(n \log n)$. Es peor que un recorrido lineal con contadores, aunque usa memoria constante.

### 8. Suma de funciones $O$ (examen, 2022-1)
Pruebe que si $f_1 \in O(g_1)$ y $f_2 \in O(g_2)$, entonces $f_1 + f_2 \in O(\max\{g_1, g_2\})$.

> [!example]- Solución
> Hay $c_i, n_i$ con $f_i \le c_i g_i$ para $n \ge n_i$. Con $n_0 = \max\{n_1, n_2\}$ y $C = c_1 + c_2$: $f_1 + f_2 \le c_1 \max\{g_1, g_2\} + c_2 \max\{g_1, g_2\} = C \max\{g_1, g_2\}$ para $n \ge n_0$.

### 9. Recurrencia de la suma y TripleMergeSort (interrogación 2, 2022-2)
(a) Resuelva $T(1) = 1$, $T(n) = T(n-1) + n$. (b) TripleMergeSort divide en tres sublistas de tamaños $\approx n/3$ y las combina con $n - 1$ comparaciones en el peor caso. Halle su complejidad.

> [!example]- Solución
> **(a)** Expandiendo, $T(n) = 1 + \sum_{k=2}^{n} k = \tfrac{n(n+1)}{2}$ (inducción: $\tfrac{(n-1)n}{2} + n = \tfrac{n(n+1)}{2}$).
> **(b)** $T(n) = T(p) + T(q - p) + T(n - q) + n - 1$, con los tres tamaños en $\{\lfloor n/3 \rfloor, \lceil n/3 \rceil\}$: $a_1 + a_2 = 3$, $b = 3$, $d = 1$, $b^d = 3$. Caso de igualdad del teorema maestro: $T \in \Theta(n \log n)$. (Los valores $5, 23, 95, 365$ para $n = 3, 9, 27, 81$ crecen como $n \log_3 n$.)

### 10. $\Theta$ es una relación de equivalencia (examen, 2024-2)
Para $f, g : \mathbb{N} \to \mathbb{R}^+$ se define $f \sim g \iff f \in \Theta(g)$. Demuestre que $\sim$ es de equivalencia.

> [!example]- Solución
> **Refleja:** $f \le 1 \cdot f \le 1 \cdot f$, con $c = d = 1$. **Simétrica:** de $c\,g \le f \le d\,g$ resulta $\tfrac{1}{d} f \le g \le \tfrac{1}{c} f$. **Transitiva:** de $c_1 g \le f \le d_1 g$ (desde $n_1$) y $c_2 h \le g \le d_2 h$ (desde $n_2$) resulta $c_1 c_2 h \le f \le d_1 d_2 h$ para $n \ge \max\{n_1, n_2\}$.

## Preguntas de repaso

> [!question]- ¿Qué se debe fijar antes de demostrar una cota $O$ por inducción?
> Las constantes $c$ y $n_0$, estimadas a partir de los primeros valores; después la inducción prueba $T(n) \le c f(n)$ para $n \ge n_0$.

> [!question]- ¿Por qué el ejercicio 5 no es $\Theta$ de ningún polinomio?
> Porque para $n$ par crece como $n$ y para $n$ impar como $n^2$; una sola potencia $n^k$ no puede acotar a la vez ambas ramas.

> [!question]- ¿Cómo se decide entre los tres casos del teorema maestro en los ejercicios 7 y 9?
> Se compara $a_1 + a_2$ con $b^d$: en ambos $a_1 + a_2 = b^d$ ($2 = 2^1$ y $3 = 3^1$), lo que da $\Theta(n \log n)$.
