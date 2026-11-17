---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - origen/complemento
prerrequisitos:
  - "[[02 - Congruencias módulo n y aritmética en Z_n]]"
  - "[[04 - Identidad de Bézout y algoritmo de Euclides extendido]]"
---

# Inversos modulares y congruencias lineales

En los reales, la ecuación $3x = 2$ se resuelve dividiendo por $3$. En $\mathbb{Z}_n$ no hay división, pero a veces existe un **inverso** que hace el mismo papel. Saber cuándo existe y cómo calcularlo permite resolver ecuaciones de congruencia y es la base de RSA.

## Inverso modular

$b$ es **inverso** de $a$ módulo $n$ si $ab \equiv 1 \pmod n$; se escribe $a^{-1}$ (no es $1/a$). Por ejemplo, $5$ es inverso de $3$ módulo $7$ porque $3 \cdot 5 = 15 \equiv 1$. En cambio, $2$ no tiene inverso módulo $4$: los productos $2 \cdot 0, 2 \cdot 1, 2 \cdot 2, 2 \cdot 3$ valen $0, 2, 0, 2$, nunca $1$.

> [!tip] Cuándo existe el inverso
> $a$ tiene inverso módulo $n$ si y solo si $\operatorname{MCD}(a, n) = 1$.

**($\Rightarrow$)** Si $ab \equiv 1$, entonces $ab = kn + 1$, o sea $1 = ab - kn$; todo divisor común de $a$ y $n$ divide a $1$, luego el MCD es $1$. **($\Leftarrow$)** Si $\operatorname{MCD}(a, n) = 1$, Bézout da $1 = sa + tn$, es decir $as = (-t)n + 1 \equiv 1 \pmod n$. Entonces **$s$ es el inverso** y se calcula con el algoritmo extendido.

**Ejemplo:** inverso de $5$ módulo $8$. De $2 \cdot 8 - 3 \cdot 5 = 1$ sale $5 \cdot (-3) \equiv 1 \pmod 8$, y $-3 \equiv 5$; en efecto $5 \cdot 5 = 25 = 3 \cdot 8 + 1$. Si $p$ es primo, todo $a \not\equiv 0$ tiene inverso módulo $p$, así que $\mathbb{Z}_p$ se comporta como un cuerpo.

## Congruencias lineales

Una **congruencia lineal** es $ax \equiv b \pmod n$ con incógnita $x$, por ejemplo $3x \equiv 2 \pmod 7$.

Si $\operatorname{MCD}(a, n) = 1$ se multiplica por $a^{-1}$:

$$ax \equiv b \iff (a^{-1}a)x \equiv a^{-1} b \iff x \equiv a^{-1} b \pmod n.$$

**Ejemplo:** $3x \equiv 2 \pmod 7$. Como $3 \cdot 5 \equiv 1$, $x \equiv 5 \cdot 2 = 10 \equiv 3$. Comprobación: $3 \cdot 3 = 9 \equiv 2$. La solución es única módulo $7$.

## Cuando $\operatorname{MCD}(a, n) \ne 1$

Sea $g = \operatorname{MCD}(a, n)$. La ecuación $ax \equiv b \pmod n$ equivale a $ax + ny = b$ para algún entero $y$, y esta tiene solución si y solo si $g \mid b$ (ver Bézout: si $g \mid b$, se multiplica $g = sa + tn$ por $b/g$).

- Si $g \nmid b$ no hay solución: $4x \equiv 3 \pmod 6$ no tiene solución, porque $4x - 3$ es impar y nunca es múltiplo de $6$.
- Si $g \mid b$, se divide todo por $g$: $(a/g) x \equiv (b/g) \pmod{n/g}$, ahora con coeficiente coprimo, y hay exactamente $g$ soluciones módulo $n$. Por ejemplo $4x \equiv 2 \pmod 6$ pasa a $2x \equiv 1 \pmod 3$, de donde $x \equiv 2 \pmod 3$, o sea $x \in \{2, 5\}$ módulo $6$.

> [!warning] No se puede cancelar sin cuidado
> De $ac \equiv bc \pmod m$ solo se concluye $a \equiv b \pmod{m / \operatorname{MCD}(m, c)}$. Por ejemplo $2 \cdot 3 \equiv 2 \cdot 6 \pmod 6$ no implica $3 \equiv 6 \pmod 6$, sino $3 \equiv 6 \pmod 3$.

## Ecuaciones con dos incógnitas enteras

El mismo argumento resuelve $ax + by = c$: hay solución si y solo si $\operatorname{MCD}(a, b) \mid c$. Ejemplo: $8p + 5g = 100$ (perros y gatos que gastan \$100). De $2 \cdot 8 - 3 \cdot 5 = 1$ resulta la solución $p_0 = 200$, $g_0 = -300$, y las demás son $p = 200 - 5k$, $g = -300 + 8k$. Con $p, g \ge 0$ se necesita $38 \le k \le 40$: $(p, g) \in \{(10, 4), (5, 12), (0, 20)\}$.

## Preguntas de repaso

> [!question]- ¿Por qué $2$ no tiene inverso módulo $4$?
> Porque $\operatorname{MCD}(2, 4) = 2 \ne 1$; de hecho $2x$ siempre es par y $4 \mid (2x - 1)$ es imposible.

> [!question]- ¿Cómo se calcula $7^{-1} \bmod 40$?
> Con Euclides extendido: $\operatorname{MCD} = 1$ y $7 \cdot 23 = 161 = 4 \cdot 40 + 1$, luego el inverso es $23$.

> [!question]- ¿Cuántas soluciones tiene $6x \equiv 4 \pmod{10}$ módulo $10$?
> $\operatorname{MCD}(6, 10) = 2$ divide a $4$, así que hay $2$ soluciones: $x = 4$ y $x = 9$.

> [!question]- ¿Por qué si $p$ es primo todo $a \not\equiv 0 \pmod p$ tiene inverso?
> Porque los únicos divisores de $p$ son $1$ y $p$, y $p \nmid a$, luego $\operatorname{MCD}(a, p) = 1$.
