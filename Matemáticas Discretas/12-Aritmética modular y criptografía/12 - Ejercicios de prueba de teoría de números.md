---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Teorema chino del resto]]"
  - "[[07 - Pequeño teorema de Fermat]]"
  - "[[10 - Palomar sobre sumas parciales y teorema multinomial]]"
---

# Ejercicios de prueba de teoría de números

Doce preguntas de interrogaciones y exámenes que cubren los tipos habituales: criterios de divisibilidad, potencias módulo $m$, Euclides y Bézout, teorema chino, Fermat, representación en base $b$ y conteo.

## Ejercicios

### 1. Criterio del 3 e inverso modular (examen, 2018-2)
(a) Un número es divisible por $3$ si y solo si la suma de sus dígitos lo es. (b) $a$ tiene inverso módulo $n$ si y solo si $\operatorname{MCD}(a, n) = 1$.

> [!example]- Solución
> (a) Con $n = \sum d_i 10^i$ y $10 \equiv 1 \pmod 3$, se tiene $n \equiv \sum d_i \pmod 3$; luego $n \equiv 0$ si y solo si la suma de dígitos es $\equiv 0$ (cada paso es una equivalencia).
>
> (b) ($\Rightarrow$) Si $ab \equiv 1$, entonces $1 = ab - kn$ y todo divisor común de $a$ y $n$ divide a $1$. ($\Leftarrow$) Si $\operatorname{MCD}(a, n) = 1$, Bézout da $1 = as + nt$, de donde $as \equiv 1 \pmod n$.

### 2. Potencias módulo $m$ y último dígito (examen, 2018-2)
(a) Si $a \equiv b \pmod m$ y $n > 0$, entonces $a^n \equiv b^n$. (b) Último dígito de $4321^{4321}$. (c) $10 \mid 101^{2003} - 1$.

> [!example]- Solución
> (a) Inducción en $n$: $n = 1$ es la hipótesis; si $a^n \equiv b^n$ y $a \equiv b$, el producto de congruencias da $a^{n+1} \equiv b^{n+1}$.
>
> (b) El último dígito es el resto módulo $10$. Como $4321 \equiv 1$, $4321^{4321} \equiv 1^{4321} = 1$: el último dígito es **1**.
>
> (c) $101 \equiv 1 \pmod{10}$, luego $101^{2003} \equiv 1$ y $10 \mid 101^{2003} - 1$.

### 3. MCD y simplificación de un factor (interrogación 3, 2017-1)
Para $m > 1$: (1) si $a \equiv b \pmod m$, entonces $\operatorname{MCD}(a, m) = \operatorname{MCD}(b, m)$; (2) si $ac \equiv bc \pmod m$, entonces $a \equiv b \pmod{m / \operatorname{MCD}(m, c)}$.

> [!example]- Solución
> (1) Como $a \bmod m = b \bmod m$, por Euclides $\operatorname{MCD}(a, m) = \operatorname{MCD}(m, a \bmod m) = \operatorname{MCD}(m, b \bmod m) = \operatorname{MCD}(b, m)$.
>
> (2) Sea $g = \operatorname{MCD}(c, m)$, $c = gs$, $m = gt$. De $ac - bc = km$ se obtiene $g s (a - b) = k g t$, o sea $s(a - b) = kt$ y $as \equiv bs \pmod t$. Como $\operatorname{MCD}(s, t) = 1$ ($ps + qt = 1$ por Bézout), $s$ tiene inverso módulo $t$ y se cancela: $a \equiv b \pmod t$, con $t = m/g$.

### 4. Euclides, Bézout e inversos (examen, 2025-1)
Sean $a, b > 0$. (1) Si $a > b$, $\operatorname{MCD}(a, b) = \operatorname{MCD}(b, r)$ con $r = a \bmod b$. (2) Existen $s, t$ con $\operatorname{MCD}(a, b) = sa + tb$. (3) Si $sa + tb = 1$, entonces $sa \equiv_b 1$. (4) Si $\operatorname{MCD}(a, b) = 1$, $ax \equiv_b c$ tiene solución.

