---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - origen/complemento
prerrequisitos:
  - "[[03 - Vecindades e intervalos con valor absoluto]]"
---

# Ecuaciones con valor absoluto

Resolver una ecuación con valor absoluto es decidir, para cada posible signo de lo que hay dentro, qué ecuación sin valor absoluto queda. Hay un puñado de formas estándar; reconocerlas ahorra casos y evita soluciones falsas, que son el error más común en las interrogaciones.

## Las formas básicas

> [!tip] Tres reglas
> - $|x| = a$ con $a \ge 0$ equivale a $x = a$ ó $x = -a$. Con $a < 0$ **no tiene solución**.
> - $|f| = |g| \iff f = g$ ó $f = -g \iff f^2 = g^2$.
> - $|f| = g \iff g \ge 0 \ \wedge\ (f = g \vee f = -g)$.

La primera sale de $|x| = a \iff |x|^2 = a^2 \iff x^2 = a^2 \iff x = \pm a$. La tercera incluye la **condición** $g \ge 0$, que descarta soluciones.

**Ejemplos de la clase.**
- $|x - 1| = 3$: $x - 1 = 3$ ó $x - 1 = -3$, es decir $x = 4$ ó $x = -2$. Son los dos puntos a distancia $3$ de $1$.
- $|3x - 5| + 3 = 0$: equivale a $|3x - 5| = -3$, imposible porque un valor absoluto es $\ge 0$. No hay solución.
- $|x + 2| = |x - 1|$: se eleva al cuadrado, $(x + 2)^2 = (x - 1)^2 \iff 6x + 3 = 0 \iff x = -\tfrac{1}{2}$. Es el punto medio entre $-2$ y $1$.

## La condición del lado derecho

Resolver $|2x + 2| = 6x - 18$. Se exige primero $6x - 18 \ge 0$, es decir $x \ge 3$. Luego $2x + 2 = 6x - 18$ da $x = 5$ y $2x + 2 = -(6x - 18)$ da $x = 2$. Solo $x = 5$ cumple $x \ge 3$; $x = 2$ se descarta (de hecho $|6| = 6 \neq -6$). La solución es $\{5\}$.

> [!warning] Verificar siempre
> Después de resolver $|f| = g$ se comprueba cada candidato contra $g \ge 0$. Una raíz "obtenida correctamente" de $f = -g$ puede no pertenecer al conjunto solución.

## Un cociente en valor absoluto

Resolver $\left|\dfrac{x - 1}{x + 1}\right| = \dfrac{1}{7}$. Se exige $x \neq -1$. Como $|a/b| = |a|/|b|$, la ecuación es $7|x - 1| = |x + 1|$. Elevando al cuadrado, $49(x - 1)^2 = (x + 1)^2$, que da $12x^2 - 25x + 12 = 0$ y $x = \tfrac{25 \pm 7}{24}$, es decir $x = \tfrac{3}{4}$ ó $x = \tfrac{4}{3}$. Ambos distintos de $-1$, y la solución es $\{\tfrac{3}{4}, \tfrac{4}{3}\}$.

Esta ecuación también se resuelve por casos, con los puntos críticos $x = \pm 1$ (donde cambian de signo $x - 1$ y $x + 1$): en $x < -1$ no hay solución, en $(-1, 1)$ aparece $\tfrac{3}{4}$ y en $x > 1$ aparece $\tfrac{4}{3}$.

## Evaluar una expresión conociendo el signo

A veces no se resuelve una ecuación sino que se **simplifica** una expresión sabiendo en qué intervalo vive $x$. Si $0 < x < 1$, entonces $4x + 1 > 0$ y $x - 1 < 0$, así que $|4x + 1| = 4x + 1$ y $|x - 1| = 1 - x$, y
$$\frac{|4x + 1| - |x - 1|}{x} = \frac{(4x + 1) - (1 - x)}{x} = \frac{5x}{x} = 5.$$

## Método por casos

Con varios valores absolutos se marcan los **puntos críticos** (donde cada expresión interior vale cero) y se resuelve en cada tramo, quitando los valores absolutos con el signo correspondiente. La solución final es la unión de las soluciones de cada tramo, **intersecadas con ese tramo**.

## Preguntas de repaso

> [!question]- ¿Por qué $|x - 4| = -2$ no tiene solución?
> Porque el valor absoluto nunca es negativo; la condición $g \ge 0$ con $g = -2$ falla de entrada.

> [!question]- ¿Qué paso asegura que no se cuelen soluciones falsas en $|f| = g$?
> Imponer $g \ge 0$ y verificar cada candidato. Al elevar al cuadrado o resolver $f = -g$ pueden aparecer valores con $g < 0$.

> [!question]- ¿Qué describe geométricamente $|x - a| = |x - b|$?
> Los puntos equidistantes de $a$ y $b$: solo el punto medio, $x = \tfrac{a + b}{2}$ cuando $a \neq b$.

> [!question]- ¿Qué restricción hay que recordar en $\left|\tfrac{x-1}{x+1}\right| = \tfrac{1}{7}$ aunque se resuelva elevando al cuadrado?
> El dominio: $x \neq -1$, porque el denominador no puede anularse. Al multiplicar por $|x + 1|$ esa restricción desaparece de la ecuación resultante, así que se contrastan los candidatos con ella al final.
