---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[05 - Caminatas y conectividad]]"
  - "[[07 - Ciclos y caminos eulerianos]]"
---

# Ciclos hamiltonianos

Un recorrido euleriano visita todas las **aristas** una vez; uno hamiltoniano visita todos los **vértices** una vez. Parecen problemas gemelos, pero el primero se decide mirando grados y el segundo no tiene un criterio simple conocido.

## Definición

Un **ciclo hamiltoniano** en $G$ es un ciclo que contiene a todos los vértices de $G$ una única vez cada uno (salvo el inicial, que se repite al final). $G$ es **hamiltoniano** si tiene uno. Es el modelo del "viajero que quiere pasar por cada ciudad una vez y volver".

## Tres grafos de ejemplo

![Tres grafos para ciclos hamiltonianos](adjuntos/Tres%20grafos%20para%20ciclos%20hamiltonianos.png)

> [!example]- Transcripción de la imagen
> Tres grafos dibujados sobre un cuadrado con vértices $v_1$ (arriba izquierda), $v_2$ (arriba derecha), $v_3$ (abajo derecha), $v_4$ (abajo izquierda). $G_1$: el cuadrado más las dos diagonales que se cruzan en un vértice central $v_5$. $G_2$: el cuadrado más la diagonal de $v_1$ a $v_3$, que pasa por $v_5$. $G_3$: el cuadrado más dos recorridos de $v_1$ a $v_3$, uno por $v_5$ y otro por $v_6$.

- **$G_1$ es hamiltoniano:** $(v_1, v_2, v_3, v_4, v_5, v_1)$ usa los cinco vértices una vez. No es euleriano: las esquinas tienen grado $3$.
- **$G_2$ no es hamiltoniano ni euleriano.** Los vértices $v_2$, $v_4$ y $v_5$ tienen grado $2$, así que sus dos aristas quedan forzadas en cualquier ciclo hamiltoniano: $v_1 v_2 v_3$, $v_1 v_4 v_3$ y $v_1 v_5 v_3$. Eso exigiría tres aristas del ciclo en $v_1$, y un ciclo solo admite dos. Tampoco es euleriano: $v_1$ y $v_3$ tienen grado $3$.
- **$G_3$ es euleriano pero no hamiltoniano.** Todos los grados son pares ($4$ en $v_1$ y $v_3$, $2$ en los demás), así que tiene ciclo euleriano. Pero los cuatro vértices de grado $2$ ($v_2, v_4, v_5, v_6$) fuerzan cuatro caminos de largo $2$ entre $v_1$ y $v_3$, es decir cuatro aristas del ciclo en $v_1$: imposible.

Los tres casos (hamiltoniano sin ser euleriano, ninguno, euleriano sin ser hamiltoniano) muestran que **no hay relación** entre ambas propiedades.

> [!tip] Un vértice de grado 2 fija sus dos aristas
> En un ciclo hamiltoniano cada vértice tiene exactamente dos aristas del ciclo. Si un vértice tiene grado $2$, ambas están forzadas. Un vértice de grado $1$ lo hace imposible.

## Dificultad

No se conoce una propiedad simple que decida si un grafo es hamiltoniano, y el problema es **NP-completo**: no se conoce un algoritmo eficiente, aunque verificar un ciclo dado sí es fácil. Contrasta con los ciclos eulerianos, que se deciden mirando conexidad y paridad de grados.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre un ciclo euleriano y uno hamiltoniano?
> El euleriano usa cada **arista** exactamente una vez (los vértices pueden repetirse); el hamiltoniano usa cada **vértice** exactamente una vez (no todas las aristas se recorren).

> [!question]- ¿Por qué $K_n$ con $n \geq 3$ es siempre hamiltoniano?
> Porque todos los pares son adyacentes: cualquier ordenación $(v_1, \dots, v_n)$ de los vértices, cerrada con $v_n v_1$, es un ciclo hamiltoniano.

> [!question]- ¿Puede un grafo con un vértice de grado $1$ ser hamiltoniano?
> No. Un ciclo hamiltoniano necesita dos aristas distintas en cada vértice, y un vértice de grado $1$ solo tiene una.
