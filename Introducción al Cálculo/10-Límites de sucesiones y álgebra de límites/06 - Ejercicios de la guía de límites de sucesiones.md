---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Teorema del sándwich y límites por acotación]]"
---

# Ejercicios de la guía de límites de sucesiones

De los dieciséis ejercicios de la Guía 10, esta nota resuelve los de **cálculo de límites con álgebra, sándwich y cotas** (3, 4, 5, 7, 9, 10, 11, 14, 15 y 16). Los de monotonía y cota (1, 2, 6 y 12) están en [[05 - Ejercicios de la guía de sucesiones acotadas y monótonas|su nota]], y los que requieren el número $e$ (8 y 13) están en el tema siguiente.

## Ejercicios

### 3. Un cociente de polinomios
Calcule $\lim\dfrac{n + n^2}{n^3}$.

> [!example]- Solución
> $\dfrac{n + n^2}{n^3} = \dfrac{1}{n^2} + \dfrac{1}{n} \to 0$.

### 4. Potencias de $1 - \tfrac{1}{n}$
Calcule $\lim\dfrac{1 - \left(1 - \tfrac{1}{n}\right)^4}{1 - \left(1 - \tfrac{1}{n}\right)^3}$.

> [!example]- Solución
> Con $x = \tfrac{1}{n}$: $1 - (1 - x)^4 = 4x - 6x^2 + 4x^3 - x^4$ y $1 - (1 - x)^3 = 3x - 3x^2 + x^3$. Dividiendo por $x$: $\dfrac{4 - 6x + 4x^2 - x^3}{3 - 3x + x^2} \to \dfrac{4}{3}$ cuando $x = \tfrac{1}{n} \to 0$.

### 5. Un cociente simple
Calcule $\lim\dfrac{n + 1}{n}$.

> [!example]- Solución
> $\dfrac{n + 1}{n} = 1 + \dfrac{1}{n} \to 1$.

### 7. Diferencia de raíces
Calcule $\lim\left(\sqrt{n + 1} - \sqrt{n}\right)$.

> [!example]- Solución
> Con el conjugado: $\sqrt{n + 1} - \sqrt{n} = \dfrac{1}{\sqrt{n + 1} + \sqrt{n}}$. El denominador tiende a $\infty$ y el cociente a $0$. (Cota: $0 < \tfrac{1}{\sqrt{n + 1} + \sqrt{n}} < \tfrac{1}{\sqrt{n}} \to 0$.)

### 9. Raíz $n$-ésima de $n$
Decida la convergencia de $a_n = \sqrt[n]{n}$.

> [!example]- Solución
> Converge a $1$. Con $x_n = \sqrt[n]{n} - 1 \ge 0$, el binomio da $n = (1 + x_n)^n \ge \tfrac{n(n - 1)}{2}x_n^2$, luego $0 \le x_n \le \sqrt{\tfrac{2}{n - 1}} \to 0$ y, por sándwich, $x_n \to 0$.

### 10. Razón menor que 1
Demuestre que si $x_n > 0$ y $\lim\dfrac{x_{n+1}}{x_n} = a < 1$, entonces $\lim x_n = 0$.

> [!example]- Solución
> Se elige $r$ con $a < r < 1$ (por ejemplo, $r = \tfrac{a + 1}{2}$). Como $\tfrac{x_{n+1}}{x_n} \to a < r$, existe $N$ con $\tfrac{x_{n+1}}{x_n} < r$ para $n \ge N$. Entonces $x_{N+j} < r^j x_N$ para todo $j \ge 0$, es decir $0 < x_n < x_N\, r^{-N} r^n$ para $n \ge N$. Como $r^n \to 0$ ($0 < r < 1$), el sándwich da $x_n \to 0$.

### 11. Potencias, exponenciales y factoriales
Demuestre que $\lim\dfrac{n^k}{a^n} = \lim\dfrac{a^n}{n!} = \lim\dfrac{n!}{n^n} = 0$ (con $a > 1$ y $k$ fijo).

