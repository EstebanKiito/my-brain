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

# Ejercicios de ayudantías de algoritmos y complejidad

Cinco ejercicios de ayudantía sobre las tres habilidades del tema: diseñar un algoritmo y analizar su costo, demostrar propiedades de las notaciones asintóticas, acotar una recurrencia por inducción y probar la corrección de un ciclo con un invariante. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Máximo de un cerro
Un **cerro** es una lista formada por una serie estrictamente creciente seguida de una estrictamente decreciente, como $[1, 2, 4, 19, 8, 3]$. (a) Escriba un algoritmo de dividir para conquistar que reciba un cerro y entregue su máximo. (b) Calcule su complejidad; se espera $O(\log n)$.

> [!example]- Solución
> **(a)** Se mira el elemento del medio y su vecino derecho. Si $A[m] > A[m+1]$, el máximo está en $A[0..m]$ (ya se pasó la cima o se está en ella); si $A[m] < A[m+1]$, está en $A[m+1..n-1]$.
> ```
> Cerro(A[a..b]):
>   n ← b − a + 1
>   if n = 1: return A[a]
>   m ← a + ⌊(n−1)/2⌋
>   if A[m] > A[m+1]: return Cerro(A[a..m])
>   else:             return Cerro(A[m+1..b])
> ```
> Los elementos del cerro son distintos, así que no hay empate. Con $[1, 2, 4, 19, 8, 3]$ se compara $4 < 19$ (se sigue a la derecha, con $[19, 8, 3]$), luego $8 > 3$ (queda $[19, 8]$) y por último $19 > 8$ (queda $[19]$), que se devuelve.
>
> **(b)** Se cuentan comparaciones: la prueba $n = 1$ y las dos de $A[m]$ con $A[m+1]$, y se continúa sobre a lo más $\lceil n/2 \rceil$ elementos: $T(1) = 1$, $T(n) = T(\lceil n/2 \rceil) + 3$. Con $n = 2^k$: $T(2^k) = T(2^{k-1}) + 3 = \dots = T(1) + 3k = 3 \log_2 n + 1$. Como $T$ es asintóticamente no decreciente y $\log n$ es no decreciente y 2-armónica, el teorema de extensión da $T \in O(\log n)$. (Verificado: con $n = 1, 2, 4, 8, \dots$ el peor caso medido es $1, 4, 7, 10, \dots$.)

### 2. $\Theta$ con mínimo y máximo
Sean $f, g : \mathbb{N} \to \mathbb{R}^+$ con $f \in \Theta(g)$. Demuestre que $\min\{f, g\} \in \Theta(\max\{f, g\})$.

> [!example]- Solución
> Hay $c, d > 0$ y $n_0$ con $c\,g \le f \le d\,g$ para $n \ge n_0$. Sea $h = \min\{f, g\}$ y $H = \max\{f, g\}$; siempre $h \le H$.
> - Si $f(n) \le g(n)$: $h = f \ge c\,g = c\,H$.
> - Si $g(n) < f(n)$: $h = g \ge \tfrac{1}{d} f = \tfrac{1}{d} H$.
>
> En ambos casos $\min\{c, \tfrac1d\}\, H \le h \le 1 \cdot H$ para $n \ge n_0$, que es la definición de $\Theta$.

### 3. Contraejemplo con potencias
Pruebe o refute: si $f \in O(g)$, entonces $f(n)^{g(n)} \in O\big(g(n)^{f(n)}\big)$.

> [!example]- Solución
> Es falso. Con $f(n) = 2$ y $g(n) = n$ se tiene $f \in O(g)$, pero $f^g = 2^n$ y $g^f = n^2$, y $2^n \notin O(n^2)$ porque $\tfrac{2^n}{n^2} \to \infty$ (una exponencial supera a todo polinomio). Basta este contraejemplo.

### 4. Recurrencia con logaritmo
Sea $T(1) = 1$ y $T(n) = 4\,T(\lfloor n/2 \rfloor) + n^2 \log_2 n$ para $n > 1$. Demuestre por inducción que $T(n) \in O(n^2 (\log n)^2)$.

