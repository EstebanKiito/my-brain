---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[03 - Factorización en irreducibles]]"
---

# Número de raíces y raíces complejas

Un polinomio de grado $n$ tiene exactamente $n$ raíces complejas (contando multiplicidades), aunque algunas no sean reales. Y las raíces complejas de un polinomio real vienen de a dos: junto con cada complejo aparece su conjugado.

## El teorema fundamental del álgebra

> [!tip] Teorema fundamental del álgebra
> Todo polinomio no constante $P \in \mathbb{C}[x]$ tiene al menos una raíz compleja. En consecuencia, un polinomio de grado $n$ se factoriza como $P(x) = a_n(x - z_1)\cdots(x - z_n)$, con exactamente $n$ raíces complejas (contando multiplicidades).

El teorema responde "cuántas raíces hay en total": tantas como el grado, si se cuentan bien y se admiten complejas.

## Raíces complejas de polinomios reales

> [!tip] Raíces conjugadas
> Si $P \in \mathbb{R}[x]$ y $\alpha \in \mathbb{C}$ es raíz de $P$, entonces su conjugado $\overline{\alpha}$ también es raíz de $P$.

**Ejemplo.** Si $\alpha = 1 + i$ es raíz de $P(x) = x^3 - 4x^2 + 6x - 4$, halle las otras raíces.

Como $P$ tiene coeficientes reales, $1 - i$ también es raíz. El producto $(x - (1+i))(x - (1-i)) = x^2 - 2x + 2$ divide a $P$, y dividiendo, $P(x) = (x^2 - 2x + 2)(x - 2)$. Las raíces son $1 + i$, $1 - i$ y $2$.

## Determinar coeficientes

**Ejemplo.** Determine $a, b \in \mathbb{R}$ para que $P(x) = x^4 + 2x^3 + ax + b$ tenga raíz $\alpha = 1 + i$.

Como $\alpha$ y $\overline{\alpha} = 1 - i$ son raíces, $x^2 - 2x + 2$ divide a $P$. Dividiendo, $P(x) = (x^2 - 2x + 2)(x^2 + 4x + 6) + (a + 4)x + (b - 12)$. Para que el resto sea $0$, $a + 4 = 0$ y $b - 12 = 0$, luego $a = -4$ y $b = 12$.

> [!tip] El factor cuadrático de dos conjugadas
> $(x - \alpha)(x - \overline{\alpha}) = x^2 - 2\operatorname{Re}(\alpha)\,x + |\alpha|^2$. Para $\alpha = 3 + 3i$ da $x^2 - 6x + 18$ sin multiplicar binomios.

## Relaciones entre raíces y coeficientes

Si $P(x) = x^3 + ax^2 + bx + c$ tiene raíces $\alpha, \beta, \gamma$, al expandir $(x - \alpha)(x - \beta)(x - \gamma)$ y comparar coeficientes:
$$\alpha + \beta + \gamma = -a, \qquad \alpha\beta + \alpha\gamma + \beta\gamma = b, \qquad \alpha\beta\gamma = -c.$$
Para grado $2$, $x^2 + bx + c$: la suma de las raíces es $-b$ y el producto es $c$. El polinomio debe estar **mónico** (coeficiente principal $1$); si no, se divide primero por él.

**Ejemplo.** Las raíces de $x^3 - \frac{5}{3}x^2 + \frac{31}{36}x - \frac{5}{36}$ cumplen $\gamma = \alpha + \beta$. Como $\alpha + \beta + \gamma = \frac{5}{3}$, se tiene $2\gamma = \frac{5}{3}$ y $\gamma = \frac{5}{6}$, sin resolver la cúbica.

## Preguntas de repaso

> [!question]- ¿Cuántas raíces complejas tiene un polinomio de grado $n$?
> Exactamente $n$, contando multiplicidades. Es la forma que toma el teorema fundamental del álgebra.

> [!question]- Si $2 - 3i$ es raíz de un polinomio real, ¿qué otra raíz es segura?
> Su conjugado $2 + 3i$, por el teorema de las raíces conjugadas.

> [!question]- ¿Por qué un polinomio real de grado $3$ tiene una raíz real?
> Porque sus $3$ raíces complejas vienen en pares conjugados (conteo par) más las reales. Tres raíces no pueden ser todas complejas no reales, así que al menos una es real.

> [!question]- En el primer ejemplo, ¿cómo se obtiene $x^2 - 2x + 2$ a partir de $1 + i$?
> Es $(x - (1+i))(x - (1-i)) = (x - 1)^2 + 1 = x^2 - 2x + 2$: el polinomio real mínimo que anula a $1 + i$ y su conjugado.