> [!example]- Solución
> (1) Con $a = kb + r$: un divisor común de $b$ y $r$ divide a $a$, y uno de $a$ y $b$ divide a $r = a - kb$.
>
> (2) Sean $r_0 = a$, $r_1 = b$ y $r_i = r_{i-2} - k_i r_{i-1}$ los restos del algoritmo. Por inducción cada $r_i = s_i a + t_i b$: base $r_0 = 1 \cdot a + 0 \cdot b$, $r_1 = 0 \cdot a + 1 \cdot b$; paso $s_i = s_{i-2} - k_i s_{i-1}$ y análogo para $t_i$. El último resto no nulo es el MCD por (1).
>
> (3) $sa - 1 = -tb$ es múltiplo de $b$. (4) Con $s$ inverso de $a$ módulo $b$, $x = sc$ cumple $ax = (as)c \equiv c$.

### 5. Teorema chino del resto y cuadrados de primos (examen, 2020-2)
(a) Menor número cuyo resto al dividir por $5, 7, 9, 11$ es $1, 2, 3, 4$. (b) Para todo primo $p \ge 6$, $p^2 - 1$ o $p^2 + 1$ es múltiplo de $10$.

> [!example]- Solución
> (a) $m = 3465$ y $M_i = 693, 495, 385, 315$ con inversos $2, 3, 4, 8$ módulo $5, 7, 9, 11$. Entonces
> $$x \equiv 1 \cdot 693 \cdot 2 + 2 \cdot 495 \cdot 3 + 3 \cdot 385 \cdot 4 + 4 \cdot 315 \cdot 8 = 19056 \equiv 1731 \pmod{3465}.$$
> El menor es **1731** (una búsqueda exhaustiva en $[0, 3465)$ confirma que es el único).
>
> (b) $p$ es impar, así que $p^2 \pm 1$ es par. Además $5 \nmid p$ y los cuadrados módulo $5$ de $1, 2, 3, 4$ son $1, 4, 4, 1$: luego $p^2 \equiv \pm 1 \pmod 5$, es decir $5 \mid p^2 - 1$ o $5 \mid p^2 + 1$. Como $2$ y $5$ son coprimos, $10$ divide a $p^2 - 1$ o a $p^2 + 1$. (Es la misma idea de un examen de 2026-1 para $p \ge 7$.)

### 6. Sistema de dos congruencias (examen, 2022-2)
Demuestre que $x \equiv a_1 \pmod{m_1}$, $x \equiv a_2 \pmod{m_2}$ tiene solución si y solo si $\operatorname{MCD}(m_1, m_2) \mid (a_1 - a_2)$.

> [!example]- Solución
> Sea $d = \operatorname{MCD}(m_1, m_2)$. ($\Rightarrow$) Si $x = a_1 + m_1 k_1 = a_2 + m_2 k_2$, entonces $a_1 - a_2 = m_2 k_2 - m_1 k_1$, que es múltiplo de $d$.
>
> ($\Leftarrow$) Si $a_1 - a_2 = dk$ y, por Euclides extendido, $d = s m_1 + t m_2$, entonces $z = a_1 - sk\, m_1 = a_2 + tk\, m_2$ (porque $a_1 - a_2 = k(sm_1 + tm_2)$) es congruente con $a_1$ módulo $m_1$ y con $a_2$ módulo $m_2$.

### 7. $a^{(p-1)/2} \equiv \pm 1$ (examen, 2016-2)
Sea $p$ primo impar. Para cada $a \in \mathbb{Z}_p$, $a \ne 0$, demuestre $a^{(p-1)/2} \equiv 1$ o $\equiv -1 \pmod p$.

> [!example]- Solución
> Por Fermat, $a^{p-1} - 1 = \alpha p$. Factorizando, $\left(a^{\frac{p-1}{2}} - 1\right)\left(a^{\frac{p-1}{2}} + 1\right) = \alpha p$, y como $p$ es primo divide a un factor. Se requiere $a \ne 0$ para poder usar Fermat; con $a = 0$ la afirmación es falsa.

### 8. Dos congruencias implican una módulo $pq$ (examen, 2024-2)
Sean $p \ne q$ primos con $a^q \equiv a \pmod p$ y $a^p \equiv a \pmod q$. Demuestre que $a^{pq} \equiv a \pmod{pq}$.

> [!example]- Solución
> Elevando la primera a $p$: $a^{pq} = (a^q)^p \equiv a^p \equiv a \pmod p$ (la última por Fermat). Análogamente $a^{pq} = (a^p)^q \equiv a^q \equiv a \pmod q$. Entonces $a^{pq} - a = xp = yq$; como $p \mid yq$ y $p, q$ son primos distintos, $p \mid y$, $y = kp$ y $a^{pq} - a = kpq$.

