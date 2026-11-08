---
ramo: "Álgebra Lineal"
tema: "Reducción por filas"
tags:
  - algebra-lineal/sistemas
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Existencia y unicidad de soluciones]]"
---

# Ejercicios de prueba de reducción por filas

Preguntas de interrogaciones y exámenes anteriores donde hay que escalonar y decidir cuántas soluciones hay, casi siempre con parámetros. La clave en todas es separar casos **antes** de dividir por una expresión que puede anularse.

## Ejercicios

### 1. Sistema de $2 \times 2$ con parámetro
¿Para qué $k$ el sistema $x + ky = 1$, $kx + y = 1$ tiene solución única, infinitas o ninguna?

> [!example]- Solución
> $\left[\begin{array}{cc|c} 1 & k & 1 \\ k & 1 & 1 \end{array}\right] \xrightarrow{F_2 - kF_1} \left[\begin{array}{cc|c} 1 & k & 1 \\ 0 & 1 - k^2 & 1 - k \end{array}\right]$.
> - Única si $1 - k^2 \neq 0$, es decir, $k \neq \pm1$.
> - $k = 1$: la fila es $[0\ 0 \mid 0]$, infinitas (las dos rectas coinciden).
> - $k = -1$: la fila es $[0\ 0 \mid 2]$, ninguna (rectas paralelas).

### 2. V o F: única para unos $r$ y ninguna para otros
El sistema $\begin{bmatrix} 1 & 2 \\ 1 & 3 \\ 1 & r \end{bmatrix}\mathbf x = \begin{bmatrix}4\\5\\6\end{bmatrix}$ tiene solución única para algunos $r$ y ninguna para otros.

> [!example]- Solución
> **Verdadero.** $F_2 - F_1$ y $F_3 - F_1$ dan $[0\ 1 \mid 1]$ y $[0\ r - 2 \mid 2]$; luego $F_3 - (r - 2)F_2$ da $[0\ 0 \mid 4 - r]$. Para $r = 4$ es consistente y sin libres: solución única $\mathbf x = \langle 2, 1\rangle$. Para $r \neq 4$ es inconsistente.

### 3. Dos parámetros
Para $\begin{cases} x + ay + 2z = 1 \\ y + 2z = 2 \\ x + y + az = b \end{cases}$, ¿cuándo hay infinitas soluciones, una o ninguna?

> [!example]- Solución
> $F_3 - F_1$ da $[0\ \ 1 - a\ \ a - 2 \mid b - 1]$, y luego $F_3 - (1 - a)F_2$:
> $$\left[\begin{array}{ccc|c} 1 & a & 2 & 1 \\ 0 & 1 & 2 & 2 \\ 0 & 0 & 3a - 4 & 2a + b - 3 \end{array}\right].$$
> - Si $a \neq \tfrac43$: tres pivotes, **solución única** (para cualquier $b$).
> - Si $a = \tfrac43$: la fila es $[0\ 0\ 0 \mid b - \tfrac13]$. **Infinitas** si $b = \tfrac13$, **ninguna** si $b \neq \tfrac13$.

### 4. ¿Puede la solución ser una recta?
Para $\begin{cases} x + y + az = 1 \\ x + ay + z = 1 \\ ax + y + z = 1 \end{cases}$: (a) ¿cuándo tiene solución? (b) ¿Para qué $a$ es una recta?

> [!example]- Solución
> $F_2 - F_1$ da $[0\ \ a - 1\ \ 1 - a \mid 0]$ y $F_3 - aF_1$ da $[0\ \ 1 - a\ \ 1 - a^2 \mid 1 - a]$. Sumando estas dos filas:
> $$[\,0\ \ 0\ \ (1 - a)(a + 2) \mid 1 - a\,].$$
> - $a = 1$: las filas 2 y 3 se anulan y queda el plano $x + y + z = 1$.
> - $a = -2$: la fila es $[0\ 0\ 0 \mid 3]$, inconsistente.
> - Otro $a$: tres pivotes, solución única.
>
> (a) Tiene solución si y solo si $a \neq -2$. (b) **Nunca** es una recta: o es un punto, o un plano, o vacío.

### 5. Solución recta y su ecuación
Para $\begin{cases} x - az = 2 \\ 2x + ay + az = 5 \\ -x + ay + (5a - 1)z = -a \end{cases}$: (a) ¿cuándo no hay solución? (b) ¿Cuándo es una recta? (c) Dé la recta.

