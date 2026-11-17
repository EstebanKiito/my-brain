---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - origen/complemento
prerrequisitos:
  - "[[05 - Inversos modulares y congruencias lineales]]"
---

# Teorema chino del resto

A veces se conocen los restos de un número al dividirlo por varios módulos y se quiere recuperar el número. Si un ejército se ordena en filas de 3 sobran 2 soldados, en filas de 5 sobran 3 y en filas de 7 sobran 2, ¿cuántos soldados hay? El teorema chino del resto asegura que, con módulos coprimos, hay una única respuesta módulo el producto, y la demostración la construye.

## Enunciado

> [!tip] Teorema chino del resto
> Sean $m_1, \dots, m_n > 1$ primos relativos de a pares y $a_1, \dots, a_n \in \mathbb{Z}$. El sistema $x \equiv a_i \pmod{m_i}$ para $i = 1, \dots, n$ tiene una **única** solución módulo $m = m_1 m_2 \cdots m_n$.

Para el ejército: $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$, $x \equiv 2 \pmod 7$.

## Existencia: la solución se construye

Para cada $k$ se define $M_k = m / m_k$, el producto de todos los módulos salvo $m_k$. Como los módulos son coprimos entre sí, $\operatorname{MCD}(M_k, m_k) = 1$, y por tanto $M_k$ tiene inverso $M_k^{-1}$ módulo $m_k$. Se propone

$$x^* = a_1 M_1 M_1^{-1} + a_2 M_2 M_2^{-1} + \dots + a_n M_n M_n^{-1}.$$

**Por qué funciona:** módulo $m_k$ todo $M_j$ con $j \ne k$ es múltiplo de $m_k$, así que esos sumandos valen $0$. Queda $x^* \equiv a_k (M_k M_k^{-1}) \equiv a_k \pmod{m_k}$. Cada sumando "enciende" una sola congruencia y "apaga" las demás.

## Unicidad

Si $u$ y $v$ son soluciones, entonces $u \equiv v \pmod{m_i}$ para todo $i$. Se usa el lema siguiente.

> [!tip] Lema
> Si $m_1, m_2$ son coprimos y $u \equiv v$ módulo $m_1$ y módulo $m_2$, entonces $u \equiv v \pmod{m_1 m_2}$.

Prueba: $u - v = k_1 m_1$ y $m_2 \mid (u - v)$, así que $m_2 \mid k_1 m_1$; como $\operatorname{MCD}(m_1, m_2) = 1$, el lema de Euclides da $m_2 \mid k_1$, es decir $k_1 = k m_2$ y $u - v = k\, m_1 m_2$. Aplicándolo de forma repetida (inducción) se llega a $u \equiv v \pmod m$.

## Ejemplo: el ejército

Aquí $m = 3 \cdot 5 \cdot 7 = 105$, $M_1 = 35$, $M_2 = 21$, $M_3 = 15$. Los inversos son:

- $35 \equiv 2 \pmod 3$ y $2 \cdot 2 = 4 \equiv 1$, así que $M_1^{-1} = 2$.
- $21 \equiv 1 \pmod 5$, así que $M_2^{-1} = 1$.
- $15 \equiv 1 \pmod 7$, así que $M_3^{-1} = 1$.

Entonces $x^* = 2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1 = 140 + 63 + 30 = 233 \equiv 23 \pmod{105}$. Comprobación: $23 = 7 \cdot 3 + 2$, $23 = 4 \cdot 5 + 3$ y $23 = 3 \cdot 7 + 2$. El ejército tiene $23 + 105k$ soldados.

## Un caso con cuatro módulos

Menor número con restos $1, 2, 3, 4$ al dividir por $5, 7, 9, 11$: $m = 3465$, $M_i = 693, 495, 385, 315$ con inversos $2, 3, 4, 8$, y

$$x \equiv 1 \cdot 693 \cdot 2 + 2 \cdot 495 \cdot 3 + 3 \cdot 385 \cdot 4 + 4 \cdot 315 \cdot 8 = 19056 \equiv 1731 \pmod{3465}.$$

## Qué pasa con módulos no coprimos

Si los módulos no son coprimos, puede no haber solución. Para dos congruencias $x \equiv a_1 \pmod{m_1}$ y $x \equiv a_2 \pmod{m_2}$ hay solución si y solo si $\operatorname{MCD}(m_1, m_2) \mid (a_1 - a_2)$. Por ejemplo, $x \equiv 1 \pmod 4$ y $x \equiv 2 \pmod 6$ no tienen solución (el MCD es $2$ y $a_1 - a_2 = -1$ no es divisible por $2$), mientras que $x \equiv 1 \pmod 4$ y $x \equiv 3 \pmod 6$ sí la tienen ($x = 9$).

## Preguntas de repaso

> [!question]- ¿Por qué hace falta que los módulos sean coprimos de a pares?
> Para que cada $M_k$ tenga inverso módulo $m_k$ (existencia) y para poder aplicar el lema de $m_1 m_2$ (unicidad).

> [!question]- ¿Por qué cada sumando de $x^*$ solo afecta a una congruencia?
> Porque $M_j$ es múltiplo de $m_k$ para todo $j \ne k$, así que módulo $m_k$ solo sobrevive el sumando $a_k M_k M_k^{-1} \equiv a_k$.

> [!question]- ¿Cuál es la solución de $x \equiv 1 \pmod 3$, $x \equiv 2 \pmod 5$?
> $m = 15$, $M_1 = 5$ (inverso $2$), $M_2 = 3$ (inverso $2$): $x = 1 \cdot 5 \cdot 2 + 2 \cdot 3 \cdot 2 = 22 \equiv 7$. Se verifica: $7 = 2 \cdot 3 + 1$ y $7 = 5 + 2$.

> [!question]- ¿Existe solución para $x \equiv 1 \pmod 4$ y $x \equiv 2 \pmod 6$?
> No: $\operatorname{MCD}(4, 6) = 2$ no divide a $1 - 2 = -1$ (la primera exige $x$ impar y la segunda $x$ par).