### 9. Fermat y números compuestos (examen, 2025-2)
(a) Sea $p$ primo y $a \in \{1, \dots, p-1\}$. Si $b \equiv_{p-1} c$, entonces $a^b \bmod p = a^c \bmod p$. (b) Si $n \ge 2$ es compuesto, existe $a \in \{1, \dots, n-1\}$ con $a^{n-1} \bmod n \ne 1$.

> [!example]- Solución
> (a) Sea $b \ge c$ con $b - c = k(p-1)$. Como $p \nmid a$, $a^{p-1} \equiv 1$ y $a^b = a^c (a^{p-1})^k \equiv a^c \pmod p$.
>
> (b) Sea $d$ un divisor con $1 < d < n$. Si $d^{n-1} \equiv 1 \pmod n$, entonces $d^{n-1} = qn + 1$ y $d$ divide a $1 = d^{n-1} - qn$, absurdo. Luego $a = d$ sirve. Ejemplo: $n = 15$, $d = 3$: $3^{14} \bmod 15 = 9 \ne 1$.

### 10. Representación en base $b$ (interrogación 3, 2017-1)
Demuestre que para $b > 1$ todo $n \ge 1$ se escribe de forma única como $n = \sum_{i=0}^{k-1} a_i b^i$, con $a_{k-1} \ne 0$ y $0 \le a_i < b$.

> [!example]- Solución
> Inducción fuerte sobre $n$. Para $n = 1$ la única representación es $a_0 = 1$. Para $n > 1$ se escribe $n = qb + r$ con $q$ y $r$ únicos, $0 \le r < b$ y $q < n$. Si $q = 0$, $n = r$ es de un solo dígito. Si $q \ge 1$, por HI $q$ tiene representación única; se agrega $r$ como $a_0$ y se desplazan los demás dígitos. Unicidad: cualquier representación de $n$ cumple $n = (\sum_{i \ge 1} a_i b^{i-1}) b + a_0$, y por unicidad de cuociente y resto $a_0 = r$ y lo restante es una representación de $q$.

### 11. Palomar (interrogación 2, 2025-1)
Sea $m > 0$. En toda secuencia de $m$ enteros hay uno o más términos consecutivos cuya suma es divisible por $m$.

> [!example]- Solución
> Se toman $S_i = a_1 + \dots + a_i$ ($1 \le i \le m$). Si algún $S_i \equiv 0 \pmod m$, listo. Si no, los $m$ restos están en $\{1, \dots, m-1\}$ y por el palomar hay $i < j$ con $S_i \equiv S_j$, luego $S_j - S_i = a_{i+1} + \dots + a_j \equiv 0$.

### 12. Teorema multinomial (examen, 2025-1)
Demuestre $(x_1 + \dots + x_m)^n = \sum_{n_1 + \dots + n_m = n} \frac{n!}{n_1! \cdots n_m!} x_1^{n_1} \cdots x_m^{n_m}$.

> [!example]- Solución
> Al desarrollar el producto de $n$ factores aparecen monomios $x_1^{n_1} \cdots x_m^{n_m}$ con $\sum n_i = n$. Para formar uno se escoge $x_1$ en $n_1$ de los $n$ factores, $x_2$ en $n_2$ de los restantes, y así hasta $x_m$: $\binom{n}{n_1}\binom{n-n_1}{n_2} \cdots \binom{n - n_1 - \dots - n_{m-1}}{n_m} = \dfrac{n!}{n_1! \cdots n_m!}$ maneras. Sumando sobre todas las $m$-tuplas se obtiene la fórmula.

## Preguntas de repaso

> [!question]- ¿Qué herramienta resuelve casi todas las preguntas de existencia de inversos o soluciones?
> La identidad de Bézout: convierte "el MCD es 1" en una combinación $sa + tb = 1$ que da el inverso.

> [!question]- ¿Cuándo conviene el teorema de Fermat frente a reducir potencias a mano?
> Cuando el módulo es primo y la base no es múltiplo suyo: el exponente puede reducirse módulo $p - 1$.

> [!question]- ¿Cómo se prueba que una congruencia vale módulo $pq$ con $p, q$ primos distintos?
> Se prueba módulo $p$ y módulo $q$ por separado y se combina con el lema del teorema chino del resto.
