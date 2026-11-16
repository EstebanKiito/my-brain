---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - El teorema del binomio y cómo hallar coeficientes]]"
  - "[[04 - Progresiones en problemas]]"
---

# Ejercicios de la guía de progresiones, sumas y binomio

Los dieciocho ejercicios de la Guía 9. Los primeros nueve son sumas; el 10 es una sucesión recursiva; del 11 al 18 son progresiones. Conviene intentar cada uno antes de abrir la solución.

## Sumas

### 1. Múltiplos de 3
Calcule la suma de los múltiplos de $3$ menores que $100$.

> [!example]- Solución
> $3 + 6 + \dots + 99 = 3\sum_{k=1}^{33}k = 3\cdot\tfrac{33\cdot 34}{2} = 1683$.

### 2. Una suma con $r^i$
Sea $r > 0$. Calcule $\sum_{i=1}^{n} i\,r^i$.

> [!example]- Solución
> Para $r = 1$ es $\tfrac{n(n+1)}{2}$. Para $r \neq 1$, con $T = \sum i r^i$: $T - rT = \sum_{i=1}^{n} r^i - n r^{n+1} = \tfrac{r - r^{n+1}}{1 - r} - n r^{n+1}$, y por tanto $T = \dfrac{r\left(1 - (n + 1)r^n + n r^{n+1}\right)}{(1 - r)^2}$.

### 3. Con factoriales
Calcule $\sum_{k=1}^{n}\dfrac{k}{(k + 1)!}$.

> [!example]- Solución
> $\tfrac{k}{(k + 1)!} = \tfrac{(k + 1) - 1}{(k + 1)!} = \tfrac{1}{k!} - \tfrac{1}{(k + 1)!}$: telescópica. La suma es $1 - \tfrac{1}{(n + 1)!}$.

### 4. Con potencias de 2
Calcule $\sum_{k=1}^{n}\dfrac{k + 2}{k(k + 1)2^k}$.

> [!example]- Solución
> Con $a_k = \tfrac{1}{k\,2^{k-1}}$, $a_k - a_{k+1} = \tfrac{2(k + 1) - k}{k(k + 1)2^k} = \tfrac{k + 2}{k(k + 1)2^k}$. La suma es $a_1 - a_{n+1} = 1 - \dfrac{1}{(n + 1)2^n}$.

### 5. Signos alternados
Calcule $\sum_{k=1}^{n}(-1)^k\, 2k^2$.

> [!example]- Solución
> Es $(-1)^n n(n + 1)$. Por inducción: $n = 1$ da $-2$. Si vale para $n$, $(-1)^n n(n + 1) + (-1)^{n+1}2(n + 1)^2 = (-1)^{n+1}(n + 1)\big(2(n + 1) - n\big) = (-1)^{n+1}(n + 1)(n + 2)$.

### 6. Un término del binomio
Calcule el sexto término del desarrollo de $(x + y)^{15}$.

> [!example]- Solución
> El término $k$-ésimo (a partir de $k = 0$) es $\binom{15}{k}x^{15-k}y^k$; el sexto es $k = 5$: $\binom{15}{5}x^{10}y^5 = 3003\,x^{10}y^5$.

### 7. Una suma doble
Calcule $\sum_{k=2}^{n}\binom{n}{k}\left(\tfrac{1}{2} + \dots + \tfrac{1}{2^k}\right)$.

> [!example]- Solución
> $\tfrac{1}{2} + \dots + \tfrac{1}{2^k} = 1 - \tfrac{1}{2^k}$. Luego la suma es $\sum_{k=2}^{n}\binom{n}{k} - \sum_{k=2}^{n}\binom{n}{k}\tfrac{1}{2^k} = (2^n - 1 - n) - \left[\left(\tfrac{3}{2}\right)^n - 1 - \tfrac{n}{2}\right] = 2^n - \left(\tfrac{3}{2}\right)^n - \tfrac{n}{2}$.

### 8. Binomiales con peso
Calcule $\binom{n}{1} + 2\binom{n}{2} + \dots + n\binom{n}{n}$.

> [!example]- Solución
> Es $\sum_{k=1}^{n}k\binom{n}{k}$. Como $k\binom{n}{k} = n\binom{n-1}{k-1}$, vale $n\sum_{j=0}^{n-1}\binom{n-1}{j} = n\,2^{n-1}$.

### 9. Suma de pares
Calcule $2 + 4 + 6 + \dots + 20$.

