---
ramo: "Álgebra Lineal"
tema: "Transformaciones lineales"
tags:
  - algebra-lineal/transformaciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Matriz estándar de una transformación lineal]]"
  - "[[03 - Independencia lineal]]"
---

# Transformaciones sobreyectivas e inyectivas

Las dos preguntas que se le hacen a un sistema, **existencia** y **unicidad**, tienen su versión para transformaciones: ¿toda salida posible se alcanza? (sobreyectividad) y ¿cada salida viene de una sola entrada? (inyectividad). Para una transformación lineal ambas se deciden escalonando su matriz estándar, y conectan todo lo visto: generadores, independencia lineal y pivotes.

## Definiciones

> [!tip] Sobreyectiva (sobre)
> $T: \mathbb{R}^n \to \mathbb{R}^m$ es **sobreyectiva**, o **mapea $\mathbb{R}^n$ sobre $\mathbb{R}^m$**, si todo $\mathbf b \in \mathbb{R}^m$ es imagen de **al menos un** $\mathbf x$. Es decir, el rango de $T$ es todo el codominio. Es una pregunta de **existencia**.

> [!tip] Inyectiva (uno a uno)
> $T$ es **inyectiva** si todo $\mathbf b \in \mathbb{R}^m$ es imagen de **a lo más un** $\mathbf x$. Es una pregunta de **unicidad**: si $T(\mathbf x) = \mathbf b$ tiene solución, la tiene única.

Una no implica la otra. La proyección $\langle x_1, x_2, x_3\rangle \mapsto \langle x_1, x_2\rangle$ es sobre (todo punto del plano es sombra de algo) pero no inyectiva (todo el eje $x_3$ va a $\mathbf 0$). La inclusión $\langle x_1, x_2\rangle \mapsto \langle x_1, x_2, 0\rangle$ es inyectiva pero no sobre.

## Inyectividad y el núcleo

> [!tip] Teorema
> Una transformación lineal $T$ es inyectiva si y solo si $T(\mathbf x) = \mathbf 0$ tiene **solo** la solución trivial.

**Demostración.** Si $T$ es inyectiva, como $T(\mathbf 0) = \mathbf 0$, ningún otro vector puede ir a $\mathbf 0$. Recíprocamente, si $T(\mathbf u) = T(\mathbf v)$, entonces $T(\mathbf u - \mathbf v) = \mathbf 0$, y si solo $\mathbf 0$ va a $\mathbf 0$, $\mathbf u = \mathbf v$. $\blacksquare$

Basta revisar **un** lado derecho, el cero, en vez de todos. Es la misma idea del teorema de la traslación: todas las soluciones de $A\mathbf x = \mathbf b$ son "una más las homogéneas".

## Criterio con la matriz estándar

> [!tip] Teorema
> Sea $T(\mathbf x) = A\mathbf x$ con $A = [\mathbf a_1 \cdots \mathbf a_n]$ de $m \times n$.
>
> | $T$ es sobre $\mathbb{R}^m$ | $T$ es inyectiva |
> |---|---|
> | $A\mathbf x = \mathbf b$ es consistente para todo $\mathbf b$ | $A\mathbf x = \mathbf 0$ solo tiene la solución trivial |
> | las columnas de $A$ **generan** $\mathbb{R}^m$ | las columnas de $A$ son **LI** |
> | $A$ tiene un **pivote en cada fila** | $A$ tiene un **pivote en cada columna** |

Las dos columnas de la tabla son la misma moneda vista desde las filas y desde las columnas de la forma escalonada.

**Ejemplo.** $T(\mathbf x) = A\mathbf x$ con $A = \begin{bmatrix} 1 & -4 & 8 & 1 \\ 0 & 2 & -1 & 3 \\ 0 & 0 & 0 & 5 \end{bmatrix}$. $A$ es de $3 \times 4$, así que $T: \mathbb{R}^4 \to \mathbb{R}^3$. Ya está escalonada, con pivotes en las columnas 1, 2 y 4:

- hay un pivote en cada una de las 3 filas: **es sobre**;
- la columna 3 no tiene pivote ($x_3$ libre): **no es inyectiva**.

## Restricciones por tamaño

Los pivotes son a lo más $\min(m, n)$, lo que da respuestas sin calcular:

> [!tip] Consecuencias
> - Si $n > m$ (dominio "más grande"): no hay pivotes para todas las columnas, así que $T$ **no es inyectiva**.
> - Si $n < m$ (dominio "más chico"): no hay pivotes para todas las filas, así que $T$ **no es sobre**.
> - Solo si $n = m$ puede ser ambas cosas a la vez.

Dicho de otro modo: si $T$ es sobre, $m \leq n$; si es inyectiva, $n \leq m$. Intuitivamente, una transformación lineal no puede "inflar" $\mathbb{R}^2$ hasta llenar $\mathbb{R}^3$, ni "meter" $\mathbb{R}^3$ en $\mathbb{R}^2$ sin aplastar algo.

> [!warning] Las restricciones son en un solo sentido
> $n \geq m$ no garantiza que sea sobre (la transformación nula de $\mathbb{R}^3$ en $\mathbb{R}^2$ no lo es), y $n \leq m$ no garantiza que sea inyectiva. El tamaño solo descarta; para afirmar hay que escalonar.

## Preguntas de repaso

> [!question]- $T: \mathbb{R}^5 \to \mathbb{R}^3$ es lineal. ¿Puede ser inyectiva? ¿Puede ser sobre?
> No puede ser inyectiva: hay 5 columnas y a lo más 3 pivotes. Sí puede ser sobre, si su matriz tiene pivote en las 3 filas.

> [!question]- ¿Por qué para la inyectividad basta mirar $T(\mathbf x) = \mathbf 0$?
> Porque si $T(\mathbf u) = T(\mathbf v)$ con $\mathbf u \neq \mathbf v$, entonces $\mathbf u - \mathbf v$ es una solución no trivial de $T(\mathbf x) = \mathbf 0$. Y al revés, una solución no trivial $\mathbf w$ da dos preimágenes de $\mathbf 0$: $\mathbf w$ y $\mathbf 0$.

> [!question]- ¿Es inyectiva la rotación de un ángulo $\varphi$? ¿Es sobre?
> Ambas. Su matriz $\begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix}$ tiene columnas ortogonales de largo 1, que son LI, así que hay dos pivotes: uno por fila y uno por columna. Geométricamente, rotar en $-\varphi$ deshace la rotación.

> [!question]- ¿Es inyectiva la proyección sobre el eje $x_1$ en $\mathbb{R}^2$?
> No: su matriz $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ tiene una columna sin pivote, y todo el eje $x_2$ va a $\mathbf 0$.

> [!question]- Si $T: \mathbb{R}^n \to \mathbb{R}^n$ es inyectiva, ¿es necesariamente sobre?
> Sí. Inyectiva significa un pivote en cada una de las $n$ columnas; como la matriz es cuadrada, eso da $n$ pivotes, uno en cada una de las $n$ filas.
