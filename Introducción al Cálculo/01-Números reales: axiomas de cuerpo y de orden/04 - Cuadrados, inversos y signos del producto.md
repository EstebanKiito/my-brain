---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - origen/complemento
prerrequisitos:
  - "[[03 - Axiomas de orden y números positivos]]"
---

# Cuadrados, inversos y signos del producto

Los cuatro axiomas de orden bastan para demostrar los hechos que más se usan al trabajar con desigualdades: un cuadrado nunca es negativo, el inverso de un positivo es positivo, el signo de un producto y cómo se comportan los cuadrados con el orden. Casi toda desigualdad de la guía termina apoyándose en alguno de estos resultados.

## El teorema de los cuadrados y los inversos

> [!tip] Teorema
> 1. Para todo $a \in \mathbb{R}$, $a^2 \ge 0$.
> 2. Si $a > 0$, entonces $a^{-1} > 0$.
> 3. Si $a < 0$, entonces $a^{-1} < 0$.
> 4. $ab > 0 \iff (a > 0 \wedge b > 0) \vee (a < 0 \wedge b < 0)$.

*Demostración de 1.* Por tricotomía hay tres casos. Si $a > 0$, el producto de positivos es positivo: $a \cdot a > 0$. Si $a = 0$, $a^2 = 0 \ge 0$. Si $a < 0$, entonces $-a > 0$ y $(-a)(-a) = a^2 > 0$. En los tres casos, $a^2 \ge 0$.

*Demostración de 2, por contradicción.* Sea $a > 0$ y supóngase $a^{-1} < 0$. Como $a \neq 0$, por (1) $a^2 > 0$ (el caso $a^2 = 0$ ocurre solo si $a = 0$). Multiplicar $a^{-1} < 0$ por el positivo $a^2$ da $a^2 \cdot a^{-1} < 0$, o sea $a < 0$, lo que contradice $a > 0$. La parte 3 es análoga.

*Demostración de 4.* Si $ab > 0$, entonces $a \neq 0$ y $b \neq 0$. Si $a > 0$, también $a^{-1} > 0$ y $ab \cdot a^{-1} = b > 0$; si $a < 0$, $a^{-1} < 0$ y $ab \cdot a^{-1} = b < 0$. Recíprocamente, dos positivos dan producto positivo por cerradura, y dos negativos también: $(-a)(-b) = ab$ con $-a, -b > 0$.

> [!warning] Multiplicar por un negativo invierte el orden
> Si $x < y$ y $z < 0$, entonces $xz > yz$. Se deduce de O4 aplicado a $-z > 0$: $x(-z) < y(-z)$, y luego se suma $xz + yz$ a ambos lados. Olvidarlo es el error más frecuente al resolver inecuaciones.

## Cuadrados y orden

> [!tip] Elevar al cuadrado conserva el orden entre positivos
> Si $0 < a < b$, entonces $a^2 < b^2$.

Se prueba con la diferencia: $b - a > 0$ y $a + b > 0$ (suma de positivos), así que $(b - a)(a + b) = b^2 - a^2 > 0$.

> [!warning] Solo entre positivos
> Con negativos el orden se invierte: $-3 < -2$ pero $9 > 4$. Y sin signo conocido no hay conclusión: $-3 < 2$ y $9 > 4$. Por eso "elevar al cuadrado ambos lados" requiere que los dos lados sean $\ge 0$.

## Inversos y orden

Si $0 < a < b$, entonces $b^{-1} < a^{-1}$. Se calcula $a^{-1} - b^{-1} = (b - a)\,a^{-1} b^{-1}$: es un producto de tres positivos, así que es positivo. Tomar inverso **invierte** el orden entre positivos.

## Preguntas de repaso

> [!question]- ¿Por qué no existe $x \in \mathbb{R}$ con $x^2 + 1 = 0$?
> Porque $x^2 \ge 0$ para todo real, luego $x^2 + 1 \ge 1 > 0$. Ninguna $x$ puede anular la expresión.

> [!question]- ¿Por qué $ab > 0$ obliga a que $a$ y $b$ tengan el mismo signo?
> Si fueran de signos distintos, uno positivo y otro negativo, por la parte 4 el producto sería negativo; y si alguno fuera $0$ el producto sería $0$, no positivo.

> [!question]- Si $0 < a < b$, ¿qué ocurre con $a^{-1}$ y $b^{-1}$, y cómo se prueba?
> $b^{-1} < a^{-1}$. Se prueba viendo que $a^{-1} - b^{-1} = (b - a)a^{-1}b^{-1}$ es producto de positivos (hipótesis $b - a > 0$ y la parte 2 del teorema), luego positivo.

> [!question]- ¿Es cierto que $a < b \Rightarrow a^2 < b^2$ para todos los reales?
> No. Solo si $0 < a < b$. Contraejemplo: $a = -3$, $b = 2$: $a < b$, pero $a^2 = 9 > 4 = b^2$.
