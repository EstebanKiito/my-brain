---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[02 - Teorema de los ceros racionales]]"
---

# Factorización en irreducibles

Factorizar un polinomio es descomponerlo en piezas que ya no se pueden partir: los **irreducibles**. En los reales, esas piezas son de dos tipos: lineales y cuadráticos sin raíces reales. Conocerlas es la base para escribir cualquier polinomio en forma factorizada.

## Polinomios irreducibles

Un polinomio no constante $P \in \mathbb{R}[x]$ es **irreducible** si no se puede escribir como producto de dos polinomios reales de grado menor (y $\ge 1$).

> [!tip] Irreducibles reales
> Los únicos polinomios reales irreducibles son:
> - los de **primer grado** $ax + b$, y
> - los de **segundo grado** $ax^2 + bx + c$ con **discriminante negativo** ($b^2 - 4ac < 0$, sin raíces reales).

## Factorización en $\mathbb{R}$

Todo polinomio real de grado $n \ge 1$ se factoriza como

$$
P(x) = a_n\,(x - c_1)\cdots(x - c_m)\,(x^2 + p_1 x + q_1)\cdots(x^2 + p_s x + q_s),
$$

donde $a_n$ es el coeficiente principal, los $c_i$ son las raíces reales (con sus multiplicidades) y los cuadráticos no tienen raíces reales. Es decir: **lineales** para las raíces reales y **cuadráticos irreducibles** para las complejas (agrupadas por pares conjugados).

## Una consecuencia útil

Como los irreducibles reales tienen grado $1$ o $2$, y un producto de factores de grado $2$ tiene grado par:

> [!tip] Polinomio de grado impar
> Todo polinomio real de grado **impar** tiene al menos una raíz real. (Si no tuviera ninguna, quedaría factorizado solo en cuadráticos irreducibles, con grado par.)

## Preguntas de repaso

> [!question]- ¿Cuáles son los polinomios reales irreducibles?
> Los lineales $ax + b$ y los cuadráticos $ax^2 + bx + c$ con $b^2 - 4ac < 0$. Un cuadrático con discriminante $\ge 0$ se parte en dos lineales.

> [!question]- ¿Por qué todo polinomio real de grado impar tiene una raíz real?
> Porque si no tuviera raíces reales, su factorización tendría solo cuadráticos irreducibles, cuyo producto tiene grado par. Un grado impar exige al menos un factor lineal, es decir, una raíz real.

> [!question]- ¿Cómo se factoriza $x^2 + 1$ en $\mathbb{R}[x]$ y en $\mathbb{C}[x]$?
> En $\mathbb{R}[x]$ es irreducible (discriminante $-4 < 0$). En $\mathbb{C}[x]$ se factoriza como $(x - i)(x + i)$.

> [!question]- ¿Qué papel juega el coeficiente principal en la factorización?
> Encabeza el producto: $P(x) = a_n\,(x - c_1)\cdots$. Sin él, el producto tendría coeficiente principal $1$ en vez de $a_n$.
