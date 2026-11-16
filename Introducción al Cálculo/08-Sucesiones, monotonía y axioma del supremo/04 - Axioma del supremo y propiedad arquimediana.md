---
ramo: "Introducción al Cálculo"
tema: "Sucesiones, monotonía y axioma del supremo"
tags:
  - intro-calculo/sucesiones
  - origen/complemento
prerrequisitos:
  - "[[03 - Cotas, supremo e ínfimo]]"
---

# Axioma del supremo y propiedad arquimediana

Los axiomas de cuerpo y de orden también los cumplen los racionales, y aun así $\mathbb{Q}$ tiene "huecos" (como $\sqrt{2}$). Lo que distingue a $\mathbb{R}$ es un último axioma, el del supremo o de **completitud**. De él salen resultados que hasta ahora se usaban sin demostración, como que los naturales no están acotados o que entre dos reales siempre hay un racional.

## El axioma

> [!tip] Axioma del supremo
> Todo conjunto de números reales **no vacío y acotado superiormente** tiene un supremo en $\mathbb{R}$.

Es falso en $\mathbb{Q}$: el conjunto $\{q \in \mathbb{Q} : q^2 < 2\}$ está acotado superiormente por $2$, pero ninguna cota superior racional es la menor (la menor sería $\sqrt{2}$, que no es racional). En $\mathbb{R}$ ese hueco está lleno.

> [!tip] Versión para ínfimos
> Todo conjunto no vacío y **acotado inferiormente** tiene un ínfimo.

*Demostración.* Si $A$ es acotado inferiormente por $a$, el conjunto $B = \{-x : x \in A\}$ no es vacío y está acotado superiormente por $-a$. Por el axioma, $B$ tiene un supremo $b$, y $-b$ es el ínfimo de $A$: es cota inferior de $A$ porque $b$ es cota superior de $B$, y es la mayor porque si $c$ es otra cota inferior de $A$, entonces $-c$ es cota superior de $B$ y por tanto $b \le -c$, es decir $c \le -b$. $\blacksquare$

## Propiedad arquimediana

> [!tip] Consecuencias del axioma del supremo
> 1. **Propiedad arquimediana:** para todo $x > 0$ y todo $y > 0$ existe $n \in \mathbb{N}$ con $nx > y$.
> 2. $\mathbb{N}$ no está acotado superiormente: para todo $x \in \mathbb{R}$ existe $n \in \mathbb{N}$ con $n > x$.
> 3. Para todo $x > 0$ existe $n \in \mathbb{N}$ con $\tfrac{1}{n} < x$.
> 4. Para todo $x \in \mathbb{R}$ existe un único entero $p$ con $p \le x < p + 1$ (la parte entera).
> 5. **$\mathbb{Q}$ es denso en $\mathbb{R}$:** si $x < y$ existe $q \in \mathbb{Q}$ con $x < q < y$.

*Demostración de 1, por contradicción.* Si no fuera cierto, existirían $x, y > 0$ con $nx \le y$ para todo $n$. El conjunto $A = \{nx : n \in \mathbb{N}\}$ es no vacío y acotado superiormente por $y$, así que tiene supremo $a$. Como $a - x < a$ no es cota superior, existe $n$ con $a - x < nx$, o sea $a < (n + 1)x$; pero $(n + 1)x \in A$, lo que contradice que $a$ sea cota superior. $\blacksquare$

Los puntos 2 y 3 son el caso $x = 1$ (o $y = 1$): si $x > 0$, hay $n$ con $n \cdot 1 > x$, y hay $n$ con $n \cdot x > 1$, es decir $\tfrac{1}{n} < x$. El 3 es el que se usa a diario: **siempre hay un $\tfrac{1}{n}$ más pequeño que cualquier margen $\varepsilon > 0$**.

*Idea de 5.* Si $x < y$, se toma $n$ con $\tfrac{1}{n} < y - x$ y el racional $q = \tfrac{p}{n}$ donde $p$ es la parte entera de $nx + 1$: queda $x < q < y$.

## Dónde se usa

- **$e^x > 0$** para $x \le -1$ (nota de la exponencial): se elige $n$ con $-x < n$ (punto 2), y así $1 + \tfrac{x}{n} > 0$.
- **Límites:** para probar que $\tfrac{1}{n} \to 0$ se toma $n > \tfrac{1}{\varepsilon}$ (punto 3); es el paso inicial de casi toda demostración con la definición de límite.
- **Supremos de conjuntos como $\{1 - \tfrac{1}{n}\}$:** el punto 3 muestra que el supremo es $1$.
- **Existencia de raíces:** la raíz cuadrada de $2$ se construye como $\sup\{x > 0 : x^2 < 2\}$, y el axioma garantiza que existe.

> [!warning] Por qué los racionales no bastan
> En $\mathbb{Q}$ vale la propiedad arquimediana, pero **no** el axioma del supremo. Esta distinción es la que hace posible que una sucesión monótona y acotada de racionales converja a un número que no es racional (como las aproximaciones decimales de $\sqrt{2}$).

## Preguntas de repaso

> [!question]- ¿Qué diferencia a $\mathbb{R}$ de $\mathbb{Q}$ en cuanto a los axiomas?
> $\mathbb{R}$ cumple el axioma del supremo; $\mathbb{Q}$ no. Por ejemplo, $\{q \in \mathbb{Q} : q^2 < 2\}$ está acotado superiormente pero no tiene supremo racional.

> [!question]- ¿Cómo se usa la propiedad arquimediana para encontrar $n$ con $\frac{1}{n} < 0{,}001$?
> Se toma cualquier $n > 1000$ (existe porque $\mathbb{N}$ no está acotado): entonces $\frac{1}{n} < 0{,}001$.

> [!question]- ¿Por qué un conjunto no vacío acotado inferiormente tiene ínfimo?
> Se refleja el conjunto ($B = \{-x\}$), se aplica el axioma del supremo a $B$ y el opuesto de ese supremo es el ínfimo de $A$.

> [!question]- Dé un racional entre $\sqrt{2}$ y $\sqrt{2} + 0{,}01$.
> Por densidad existe; por ejemplo $1{,}415$ (pues $\sqrt{2} \approx 1{,}4142$).