> [!example]- Solución
> Valores: $T(2) = 8 > 2^2 \cdot 1^2 = 4$, así que $c = 1$ no sirve desde $n = 2$, pero $T(3) \approx 18{,}3 \le 22{,}6$, $T(4) = 64 \le 64$ y $T(5) \approx 90 \le 134{,}8$. Se prueba $T(n) \le n^2 \log_2^2 n$ para $n \ge 3$ por inducción fuerte.
> - **Bases:** $n = 3, 4, 5$ (sus mitades $1$ y $2$ quedan fuera del rango; $n = 6$ ya usa $T(3)$).
> - **Paso** ($n \ge 6$, $3 \le \lfloor n/2 \rfloor < n$): por HI y $\lfloor n/2 \rfloor \le n/2$,
> $$T(n) \le 4 \cdot \tfrac{n^2}{4} \log_2^2 \tfrac n2 + n^2 \log_2 n = n^2\big((\log_2 n - 1)^2 + \log_2 n\big) = n^2(\log_2^2 n - \log_2 n + 1) \le n^2 \log_2^2 n,$$
> la última desigualdad porque $\log_2 n \ge 1$. Lo esencial es fijar $c$ y $n_0$ **antes** de empezar. Se comprobó por cálculo que la cota vale para todo $3 \le n < 4000$.

### 5. Mínimo común múltiplo (corrección)
Escriba un algoritmo iterativo que calcule $\mathrm{mcm}(a, b)$ para $a, b \ge 1$ y demuestre que es correcto.

> [!example]- Solución
> ```
> MCM(a, b):   ia ← a;  ib ← b
>   while a ≠ b:
>       if a < b: a ← a + ia  else: b ← b + ib
>   return a
> ```
> Se avanza siempre el menor de los dos múltiplos hasta que coincidan. Con $a = 4$ y $b = 6$: $(4,6) \to (8,6) \to (8,12) \to (12,12)$ y devuelve $12$.
>
> **Invariante** (tras $k$ iteraciones): (1) $a$ es múltiplo de $ia$ y $b$ de $ib$; (2) $a - ia < b$ y $b - ib < a$; (3) ningún múltiplo común positivo es menor que $\min\{a, b\}$. Además, $a/ia + b/ib = k + 2$ (cada vuelta suma $1$ a uno de los dos cocientes).
> - **Base:** $a - ia = 0 < b$, $b - ib = 0 < a$, y un múltiplo común es $\ge \max\{ia, ib\} \ge \min$.
> - **Paso** ($a < b$; el otro caso es simétrico): $a' = a + ia$. (2): $a' - ia = a < b$ y $b - ib < a < a'$. (3): si $m$ fuera común con $m < \min\{a', b\}$, por (3) $m \ge a$ y, siendo múltiplo de $ia$ menor que $a + ia$, $m = a$. Pero entonces $a$ sería múltiplo de $ib$ con $b - ib < a < b$, imposible entre dos múltiplos consecutivos de $ib$.
> - **Salida:** con $a = b$ es múltiplo común de ambos y, por (3), ningún múltiplo común es menor: es el mínimo.
> - **Terminación:** sea $L = \mathrm{mcm}(ia, ib)$. Mientras $a < b \le L$, el siguiente múltiplo de $ia$ es $\le L$ (pues $L$ es múltiplo de $ia$ mayor que $a$); lo mismo para $b$. Así $a, b \le L$ siempre, y como $a + b$ crece estrictamente en cada vuelta, el ciclo termina. (Verificado por cálculo para $1 \le a, b < 40$: coincide con $ab/\gcd(a, b)$.)

## Preguntas de repaso

> [!question]- ¿Qué tienen en común el cerro y la búsqueda binaria?
> Ambos descartan la mitad de la entrada con una comparación constante, de modo que $T(n) = T(\lceil n/2 \rceil) + \text{constante}$ y el costo es logarítmico.

> [!question]- ¿Por qué en el ejercicio 4 no sirve $c = 1$ desde $n = 2$?
> Porque $T(2) = 8$ supera $2^2 \log_2^2 2 = 4$. Por eso se fija $n_0 = 3$ y se tratan $3, 4, 5$ como casos base.

> [!question]- ¿Para qué sirve la condición (2) del invariante del MCM?
> Para impedir que $a$ sea un múltiplo común escondido por debajo de $b$; sin ella, el paso inductivo de (3) no se cierra.

> [!question]- ¿Cuándo basta un contraejemplo y cuándo hay que demostrar?
> Para refutar una afirmación general ("para todo $f, g$") basta una pareja concreta, como en el ejercicio 3; para probarla hay que dar constantes que sirvan para $f, g$ arbitrarias, como en el 2.
