---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[04 - Álgebra de límites y cocientes de polinomios]]"
---

# Teorema del sándwich y límites por acotación

El álgebra de límites no alcanza para sucesiones con senos, logaritmos, factoriales o potencias de $n$ en el exponente. En esos casos se **acota** la sucesión entre dos sucesiones simples que tienen el mismo límite: el teorema del sándwich. Es también la herramienta para los límites básicos que alimentan todo lo demás ($x^n \to 0$, $\sqrt[n]{p} \to 1$, $\sqrt[n]{n} \to 1$).

## Producto de una sucesión nula por una acotada

> [!tip] Nula por acotada
> Si $\lim a_n = 0$ y $\{b_n\}$ es **acotada**, entonces $\lim a_n b_n = 0$.

*Demostración.* Sea $|b_n| \le c$. Dado $\varepsilon > 0$, existe $N$ con $|a_n| < \tfrac{\varepsilon}{c}$ para $n > N$, y entonces $|a_n b_n| < \tfrac{\varepsilon}{c}\cdot c = \varepsilon$. $\blacksquare$

Por ejemplo, $b_n = \operatorname{sen}(n)$ no converge, pero está acotada por $1$, de modo que $\dfrac{\operatorname{sen}(n)}{n} \to 0$. Un resultado afín: si $\lim |a_n| = 0$, entonces $\lim a_n = 0$ (así, $\tfrac{(-1)^n}{n} \to 0$ porque $\left|\tfrac{(-1)^n}{n}\right| = \tfrac{1}{n} \to 0$).

## El teorema del sándwich

> [!tip] Teorema del sándwich
> Si $a_n \le b_n \le c_n$ para todo $n \ge n_0$ y $\lim a_n = \lim c_n = L$, entonces $\lim b_n = L$.

*Demostración.* Dado $\varepsilon > 0$ existen $N_1$ y $N_2$ con $L - \varepsilon < a_n$ para $n > N_1$ y $c_n < L + \varepsilon$ para $n > N_2$. Con $N = \max\{N_1, N_2\}$, para $n > N$: $L - \varepsilon < a_n \le b_n \le c_n < L + \varepsilon$. $\blacksquare$

> [!tip] Cómo usarlo
> 1. Acotar $b_n$ por abajo y por arriba con sucesiones cuyos límites se conocen.
> 2. Verificar que ambos límites **coinciden**.
> 3. Concluir. (Si $b_n \ge 0$, la cota inferior puede ser simplemente $0$.)

## Ejemplos

**Con funciones acotadas (I7, 2026-1; I3, 2025-2).** Como $-1 \le \operatorname{sen}(n) \le 1$, para $n \ge 5$:
$$-\frac{1}{n^2 - 16} \le \frac{\operatorname{sen}(n)}{n^2 - 16} \le \frac{1}{n^2 - 16},$$
y ambos extremos tienden a $0$. Luego $\dfrac{\operatorname{sen}(n)}{n^2 - 16} \to 0$ y, con $\dfrac{n}{n^2 - 16} \to 0$, resulta $\dfrac{n - \operatorname{sen}(n)}{n^2 - 16} \to 0$. De igual forma, $-\tfrac{1}{n} \le \tfrac{\cos(n^3 + 1)}{n} \le \tfrac{1}{n}$ da límite $0$.

**Con una cota que sube y baja (I8, 2023-1).** $a_n = \dfrac{n + \operatorname{sen}(n\pi/2)}{2n + 1}$. Como $-1 \le \operatorname{sen}\!\left(\tfrac{n\pi}{2}\right) \le 1$,
$$\frac{n - 1}{2n + 1} \le a_n \le \frac{n + 1}{2n + 1}, \qquad \frac{n \mp 1}{2n + 1} \to \frac{1}{2},$$
luego $\lim a_n = \tfrac{1}{2}$.

**Con el logaritmo: $\dfrac{\ln n}{n}$ (clase 22).** Por la desigualdad fundamental $\ln x \le x - 1 < x$, aplicada a $\sqrt{n}$: $0 \le \ln\sqrt{n} \le \sqrt{n}$, o sea $0 \le \tfrac{1}{2}\ln n \le \sqrt{n}$ y
$$0 \le \frac{\ln n}{n} \le \frac{2\sqrt{n}}{n} = \frac{2}{\sqrt{n}} \to 0.$$
Entonces $\dfrac{\ln n}{n} \to 0$.