> [!example]- Solución
> - $\tfrac{n^k}{a^n}$: la razón $\tfrac{(n + 1)^k/a^{n+1}}{n^k/a^n} = \left(\tfrac{n + 1}{n}\right)^k\tfrac{1}{a} \to \tfrac{1}{a} < 1$ (por álgebra de límites, pues $\tfrac{n + 1}{n} \to 1$). Por el ejercicio 10, $\to 0$.
> - $\tfrac{a^n}{n!}$: la razón es $\tfrac{a}{n + 1} \to 0 < 1$; por el ejercicio 10, $\to 0$.
> - $\tfrac{n!}{n^n}$: $0 < \tfrac{n!}{n^n} \le \tfrac{1}{n}$ (producto de factores $\tfrac{k}{n} \le 1$, el primero $\tfrac{1}{n}$); por sándwich, $\to 0$.

### 14. Máximo de dos números
Sean $a, b \ge 0$. Demuestre que $\lim\sqrt[n]{a^n + b^n} = \max\{a, b\}$.

> [!example]- Solución
> Sea $m = \max\{a, b\}$. Entonces $m^n \le a^n + b^n \le 2m^n$, y tomando raíz $n$-ésima, $m \le \sqrt[n]{a^n + b^n} \le \sqrt[n]{2}\,m$. Como $\sqrt[n]{2} \to 1$, ambos extremos tienden a $m$ y el sándwich concluye.

### 15. Cada término es una fracción del anterior
Sea $\{a_n\}$ de términos no negativos con $a_{n+1} \le K a_n$ para todo $n$, donde $K \in (0, 1)$. Demuestre que $\lim a_n = 0$.

> [!example]- Solución
> Por inducción, $a_n \le K^{n-1}a_1$. Entonces $0 \le a_n \le K^{n-1}a_1$ y $K^{n-1}a_1 \to 0$ (pues $0 < K < 1$). Por sándwich, $a_n \to 0$.

### 16. La propiedad de Galileo (difícil)
La sucesión de impares cumple $\tfrac{1}{3} = \tfrac{1 + 3}{5 + 7} = \tfrac{1 + 3 + 5}{7 + 9 + 11} = \cdots$. ¿Es la única progresión aritmética con esa propiedad?

> [!example]- Solución (para progresiones aritméticas)
> Sea $a_k = a + (k - 1)d$. La suma de los primeros $n$ es $S_n = \tfrac{n}{2}\big(2a + (n - 1)d\big)$ y la de los $n$ siguientes es $S_{2n} - S_n = \tfrac{n}{2}\big(2a + (3n - 1)d\big)$. La razón $\tfrac{2a + (n - 1)d}{2a + (3n - 1)d}$ es una constante $c$ para todo $n$ si y solo si $d = 3cd$ y $2a - d = c(2a - d)$. Si $d \neq 0$, $c = \tfrac{1}{3}$ y entonces $2a - d = 0$, es decir $d = 2a$: son las progresiones $a, 3a, 5a, \ldots$, o sea **los impares multiplicados por una constante**. Si $d = 0$ (sucesión constante) la razón es $1$. Por tanto la afirmación de Galileo es correcta salvo múltiplos (y las constantes). Para progresiones geométricas la razón de las sumas es $r^{-n}$, que solo es constante si $r = 1$.

## Preguntas de repaso

> [!question]- ¿Cómo se aplica el ejercicio 10 al límite $\frac{n^k}{a^n}$?
> Se calcula la razón de términos consecutivos, $\left(\frac{n+1}{n}\right)^k\frac{1}{a}$, cuyo límite es $\frac{1}{a} < 1$; entonces el ejercicio 10 da límite $0$.

> [!question]- ¿Por qué en el ejercicio 14 sirve acotar por $2m^n$?
> Porque $a^n + b^n$ es la suma de dos números que no superan $m^n$ y el mayor es exactamente $m^n$: queda entre $m^n$ y $2m^n$, y la raíz $n$-ésima de $2$ tiende a $1$.

> [!question]- ¿Qué indica el ejercicio 15 sobre una sucesión que se reduce siempre a una fracción $K < 1$ de la anterior?
> Que decae al menos tan rápido como una geométrica de razón $K$ y por eso converge a $0$.
