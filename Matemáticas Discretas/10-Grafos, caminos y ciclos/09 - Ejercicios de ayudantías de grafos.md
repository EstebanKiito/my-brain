---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Caminatas y conectividad]]"
  - "[[04 - Isomorfismo y complemento de grafos]]"
---

# Ejercicios de ayudantías de grafos

Las ayudantías de grafos mezclan tres técnicas: **principio del palomar** y **inducción** sobre grafos (coloración de aristas), **distancias en un grafo y su complemento** (diámetro o "ancho") y **construcción de ciclos largos** a partir de caminos. Todos son demostraciones; lo difícil es elegir bien el objeto sobre el que se razona (un vértice, un par de vértices extremos, un camino más largo).

## Ejercicios

### 1. Coloración de aristas
Una $k$-coloración de aristas de un grafo no dirigido $G = (V, E)$ es una función $f : E \to \{1, \dots, k\}$ con $f(e) \neq f(e')$ para todo par de aristas distintas que comparten un vértice. (a) Demuestre que $k \geq \max_{v \in V} \deg(v)$. (b) Demuestre por inducción que un mismo color se usa en a lo más $\lvert V \rvert / 2$ aristas.

> [!example]- Solución
> (a) Si algún vértice $v$ tuviera $m = \deg(v) > k$, sus $m$ aristas incidentes usarían $m > k$ colores posibles, así que por el principio del palomar dos de ellas tendrían el mismo color. Esas dos comparten $v$, lo que contradice la definición. Luego $k \geq \deg(v)$ para todo $v$.
>
> (b) Inducción sobre $n = \lvert V \rvert$, fijando un color $c$. **Base** ($n = 1$): no hay aristas, y $0 \leq 1/2$. **Paso:** se toma un vértice $v$ cualquiera. Si ninguna arista incidente en $v$ tiene color $c$, se borra $v$; por hipótesis el grafo restante tiene a lo más $(n-1)/2$ aristas de color $c$, y esas son todas las de $G$, que es $\leq n/2$. Si alguna arista $e_c = \{u, v\}$ tiene color $c$, ninguna otra arista incidente en $u$ ni en $v$ puede tener color $c$ (comparten un extremo con $e_c$). Se borran $u$ y $v$; por hipótesis quedan a lo más $(n-2)/2$ aristas de color $c$ y, sumando $e_c$, hay a lo más $(n-2)/2 + 1 = n/2$.

### 2. Si el diámetro es grande, el del complemento es pequeño
Sea $G$ conexo. La distancia $d(u, v)$ es el largo del camino más corto entre $u$ y $v$ y el **ancho** $A(G)$ es la mayor distancia entre dos vértices. Demuestre que si $A(G) \geq 4$ entonces $A(\overline{G}) \leq 2$.

> [!example]- Solución
> Sean $u, v$ con $d(u, v) = A(G) \geq 4$. Ningún vértice $x$ es adyacente a $u$ y a $v$ a la vez (daría un camino $u x v$ de largo $2$). Se toman $x, y$ cualesquiera y se muestra $d_{\overline{G}}(x, y) \leq 2$.
> - Si $\{x, y\} \notin E$, entonces es arista de $\overline{G}$: distancia $1$.
> - Si $\{x, y\} \in E$: no puede ocurrir que uno sea adyacente a $u$ y el otro a $v$, pues $u, x, y, v$ sería un camino de largo $3 < 4$. Entonces $u$ o $v$ no es adyacente a ninguno de los dos (si $u$ fuera adyacente a alguno de ellos, $v$ no lo es a ninguno). Si $u$ no es adyacente a $x$ ni a $y$, $x u y$ es un camino de largo $2$ en $\overline{G}$; si es $v$, $x v y$.
>
> En todos los casos $d_{\overline{G}}(x, y) \leq 2$.

### 3. Vértice de corte y ancho $2$
Si $G$ es conexo, tiene un vértice de corte y $A(G) = 2$, demuestre que $\overline{G}$ tiene un vértice sin vecinos.

> [!example]- Solución
> Sea $v$ el vértice de corte. Se prueba que $v$ es adyacente a **todos** los demás en $G$, lo que lo deja sin vecinos en $\overline{G}$. Al quitar $v$ quedan al menos dos componentes. Sea $x \neq v$ en una de ellas $C$ y $w$ un vecino de $v$ en otra componente. Si $d(v, x) = k \geq 2$, el camino de $x$ a $w$ debe pasar por $v$ (están en componentes distintas de $G - v$), así que $d(x, w) = d(x, v) + 1 = k + 1 \geq 3$, contradiciendo $A(G) = 2$. Luego $d(v, x) = 1$ para todo $x$ en $C$, y como $C$ y $x$ eran arbitrarios, $v$ es adyacente a todos.

### 4. Un ciclo de largo al menos $\sqrt{k}$
Sea $C$ un ciclo en $G$ y suponga que hay un camino $P$ de largo $k$ entre dos vértices distintos de $C$. Demuestre que $G$ tiene un ciclo de largo al menos $\sqrt{k}$.

> [!example]- Solución
> Se supone $P$ sin vértices repetidos y que sus extremos están en $C$. Sea $c$ el largo de $C$. Si $c \geq \sqrt{k}$ ya está. Si no, $c < \sqrt{k}$: los vértices de $P$ que pertenecen a $C$ son a lo más $c$, y dividen a $P$ en a lo más $c - 1$ tramos entre vértices consecutivos de $C$ (con interior fuera de $C$). Los largos de los tramos suman $k$, así que algún tramo $Q$ tiene largo al menos $k/(c-1) > k/\sqrt{k} = \sqrt{k}$. Sean $a \neq b$ los extremos de $Q$, ambos en $C$; $Q$ más cualquiera de los dos arcos de $C$ entre $a$ y $b$ es un ciclo (el interior de $Q$ no toca $C$) y tiene largo mayor que el de $Q$, es decir, mayor que $\sqrt{k}$.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio de coloración se puede borrar $u$ y $v$ cuando hay una arista de color $c$?
> Porque ninguna otra arista del color $c$ puede tocar a $u$ ni a $v$ (compartiría un extremo con $e_c$ y tendría el mismo color). Al borrar esos dos vértices solo se pierden aristas de otros colores y $e_c$, que se suma a mano después.

> [!question]- ¿Por qué los vértices extremos $u, v$ a distancia $\geq 4$ son tan útiles para acotar el complemento?
> Porque casi todos los vértices quedan a distancia $\geq 2$ de alguno de los dos, y esa falta de arista en $G$ es una arista en $\overline{G}$: $u$ o $v$ sirve de intermediario para unir cualquier par en $\overline{G}$.

> [!question]- ¿Qué idea del palomar aparece en el ejercicio del ciclo largo?
> Si hay a lo más $c - 1$ tramos y suman $k$, alguno es largo (al menos el promedio $k/(c-1)$). Es el palomar en forma de promedio.