**Con una potencia: $\dfrac{n}{2^n}$ (I3, 2025-2).** Del binomio, $2^n = (1 + 1)^n \ge 1 + n + \tfrac{n(n-1)}{2}$, así que para $n \ge 2$:
$$0 \le \frac{n}{2^n} \le \frac{n}{1 + n + n(n - 1)/2} \le \frac{2}{n - 1} \to 0.$$
Del mismo modo, $\tfrac{n^k}{a^n} \to 0$ si $a > 1$ (Guía 10): $a^n$ crece más rápido que cualquier potencia de $n$.

**Con un factorial: $\dfrac{n!}{n^n}$ (clase 24).** $\dfrac{n!}{n^n} = \dfrac{1}{n}\cdot\dfrac{2}{n}\cdots\dfrac{n}{n}$ y cada factor es $\le 1$; luego $0 < \dfrac{n!}{n^n} \le \dfrac{1}{n} \to 0$. Entonces $\dfrac{n!}{n^n} \to 0$.

**Una suma con $n$ términos (clase 22/24).** $a_n = \dfrac{n + 1}{n^2 + 1} + \dfrac{n + 2}{n^2 + 2} + \cdots + \dfrac{n + n}{n^2 + n}$. Cada sumando $\dfrac{n + k}{n^2 + k}$ se acota entre $\dfrac{n + k}{n^2 + n}$ y $\dfrac{n + k}{n^2 + 1}$, y como $\sum_{k=1}^{n}(n + k) = \tfrac{3n^2 + n}{2}$:
$$\frac{3n^2 + n}{2(n^2 + n)} \le a_n \le \frac{3n^2 + n}{2(n^2 + 1)}.$$
Ambos extremos tienden a $\tfrac{3}{2}$, luego $\lim a_n = \tfrac{3}{2}$.

## Tres límites básicos

> [!tip] Límites que se usan sin demostrar de nuevo
> 1. Si $|x| < 1$: $\ x^n \to 0$.
> 2. Si $p > 0$: $\ \sqrt[n]{p} \to 1$.
> 3. $\ \sqrt[n]{n} \to 1$.

- **$x^n \to 0$.** Dado $\varepsilon > 0$: $|x|^n < \varepsilon \iff n\ln|x| < \ln\varepsilon \iff n > \dfrac{\ln\varepsilon}{\ln|x|}$ (se invierte la desigualdad porque $\ln|x| < 0$). Se elige $N$ con Arquímedes.
- **$\sqrt[n]{p} \to 1$** (si $p > 1$). Con $x_n = \sqrt[n]{p} - 1 > 0$, la desigualdad de Bernoulli da $p = (1 + x_n)^n \ge 1 + n x_n$, luego $0 < x_n \le \tfrac{p - 1}{n} \to 0$. Para $p = 1$ es trivial y para $0 < p < 1$ se toman recíprocos.
- **$\sqrt[n]{n} \to 1$.** Con $x_n = \sqrt[n]{n} - 1 \ge 0$, el teorema del binomio da $n = (1 + x_n)^n \ge \tfrac{n(n - 1)}{2}x_n^2$, y así $0 \le x_n \le \sqrt{\tfrac{2}{n - 1}} \to 0$.

> [!warning] Los extremos deben coincidir
> Si las dos cotas tienen límites **distintos**, el sándwich no concluye nada. Y la acotación debe valer para $n$ grande, no solo para algunos valores.

## Preguntas de repaso

> [!question]- ¿Por qué $\frac{\cos(n)}{n^2} \to 0$ aunque $\cos(n)$ no converja?
> Porque $\cos(n)$ está acotado por $1$ y $\frac{1}{n^2} \to 0$: el producto de una sucesión nula por una acotada es nula (o, con sándwich, $-\frac{1}{n^2} \le \frac{\cos n}{n^2} \le \frac{1}{n^2}$).

> [!question]- ¿Qué desigualdad se usa para acotar $\frac{\ln n}{n}$ y por qué sirve?
> $\ln x \le x - 1 < x$ aplicada a $\sqrt{n}$: da $\ln n \le 2\sqrt{n}$, y por tanto $\frac{\ln n}{n} \le \frac{2}{\sqrt{n}} \to 0$.

> [!question]- ¿Cómo se acota $\frac{n!}{n^n}$ para el sándwich?
> Es un producto de $n$ factores $\frac{k}{n} \le 1$, el primero igual a $\frac{1}{n}$; entonces $0 < \frac{n!}{n^n} \le \frac{1}{n}$.

> [!question]- ¿Qué límite tiene $\sqrt[n]{5}$ y cómo se prueba?
> $1$: con $x_n = \sqrt[n]{5} - 1$ y Bernoulli, $5 \ge 1 + n x_n$ y $0 < x_n \le \frac{4}{n}$.
