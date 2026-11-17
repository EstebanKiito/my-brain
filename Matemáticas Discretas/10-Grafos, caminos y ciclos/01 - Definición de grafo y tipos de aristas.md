---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos: []
---

# Definición de grafo y tipos de aristas

Un **grafo** es la forma más simple de modelar "cosas" y "conexiones entre ellas": ciudades y vuelos, personas y amistades, páginas y enlaces. Como toda relación binaria es un conjunto de pares, los grafos son exactamente las relaciones binarias vistas como dibujo, y por eso sirven para casi todo lo que se pueda expresar con una relación.

## Definición: un grafo es una relación binaria

Un **grafo** $G = (V, E)$ es un par donde $V$ es un conjunto de **vértices** (o nodos) y $E \subseteq V \times V$ es una relación binaria sobre $V$ cuyos elementos se llaman **aristas**. Con esta definición general, el grafo es **dirigido**: cada arista $(x, y)$ se dibuja como una flecha de $x$ a $y$.

Ejemplo de motivación: una aerolínea con vuelos Stgo→BsAs, BsAs→Stgo, Londres→París, Moscú→Frankfurt, etc. forma un grafo dirigido cuyos vértices son ciudades. Una pregunta natural ("¿puedo viajar de Santiago a Moscú combinando vuelos?") es una pregunta sobre caminos en ese grafo.

![Grafo dirigido con rulos y aristas paralelas](adjuntos/Grafo%20dirigido%20con%20rulos%20y%20aristas%20paralelas.png)

> [!example]- Transcripción de la imagen
> Grafo con $V = \{1,2,3,4\}$ y doce aristas dibujadas como flechas. Los vértices $1$, $2$ y $4$ tienen una flecha que sale y vuelve a ellos mismos (rulos). Entre casi todos los pares hay dos flechas en sentidos opuestos (aristas paralelas, como $(1,2)$ y $(2,1)$), y las flechas que unen $2$ con $4$ y $1$ con $4$ aparecen en ambos sentidos.

## Rulos, aristas paralelas y grafos simples

- Un **rulo** (*loop*) es una arista $(x, x)$: conecta un vértice consigo mismo.
- Dos aristas $(x, y)$ y $(z, w)$ son **paralelas** si $x = w$ e $y = z$, es decir, si conectan los mismos vértices (en sentidos opuestos).
- Un grafo es **no dirigido** si toda arista tiene una paralela; dicho como relación, si $E$ es **simétrica**. Se dibuja con trazos, sin flechas, y cada par $\{x, y\}$ cuenta como una sola línea.
- Un grafo no dirigido es **simple** si no tiene rulos, es decir, si $E$ es **irrefleja**.

> [!tip] Convención del ramo
> Salvo que se diga otra cosa, "grafo" significa **grafo simple, no dirigido, finito y no vacío**: $V \neq \emptyset$, $\lvert V \rvert = n$, y $E$ simétrica e irrefleja. Dos vértices $x, y$ son **adyacentes** (o vecinos) si $(x, y) \in E$.

![Grafo simple de cuatro vértices](adjuntos/Grafo%20simple%20de%20cuatro%20vértices.png)

> [!example]- Transcripción de la imagen
> Grafo no dirigido sobre $V = \{1,2,3,4\}$ con aristas $\{1,2\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$ (cada una aparece en $E$ en ambos sentidos). Los vértices $1$ y $3$ están arriba y abajo, $2$ y $4$ a los lados; hay una arista horizontal entre $2$ y $4$. No hay rulos.

Este es el grafo que se usa como ejemplo en las demás notas: tiene $5$ aristas, y $\lvert E \rvert$ cuenta cada arista no dirigida una sola vez aunque la relación guarde $10$ pares ordenados.

## Multigrafos

Cuando se necesitan varias aristas entre los mismos vértices (por ejemplo, dos puentes distintos entre las mismas dos orillas) la relación $E$ no alcanza, porque un par aparece una sola vez. Un **multigrafo** es una terna $G = (V, E, f)$ con $f : E \to S$, donde $S$ es el conjunto de pares $\{u, v\}$ de vértices: la función $f$ dice qué dos vértices une cada arista. Con $V = \{1,2,3\}$, $E = \{e_1, e_2, e_3\}$ y $f(e_1) = \{1,2\}$, $f(e_2) = f(e_3) = \{2,3\}$ hay dos aristas paralelas entre $2$ y $3$.

![Puentes de Konigsberg y su grafo](adjuntos/Puentes%20de%20Konigsberg%20y%20su%20grafo.png)

> [!example]- Transcripción de la imagen
> A la izquierda, grabado de un río con una isla y siete puentes rotulados $a$ a $g$ que conectan cuatro zonas de tierra $A$, $B$, $C$ y $D$. A la derecha, el multigrafo correspondiente: cuatro vértices $A, B, C, D$ y siete aristas; $A$–$C$ tiene dos aristas paralelas ($c$, $d$), $A$–$B$ también ($a$, $b$), y hay una arista simple $A$–$D$ ($e$), $C$–$D$ ($g$) y $B$–$D$ ($f$).

Este es el multigrafo de los puentes de Königsberg, que reaparece en [[07 - Ciclos y caminos eulerianos]].

> [!warning] Dirigido no es lo mismo que "con dos flechas"
> Un grafo no dirigido guarda cada arista en los dos sentidos de $E$ porque $E$ es simétrica, pero se **dibuja** y se **cuenta** una vez. Cuando se habla de $\lvert E \rvert$ (por ejemplo en el apretón de manos) se cuentan aristas no dirigidas.

## Preguntas de repaso

> [!question]- ¿Por qué un grafo no dirigido es lo mismo que una relación simétrica?
> Porque que la arista $(x, y)$ tenga una paralela $(y, x)$ significa justamente que $(x, y) \in E \Rightarrow (y, x) \in E$, que es la definición de simetría. Al dibujar se omiten las flechas.

> [!question]- ¿Qué condición sobre $E$ elimina los rulos?
> Que $E$ sea irrefleja: ningún $(x, x)$ pertenece a $E$. Un grafo no dirigido e irreflejo es un grafo simple.

> [!question]- ¿Por qué hace falta la función $f$ en un multigrafo?
> Porque dos aristas distintas pueden unir los mismos vértices, y un conjunto de pares no puede repetir el mismo par. Con $f$ las aristas son objetos propios y $f$ indica sus extremos.
