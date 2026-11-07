---
ramo: "Álgebra Lineal"
tema: "Espacios y subespacios vectoriales"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[01 - Vectores y sus operaciones]]"
  - "[[01 - Operaciones con matrices]]"
---

# Espacios vectoriales

Los vectores de $\mathbb{R}^n$ se suman y se escalan. Las matrices también. Y los polinomios, las funciones y las señales. Todo lo que se demostró sobre combinaciones lineales, independencia o generadores usó **solo** esas dos operaciones y sus reglas, no el hecho de que los vectores fueran listas de números. Un **espacio vectorial** es cualquier conjunto con esas operaciones y esas reglas. La recompensa es grande: toda la maquinaria del curso funciona igual para polinomios, matrices o funciones.

## Definición

> [!tip] Definición
> Un **espacio vectorial** $V$ es un conjunto no vacío de objetos, llamados **vectores**, con una suma y un producto por escalares (reales) que cumplen, para todo $\mathbf u, \mathbf v, \mathbf w \in V$ y escalares $c, d$:
> 1. $\mathbf u + \mathbf v \in V$ (cerrado bajo la suma).
> 2. $\mathbf u + \mathbf v = \mathbf v + \mathbf u$.
> 3. $(\mathbf u + \mathbf v) + \mathbf w = \mathbf u + (\mathbf v + \mathbf w)$.
> 4. Existe un **vector cero** $\mathbf 0 \in V$ con $\mathbf u + \mathbf 0 = \mathbf u$.
> 5. Para cada $\mathbf u$ existe $-\mathbf u \in V$ con $\mathbf u + (-\mathbf u) = \mathbf 0$.
> 6. $c\mathbf u \in V$ (cerrado bajo el producto por escalar).
> 7. $c(\mathbf u + \mathbf v) = c\mathbf u + c\mathbf v$.
> 8. $(c + d)\mathbf u = c\mathbf u + d\mathbf u$.
> 9. $c(d\mathbf u) = (cd)\mathbf u$.
> 10. $1\mathbf u = \mathbf u$.

Los axiomas 1 y 6 son los que suelen fallar: piden que sumar o escalar **no saque** del conjunto. El resto suele heredarse de las propiedades de los números.

De los axiomas se deducen las propiedades esperables: $0\mathbf u = \mathbf 0$, $c\mathbf 0 = \mathbf 0$ y $-\mathbf u = (-1)\mathbf u$. Por ejemplo, $0\mathbf u = (0 + 0)\mathbf u = 0\mathbf u + 0\mathbf u$, y sumando $-0\mathbf u$ a ambos lados queda $\mathbf 0 = 0\mathbf u$.

## Ejemplos

| Espacio | Vectores | Cero |
|---|---|---|
| $\mathbb{R}^n$ | listas de $n$ números | $\langle 0, \dots, 0\rangle$ |
| $\mathbb{P}_n$ | polinomios de grado **a lo más** $n$: $a_0 + a_1t + \dots + a_nt^n$ | el polinomio nulo |
| $\mathbb{P}$ | todos los polinomios | el polinomio nulo |
| $M_{m \times n}(\mathbb{R})$ | matrices de $m \times n$ | la matriz nula |
| $\{f: \mathbb{R} \to \mathbb{R}\}$ | funciones reales, con $(f + g)(t) = f(t) + g(t)$ | la función constante 0 |
| $\mathbb{S}$ | sucesiones doblemente infinitas $(\dots, y_{-1}, y_0, y_1, \dots)$, como señales discretas | la sucesión de ceros |

En todos, la suma y el producto por escalar se hacen "componente a componente" (coeficiente a coeficiente, entrada a entrada, punto a punto).

> [!warning] Dos que no son espacios vectoriales
> - **Los polinomios de grado exactamente $n$**: $(t^2 + t) + (-t^2) = t$ tiene grado 1, así que la suma sale del conjunto; además no contiene al polinomio nulo.
> - **Todas las matrices reales juntas** (de cualquier tamaño): no se puede sumar una de $2 \times 2$ con una de $3 \times 3$, así que la suma no está definida para todo par.

## Por qué importa

En un espacio vectorial cualquiera tienen sentido, sin cambiar una palabra, las nociones de combinación lineal, conjunto generado, independencia lineal y transformación lineal. Por ejemplo, $t^2 + 4t + 1$ es combinación lineal de $t^2 - 3t$ y $t + 1$ si existen $a, b$ con $a(t^2 - 3t) + b(t + 1) = t^2 + 4t + 1$. Igualando coeficientes: $a = 1$, $b = 1$ (término constante) y $-3a + b = 4$ (coeficiente de $t$), que da $-2 = 4$. No lo es. Igualar coeficientes convierte la pregunta en un sistema lineal, como en $\mathbb{R}^n$.

## Preguntas de repaso

> [!question]- ¿Es un espacio vectorial el conjunto de vectores de $\mathbb{R}^2$ con ambas componentes no negativas?
> No. No es cerrado bajo el producto por escalar: $\langle 1, 1\rangle$ está, pero $(-1)\langle 1, 1\rangle$ no. Tampoco contiene opuestos.

> [!question]- ¿Por qué $\mathbb{P}_2$ sí es un espacio vectorial pero los polinomios de grado exactamente 2 no?
> Sumar o escalar polinomios de grado a lo más 2 nunca sube el grado, y el polinomio nulo está incluido. Con grado exactamente 2, la suma puede bajar de grado ($t^2 + 1$ más $-t^2$) y el cero no pertenece.

> [!question]- ¿Cuál es el vector cero del espacio de funciones $\mathbb{R} \to \mathbb{R}$?
> La función $f(t) = 0$ para todo $t$. Es la única que sumada a cualquier $g$ la deja igual.

> [!question]- Demuestre que $c\mathbf 0 = \mathbf 0$ usando los axiomas.
> $c\mathbf 0 = c(\mathbf 0 + \mathbf 0) = c\mathbf 0 + c\mathbf 0$ por los axiomas 4 y 7. Sumando $-c\mathbf 0$ a ambos lados (axioma 5) queda $\mathbf 0 = c\mathbf 0$.
