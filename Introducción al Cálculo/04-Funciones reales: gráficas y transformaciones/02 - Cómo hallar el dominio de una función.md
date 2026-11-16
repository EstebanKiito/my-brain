---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones, dominio, recorrido y gráfico]]"
  - "[[03 - Inecuaciones racionales y restricciones]]"
---

# Cómo hallar el dominio de una función

Cuando una función se da solo con su fórmula, el **dominio** es el mayor conjunto de reales donde la fórmula tiene sentido. Encontrarlo es identificar las operaciones que pueden fallar y resolver las inecuaciones que las controlan. Es la aplicación más directa de todo el tema de inecuaciones.

## Qué puede fallar

> [!tip] Convención del dominio maximal
> Si $y = f(x)$ se da por una regla, $\operatorname{Dom}(f) = \{x \in \mathbb{R} \mid f(x) \in \mathbb{R}\}$. Las únicas restricciones habituales son:
> - un **denominador** no puede ser cero;
> - bajo una **raíz de índice par** el radicando debe ser $\ge 0$;
> - (más adelante) el argumento de un logaritmo debe ser positivo.

Cada restricción es una condición sobre $x$; el dominio es la **intersección** de todas, porque se piden a la vez. Si hay raíces dentro de raíces, se exige la condición de cada raíz, de adentro hacia afuera.

## Ejemplos de la clase

- $f(x) = \dfrac{x}{x^2 - 1}$: solo falla si $x^2 - 1 = 0$, es decir $x = \pm 1$. $\operatorname{Dom}(f) = \mathbb{R} \setminus \{-1, 1\}$.
- $f(x) = \sqrt{x}$: $\operatorname{Dom}(f) = [0, \infty)$.
- $f(x) = \sqrt{\dfrac{2x - 3}{x^2 - 1}}$: se necesita $\dfrac{2x - 3}{x^2 - 1} \ge 0$ y $x \neq \pm 1$. Con puntos críticos $-1$, $1$ y $\tfrac{3}{2}$, el cociente es positivo en $(-1, 1)$ y en $\left(\tfrac{3}{2}, \infty\right)$, y vale $0$ en $\tfrac{3}{2}$. $\operatorname{Dom}(f) = (-1, 1) \cup \left[\tfrac{3}{2}, \infty\right)$.

## Cuando un radicando no es sencillo

> [!tip] Un radicando siempre positivo
> Si el radicando es un cuadrado más un número positivo, no impone restricción. Por ejemplo, en $\sqrt{x^2 + 2}$ o en $\dfrac{x}{x^2 + 1}$ el interior no se anula ni es negativo para ningún real: el dominio es $\mathbb{R}$.

**Raíces anidadas.** Para $f(x) = \sqrt{\sqrt{1 - 2x} + \sqrt{\dfrac{x}{x^2 + 1}}}$ se exigen las dos raíces interiores: $1 - 2x \ge 0$ ($x \le \tfrac{1}{2}$) y $\dfrac{x}{x^2 + 1} \ge 0$ ($x \ge 0$, porque $x^2 + 1 > 0$). Su intersección es $\left[0, \tfrac{1}{2}\right]$. Y en ese conjunto el radicando exterior es una suma de dos números $\ge 0$, luego la raíz exterior no añade restricción: $\operatorname{Dom}(f) = \left[0, \tfrac{1}{2}\right]$.

**Valor absoluto y raíz.** $f(x) = \dfrac{\sqrt{|x| - 4}}{x^2 - 16}$ pide $|x| - 4 \ge 0$ (o sea $x \le -4$ ó $x \ge 4$) y $x^2 \neq 16$ (o sea $x \neq \pm 4$). Intersectando, $\operatorname{Dom}(f) = (-\infty, -4) \cup (4, \infty)$.

**Con un parámetro.** Para $f(x) = \sqrt{x^2 + 2x + a}$, completando cuadrados queda $(x + 1)^2 + (a - 1)$. Si $a \ge 1$ el radicando es siempre $\ge 0$ y $\operatorname{Dom}(f) = \mathbb{R}$. Si $a < 1$, el radicando se anula en $x = -1 \pm \sqrt{1 - a}$ y es no negativo fuera del intervalo entre esas raíces: $\operatorname{Dom}(f) = \left(-\infty, -1 - \sqrt{1 - a}\right] \cup \left[-1 + \sqrt{1 - a}, \infty\right)$. El dominio depende del valor de $a$.

## Dominio de una función definida por tramos

Si $f$ se define por tramos, el dominio es la **unión** de los tramos donde se aplica una fórmula (cada tramo con su propia restricción). Por ejemplo, $f(x) = \begin{cases} x^3 & -1 \le x \le 1 \\ -x^2 + 2 & 1 < x < 2 \\ x - 1 & 2 < x \le 4 \end{cases}$ tiene dominio $[-1, 2) \cup (2, 4]$: el punto $x = 2$ no está asignado.

> [!warning] Dos errores frecuentes
> - Olvidar una de las condiciones y quedarse con una sola.
> - Simplificar antes de hallar el dominio: el dominio de $\frac{(x - 1)(x + 2)}{x - 1}$ se calcula con la expresión **original** (excluye $x = 1$), aunque luego se simplifique.

## Preguntas de repaso

> [!question]- ¿Cómo se combinan varias restricciones sobre $x$?
> Con la intersección: el dominio es el conjunto de $x$ que cumplen todas las condiciones a la vez.

> [!question]- ¿Por qué $\sqrt{x^2 + 1}$ no impone restricciones?
> Porque $x^2 + 1 \ge 1 > 0$ para todo real: el radicando nunca es negativo.

> [!question]- Halle el dominio de $\dfrac{1}{\sqrt{x - 2}}$.
> Se necesita $x - 2 \ge 0$ por la raíz y $\sqrt{x - 2} \neq 0$ por el denominador, es decir $x - 2 > 0$: $\operatorname{Dom} = (2, \infty)$.

> [!question]- ¿Cómo se encuentra el dominio de $\sqrt{x^2 + 2x + a}$ según $a$?
> Se completa el cuadrado: $(x + 1)^2 + (a - 1)$. Para $a \ge 1$, todo $\mathbb{R}$; para $a < 1$, fuera del intervalo abierto entre las raíces $-1 \pm \sqrt{1 - a}$.
