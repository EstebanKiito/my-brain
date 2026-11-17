---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - origen/complemento
prerrequisitos:
  - "[[02 - Congruencias módulo n y aritmética en Z_n]]"
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Pequeño teorema de Fermat

Calcular $a^{p-1}$ módulo un primo $p$ siempre da $1$ (si $p \nmid a$). Este hecho permite reducir exponentes enormes y es la pieza que hace funcionar RSA.

## Enunciado

> [!tip] Pequeño teorema de Fermat
> Si $p$ es primo, para todo entero $a$ se cumple $a^p \equiv a \pmod p$. En particular, si $p \nmid a$, entonces $a^{p-1} \equiv 1 \pmod p$.

Ejemplos: $2^{10} = 1024 = 93 \cdot 11 + 1 \equiv 1 \pmod{11}$ y $3^{100} \equiv 3^{100 \bmod 6} = 3^4 = 81 \equiv 4 \pmod 7$ (aquí $3^6 \equiv 1$). Con $p = 13$, $a^{12} \equiv 1$ para todo $a = 1, \dots, 12$.

## Demostración de $a^p \equiv a$ (primero $a \ge 0$)

Por inducción sobre $a$. Casos base: $0^p = 0$ y $1^p = 1$. Paso: si $p \mid a^p - a$, se quiere $p \mid (a+1)^p - (a+1)$. Por el teorema del binomio,

$$(a+1)^p - (a+1) = (a^p - a) + \sum_{k=1}^{p-1} \binom{p}{k} a^k.$$

El primer sumando es divisible por $p$ por hipótesis. Cada $\binom{p}{k}$ con $1 \le k \le p-1$ también: $\binom{p}{k} = \dfrac{p (p-1) \cdots (p-k+1)}{k!}$ es entero y $p$ aparece en el numerador pero no en $k!$ (todos sus factores son menores que $p$), así que $p$ divide al coeficiente. Luego $p \mid (a+1)^p - (a+1)$.

Para $a < 0$ se usa $a \equiv a \bmod p$: $a^p \equiv (a \bmod p)^p \equiv a \bmod p \equiv a$, pues $a \bmod p \ge 0$.

## Corolario: $a^{p-1} \equiv 1$

Si $p \nmid a$, de $p \mid a^p - a = a (a^{p-1} - 1)$ y $\operatorname{MCD}(a, p) = 1$, el lema de Euclides da $p \mid a^{p-1} - 1$. Es la forma que más se usa.

## Para qué sirve

- **Reducir exponentes:** si $p \nmid a$ y $b \equiv c \pmod{p-1}$, entonces $a^b \equiv a^c \pmod p$, porque $a^{p-1} \equiv 1$. Por ejemplo $3^{2025} \equiv 3^{2025 \bmod 6} = 3^3 = 27 \equiv 6 \pmod 7$.
- **Raíz cuadrada de 1:** si $p$ es impar y $p \nmid a$, entonces $\left(a^{(p-1)/2} - 1\right)\left(a^{(p-1)/2} + 1\right) = a^{p-1} - 1$ es múltiplo de $p$, y como $p$ es primo divide a un factor: $a^{(p-1)/2} \equiv \pm 1 \pmod p$. Para $p = 13$: $a^6 \bmod 13 = 1, 12, 1, 1, 12, 12, \dots$ (siempre $1$ o $12$).
- **Detectar compuestos:** si algún $a$ con $1 \le a < n$ cumple $a^{n-1} \not\equiv 1 \pmod n$, entonces $n$ no es primo. Para $n$ compuesto, cualquier divisor $d$ con $1 < d < n$ sirve: si $d^{n-1} \equiv 1 \pmod n$, $d$ tendría inverso y $\operatorname{MCD}(d, n) = 1$, absurdo.
- **RSA:** la correctitud del descifrado depende de $M^{k(P-1)(Q-1)} \equiv 1$ ([[09 - RSA: construcción, correctitud e implementación]]).

> [!warning] Un caso favorable no prueba que $n$ sea primo
> Que $a^{n-1} \equiv 1 \pmod n$ para algunos $a$ no prueba que $n$ sea primo; solo el **fallo** de la congruencia prueba que es compuesto. Además el corolario exige $p \nmid a$: con $a = 0$ no se cumple $a^{p-1} \equiv 1$.

## Preguntas de repaso

> [!question]- ¿Por qué $p$ divide a $\binom{p}{k}$ para $1 \le k \le p-1$?
> Porque $p$ está en el numerador $p!$ y no en $k!(p-k)!$, ya que todos los factores de estos son menores que $p$, y el coeficiente es un entero.

> [!question]- ¿Cómo se pasa de $a^p \equiv a$ a $a^{p-1} \equiv 1$?
> Se cancela un factor $a$, lo que es válido porque $a$ es coprimo con $p$ (tiene inverso módulo $p$).

> [!question]- Calcule $2^{100} \bmod 13$.
> $2^{12} \equiv 1$ y $100 = 8 \cdot 12 + 4$, luego $2^{100} \equiv 2^4 = 16 \equiv 3$.

> [!question]- ¿Por qué falla Fermat para un compuesto como $15$?
> Porque la hipótesis "$n$ primo" es esencial: con $a = 2$ se tiene $2^{14} \equiv 4 \pmod{15}$, no $1$.
