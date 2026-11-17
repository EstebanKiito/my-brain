---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[02 - Grado de un vértice y lema del apretón de manos]]"
  - "[[05 - Caminatas y conectividad]]"
---

# Ciclos y caminos eulerianos

El problema que dio origen a la teoría de grafos: ¿se puede recorrer la ciudad de Königsberg cruzando cada uno de sus siete puentes exactamente una vez? Euler lo resolvió con una condición sobre los grados, que no requiere probar recorridos uno por uno.

## Definiciones

Un **ciclo euleriano** en un (multi)grafo $G$ es un ciclo que contiene **todas las aristas y todos los vértices** de $G$. Como es un ciclo no repite aristas (cada una se usa exactamente una vez), pero sí puede pasar varias veces por un mismo vértice. $G$ es **euleriano** si tiene un ciclo euleriano. Un **camino euleriano** es un camino no cerrado que contiene todas las aristas y vértices.

![Puentes de Konigsberg y su grafo](adjuntos/Puentes%20de%20Konigsberg%20y%20su%20grafo.png)

> [!example]- Transcripción de la imagen
> Mapa de las cuatro zonas de tierra $A, B, C, D$ unidas por siete puentes y el multigrafo asociado: $A$–$C$ y $A$–$B$ tienen dos aristas paralelas cada uno, y hay una arista $A$–$D$, $C$–$D$ y $B$–$D$. Los grados son $\delta(A) = 5$ y $\delta(B) = \delta(C) = \delta(D) = 3$.

Los cuatro vértices tienen grado impar, así que el grafo no es euleriano ni tiene camino euleriano (ver los teoremas siguientes): no hay forma de cruzar los siete puentes una sola vez.

## Teorema de los ciclos eulerianos

> [!tip] Teorema
> Un (multi)grafo sin rulos es euleriano si y solo si es **conexo** y **todos sus vértices tienen grado par**.

**($\Rightarrow$)** El ciclo euleriano $C$ pasa por todos los vértices, así que contiene caminos entre cualquier par: $G$ es conexo. Cada vez que $C$ llega a un vértice $v$ debe salir por otra arista, distinta; y el inicio y el final cuentan como una salida y una llegada. Así las aristas que inciden en $v$ aparecen en $C$ de a pares (entrada, salida) y $\delta(v)$ es par. Como $C$ se puede empezar en cualquier vértice, esto vale para todos.

**($\Leftarrow$)** Inducción sobre la cantidad de aristas.

- **Base:** el grafo de un solo vértice (el ciclo es el vértice mismo) y el de dos vértices con dos aristas paralelas son los más pequeños con estas propiedades, y ambos tienen ciclo euleriano.
- **Hipótesis:** todo grafo conexo con grados pares y menos de $n$ aristas tiene ciclo euleriano.
- **Paso:** sea $G$ con $n$ aristas y al menos $3$ vértices. Por conexidad hay un camino $v_1, v_2, v_3$ con aristas $e_1 = \{v_1, v_2\}$ y $e_2 = \{v_2, v_3\}$. Se construye $G'$ quitando $e_1$ y $e_2$ y agregando una arista nueva $e$ entre $v_1$ y $v_3$. Tiene menos aristas, y los grados siguen pares (solo $v_2$ cambió, en $2$). Hay dos casos:
  1. $G'$ **conexo:** por hipótesis tiene un ciclo euleriano $C'$, que usa $e$ como $(\dots, v_1, e, v_3, \dots)$; reemplazar $e$ por $e_1, e_2$ da un ciclo euleriano de $G$.
  2. $G'$ **disconexo:** como $G$ era conexo, tiene dos componentes, una con $v_2$ y otra con $v_1, v_3$. Por hipótesis cada una tiene su ciclo euleriano ($C'$ pasando por $v_2$, $C''$ por $e$). Se inserta $C'$ en $C''$ en el lugar de $e$: $(\dots, v_1, e_1, v_2, \dots, v_2, e_2, v_3, \dots)$.

![Construcción del ciclo euleriano desde G prima](adjuntos/Construcción%20del%20ciclo%20euleriano%20desde%20G%20prima.png)

> [!example]- Transcripción de la imagen
> Dos nubes que representan $G'$ (izquierda) y $G$ (derecha) con una curva cerrada que es el ciclo euleriano. En $G'$ el ciclo pasa por la arista $e$ entre $v_1$ y $v_3$; una flecha punteada señala "ciclo en $G'$". En $G$ la arista $e$ se reemplaza por $e_1$ (hasta $v_2$) y $e_2$ (de $v_2$ a $v_3$), y $v_2$ queda sobre el ciclo.

![Ciclos en las dos componentes de G prima](adjuntos/Ciclos%20en%20las%20dos%20componentes%20de%20G%20prima.png)

> [!example]- Transcripción de la imagen
> Dentro de $G'$ hay dos regiones: arriba la componente de $v_2$ con un ciclo $C'$ y abajo la componente que contiene a $v_1$, la arista $e$ y $v_3$, con un ciclo $C''$. Flechas punteadas indican "ciclos en ambas componentes de $G'$".

## Caminos eulerianos

> [!tip] Teorema
> Un (multi)grafo tiene un **camino euleriano** si y solo si es conexo y tiene **exactamente dos** vértices de grado impar (que son los extremos del camino).

Si $P$ va de $u$ a $v$ y se agrega una arista $e$ entre $u$ y $v$, $P$ más $e$ es un ciclo euleriano del nuevo grafo, cuyos grados son todos pares: en el original solo $u$ y $v$ tenían grado impar. Recíprocamente, si $G$ es conexo con exactamente dos vértices impares $u$ y $v$, agregar $e$ da grados pares, hay un ciclo euleriano, y quitar $e$ de él deja un camino euleriano de $u$ a $v$.

**Ejemplo con $P_4 = (1,2,3,4)$:** grados $1,2,2,1$: dos impares, el camino euleriano es el grafo mismo. En $C_4$ todos los grados son $2$: ciclo euleriano. En $K_4$ todos los grados son $3$ (cuatro impares): ni uno ni otro.

> [!warning] Condición sobre grados no basta sin conexidad
> Dos triángulos disjuntos tienen todos los grados pares pero no son conexos: ningún ciclo recorre ambos.

## Preguntas de repaso

> [!question]- ¿Por qué todos los vértices de un grafo euleriano tienen grado par?
> Cada paso por un vértice usa una arista para llegar y otra distinta para salir; el inicio y el final del ciclo en ese vértice aportan otro par. Como el ciclo usa todas las aristas una sola vez, las que inciden en $v$ se emparejan y su cantidad es par.

> [!question]- ¿Qué ocurre con el camino euleriano de $K_5$ y con el de $K_4$?
> $K_5$ tiene todos los grados iguales a $4$ (pares) y es conexo, por lo que tiene ciclo euleriano. $K_4$ tiene cuatro vértices de grado $3$ (impar): ni ciclo ni camino euleriano.

> [!question]- ¿Por qué en el paso inductivo se reemplaza un camino de largo $2$ por una arista nueva?
> Para obtener un grafo con menos aristas al que aplicar la hipótesis sin alterar la paridad de ningún grado: $v_1$ y $v_3$ pierden una arista y ganan otra, y $v_2$ pierde dos.
