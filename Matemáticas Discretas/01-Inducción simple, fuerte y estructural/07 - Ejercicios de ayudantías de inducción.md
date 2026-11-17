---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Inducción fuerte]]"
  - "[[06 - Inducción estructural]]"
---

# Ejercicios de ayudantías de inducción

Cinco ejercicios de ayudantía, uno o dos por cada variante: inducción simple, fuerte y estructural. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Suma de cuadrados
Demuestre que $\displaystyle\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$ para todo $n \ge 1$.

> [!example]- Solución
> **CB** ($n = 1$): $1^2 = 1$ y $\tfrac{1 \cdot 2 \cdot 3}{6} = 1$. **HI:** vale para $n$. **TI:**
> $$\sum_{i=1}^{n+1} i^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{(n+1)\big(n(2n+1) + 6(n+1)\big)}{6} = \frac{(n+1)(2n^2 + 7n + 6)}{6}.$$
> Como $2n^2 + 7n + 6 = (n+2)(2n+3)$, queda $\tfrac{(n+1)((n+1)+1)(2(n+1)+1)}{6}$, que es la fórmula con $n+1$.

### 2. Regiones del plano
Un conjunto de $n$ rectas en el plano, sin dos paralelas ni tres concurrentes, lo divide en $\dfrac{n^2 + n + 2}{2}$ regiones.

> [!example]- Solución
> **CB** ($n = 0$): el plano sin rectas es $1$ región y $\tfrac{0 + 0 + 2}{2} = 1$. **HI:** $n$ rectas dan $\tfrac{n^2+n+2}{2}$ regiones. **TI:** al agregar la recta $n+1$, que no es paralela a ninguna ni pasa por un cruce, corta a las $n$ rectas en $n$ puntos distintos. Esos puntos dividen la nueva recta en $n + 1$ tramos y cada tramo parte en dos una región existente: se agregan $n+1$ regiones.
> $$\frac{n^2+n+2}{2} + (n+1) = \frac{n^2 + 3n + 4}{2} = \frac{(n+1)^2 + (n+1) + 2}{2}.$$
>
> ![Regiones del plano al agregar una recta](adjuntos/Regiones%20del%20plano%20al%20agregar%20una%20recta.png)
>
> Transcripción: a la izquierda hay tres rectas (azul, verde y naranja) que dividen el plano en 7 regiones; se agrega una cuarta recta (roja, punteada). A la derecha, la recta roja cruza las tres anteriores y parte en dos las cuatro regiones que atraviesa, marcadas con la misma letra, con lo que se agregan 4 regiones: $7 + 4 = 11 = \tfrac{16 + 4 + 2}{2}$.

### 3. Fibonacci y el número áureo
Con $\varphi = \tfrac{1 + \sqrt 5}{2}$ y $F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1} + F_{n-2}$, demuestre que $F_n \ge \varphi^{n-2}$ para todo $n \ge 2$.

> [!example]- Solución
> Inducción fuerte con **dos casos base**: $F_2 = 1 \ge \varphi^0 = 1$ y $F_3 = 2 \ge \varphi^1 \approx 1{,}618$. **HI:** $F_k \ge \varphi^{k-2}$ para $2 \le k < n$ (con $n \ge 4$). **TI:**
> $$F_n = F_{n-1} + F_{n-2} \ge \varphi^{n-3} + \varphi^{n-4} = \varphi^{n-4}(\varphi + 1) = \varphi^{n-4}\varphi^2 = \varphi^{n-2},$$
> donde se usa $\varphi + 1 = \varphi^2$ (porque $\varphi$ es raíz de $x^2 = x + 1$).

### 4. $\sqrt{2}$ es irracional
Demuestre por inducción fuerte que $\sqrt 2$ no se puede escribir como $a/b$ con $a, b$ enteros positivos.

> [!example]- Solución
> Se prueba, por inducción fuerte sobre el numerador $a$, que ninguna fracción $a/b$ vale $\sqrt 2$. Si $a = 1$, $\sqrt 2 = 1/b$ da $b^2 = 1/2$, imposible en enteros (**CB**). Paso: si $\sqrt 2 = a/b$, entonces $a^2 = 2b^2$, luego $a$ es par, $a = 2c$; entonces $2c^2 = b^2$, luego $b = 2d$ es par y $\sqrt 2 = \tfrac{2c}{2d} = \tfrac{c}{d}$ con $c < a$. Eso contradice la HI (ninguna fracción con numerador menor representa $\sqrt 2$).

### 5. Árboles binarios: tamaño y altura
Los árboles binarios son el menor conjunto con $\bullet \in S$ y, si $t_1, t_2 \in S$, $\bullet(t_1, t_2) \in S$. El tamaño cumple $\lvert\bullet\rvert = 1$, $\lvert\bullet(t_1, t_2)\rvert = 1 + \lvert t_1\rvert + \lvert t_2\rvert$ y la altura $h(\bullet) = 0$, $h(\bullet(t_1, t_2)) = 1 + \max\{h(t_1), h(t_2)\}$. Demuestre $\lvert t\rvert \le 2^{h(t)+1} - 1$.

> [!example]- Solución
> Inducción estructural. **Base:** $\lvert\bullet\rvert = 1 \le 2^{0+1} - 1 = 1$. **HI:** $\lvert t_i\rvert \le 2^{h(t_i)+1} - 1$ para $i = 1, 2$. **TI** con $t = \bullet(t_1, t_2)$: como $h(t_i) \le h(t) - 1$,
> $$\lvert t\rvert = 1 + \lvert t_1\rvert + \lvert t_2\rvert \le 1 + (2^{h(t_1)+1} - 1) + (2^{h(t_2)+1} - 1) \le 2^{h(t)} + 2^{h(t)} - 1 = 2^{h(t)+1} - 1.$$

## Preguntas de repaso

> [!question]- ¿Qué cambia en el planteamiento entre el ejercicio 1 y el 3?
> En el 1, la HI solo necesita $P(n)$ (inducción simple); en el 3, el paso usa dos términos anteriores y exige inducción fuerte con dos casos base.

> [!question]- En el ejercicio 4, ¿por qué se induce sobre el numerador?
> Porque el paso produce una fracción equivalente con numerador estrictamente menor ($c < a$), lo que permite aplicar la HI fuerte.

> [!question]- ¿Cómo se ve la inducción estructural en el ejercicio 5?
> Hay un caso base ($\bullet$) y una regla; la HI se aplica a los dos subárboles $t_1, t_2$, que son estructuras más pequeñas dentro de $t$.
