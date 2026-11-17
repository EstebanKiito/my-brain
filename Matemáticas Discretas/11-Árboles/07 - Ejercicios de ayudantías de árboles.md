---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Hojas, poda y número de aristas de un árbol]]"
  - "[[04 - Árboles binarios y conteo de hojas]]"
  - "[[05 - Árboles binarios completos y altura logarítmica]]"
---

# Ejercicios de ayudantías de árboles

La ayudantía de grafos incluye un único ejercicio específico de árboles (colorear con dos colores); se completa con los ejercicios que quedan propuestos en el desarrollo de la teoría (torneos y árboles binarios completos) y con dos de práctica sobre grados y alturas. Las ideas que se repiten: **la unicidad del camino**, **quitar una hoja** y **contar aristas con $n - 1$**.

## Ejercicios

### 1. Todo árbol es 2-coloreable (ayudantía de grafos, 2024-1)
Sea $T = (V, E)$ un árbol (conexo, con camino único entre pares de vértices). Demuestre que existe una coloración $C : V \to \{0, 1\}$ tal que vértices adyacentes tienen distinto color.

> [!example]- Solución
> Se fija un vértice $v_0$ y se define $C(u) = 0$ si el único camino de $v_0$ a $u$ tiene largo par y $C(u) = 1$ si es impar (con $C(v_0) = 0$). Está bien definida porque el camino es único.
>
> Sea $\{u_0, u_1\} \in E$. Si el camino de $v_0$ a $u_0$ no pasa por $u_1$, agregarle la arista da el camino (único) a $u_1$, de largo una unidad mayor; si pasa por $u_1$, ese vértice es el anterior a $u_0$ y el camino a $u_1$ es una unidad más corto. En ambos casos los largos tienen paridad distinta, luego $C(u_0) \ne C(u_1)$.

### 2. Copa Chile: cuántos partidos se juegan (ejercicio de clase)
En un torneo de eliminación simple participan $n$ equipos. ¿Cuántos partidos se juegan?

> [!example]- Solución
> El torneo es un árbol binario con los $n$ equipos como hojas; cada partido es un vértice con dos hijos. Por el teorema de hojas, hay $n - 1$ vértices con dos hijos: **$n - 1$ partidos**. Con $n = 8$, son $7$ partidos ($4 + 2 + 1$). Otra forma: cada partido elimina a un equipo y deben quedar eliminados $n - 1$.

### 3. Hojas de un árbol según los grados (práctica)
Un árbol tiene un vértice de grado $4$, dos vértices de grado $3$ y todos los demás son hojas. ¿Cuántos vértices tiene?

> [!example]- Solución
> Sea $L$ el número de hojas; el árbol tiene $n = 3 + L$ vértices y $n - 1 = L + 2$ aristas. La suma de los grados es el doble de las aristas: $4 + 3 + 3 + L = 2(L + 2)$, de donde $10 + L = 2L + 4$ y $L = 6$. El árbol tiene $n = 9$ vértices (y $8$ aristas; suma de grados $16$).

### 4. Árbol binario completo: existencia (ejercicio de clase)
¿Existe un árbol binario completo con $31$ vértices? ¿Y con $13$? En caso afirmativo, indique su altura y su número de hojas.

> [!example]- Solución
> El número de vértices es $2^{H+1} - 1$. Con $31 = 2^5 - 1$, $H = 4$ y hay $2^4 = 16$ hojas. Con $13$, $13 + 1 = 14$ no es potencia de $2$, así que **no existe**.

### 5. Altura mínima de un árbol binario con $1000$ vértices (práctica)
Demuestre que todo árbol binario con $1000$ vértices tiene altura al menos $9$.

> [!example]- Solución
> Un árbol binario de altura $H$ tiene a lo más $2^i$ vértices en la profundidad $i$, luego a lo más $\sum_{i=0}^{H} 2^i = 2^{H+1} - 1$ vértices (la cantidad que alcanza el árbol completo). Con $H = 8$ el máximo es $2^9 - 1 = 511 < 1000$, así que se necesita $H \ge 9$. Con $H = 9$ el máximo es $1023 \ge 1000$: la cota es alcanzable.

## Preguntas de repaso

> [!question]- ¿Qué propiedad hace que la coloración por paridad esté bien definida?
> Que el camino de $v_0$ a cada vértice es único; con dos caminos de distinta paridad el color no quedaría determinado.

> [!question]- ¿Por qué el conteo de partidos no depende del cuadro del torneo?
> Porque cualquier cuadro es un árbol binario con $n$ hojas y el teorema fija en $n - 1$ el número de vértices con dos hijos.

> [!question]- ¿Cómo se relacionan la suma de grados y el número de aristas de un árbol?
> La suma de los grados es $2(n - 1)$, pues cada arista aporta $1$ al grado de dos vértices.
