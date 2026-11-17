---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - origen/complemento
prerrequisitos:
  - "[[01 - Divisibilidad y división con resto]]"
---

# Congruencias módulo n y aritmética en Z_n

Los relojes cuentan módulo 12: las 15 horas son "las 3". La congruencia formaliza esa idea para cualquier $n$ y permite hacer cuentas con enteros enormes trabajando solo con sus restos, que es justamente lo que necesitan las aplicaciones a criptografía.

## Congruencia módulo $n$

Para $n \ge 1$, $a$ es **congruente** con $b$ módulo $n$, $a \equiv_n b$ (también $a \equiv b \pmod n$), si $n \mid (b - a)$, es decir, si $b - a = kn$ para algún $k \in \mathbb{Z}$. Por ejemplo, módulo $7$: $2 \equiv 23$, $8 \equiv 1$, $-3 \equiv 4$, pero $19 \not\equiv 4$.

Es una relación de equivalencia (refleja, simétrica y transitiva), cuyas clases son los conjuntos de enteros con igual resto. El conjunto cuociente es $\mathbb{Z}_n = \{[0], [1], \dots, [n-1]\}$, y se acostumbra escribir cada clase con su representante: $\mathbb{Z}_5 = \{0, 1, 2, 3, 4\}$.

> [!tip] Congruencia y resto
> $a \equiv_n b \iff a \bmod n = b \bmod n$. En particular $a \equiv_n (a \bmod n)$.

La demostración usa $a = \alpha n + (a \bmod n)$ y $b = \gamma n + (b \bmod n)$. Si los restos coinciden, $b - a = (\gamma - \alpha) n$. Recíprocamente, si difieren (digamos $a \bmod n < b \bmod n$), entonces $b - a = (\gamma - \alpha) n + (b \bmod n - a \bmod n)$, y esa última diferencia está entre $1$ y $n-1$, así que $n \nmid (b - a)$.

## Suma y producto respetan la congruencia

Si $a \equiv_n b$ y $c \equiv_n d$, entonces $a + c \equiv_n b + d$ y $a c \equiv_n b d$. Con $b = a + k_1 n$ y $d = c + k_2 n$:

$$(b + d) - (a + c) = (k_1 + k_2) n, \qquad bd - ac = (a k_2 + c k_1 + k_1 k_2 n)\, n.$$

Por eso las operaciones de $\mathbb{Z}_n$ están bien definidas: $[i] + [j] = [(i + j) \bmod n]$ y $[i]\cdot[j] = [(ij) \bmod n]$ no dependen del representante. En la práctica, se puede **reducir módulo $n$ antes y después** de cada operación:

$$(a + b) \bmod n = ((a \bmod n) + (b \bmod n)) \bmod n, \qquad (ab) \bmod n = ((a \bmod n)(b \bmod n)) \bmod n.$$

Aplicando el producto repetidamente se obtiene $a \equiv b \Rightarrow a^m \equiv b^m \pmod n$ (inducción en $m$).

## Ejemplos resueltos

- En $\mathbb{Z}_5$: $37 + 18 = 55 \equiv 0$. Para $26 \cdot 37$ conviene reducir antes: $26 \equiv 1$ y $37 \equiv 2$, luego $26 \cdot 37 \equiv 1 \cdot 2 = 2$ (el producto completo es $962 \equiv 2$).
- $(55 \cdot 26) \bmod 4$: $55 \equiv 3$ y $26 \equiv 2$, luego $3 \cdot 2 = 6 \equiv 2$.
- **Último dígito:** el último dígito de $m$ es $m \bmod 10$. Como $4321 \equiv 1 \pmod{10}$, resulta $4321^{4321} \equiv 1^{4321} = 1$: termina en $1$.

## Criterio de divisibilidad por 3

Si $n = d_k 10^k + \dots + d_1 10 + d_0$ con dígitos $d_i$, como $10 \equiv 1 \pmod 3$ se tiene $10^i \equiv 1$, y por tanto

$$n \equiv d_k + \dots + d_1 + d_0 \pmod 3.$$

Luego $3 \mid n$ si y solo si $3 \mid$ (suma de dígitos). Por ejemplo $1347$ tiene suma $15$, múltiplo de $3$, y efectivamente $1347 = 3 \cdot 449$. El mismo argumento con $10 \equiv 1 \pmod 9$ da el criterio del $9$.

> [!warning] $\equiv$ no es lo mismo que $\bmod$
> $a \equiv b \pmod n$ es una **afirmación** sobre dos números (verdadera o falsa), mientras que $b \bmod n$ es un **número** entre $0$ y $n-1$. Además, $\equiv$ **no** permite dividir libremente: $2 \cdot 3 \equiv 2 \cdot 6 \pmod 6$ pero $3 \not\equiv 6$ (ver [[05 - Inversos modulares y congruencias lineales]]).

## Preguntas de repaso

> [!question]- ¿Por qué se puede reducir módulo $n$ en cada paso de un cálculo largo?
> Porque $a \equiv a \bmod n$ y la suma y el producto respetan la congruencia: reemplazar un operando por otro congruente no cambia el resultado módulo $n$.

> [!question]- ¿Cuántas clases tiene $\mathbb{Z}_n$ y por qué?
> $n$ clases, una por cada resto posible $0, \dots, n-1$; dos enteros están en la misma clase exactamente cuando tienen igual resto.

> [!question]- ¿Por qué $10^k \equiv 1 \pmod 3$ sirve para el criterio del 3?
> Porque cada potencia de 10 aporta un factor $1$ al multiplicarla por su dígito, así que $n$ se reduce a la suma de dígitos.

> [!question]- Calcule $7^{100} \bmod 6$ sin calculadora.
> Como $7 \equiv 1 \pmod 6$, $7^{100} \equiv 1^{100} = 1$.
