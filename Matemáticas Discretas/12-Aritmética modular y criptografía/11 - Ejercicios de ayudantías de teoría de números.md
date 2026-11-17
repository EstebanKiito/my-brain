---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Inversos modulares y congruencias lineales]]"
  - "[[07 - Pequeño teorema de Fermat]]"
---

# Ejercicios de ayudantías de teoría de números

Seis ejercicios de ayudantía sobre divisibilidad, congruencias, primos y ecuaciones con Bézout. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Representación en base 3 con dígitos $-1, 0, 1$
Demuestre que todo $n \in \mathbb{N}$ se puede escribir como $n = e_k 3^k + \dots + e_1 3 + e_0$ con $e_i \in \{-1, 0, 1\}$.

> [!example]- Solución
> Inducción fuerte sobre $n$. Para $n = 0$ basta $k = 0$ y $e_0 = 0$. Si $n \ge 1$, se divide $n = 3q + r$ con $r \in \{0, 1, 2\}$ y $q < n$.
> - Si $r \in \{0, 1\}$, se usa la representación de $q$ (por HI) y se agrega $e_0 = r$.
> - Si $r = 2$, se escribe $n = 3(q + 1) - 1$. Como $n \ge 2$, $q = (n-2)/3 \le n - 2$ y por tanto $q + 1 < n$: la HI se aplica a $q + 1$ y se agrega $e_0 = -1$.
>
> Ejemplos: $5 = 9 - 3 - 1$, con dígitos $(1, -1, -1)$; $8 = 9 + 0 - 1$, con $(1, 0, -1)$; $23 = 27 - 3 - 1$, con $(1, 0, -1, -1)$. Una verificación por computador confirma la representación para todo $n \le 3000$.

### 2. Lema de Euclides, primos y factorización única
(a) Si $\operatorname{MCD}(a, b) = 1$ y $a \mid bc$, demuestre que $a \mid c$. (b) Si $p$ es primo y $p \mid ab$, entonces $p \mid a$ o $p \mid b$. (c) Deduzca que la factorización en primos es única.

> [!example]- Solución
> (a) Por Bézout, $sa + tb = 1$. Como $a \mid bc$, $bc = ka$. Multiplicando por $c$: $c = sac + tbc = a(sc + tk)$, luego $a \mid c$.
>
> (b) Si $p \nmid a$, como $p$ es primo $\operatorname{MCD}(p, a) = 1$, y por (a) $p \mid b$.
>
> (c) Inducción fuerte sobre $n$. Si $n = p_1 \cdots p_r = q_1 \cdots q_s$, entonces $p_1 \mid q_1 \cdots q_s$ y por (b) $p_1 \mid q_j$ para algún $j$; como ambos son primos, $p_1 = q_j$. Cancelando queda un número menor que $n$ con dos factorizaciones, que por HI coinciden salvo orden.

### 3. Producto de $k$ enteros consecutivos
Demuestre que $k$ divide al producto de $k$ enteros consecutivos $x_1, \dots, x_k$.

> [!example]- Solución
> Los restos módulo $k$ de $x_1, x_1 + 1, \dots, x_1 + k - 1$ recorren todos los valores $0, \dots, k - 1$. Por tanto algún $x_j \equiv 0 \pmod k$, es decir $k \mid x_j$. Como $x_j$ es factor del producto, $k$ divide al producto. Por ejemplo, para $k = 4$ y $x = 6, 7, 8, 9$: el producto es $3024 = 4 \cdot 756$.

### 4. Cuadrados de impares y de primos
(a) Si $a$ es impar, $a^2 \equiv 1 \pmod 8$. (b) Si $p > 3$ es primo, $p^2 \equiv 1 \pmod{24}$.

> [!example]- Solución
> (a) Módulo $8$ un impar es $1, 3, 5$ o $7$, y los cuadrados son $1, 9, 25, 49$, todos congruentes con $1$ módulo $8$.
>
> (b) Como $p$ es impar, $p^2 \equiv 1 \pmod 8$ por (a). Como $3 \nmid p$, es $p \equiv \pm 1 \pmod 3$ y $p^2 \equiv 1 \pmod 3$. Al ser $8$ y $3$ coprimos, el lema del teorema chino del resto da $p^2 \equiv 1 \pmod{24}$. Ejemplos: $5^2 = 25$, $7^2 = 49$, $11^2 = 121 = 5 \cdot 24 + 1$.

### 5. Raíces cuadradas de 1 módulo un primo
Sea $p$ primo impar y $a \in \mathbb{Z}_p$, $a \ne 0$. Demuestre que $a^{(p-1)/2} \equiv 1$ o $a^{(p-1)/2} \equiv -1 \pmod p$.

> [!example]- Solución
> Por Fermat, $a^{p-1} \equiv 1$, es decir $p \mid a^{p-1} - 1 = \left(a^{\frac{p-1}{2}} - 1\right)\left(a^{\frac{p-1}{2}} + 1\right)$. Como $p$ es primo, divide a alguno de los dos factores, lo que da $a^{(p-1)/2} \equiv 1$ o $\equiv -1$. La hipótesis $a \ne 0$ es necesaria: con $a = 0$ la potencia vale $0$. Módulo $13$ se obtiene, para $a = 1, \dots, 12$, $a^6 \in \{1, 12\}$.

### 6. Perros y gatos
(a) Demuestre que $ax + by = c$ tiene solución entera si y solo si $\operatorname{MCD}(a, b) \mid c$. (b) Un grupo de perros y gatos gasta \$100; cada perro gasta \$8 y cada gato \$5. ¿Cuántos pueden ser?

> [!example]- Solución
> (a) ($\Rightarrow$) $\operatorname{MCD}(a, b)$ divide a $ax + by = c$. ($\Leftarrow$) Si $c = k \cdot \operatorname{MCD}(a, b)$ y $sa + tb = \operatorname{MCD}(a, b)$ (Bézout), entonces $x = sk$, $y = tk$ cumplen $ax + by = c$.
>
> (b) Hay que resolver $8p + 5g = 100$ con $p, g \ge 0$. Como $\operatorname{MCD}(8, 5) = 1$ divide a $100$ hay solución. De $2 \cdot 8 - 3 \cdot 5 = 1$: $p_0 = 200$, $g_0 = -300$. Quitando $5k$ perros y agregando $8k$ gatos se mantiene el gasto: $p = 200 - 5k \ge 0$ y $g = -300 + 8k \ge 0$ dan $38 \le k \le 40$. Soluciones: $(p, g) = (10, 4), (5, 12), (0, 20)$. Verificación: $80 + 20 = 100$, $40 + 60 = 100$, $0 + 100 = 100$.

## Preguntas de repaso

> [!question]- ¿Qué resultado de Bézout se usa en casi todos estos ejercicios?
> Que $\operatorname{MCD}(a, b) = sa + tb$; con él se prueba el lema de Euclides, la existencia de inversos y la solubilidad de $ax + by = c$.

> [!question]- ¿Por qué en el ejercicio 3 basta encontrar un múltiplo de $k$ entre los factores?
> Porque si $k$ divide a un factor, divide al producto completo.

> [!question]- ¿Cómo se combinan dos congruencias con módulos coprimos, como en $p^2 \equiv 1$ módulo $8$ y módulo $3$?
> Con el lema del teorema chino: $u \equiv v$ módulo $m_1$ y módulo $m_2$ coprimos implica $u \equiv v$ módulo $m_1 m_2$.
