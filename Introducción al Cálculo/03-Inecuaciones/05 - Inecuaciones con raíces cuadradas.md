---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - origen/complemento
prerrequisitos:
  - "[[05 - Raíces cuadradas y valor absoluto]]"
  - "[[03 - Inecuaciones racionales y restricciones]]"
---

# Inecuaciones con raíces cuadradas

Con una raíz cuadrada aparecen dos cosas que no existían antes: la expresión bajo la raíz debe ser $\ge 0$ (dominio) y la raíz misma es siempre $\ge 0$. Al elevar al cuadrado para eliminar la raíz hay que cuidar estas dos condiciones, que son las que separan una resolución correcta de una que se cuela soluciones extrañas.

## Paso previo: el dominio

Antes de manipular, se escribe la condición bajo cada raíz: $\sqrt{A}$ exige $A \ge 0$. Todo el conjunto solución debe vivir en esa región; se intersecta al final (o al principio) con ella.

## Dos raíces: comparar los radicandos

> [!tip] Raíz contra raíz
> Para $A, B \ge 0$: $\sqrt{A} \le \sqrt{B} \iff A \le B$ (la raíz conserva el orden). Se resuelve $A \le B$ y se intersecta con $A \ge 0$ y $B \ge 0$.

Ejemplo: $\sqrt{3 - 3x} \le \sqrt{21 + 4x - x^2}$. El dominio pide $x \le 1$ y $-3 \le x \le 7$, así que $x \in [-3, 1]$. Luego $3 - 3x \le 21 + 4x - x^2 \iff x^2 - 7x - 18 \le 0 \iff (x - 9)(x + 2) \le 0 \iff x \in [-2, 9]$. La solución es $[-3, 1] \cap [-2, 9] = [-2, 1]$.

## Raíz contra una expresión sin raíz

Si la inecuación es $\sqrt{f} < g$ o $\sqrt{f} > g$, el signo de $g$ decide cómo se actúa.

> [!tip] Reglas con $g$ arbitrario (y $f \ge 0$)
> - $\sqrt{f} < g \iff g > 0 \ \wedge\ f < g^2$.
> - $\sqrt{f} > g \iff (g < 0) \ \vee\ (g \ge 0 \ \wedge\ f > g^2)$.

La primera dice que si $g \le 0$ no hay solución (una raíz nunca es menor que un número no positivo). La segunda dice que si $g < 0$ la desigualdad es verdadera siempre que la raíz exista.

Ejemplo (clase 7): $2x - 1 > \sqrt{x^2 - 3x}$. El dominio es $x(x - 3) \ge 0$, es decir $x \le 0$ ó $x \ge 3$. Se necesita $2x - 1 > 0$, o sea $x > \tfrac{1}{2}$, y entonces $(2x - 1)^2 > x^2 - 3x \iff 3x^2 - x + 1 > 0$, cierto siempre porque su discriminante es $-11 < 0$. La solución es $x > \tfrac{1}{2}$ y ($x \le 0$ ó $x \ge 3$), es decir $S = [3, \infty)$.

> [!warning] Un extremo que se pierde
> En esa clase el resultado aparece escrito como $]3, \infty[$, pero $x = 3$ sí cumple la inecuación original: $2 \cdot 3 - 1 = 5 > \sqrt{9 - 9} = 0$. El intervalo correcto es $[3, \infty)$.

## Radicandos con la misma raíz o con valor absoluto

$\sqrt{x + 3} > \sqrt{|x - 2|}$ se reduce a $x + 3 > |x - 2|$ con la condición $x \ge -3$. Con un valor absoluto en un lado, se parte en casos: para $x \le 2$ queda $x + 3 > 2 - x$, o sea $x > -\tfrac{1}{2}$; para $x > 2$ queda $x + 3 > x - 2$, siempre cierto. La solución es $\left(-\tfrac{1}{2}, \infty\right)$.

## Una solución escondida: el caso de igualdad

$\sqrt{x^2 + x - 2} - 2\sqrt{x^2 - 1} \ge 0$ es lo mismo que $\sqrt{x^2 + x - 2} \ge 2\sqrt{x^2 - 1}$. El dominio pide $x^2 + x - 2 = (x + 2)(x - 1) \ge 0$ y $x^2 - 1 \ge 0$, es decir $x \le -2$ ó $x \ge 1$. Elevando al cuadrado, $x^2 + x - 2 \ge 4x^2 - 4 \iff 3x^2 - x - 2 \le 0 \iff (3x + 2)(x - 1) \le 0 \iff x \in \left[-\tfrac{2}{3}, 1\right]$. Intersectando con el dominio queda un único punto, $S = \{1\}$. La inecuación puede tener un conjunto solución finito (o vacío) aunque los lados sean continuos.

## Preguntas de repaso

> [!question]- ¿Por qué hay que imponer $g > 0$ al resolver $\sqrt{f} < g$?
> Porque una raíz es $\ge 0$ y no puede ser menor que un número $\le 0$. Sin esa condición, al elevar al cuadrado se obtendrían falsas soluciones (por ejemplo, con $g < 0$ y $g^2$ grande).

> [!question]- ¿Cuándo es automáticamente verdadera $\sqrt{f} > g$?
> Cuando $g < 0$ y $f \ge 0$: la raíz existe y es $\ge 0 > g$.

> [!question]- ¿Qué dos condiciones hay que verificar en $\sqrt{A} \le \sqrt{B}$?
> $A \ge 0$ y $B \ge 0$ (que las raíces existan), y $A \le B$. El conjunto solución es la intersección de las tres.

> [!question]- ¿Puede una inecuación con raíces tener un conjunto solución con un solo punto?
> Sí: $\sqrt{x^2 + x - 2} \ge 2\sqrt{x^2 - 1}$ tiene como único elemento $x = 1$, porque el dominio y la inecuación cuadrática se tocan solo en ese punto.
