---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - origen/complemento
prerrequisitos:
  - "[[01 - Los números reales como cuerpo]]"
---

# Consecuencias de los axiomas de cuerpo

Con solo los seis axiomas se pueden demostrar las reglas de álgebra que normalmente se dan por sabidas: $a \cdot 0 = 0$, la regla de los signos, la cancelación y el producto nulo. Estas demostraciones son el modelo del estilo del curso: cada igualdad se justifica con un axioma o con un resultado anterior.

## Multiplicar por cero

> [!tip] Teorema
> Para todo $a \in \mathbb{R}$, $a \cdot 0 = 0$.

*Demostración.* Por neutros y distributividad, $a \cdot 0 + a \cdot 1 = a(0 + 1) = a \cdot 1 = a$. Como $a \cdot 1 = a$, queda $a \cdot 0 + a = a$. Sumando $-a$ a ambos lados y usando inversos, $a \cdot 0 = 0$.

## Regla de los signos

> [!tip] Teorema (regla de los signos)
> Para $a, b \in \mathbb{R}$:
> 1. $-(-a) = a$
> 2. $(-a)\,b = -(ab)$
> 3. $a\,(-b) = -(ab)$
> 4. $(-a)(-b) = ab$

*Demostración de 2.* $(-a)b + ab = (-a + a)b = 0 \cdot b = 0$. Entonces $(-a)b$ es el número que sumado a $ab$ da $0$, es decir, $-(ab)$. La parte 3 es igual y la 4 sale de aplicar 2, 3 y 1: $(-a)(-b) = -(a(-b)) = -(-(ab)) = ab$. Para la parte 1, $(-a) + a = 0$ dice que $a$ es el opuesto de $-a$, o sea $a = -(-a)$.

## Inversos multiplicativos

Para $a, b \neq 0$ valen $(a^{-1})^{-1} = a$ y $a^{-1}b^{-1} = (ab)^{-1}$: el inverso del producto es el producto de los inversos. Se prueban igual, mostrando que el candidato multiplicado por el original da $1$.

## Cancelación y producto nulo

> [!tip] Leyes de cancelación
> - $a + b = a + c \iff b = c$.
> - Si $a \neq 0$: $ab = ac \iff b = c$.

> [!tip] Producto nulo
> Si $ab = 0$, entonces $a = 0$ o $b = 0$.

*Demostración.* Si $b \neq 0$, se multiplica $ab = 0$ por $b^{-1}$: $a = a \cdot 1 = a b b^{-1} = 0 \cdot b^{-1} = 0$. Si $b = 0$ ya está. $\blacksquare$

Una consecuencia directa y muy usada: si $x^2 = y^2$, entonces $x^2 - y^2 = (x - y)(x + y) = 0$, y por el producto nulo $x = y$ o $x = -y$.

> [!warning] Cancelar es dividir por algo no nulo
> Pasar de $ab = ac$ a $b = c$ exige $a \neq 0$. Con $a = 0$ la igualdad $0 \cdot 3 = 0 \cdot 5$ es cierta y $3 \neq 5$. Es la raíz del error clásico de "simplificar" un factor que podría valer cero y perder soluciones.

## Preguntas de repaso

> [!question]- ¿Por qué $(-1)(-1) = 1$ no es una convención sino un teorema?
> Es el caso $a = b = 1$ de la regla de los signos: $(-1)(-1) = (1)(1) = 1$, y esa regla se demuestra con los axiomas (en particular con $a \cdot 0 = 0$ y la distributividad).

> [!question]- ¿Dónde falla "$x(x - 2) = 3x \Rightarrow x - 2 = 3$" y qué solución se pierde?
> Se cancela $x$ sin saber si es distinto de $0$. Se pierde $x = 0$, que sí cumple $0 = 0$. La forma correcta es $x(x - 2) - 3x = 0$, factorizar $x(x - 5) = 0$ y aplicar el producto nulo.

> [!question]- ¿Cómo se concluye $x = y$ o $x = -y$ a partir de $x^2 = y^2$?
> Se pasa todo a un lado y se factoriza: $(x - y)(x + y) = 0$. Por el teorema del producto nulo, uno de los factores es cero.

> [!question]- ¿Qué axiomas aparecen en la demostración de $a \cdot 0 = 0$?
> Neutros (para escribir $a = a \cdot 1$ y $1 = 0 + 1$), distributividad, y el axioma de inversos (para sumar $-a$ y cancelarlo).