> [!example]- Solución
> $2\cdot(1 + \dots + 10) = 2\cdot 55 = 110$.

## Sucesión recursiva y progresiones

### 10. Un término general
Determine el $n$-ésimo término de $\sqrt{2},\ \sqrt{2\sqrt{2}},\ \sqrt{2\sqrt{2\sqrt{2}}},\ \dots$

> [!example]- Solución
> $a_1 = 2^{1/2}$, $a_2 = 2^{3/4}$, $a_3 = 2^{7/8}$. En general $a_n = 2^{1 - 2^{-n}}$: por inducción, $a_{n+1} = \sqrt{2\,a_n} = 2^{(1 + 1 - 2^{-n})/2} = 2^{1 - 2^{-(n+1)}}$.

### 11. Dos términos aritméticos
El décimo término de una progresión aritmética es $\tfrac{55}{2}$ y el segundo es $\tfrac{7}{2}$. Halle el primero.

> [!example]- Solución
> $8d = \tfrac{55}{2} - \tfrac{7}{2} = 24$, $d = 3$; $a_1 = \tfrac{7}{2} - 3 = \tfrac{1}{2}$.

### 12. Suma aritmética
Sume la progresión $-3, -\tfrac{3}{2}, 0, \tfrac{3}{2}, 3, \dots, 30$.

> [!example]- Solución
> $d = \tfrac{3}{2}$ y $-3 + (n - 1)\tfrac{3}{2} = 30$ da $n = 23$. $S = \tfrac{23}{2}(-3 + 30) = \tfrac{621}{2}$.

### 13. Cuántos términos
Una aritmética tiene primer término $5$ y diferencia $2$. ¿Cuántos términos suman $2700$?

> [!example]- Solución
> $\tfrac{n}{2}(10 + 2(n - 1)) = n(n + 4) = 2700$, $n^2 + 4n - 2700 = (n - 50)(n + 54) = 0$: $n = 50$.

### 14. Quinto término
El primer término de una geométrica es $8$ y el tercero es $4$. Halle el quinto.

> [!example]- Solución
> $r^2 = \tfrac{4}{8} = \tfrac{1}{2}$, $a_5 = 8r^4 = 8 \cdot \tfrac{1}{4} = 2$.

### 15. Tercer término
La razón de una geométrica es $\tfrac{3}{2}$ y el quinto término es $1$. Halle el tercero.

> [!example]- Solución
> $a_3 = \dfrac{a_5}{r^2} = \dfrac{1}{9/4} = \tfrac{4}{9}$.

### 16. Suma de seis términos
Sume los seis primeros términos de una geométrica de primer término $5$ y razón $2$.

> [!example]- Solución
> $5\cdot\tfrac{2^6 - 1}{2 - 1} = 315$.

### 17. Una suma alternada
Calcule $1 - \tfrac{1}{2} + \tfrac{1}{4} - \tfrac{1}{8} + \dots - \tfrac{1}{512}$.

> [!example]- Solución
> Son los $(-\tfrac{1}{2})^k$ con $k = 0, \ldots, 9$: $\dfrac{1 - (-1/2)^{10}}{1 + 1/2} = \dfrac{1023/1024}{3/2} = \tfrac{341}{512}$.

### 18. Qué término es
¿Cuál es el término de la progresión geométrica $2, 6, 18, \dots$ igual a $118\,098$?

> [!example]- Solución
> $2\cdot 3^{n-1} = 118\,098 \Rightarrow 3^{n-1} = 59\,049 = 3^{10} \Rightarrow n = 11$. (La guía imprime "$2, 6, 8, \ldots$"; con razón $3$ el tercer término es $18$.)

## Preguntas de repaso

> [!question]- ¿Qué identidad permite resolver los ejercicios 3 y 4?
> La telescópica: se escribe el término como $a_k - a_{k+1}$ para que solo sobrevivan los extremos.

> [!question]- ¿Por qué en el ejercicio 13 se descarta $n = -54$?
> Porque $n$ es una cantidad de términos y debe ser un natural positivo.

> [!question]- ¿Cómo se relaciona el ejercicio 8 con el teorema del binomio?
> $k\binom{n}{k} = n\binom{n-1}{k-1}$ reduce la suma a $n\sum\binom{n-1}{j} = n\,2^{n-1}$, que es el corolario $(1 + 1)^{n-1}$.
