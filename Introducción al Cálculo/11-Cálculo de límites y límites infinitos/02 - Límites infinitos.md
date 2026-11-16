---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[04 - Álgebra de límites y cocientes de polinomios]]"
  - "[[05 - Teorema del sándwich y límites por acotación]]"
---

# Límites infinitos

Una sucesión puede diverger de varias maneras. Algunas simplemente oscilan ($(-1)^n$), pero otras **crecen sin cota** o **decrecen sin cota**, y en esos casos se dice que su límite es $+\infty$ o $-\infty$. Estos límites no son números, pero se manejan con reglas propias y completan el panorama de los cálculos de límites.

## Definición

> [!tip] Límite infinito
> - $\displaystyle\lim_{n \to \infty} a_n = +\infty$ si para todo $A > 0$ existe $N \in \mathbb{N}$ tal que $n > N \Rightarrow a_n > A$.
> - $\displaystyle\lim_{n \to \infty} a_n = -\infty$ si para todo $A > 0$ existe $N$ tal que $n > N \Rightarrow a_n < -A$.

$+\infty$ y $-\infty$ **no son números**: una sucesión que tiende a $\pm\infty$ **no es convergente** (sigue siendo divergente). Como $\lim a_n = +\infty \iff \lim(-a_n) = -\infty$, basta estudiar el primer caso.

![Sucesión que supera cualquier cota M](adjuntos/Sucesi%C3%B3n%20que%20supera%20cualquier%20cota%20M.png)

> [!example]- Transcripción de la figura (cuaderno, clase 28)
> Puntos azules que suben cada vez más. Una recta roja horizontal marca la altura $M$; desde el índice $m_0$ (flecha gris) todos los puntos quedan por encima de ella: $a_n > M$ para $n \ge m_0$.

> [!tip] Relación con la acotación
> - Si $\lim a_n = +\infty$, entonces $\{a_n\}$ **no** está acotada superiormente.
> - El recíproco es **falso**: $a_n = n + (-1)^n n$ no está acotada superiormente, pero no tiende a $+\infty$, porque $a_{2n-1} = 0$ para todo $n$.
> - Si $\{a_n\}$ es **creciente** y no acotada, entonces sí $\lim a_n = +\infty$.

## Ejemplos básicos

- $\lim n = +\infty$.
- $\lim e^n = +\infty$: por la desigualdad fundamental $e^n \ge 1 + n \ge n$.
- $\lim \ln n = +\infty$: la sucesión es creciente y no acotada (si $\ln n \le M$ para todo $n$, se tendría $n \le e^M$ para todo $n$, absurdo).
- $\lim \arctan(n) = \dfrac{\pi}{2}$: converge (es creciente y acotada por $\tfrac{\pi}{2}$), no es infinito.
- Si $x > 1$, $\lim x^n = +\infty$: con $b_n = \tfrac{1}{x^n} > 0$ y $b_n = (1/x)^n \to 0$, el teorema (parte 3, abajo) da $\tfrac{1}{b_n} = x^n \to +\infty$.

## Reglas con infinitos

> [!tip] Teorema
> 1. Si $\lim a_n = +\infty$ y $\{b_n\}$ está **acotada inferiormente**, entonces $\lim(a_n + b_n) = +\infty$.
> 2. Si $\lim a_n = +\infty$ y existe $c > 0$ con $b_n > c$ para todo $n$, entonces $\lim a_n b_n = +\infty$.
> 3. Si $a_n > c > 0$, $b_n > 0$ y $\lim b_n = 0$, entonces $\lim\dfrac{a_n}{b_n} = +\infty$.
> 4. Si $\{a_n\}$ está **acotada** y $\lim b_n = +\infty$, entonces $\lim\dfrac{a_n}{b_n} = 0$.

*Demostración de 1.* Sea $b_n \ge c$. Dado $A > 0$ existe $N$ con $a_n > A - c$ para $n > N$; entonces $a_n + b_n > A - c + c = A$.
*De 2.* Dado $A$, existe $N$ con $a_n > \tfrac{A}{c}$ para $n > N$, y $a_n b_n > \tfrac{A}{c}\cdot c = A$.
*De 3.* Dado $A$, existe $N$ con $b_n < \tfrac{c}{A}$ y así $\tfrac{a_n}{b_n} > \tfrac{c}{c/A} = A$.
*De 4.* Si $|a_n| \le c$ y $b_n > \tfrac{c}{\varepsilon}$ desde algún $N$, entonces $\left|\tfrac{a_n}{b_n}\right| < \varepsilon$.

## Cuidado: el recíproco de un infinitésimo no siempre es infinito

Si $\lim a_n = 0$ **no** se deduce $\lim\tfrac{1}{a_n} = +\infty$. Por ejemplo, $a_n = \tfrac{(-1)^n}{n} \to 0$, pero $\tfrac{1}{a_n} = (-1)^n n$ oscila entre valores muy grandes positivos y negativos: no diverge ni a $+\infty$ ni a $-\infty$. La regla 3 exige $b_n > 0$ (término a término).

## Dos ejemplos de pruebas

**Un cociente que diverge (I9, 2024-1).** Sea $\lim a_n = 1$. Demostrar que $\lim\dfrac{a_n}{\sqrt{n + 1} - \sqrt{n}} = +\infty$. Como $a_n \to 1$, existe $N$ con $a_n > \tfrac{1}{2}$ para $n > N$. Además $\dfrac{1}{\sqrt{n + 1} - \sqrt{n}} = \sqrt{n + 1} + \sqrt{n} > 2\sqrt{n}$ (racionalizando). Multiplicando, para $n > N$:
$$\frac{a_n}{\sqrt{n + 1} - \sqrt{n}} > \frac{1}{2}\cdot 2\sqrt{n} = \sqrt{n} \to +\infty,$$
y por comparación el cociente tiende a $+\infty$.

**Un logaritmo que cae (Examen, 2024-1).** $\lim\ln\!\left(\dfrac{3n}{e^{2n}}\right)$. Por las leyes del logaritmo, $\ln(3n) - \ln(e^{2n}) = \ln 3 + \ln n - 2n$. Como $\ln n \le n - 1$:
$$\ln 3 + \ln n - 2n \le \ln 3 - 1 - n \to -\infty,$$
así que el límite es $-\infty$.

> [!warning] Formas indeterminadas
> $\infty - \infty$, $\tfrac{\infty}{\infty}$, $0\cdot\infty$ y $1^\infty$ **no** tienen un valor fijo: dependen de las sucesiones. Cada una se resuelve con un truco (conjugado, dividir por la potencia dominante, el número $e$).

## Preguntas de repaso

> [!question]- ¿Es convergente una sucesión que tiende a $+\infty$?
> No. Convergente significa que tiene límite **real**; $+\infty$ no es un número, y la sucesión se llama divergente.

> [!question]- ¿Por qué $n + (-1)^n n$ no tiende a $+\infty$ aunque no esté acotada superiormente?
> Porque infinitos términos valen $0$ ($a_{2n-1} = 0$), así que no se mantiene sobre cualquier $A > 0$ desde algún $N$.

> [!question]- ¿A qué tiende $\frac{(-1)^n}{n^2 + n}$ y por qué sirve la regla 4?
> A $0$: el numerador está acotado por $1$ y el denominador tiende a $+\infty$.

> [!question]- ¿Cuál es el límite de $2^n - n^2$?
> $+\infty$: $2^n$ crece más rápido que $n^2$ (la razón $\frac{n^2}{2^n} \to 0$), así que $2^n - n^2 = 2^n(1 - \frac{n^2}{2^n}) \to +\infty$.
