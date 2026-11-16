---
ramo: "Introducción al Cálculo"
tema: "Sucesiones, monotonía y axioma del supremo"
tags:
  - intro-calculo/sucesiones
  - origen/complemento
prerrequisitos:
  - "[[02 - Sucesiones acotadas y monótonas]]"
  - "[[03 - Vecindades e intervalos con valor absoluto]]"
---

# Cotas, supremo e ínfimo

Un conjunto de números puede tener un elemento más grande (máximo) o no tenerlo, y aun así "terminar" en un número bien definido. El **supremo** captura esa idea: es la menor de las cotas superiores. Sin esta noción no se puede enunciar el último axioma de los reales, que es el que garantiza que no haya "huecos" en la recta.

## Definiciones

Sea $A \subseteq \mathbb{R}$.

> [!tip] Cotas
> - $a$ es **cota superior** de $A$ si $x \le a$ para todo $x \in A$; **cota inferior** si $a \le x$ para todo $x \in A$.
> - $A$ es **acotado superiormente** si tiene una cota superior, **acotado inferiormente** si tiene una cota inferior y **acotado** si tiene ambas.

> [!tip] Supremo, ínfimo, máximo y mínimo
> - **Supremo** de $A$: la **menor cota superior** (es cota superior y es menor o igual que toda otra cota superior). Se escribe $\sup A$.
> - **Ínfimo** de $A$: la **mayor cota inferior**, $\inf A$.
> - **Máximo** de $A$: el supremo, si pertenece a $A$. **Mínimo**: el ínfimo, si pertenece a $A$.

## Ejemplos

- $A = \{-\tfrac{1}{3}, -1, 0\}$: $0$ y $2$ son cotas superiores (no así $-1$); $-1$ y $-8$ son cotas inferiores. $\inf A = \min A = -1$ y $\sup A = \max A = 0$.
- $\sup\,]{-\infty}, 2[\, = 2$ pero **no hay máximo**: $2$ no pertenece al conjunto. Lo mismo para $\sup\,[-2, 2[\, = 2$.
- $\sup [-2, 2] = \max [-2, 2] = 2$ y $\inf\,]2, \infty[\, = 2$ sin mínimo.
- $\mathbb{N}$ está acotado inferiormente (por $1$) pero no superiormente; $\mathbb{Z}$ y $\mathbb{Q}$ no están acotados ni superior ni inferiormente.

## Unicidad

> [!tip] El supremo es único
> Si $a$ y $b$ son supremos de $A$, entonces $a = b$.

*Demostración.* Como $a$ es la menor cota superior y $b$ es cota superior, $a \le b$. Simétricamente, $b \le a$. Luego $a = b$. $\blacksquare$ (Análogo para ínfimo, máximo y mínimo.)

## Caracterización con $\varepsilon$

La definición se usa poco en la práctica; lo que sirve para **demostrar** que un número es el supremo es esta equivalencia:

> [!tip] Caracterización del supremo
> $\sup A = a \iff$ (i) $x \le a$ para todo $x \in A$ y (ii) para todo $\varepsilon > 0$ existe $x \in A$ con $x > a - \varepsilon$.
> Del mismo modo, $\inf A = a \iff$ (i) $a \le x$ para todo $x \in A$ y (ii) para todo $\varepsilon > 0$ existe $x \in A$ con $x < a + \varepsilon$.

La parte (i) dice que $a$ es cota superior; la (ii) que **ningún número menor que $a$ es cota superior**: siempre hay un elemento de $A$ más cerca de $a$ que cualquier margen $\varepsilon$.

**Ejemplo: $\sup\,]{-\infty}, 2[\, = 2$.** (i) Todo $x < 2$ cumple $x \le 2$. (ii) Dado $\varepsilon > 0$, el número $x = 2 - \tfrac{\varepsilon}{2}$ pertenece al conjunto y cumple $x > 2 - \varepsilon$. Por la caracterización, el supremo es $2$.

**Ejemplo: $A = \left\{\tfrac{n}{n + 1} : n \in \mathbb{N}\right\}$.** Los términos son $\tfrac{1}{2}, \tfrac{2}{3}, \tfrac{3}{4}, \ldots$ y siempre cumplen $\tfrac{n}{n + 1} < 1$, de modo que $1$ es cota superior. Dado $\varepsilon > 0$, hay $n$ con $\tfrac{1}{n + 1} < \varepsilon$ (propiedad arquimediana), y entonces $\tfrac{n}{n + 1} = 1 - \tfrac{1}{n + 1} > 1 - \varepsilon$. Luego $\sup A = 1$, que no pertenece a $A$ (no hay máximo), y $\inf A = \min A = \tfrac{1}{2}$.

> [!warning] Supremo no es lo mismo que máximo
> El conjunto $]0, 1[$ tiene supremo $1$ e ínfimo $0$, pero ni máximo ni mínimo. Que el supremo exista no obliga a que pertenezca al conjunto.

## Preguntas de repaso

> [!question]- ¿Cuál es el supremo y el ínfimo de $[0, 1[$? ¿Tiene máximo o mínimo?
> $\sup = 1$ y $\inf = 0$. Tiene mínimo ($0 \in A$) pero no máximo ($1 \notin A$).

> [!question]- ¿Por qué $\sup A = a$ exige que $a - \varepsilon$ **no** sea cota superior?
> Porque $a$ es la **menor** cota superior: si $a - \varepsilon$ también lo fuera, habría una cota menor que $a$.

> [!question]- Halle el supremo de $\{1 - \tfrac{1}{n} : n \in \mathbb{N}\}$.
> Es $1$: $1 - \frac{1}{n} < 1$ y, por Arquímedes, para todo $\varepsilon > 0$ hay $n$ con $\frac{1}{n} < \varepsilon$, o sea $1 - \frac{1}{n} > 1 - \varepsilon$.

> [!question]- ¿Puede un conjunto tener dos supremos distintos?
> No: si $a$ y $b$ son supremos, cada uno es cota superior y a la vez la menor, así que $a \le b$ y $b \le a$.
