---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles y caracterizaciones equivalentes]]"
  - "[[02 - Hojas, poda y número de aristas de un árbol]]"
  - "[[06 - Bosques y árboles generadores]]"
---

# Ejercicios de prueba de árboles

En exámenes y tareas los árboles aparecen en dos formatos: **demostrar equivalencias** entre las definiciones (conexo y acíclico, camino único, aristas de corte) y **demostrar una propiedad estructural** (bipartito, ciclo si no hay vértices de grado $\le 1$, árbol generador). La pauta puntúa explicitar qué caracterización se usa y el argumento del ciclo. Las preguntas sobre árboles binarios por inducción estructural se encuentran en [[08 - Ejercicios de prueba de inducción]].

## Ejercicios

### 1. Tres definiciones equivalentes (Examen, 2016-2)
Demuestre que son equivalentes: (i) entre cada par de vértices de $T$ hay un único camino; (ii) $T$ es conexo y acíclico; (iii) $T$ es conexo y todas sus aristas son de corte.

> [!example]- Solución
> Se prueba el ciclo (i) ⇒ (ii) ⇒ (iii) ⇒ (i).
>
> **(i) ⇒ (ii).** Hay camino entre todo par, así que es conexo. Un ciclo por $u$ y $v$ da dos caminos distintos entre ellos, contradiciendo (i).
>
> **(ii) ⇒ (iii).** Sea $e = \{u, v\}$. Si $T - e$ fuera conexo, un camino de $u$ a $v$ en $T - e$ más $e$ sería un ciclo, contra (ii). Luego $T - e$ es desconexo y $e$ es de corte.
>
> **(iii) ⇒ (i).** Hay camino por conexión. Si hubiera dos distintos entre $u$ y $v$, se toma el vértice $x$ donde se separan y el siguiente vértice común $y$: los tramos $x \to y$ forman un ciclo. Una arista $e$ del ciclo no es de corte (el resto del ciclo une sus extremos), contra (iii).

### 2. Conexo y acíclico (Examen, 2021-2)
Un grafo $T$ donde entre cada par de vértices hay un único camino es un árbol. Demuestre que $T$ es árbol si y solo si es conexo y acíclico.

> [!example]- Solución
> (⇒) Es conexo por existir caminos. Un ciclo que pasa por $u$ y $v$ se parte en dos caminos distintos de $u$ a $v$: contradicción. (⇐) Hay caminos por conexión; si $p_1 \ne p_2$ unen $u$ con $v$, sea $x$ el vértice anterior al primero en que difieren e $y$ el siguiente vértice común. Los tramos de $x$ a $y$ por $p_1$ y por $p_2$ no comparten aristas y forman un ciclo, contra la hipótesis. Luego el camino es único.

### 3. Grado mínimo 2 implica ciclo (Examen, 2025-1)
Sea $G$ un grafo sin rulos ni aristas múltiples con $n \ge 3$ vértices y grado mínimo $\delta(G) \ge 2$. Demuestre que contiene un ciclo.

> [!example]- Solución
> Se toma un camino $v_1, \dots, v_k$ de largo máximo (existe porque el grafo es finito y tiene aristas). Todo vecino de $v_1$ está en el camino: si no, se podría alargar. Como $\delta \ge 2$, $v_1$ tiene un vecino $v_i \ne v_2$ y entonces $i \ge 3$. Así $v_1, v_2, \dots, v_i, v_1$ es un ciclo de largo $i \ge 3$.
>
> En términos de árboles: un grafo sin ciclos (bosque) siempre tiene un vértice de grado $\le 1$, una hoja o un vértice aislado.

### 4. Un bosque es bipartito (Tarea 6, 2022-2)
Sea $G = (V, E)$ un bosque. Demuestre que existe $f : V \to \{0, 1\}$ tal que si $(u, v) \in E$ entonces $f(u) \ne f(v)$.

> [!example]- Solución
> Es equivalente a probar que $G$ es bipartito. En cada componente (un árbol) se fija una raíz $r$ y se define $f(u)$ como la paridad del largo del único camino de $r$ a $u$. Si $\{u, v\}$ es arista, uno de los dos caminos es el otro más la arista (el camino a $v$ pasa por $u$, o viceversa, pues el camino es único y no hay ciclos), así que los largos difieren en $1$ y las paridades son distintas. Los vértices de componentes distintas no comparten aristas.
>
> La pauta lo hace por inducción en $|E|$: con $0$ aristas, $f \equiv 0$ sirve; al agregar una arista $e = \{u, v\}$ a $G - e$, si $f(u) = f(v)$ se invierten los colores de toda la componente de $v$ (que no contiene a $u$, pues no hay ciclos), con lo que $f(u) \ne f(v)$ y las demás aristas siguen bien.

### 5. Un árbol generador de un grafo concreto (Tarea 6, 2022-2)
Dé un grafo simple $G$ con $7$ vértices y un árbol generador de $G$.

> [!example]- Solución
> Sea $G$ con vértices $a, \dots, g$ y aristas $ab, ae, bf, cf, cd, cg, ef, fg, eg$. Es conexo (9 aristas) pero no es árbol: un árbol con $7$ vértices tiene $6$ aristas. Se quitan $ae$, $ef$ y $cg$, una arista de un ciclo cada vez ($a, b, f, e$; $e, f, g$; $c, f, g$). Quedan $ab, bf, cf, cd, fg, eg$: $6$ aristas, conexo y con los $7$ vértices, luego un árbol (cumple $n - 1$ aristas).

## Preguntas de repaso

> [!question]- ¿Qué se necesita para pasar de "sin ciclos" a "camino único"?
> Mostrar que dos caminos distintos entre el mismo par generan un ciclo (con el vértice de separación $x$ y el siguiente en común $y$).

> [!question]- ¿Por qué en el ejercicio 3 se usa el extremo de un camino de largo máximo?
> Porque no puede tener vecinos fuera del camino; con grado al menos $2$ debe tener otro vecino dentro, lo que cierra el ciclo.

> [!question]- ¿Cómo se comprueba rápido que un subgrafo conexo es árbol generador?
> Contando: debe contener todos los vértices y tener exactamente $n - 1$ aristas.
