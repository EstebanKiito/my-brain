---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades del valor absoluto y desigualdad triangular]]"
---

# Raíces cuadradas y valor absoluto

La raíz cuadrada aparece en casi todo: en la forma $|x| = \sqrt{x^2}$, en distancias, en inecuaciones con radicales. Su definición cuida un detalle fino (la raíz es **no negativa**) y de él salen tanto la identidad con el valor absoluto como la regla de cuándo se puede elevar al cuadrado sin perder equivalencia.

## Definición e identidad central

> [!tip] Raíz cuadrada
> Para $a \ge 0$, $\sqrt{a}$ es el único número $y \ge 0$ tal que $y^2 = a$. No está definida para $a < 0$ en $\mathbb{R}$.

De ahí que $(\sqrt{a})^2 = a$ para $a \ge 0$, pero la identidad al revés **necesita** el valor absoluto:

> [!tip] Raíz de un cuadrado
> $\sqrt{x^2} = |x|$ para todo $x \in \mathbb{R}$.

Por ejemplo, $\sqrt{(-3)^2} = \sqrt{9} = 3 = |-3|$, no $-3$. Esta identidad explica resultados como $\sqrt{x^2 - 4x + 4} = \sqrt{(x - 2)^2} = |x - 2|$, que se usa mucho en las pruebas.

> [!warning] $\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}$
> La raíz respeta el producto ($\sqrt{ab} = \sqrt{a}\sqrt{b}$ para $a, b \ge 0$) pero no la suma: $\sqrt{9 + 16} = 5$ y $\sqrt{9} + \sqrt{16} = 7$.

## La raíz conserva el orden

> [!tip] Monotonía de la raíz
> Si $0 \le a < b$, entonces $\sqrt{a} < \sqrt{b}$. Por lo tanto, para $a, b \ge 0$: $a \le b \iff \sqrt{a} \le \sqrt{b}$.

*Demostración, por contradicción.* Supóngase $\sqrt{a} \ge \sqrt{b}$ con $0 \le a < b$. Como ambas raíces son $\ge 0$, elevar al cuadrado conserva el orden y da $a \ge b$, lo que contradice $a < b$. Luego $\sqrt{a} < \sqrt{b}$.

La consecuencia práctica es una regla para quitar raíces:

> [!tip] Elevar al cuadrado
> Si $A, B \ge 0$, entonces $A \le B \iff A^2 \le B^2$, y $A = B \iff A^2 = B^2$. Si algún lado puede ser negativo, elevar al cuadrado **no** es una equivalencia.

Por eso $-3 < 2$ pero $(-3)^2 > 2^2$: el lado izquierdo es negativo.

## Ecuaciones con una raíz

Para $\sqrt{f} = g$ hacen falta dos condiciones antes de elevar al cuadrado: $f \ge 0$ (para que la raíz exista) y $g \ge 0$ (porque la raíz es no negativa). Luego $\sqrt{f} = g \iff f = g^2 \ \wedge\ g \ge 0$.

Ejemplo: $\sqrt{x + 2} = x$. Se exige $x \ge 0$. Entonces $x + 2 = x^2$, es decir $x^2 - x - 2 = (x - 2)(x + 1) = 0$, con $x = 2$ ó $x = -1$. Solo $x = 2$ cumple $x \ge 0$; $x = -1$ es una solución **extraña** que nace al elevar al cuadrado ($\sqrt{1} = 1 \neq -1$).

## Preguntas de repaso

> [!question]- ¿Por qué $\sqrt{x^2} = x$ es falso en general?
> Porque la raíz es siempre $\ge 0$. Si $x < 0$, $\sqrt{x^2} = -x = |x| \neq x$. La identidad correcta es $\sqrt{x^2} = |x|$.

> [!question]- ¿Cómo se prueba que $0 \le a < b$ implica $\sqrt{a} < \sqrt{b}$?
> Por contradicción: si $\sqrt{a} \ge \sqrt{b}$, al elevar al cuadrado (ambas raíces son no negativas) se obtendría $a \ge b$, contra la hipótesis.

> [!question]- ¿Qué condiciones hay que imponer antes de elevar al cuadrado en $\sqrt{f} = g$?
> $f \ge 0$ para que la raíz exista, y $g \ge 0$ porque la raíz no es negativa. Sin $g \ge 0$ se pueden colar soluciones extrañas.

> [!question]- Simplifique $\sqrt{x^2 - 6x + 9}$.
> Es $\sqrt{(x - 3)^2} = |x - 3|$, que vale $x - 3$ si $x \ge 3$ y $3 - x$ si $x < 3$.
