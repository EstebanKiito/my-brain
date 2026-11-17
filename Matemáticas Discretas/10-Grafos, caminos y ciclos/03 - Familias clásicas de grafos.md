---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de grafo y tipos de aristas]]"
  - "[[02 - Grado de un vértice y lema del apretón de manos]]"
---

# Familias clásicas de grafos

Algunos grafos aparecen tantas veces que se les da nombre. Para no depender de cómo se rotulan los vértices ni de cómo se dibujan, cada familia se define salvo isomorfismo (ver [[04 - Isomorfismo y complemento de grafos]]): "ser un camino" significa "tener la forma de un camino".

## Camino $P_n$ y ciclo $C_n$

El grafo $G^P_n$ tiene vértices $v_1, \dots, v_n$ y aristas $\{v_i, v_{i+1}\}$ para $i = 1, \dots, n-1$. Un **camino** (de $n$ vértices) es cualquier grafo isomorfo a $G^P_n$; la clase de todos ellos se escribe $P_n$. Informalmente: los vértices se pueden poner en una línea y son adyacentes si y solo si son consecutivos. $P_n$ tiene $n-1$ aristas.

![Camino de seis vértices](adjuntos/Camino%20de%20seis%20vértices.png)

> [!example]- Transcripción de la imagen
> Seis vértices numerados $0$ a $5$ en una fila, cada uno unido al siguiente por una arista: es $P_6$.

El **ciclo** $C_n$ agrega la arista $\{v_n, v_1\}$ que cierra la línea: los vértices se pueden dibujar en un círculo y son adyacentes si y solo si son consecutivos. $C_n$ tiene $n$ aristas y todos sus vértices tienen grado $2$.

![Ciclo de siete vértices](adjuntos/Ciclo%20de%20siete%20vértices.png)

> [!example]- Transcripción de la imagen
> Siete vértices numerados $0$ a $6$ dispuestos en círculo, cada uno unido solo a sus dos vecinos inmediatos del círculo (el $6$ con el $0$): es $C_7$.

## Grafo completo $K_n$

Un grafo es **completo** si todos los pares de vértices son adyacentes; $K_n$ es la clase de los completos de $n$ vértices. Tiene $\binom{n}{2} = \frac{n(n-1)}{2}$ aristas y todos sus vértices tienen grado $n - 1$.

![Grafo completo K5](adjuntos/Grafo%20completo%20K5.png)

> [!example]- Transcripción de la imagen
> Cinco vértices $1$ a $5$ con una arista entre cada par (diez aristas): $K_5$ dibujado como pentágono con todas sus diagonales.

Comprobación con el lema del apretón de manos: $5$ vértices de grado $4$ suman $20 = 2 \cdot 10$.

## Grafos bipartitos y $K_{n,m}$

Un grafo es **bipartito** si $V$ se puede partir en dos conjuntos no vacíos $V_1$ y $V_2$ ($V = V_1 \cup V_2$, $V_1 \cap V_2 = \emptyset$) tales que **toda arista une un vértice de $V_1$ con uno de $V_2$**: dentro de cada parte no hay aristas. Sirve para modelar relaciones entre dos tipos de objetos distintos (alumnos y cursos, trabajadores y tareas).

![Grafo bipartito con partición](adjuntos/Grafo%20bipartito%20con%20partición.png)

> [!example]- Transcripción de la imagen
> Cinco vértices con aristas $\{1,3\}$, $\{2,3\}$ y $\{2,5\}$; el vértice $4$ queda aislado. Una partición válida es $V_1 = \{1, 2\}$ y $V_2 = \{3, 4, 5\}$, pues cada arista une un vértice de $\{1,2\}$ con uno de $\{3,4,5\}$.

El **bipartito completo** $K_{n,m}$ tiene partes de tamaños $n$ y $m$ y **todas** las aristas posibles entre las partes, $n \cdot m$ en total.

![Grafo bipartito completo K2-3](adjuntos/Grafo%20bipartito%20completo%20K2-3.png)

> [!example]- Transcripción de la imagen
> Partes $\{1, 2\}$ y $\{3, 4, 5\}$ con las seis aristas posibles entre ellas (cada uno de $1$ y $2$ unido a $3$, $4$ y $5$): es $K_{2,3}$.

> [!warning] La partición no es única ni tiene por qué ser "visible"
> Que un dibujo no se vea en dos columnas no significa que no sea bipartito: un ciclo $C_4$ dibujado como cuadrado lo es. En [[06 - Grafos bipartitos y ciclos impares]] se caracteriza exactamente cuáles lo son. Además, un vértice aislado como el $4$ puede ir en cualquiera de las dos partes.

| Familia | Vértices | Aristas | Grados |
|---|---|---|---|
| $P_n$ | $n$ | $n-1$ | extremos $1$, resto $2$ |
| $C_n$ ($n \ge 3$) | $n$ | $n$ | todos $2$ |
| $K_n$ | $n$ | $\binom{n}{2}$ | todos $n-1$ |
| $K_{n,m}$ | $n + m$ | $nm$ | $m$ en una parte, $n$ en la otra |

## Preguntas de repaso

> [!question]- ¿Por qué se definen $P_n$ y $C_n$ como clases de isomorfismo y no como un grafo concreto?
> Porque los nombres de los vértices y la forma del dibujo son irrelevantes: lo que importa es la estructura de adyacencias. Definirlos por isomorfismo hace que cualquier rotulación o dibujo de la misma estructura "sea" un camino o un ciclo.

> [!question]- ¿Cuántas aristas tiene $K_{3,4}$ y cuántas $K_7$?
> $K_{3,4}$ tiene $3 \cdot 4 = 12$ aristas y $K_7$ tiene $\binom{7}{2} = 21$.

> [!question]- ¿Es $K_3$ bipartito?
> No. Con tres vértices mutuamente adyacentes, dos de ellos caerían en la misma parte y tendrían una arista entre sí. Un triángulo es un ciclo de largo impar, y esos grafos nunca son bipartitos.
