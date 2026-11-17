---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - origen/complemento
prerrequisitos: []
---

# Árboles y caracterizaciones equivalentes

Un **árbol** es el grafo conexo más económico posible: conecta todos los vértices sin ninguna arista de sobra. Aparece cada vez que se quiere comunicar n puntos con el mínimo de enlaces (una red de computadores, una jerarquía, una estructura de datos), y existen varias formas equivalentes de definirlo; elegir la más cómoda en cada demostración es la mitad del trabajo.

## La definición y la idea de la red mínima

> [!tip] Definición
> Un grafo $T = (V, E)$ es un **árbol** si para cada par de vértices $x, y \in V$ existe **un único camino** entre ellos.

Como siempre existe un camino, un árbol es conexo. Si se relaja la condición a "si existe un camino entre $x$ e $y$, es único", se obtiene un **bosque**: un grafo que se ve como un conjunto de árboles separados.

![Red de computadores con el mínimo de conexiones](adjuntos/Red%20de%20computadores%20con%20el%20m%C3%ADnimo%20de%20conexiones.png)

> [!example]- Transcripción de la imagen
> - Nueve computadores unidos por ocho cables directos.
> - Cualquier computador puede enviar información a cualquier otro, pasando por intermedios.
> - Entre cada par de computadores hay una única ruta: si se cortara un cable, la red quedaría partida en dos.

Si se agregara un cable más entre dos computadores ya comunicados, aparecería una segunda ruta (un ciclo) y ese cable sería redundante. Un árbol es exactamente la red sin redundancia.

![Un árbol con diez vértices](adjuntos/Un%20%C3%A1rbol%20con%20diez%20v%C3%A9rtices.png)

> [!example]- Transcripción de la imagen
> Árbol de diez vértices $v_1, \dots, v_{10}$ con nueve aristas: $v_1v_7$, $v_7v_3$, $v_2v_3$, $v_2v_6$, $v_9v_3$, $v_{10}v_3$, $v_{10}v_5$, $v_4v_5$, $v_4v_8$. Entre cualquier par hay un solo camino; por ejemplo, de $v_6$ a $v_8$ el único camino es $v_6, v_2, v_3, v_{10}, v_5, v_4, v_8$.

## Tres definiciones equivalentes

> [!tip] Teorema
> Para un grafo $T = (V, E)$ son equivalentes:
> 1. entre cada par de vértices hay un único camino;
> 2. $T$ es **conexo y acíclico** (sin ciclos);
> 3. $T$ es conexo y **todas sus aristas son de corte** (quitar cualquiera lo desconecta).

**(1 ⇒ 2).** Un árbol es conexo. Si tuviera un ciclo por $u$ y $v$, el ciclo se parte en dos caminos distintos de $u$ a $v$ (distintos porque un ciclo no repite aristas), lo que contradice la unicidad.

![Dos caminos distintos forman un ciclo](adjuntos/Dos%20caminos%20distintos%20forman%20un%20ciclo.png)

> [!example]- Transcripción de la imagen
> Un ciclo $C$ que pasa por $u$ y $v$; sus dos mitades son los caminos $p_1$ (arriba) y $p_2$ (abajo) entre $u$ y $v$.

**(2 ⇒ 1).** Por conexión hay al menos un camino. Si hubiera dos distintos $p_1, p_2$ entre $u$ y $v$, se toma el vértice $x$ justo antes de que se separen y el siguiente vértice $y$ que vuelven a compartir: los tramos de $x$ a $y$ por $p_1$ y por $p_2$ forman un ciclo, contra la hipótesis.

![Dos caminos entre u y v contienen un ciclo](adjuntos/Dos%20caminos%20entre%20u%20y%20v%20contienen%20un%20ciclo.png)

> [!example]- Transcripción de la imagen
> Los caminos $p_1$ y $p_2$ salen de $u$, coinciden hasta $x$, se separan entre $x$ e $y$ (dos arcos distintos) y vuelven a coincidir de $y$ a $v$. El "ojo" entre $x$ e $y$ es el ciclo.

**(2 ⇔ 3).** Una arista $e = \{u,v\}$ es de corte si y solo si no pertenece a ningún ciclo: si está en un ciclo, el resto del ciclo da otro camino de $u$ a $v$ y quitar $e$ no desconecta; si $T - e$ sigue conexo, un camino de $u$ a $v$ en $T - e$ más $e$ cierra un ciclo. Luego "conexo y sin ciclos" equivale a "conexo y ninguna arista en un ciclo", es decir, todas de corte.

> [!warning] "Acíclico" no basta solo
> Un grafo acíclico pero desconexo es un bosque, no un árbol. Las dos condiciones (conexo y acíclico) van juntas.

## Preguntas de repaso

> [!question]- ¿Por qué un ciclo contradice la unicidad del camino?
> Dos vértices cualesquiera de un ciclo quedan unidos por dos caminos que usan aristas distintas, así que habría dos caminos entre ellos.

> [!question]- ¿Qué diferencia hay entre un árbol y un bosque?
> En un bosque basta con que el camino sea único cuando existe; un árbol exige además que exista, es decir, que sea conexo. Un bosque es una unión de árboles.

> [!question]- ¿Por qué todas las aristas de un árbol son de corte?
> Porque ninguna está en un ciclo: al quitar una arista $\{u,v\}$, el único camino entre $u$ y $v$ era la propia arista, y ya no queda ninguno.

> [!question]- ¿Cómo se usa la equivalencia en una demostración?
> Se elige la forma más cómoda: "sin ciclos" para probar que algo no se repite, "camino único" para definir funciones desde la raíz, "aristas de corte" para argumentos de desconexión.