> [!example]- Solución
> $F_2 - 2F_1$ da $[0\ a\ 3a \mid 1]$; $F_3 + F_1$ da $[0\ a\ 4a - 1 \mid 2 - a]$; luego $F_3 - F_2$ da $[0\ 0\ a - 1 \mid 1 - a]$.
> - (a) $a = 0$: la segunda fila es $[0\ 0\ 0 \mid 1]$, **sin solución**.
> - (b) $a = 1$: la tercera fila se anula y queda una variable libre: **recta**. Para $a \notin \{0, 1\}$ la solución es única.
> - (c) Con $a = 1$: $x = 2 + z$ e $y + 3z = 1$. Con $z = t$: $\mathbf x = \langle 2, 1, 0\rangle + t\langle 1, -3, 1\rangle$.

### 6. Tres planos con parámetro
$\Pi_1: x + y + z = 1$, $\Pi_2: x + y + az = a^2$, $\Pi_3: a^2x + a^2y + z = 1$. (a) ¿Coinciden para algún $a$? (b) ¿Cuándo se cortan en una recta? (c) ¿Alguna vez en un solo punto?

> [!example]- Solución
> $F_2 - F_1$ da $[0\ 0\ \ a - 1 \mid a^2 - 1]$ y $F_3 - a^2F_1$ da $[0\ 0\ \ 1 - a^2 \mid 1 - a^2]$.
> - (a) $a = 1$: ambas filas se anulan y los tres planos son $x + y + z = 1$. **Sí, coinciden.**
> - (b) Si $a \neq 1$, la fila 2 da $z = a + 1$. Si además $a = -1$, la fila 3 se anula: $z = 0$ y queda la recta $x + y = 1$, $z = 0$. Si $a \neq \pm1$, la fila 3 da $z = 1$, compatible solo si $a + 1 = 1$, o sea $a = 0$; queda la recta $x + y = 0$, $z = 1$. **Recta para $a = 0$ y $a = -1$**; inconsistente para el resto.
> - (c) **Nunca**: las columnas de $x$ e $y$ son iguales, así que la columna 2 jamás es pivote y siempre hay al menos una variable libre.

### 7. Un sistema de $4 \times 4$ inconsistente
Resuelva $\begin{cases} x + y + z - w = 2 \\ 2x + y + w = 5 \\ 3x + z + w = 1 \\ 3x + 2y + z = 3 \end{cases}$.

> [!example]- Solución
> Los coeficientes de la cuarta ecuación son la suma de los de las dos primeras: $(1, 1, 1, -1) + (2, 1, 0, 1) = (3, 2, 1, 0)$. Entonces $F_4 - F_1 - F_2$ deja $[0\ 0\ 0\ 0 \mid 3 - 7] = [0\ 0\ 0\ 0 \mid -4]$. El sistema es **inconsistente** y el conjunto solución es vacío. Detectar combinaciones entre filas ahorra escalonar todo.

### 8. Sistema homogéneo con infinitas soluciones
¿Qué deben cumplir $a, b, c$ para que $x_1 + ax_2 + a^2x_3 = 0$, $x_1 + bx_2 + b^2x_3 = 0$, $x_1 + cx_2 + c^2x_3 = 0$ tenga infinitas soluciones?

> [!example]- Solución
> $F_2 - F_1 = [0\ \ b - a\ \ (b - a)(b + a)]$ y $F_3 - F_1 = [0\ \ c - a\ \ (c - a)(c + a)]$.
> - Si $b = a$ o $c = a$, alguna de esas filas es nula: hay a lo más dos pivotes y una variable libre.
> - Si $b \neq a$ y $c \neq a$, se dividen las filas por $b - a$ y $c - a$: $[0\ 1\ \ a + b]$ y $[0\ 1\ \ a + c]$. Restando queda $[0\ 0\ \ c - b]$, que da variable libre si y solo si $b = c$.
>
> Como es homogéneo, siempre es consistente. Infinitas soluciones **si y solo si $a = b$, $a = c$ o $b = c$**.

## Preguntas de repaso

> [!question]- En el ejercicio 4, ¿por qué es imposible que la solución sea una recta, sin hacer más cuentas?
> Porque, después de escalonar, las filas 2 y 3 se anulan juntas (cuando $a = 1$) o ninguna se anula. Nunca queda exactamente una fila nula, que es lo que daría un solo parámetro.

> [!question]- ¿Qué técnica del ejercicio 7 sirve antes de escalonar?
> Buscar si alguna fila de coeficientes es combinación de otras y comparar los lados derechos con la misma combinación. Si no calzan, el sistema es inconsistente; si calzan, esa ecuación es redundante.

> [!question]- ¿Por qué en el ejercicio 8 no hay que preocuparse por la consistencia?
> Porque es homogéneo: $\mathbf x = \mathbf 0$ siempre es solución. Lo único que se decide es si hay variables libres.
