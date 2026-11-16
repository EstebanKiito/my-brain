---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de valor absoluto y distancia]]"
---

# Propiedades del valor absoluto y desigualdad triangular

Como el valor absoluto se define con desigualdades, todas sus propiedades se demuestran desde los axiomas de orden. La más importante es la desigualdad triangular, que acota la suma de dos números en valor absoluto y que reaparece en inecuaciones, en demostraciones con $\varepsilon$ y en límites.

## El teorema

> [!tip] Propiedades
> Para $x, y \in \mathbb{R}$ y $a \ge 0$:
> 1. $|x| \ge 0$.
> 2. $-|x| \le x \le |x|$.
> 3. $|xy| = |x|\,|y|$.
> 4. $|x| \le a \iff -a \le x \le a$.
> 5. $|x| \ge a \iff x \le -a \ \text{ó}\ x \ge a$.
> 6. $|x + y| \le |x| + |y|$ (**desigualdad triangular**).

Las propiedades 4 y 5 son las que traducen cada inecuación con valor absoluto a inecuaciones sin él; se usan casi en cada ejercicio de las notas siguientes. La 3 se prueba por casos de signo, y la 2 se obtiene de la 1 y de la definición.

## Demostración de la desigualdad triangular

Se usa $|t|^2 = t^2$. Entonces
$$|x + y|^2 = (x + y)^2 = x^2 + 2xy + y^2 = |x|^2 + 2xy + |y|^2.$$
Por la propiedad 2, $xy \le |xy| = |x||y|$, y por orden $2xy \le 2|x||y|$. Reemplazando,
$$|x + y|^2 \le |x|^2 + 2|x||y| + |y|^2 = (|x| + |y|)^2.$$
Como ambos números $|x + y|$ y $|x| + |y|$ son $\ge 0$, tomar raíz cuadrada conserva el orden (ver [[05 - Raíces cuadradas y valor absoluto|raíces cuadradas]]) y queda $|x + y| \le |x| + |y|$. $\blacksquare$

## Triangular inversa y caso de igualdad

> [!tip] Desigualdad triangular inversa
> Para todo $x, y$: $\big|\,|x| - |y|\,\big| \le |x - y|$.

*Demostración.* Escribiendo $x = (x - y) + y$ y usando la triangular, $|x| \le |x - y| + |y|$, es decir $|x| - |y| \le |x - y|$. Intercambiando los papeles, $|y| - |x| \le |y - x| = |x - y|$. Las dos cotas dicen que $|x| - |y|$ y su opuesto son $\le |x - y|$; por la propiedad 4, $\big||x| - |y|\big| \le |x - y|$.

> [!tip] ¿Cuándo vale la igualdad $|x + y| = |x| + |y|$?
> Si y solo si $xy \ge 0$ (ambos del mismo signo, o alguno nulo). En la demostración, la igualdad $xy = |xy|$ ocurre justamente cuando $xy \ge 0$; en cualquier otro caso la desigualdad es estricta.

Por ejemplo, $|3 + 5| = 3 + 5$ pero $|3 + (-5)| = 2 < 8 = |3| + |-5|$.

> [!warning] Dos errores clásicos
> No es cierto que $|x + y| = |x| + |y|$ en general, ni que $|x - y| = |x| - |y|$. Lo que sí vale es la triangular (una desigualdad) y la triangular inversa.

## Preguntas de repaso

> [!question]- ¿Cómo se usa la propiedad 4 para resolver $|2x - 1| \le 3$?
> Se traduce a $-3 \le 2x - 1 \le 3$, de donde $-2 \le 2x \le 4$ y $x \in [-1, 2]$.

> [!question]- ¿Qué da la propiedad 5 para $|x| \ge 2$?
> $x \le -2$ ó $x \ge 2$: los números a distancia al menos $2$ del origen, es decir, el exterior del intervalo $(-2, 2)$.

> [!question]- ¿Por qué se puede elevar al cuadrado $|x + y| \le |x| + |y|$ en la demostración?
> Se parte de que $|x + y|^2 \le (|x| + |y|)^2$ y, como ambos números son no negativos, se concluye la desigualdad original por la monotonía de la raíz entre no negativos.

> [!question]- ¿En qué casos es estricta la desigualdad triangular?
> Cuando $xy < 0$, es decir, cuando $x$ e $y$ tienen signos opuestos; si $xy \ge 0$ vale la igualdad.
