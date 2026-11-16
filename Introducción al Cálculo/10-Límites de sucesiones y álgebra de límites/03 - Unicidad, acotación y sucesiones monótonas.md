---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de límite de una sucesión]]"
  - "[[02 - Sucesiones acotadas y monótonas]]"
---

# Unicidad, acotación y sucesiones monótonas

Tres propiedades estructurales de las sucesiones convergentes: el límite es **único**, la sucesión está **acotada** y, a la inversa, una sucesión **monótona y acotada** siempre converge. Esta última es la que permite demostrar que existe un límite sin conocerlo de antemano, y se usa en toda recurrencia.

## El límite es único

> [!tip] Unicidad
> Una sucesión no puede converger a dos límites distintos.

*Demostración.* Sea $\lim a_n = L$ y sea $M \neq L$. Se elige $\varepsilon > 0$ (por ejemplo, $\varepsilon = \tfrac{|L - M|}{2}$) de modo que las vecindades $I = (L - \varepsilon, L + \varepsilon)$ y $J = (M - \varepsilon, M + \varepsilon)$ sean disjuntas. Existe $N$ tal que $a_n \in I$ para $n > N$, y por tanto $a_n \notin J$ para esos $n$: no se cumple que $\lim a_n = M$. $\blacksquare$

Gracias a esto tiene sentido escribir "**el** límite" de una sucesión convergente.

![Unicidad del límite con dos franjas disjuntas](adjuntos/Unicidad%20del%20l%C3%ADmite%20con%20dos%20franjas%20disjuntas.png)

> [!example]- Transcripción de la figura (cuaderno, clase 26)
> Dos rectas, $y = L_1$ (roja) y $y = L_2$ (morada), cada una con su franja de radio $\varepsilon$. Los puntos de la sucesión entran en la franja de $L_1$ y quedan allí; la franja de $L_2$ (gris) queda vacía a partir de ese índice, así que $L_2$ no puede ser límite.

## Convergente implica acotada

> [!tip] Convergentes son acotadas
> Si $\{a_n\}$ converge, entonces existe $M > 0$ con $|a_n| \le M$ para todo $n$.

*Demostración.* Sea $\lim a_n = L$. Con $\varepsilon = 1$ existe $N$ tal que $a_n \in (L - 1, L + 1)$ para $n > N$. El conjunto finito $\{a_1, \ldots, a_N, L - 1, L + 1\}$ tiene un menor elemento $a$ y un mayor $b$, y todos los términos están en $[a, b]$. $\blacksquare$

Su contrarrecíproca da un criterio de divergencia: **una sucesión no acotada es divergente**. Así, $a_n = n$ y $a_n = n^2$ divergen (crecen sin cota, sus términos no se acumulan en torno a un número fijo). El recíproco es falso: $a_n = (-1)^n$ está acotada ($|a_n| = 1$) y diverge, porque salta entre $-1$ y $1$.

**Ejemplo.** $b_n = \tfrac{n}{n + 1}$ está acotada, pues $n < n + 1$ da $|b_n| < 1$ (y converge a $1$).

![Sucesión convergente encerrada entre menos K y K](adjuntos/Sucesi%C3%B3n%20convergente%20encerrada%20entre%20menos%20K%20y%20K.png)

> [!example]- Transcripción de la figura (cuaderno, clase 25)
> Una sucesión creciente que se acerca a la recta morada $y = L$ y queda toda entre las rectas rojas $y = K$ e $y = -K$: una sucesión convergente está acotada.

## Un límite no preserva la desigualdad estricta, pero sí la no estricta

> [!tip] Signo del límite
> Si $a_n \ge 0$ para todo $n$ y $\{a_n\}$ converge, entonces $\lim a_n \ge 0$.

*Demostración (I7, 2024-1).* Sea $L = \lim a_n$ y supóngase $L < 0$. Con $\varepsilon = -L > 0$ existe $N$ tal que, para $n > N$, $|a_n - L| < -L$, es decir $2L < a_n < 0$: términos negativos, lo que contradice $a_n \ge 0$. Luego $L \ge 0$. $\blacksquare$

Con $a_n > 0$ el límite puede ser $0$ (por ejemplo, $\tfrac{1}{n} > 0$ y su límite es $0$): la desigualdad estricta **no** se conserva.

## Sucesiones monótonas y acotadas

> [!tip] Teorema de la sucesión monótona
> Toda sucesión **monótona y acotada** es convergente. Si $\{a_n\}$ es creciente y acotada superiormente, converge a $\sup\{a_n\}$; si es decreciente y acotada inferiormente, converge a $\inf\{a_n\}$.

*Demostración (caso creciente).* El conjunto $A = \{a_n : n \in \mathbb{N}\}$ es no vacío y acotado superiormente, así que por el axioma del supremo existe $L = \sup A$. Dado $\varepsilon > 0$, $L - \varepsilon$ no es cota superior: existe $N$ con $a_N > L - \varepsilon$. Como la sucesión es creciente, para $n > N$ vale $L - \varepsilon < a_N \le a_n \le L$, y por tanto $|a_n - L| < \varepsilon$. $\blacksquare$

![Sucesión creciente y acotada que converge](adjuntos/Sucesi%C3%B3n%20creciente%20y%20acotada%20que%20converge.png)

> [!example]- Transcripción de la figura (cuaderno, clase 24)
> Puntos azules que suben y se aplanan hacia una recta verde $y = L$, siempre entre $y = K$ y $y = -K$; a partir de cierto índice quedan dentro de la franja alrededor de $L$. Es la idea del teorema: monótona y acotada implica convergente.

La idea es que una sucesión que sube sin pasarse de una cota "se va a aproximar a la menor de las cotas superiores". El teorema **no dice** cuánto vale el límite, solo que existe; para calcularlo se usa la ecuación del punto fijo (tema 11).

> [!warning] Las dos hipótesis son necesarias
> - Creciente **no** acotada: $a_n = n$ diverge a $+\infty$.
> - Acotada **no** monótona: $a_n = (-1)^n$ no converge.
> Las pruebas puntúan por separado la monotonía y la cota.

## Preguntas de repaso

> [!question]- ¿Por qué la unicidad del límite justifica escribir $\lim a_n = L$?
> Porque si una sucesión convergiera a dos números distintos la notación sería ambigua; el teorema asegura que, si converge, lo hace a un único valor.

> [!question]- ¿Es acotada $a_n = \frac{n^2}{n + 1}$? ¿Converge?
> No es acotada (para $n$ grande, $a_n > n - 1$), así que diverge.

> [!question]- ¿Qué pasa con una sucesión de términos positivos cuyo límite es $0$?
> Ejemplo: $\frac{1}{n}$. El límite no es positivo: la desigualdad estricta no se conserva en el límite; solo se conserva $\ge$.

> [!question]- ¿A qué converge una sucesión creciente y acotada superiormente?
> A su supremo: la menor de sus cotas superiores.
