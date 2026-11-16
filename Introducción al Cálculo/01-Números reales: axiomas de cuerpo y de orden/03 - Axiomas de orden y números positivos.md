---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - origen/complemento
prerrequisitos:
  - "[[02 - Consecuencias de los axiomas de cuerpo]]"
---

# Axiomas de orden y números positivos

La idea de que unos números son "más grandes" que otros también se axiomatiza. Agregando cuatro axiomas de orden a los de cuerpo se obtiene un **cuerpo ordenado**, que es lo que realmente es $\mathbb{R}$. El orden permite hablar de desigualdades, de signos y, más adelante, de intervalos y de límites.

## Los cuatro axiomas de orden

Aquí $a < b$ es una afirmación que puede ser verdadera o falsa.

> [!tip] Axiomas de orden
> - **O1. Tricotomía:** para $a, b$ se cumple una y solo una de: $a = b$, $a < b$, $b < a$.
> - **O2. Transitividad:** si $a < b$ y $b < c$, entonces $a < c$.
> - **O3. Monotonía de la suma:** si $a < b$, entonces $a + c < b + c$ para todo $c \in \mathbb{R}$.
> - **O4. Monotonía del producto:** si $a < b$ y $c > 0$, entonces $ac < bc$.

Las desigualdades no estrictas se definen a partir de estas: $a \le b$ significa $(a < b) \vee (a = b)$, y $a \ge b$ significa $(a > b) \vee (a = b)$.

## Los reales positivos

El conjunto $\mathbb{R}^+ = \{x \in \mathbb{R} \mid x > 0\}$ concentra toda la información del orden. Con él, "menor que" se reduce a una pregunta de signo.

> [!tip] Orden = positividad de la diferencia
> $a < b \iff b - a \in \mathbb{R}^+$.

En efecto, si $a < b$, sumar $-a$ a ambos lados (O3) da $0 < b - a$. Esta equivalencia es la herramienta central: para probar $a < b$ basta mostrar que $b - a$ es positivo.

> [!tip] $\mathbb{R}^+$ es cerrado
> Si $a, b \in \mathbb{R}^+$, entonces $a + b \in \mathbb{R}^+$ y $ab \in \mathbb{R}^+$.

*Demostración.* Suma: de $a > 0$ y O3 sale $a + b > 0 + b = b$; como $b > 0$, por transitividad $a + b > 0$. Producto: de $a > 0$ y $b > 0$, O4 aplicado a $0 < a$ con $c = b$ da $0 \cdot b < ab$, o sea $0 < ab$. $\blacksquare$

## Primer uso: desigualdades que se suman y multiplican

Con O2, O3 y O4 se justifican las manipulaciones habituales:

- **Sumar desigualdades:** si $x < y$ y $z < r$, entonces $x + z < y + z$ (O3), $y + z < y + r$ (O3 otra vez) y $x + z < y + r$ (O2).
- **Multiplicar desigualdades de positivos:** si $0 < x < y$ y $0 < w < z$, entonces $xw < yw$ (O4 con $w > 0$), $yw < yz$ (O4 con $y > 0$) y $xw < yz$ (O2).

> [!warning] Estas reglas no valen sin las hipótesis
> $-3 < -2$ y $-5 < -1$, pero $(-3)(-5) = 15 \not< 2 = (-2)(-1)$. Multiplicar desigualdades exige que los números sean positivos; sumarlas, en cambio, funciona siempre.

## Ejemplo: de $a < b$ y $c < d$ a una desigualdad cruzada

Probar que $ad + bc < ac + bd$.

Como $a < b$ y $c < d$, ambas diferencias son positivas: $b - a \in \mathbb{R}^+$ y $d - c \in \mathbb{R}^+$. Por cerradura del producto, $(b - a)(d - c) > 0$. Desarrollando, $bd - bc - ad + ac > 0$, es decir $ac + bd > ad + bc$.

El patrón se repite en casi todas las demostraciones del tema: traducir las hipótesis a "tal cosa es positiva", multiplicar o sumar positivos y desarrollar.

## Preguntas de repaso

> [!question]- ¿Qué significa en términos de $\mathbb{R}^+$ que $a < b$?
> Que $b - a \in \mathbb{R}^+$. Probar una desigualdad equivale a probar que cierta diferencia es positiva.

> [!question]- ¿Por qué la tricotomía es más fuerte que "$a \le b$ o $b \le a$"?
> Porque dice que se cumple **exactamente una** de las tres opciones: no pueden darse a la vez $a < b$ y $a = b$, por ejemplo. Esa exclusión es la que se usa para separar demostraciones en casos disjuntos.

> [!question]- ¿Cómo se prueba que la suma de dos positivos es positivo usando solo los axiomas de orden?
> De $a > 0$ y O3 se obtiene $a + b > b$; como $b > 0$, por transitividad $a + b > 0$.

> [!question]- ¿Qué falla en "$x < y$ y $z < r$ implican $xz < yr$"?
> Que sin positividad no es cierto. Con $x = -3, y = -2, z = -5, r = -1$ el producto $xz = 15$ no es menor que $yr = 2$.
