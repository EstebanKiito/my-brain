---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles y caracterizaciones equivalentes]]"
  - "[[02 - Hojas, poda y número de aristas de un árbol]]"
---

# Bosques y árboles generadores

Dado un grafo conexo, a menudo interesa quedarse con "lo justo" para mantenerlo conectado: un árbol que toque todos los vértices. Eso es un **árbol generador** (o de cobertura). Los bosques sirven para hablar del mismo problema cuando el grafo no es conexo.

## Árboles generadores

> [!tip] Definición
> Un **árbol generador** de un grafo $G$ es un subgrafo de $G$ que es un árbol y contiene a todos los vértices de $G$.

Un grafo tiene árbol generador si y solo si es conexo. Para construirlo se parte de $G$ y, mientras quede un ciclo, se quita una de sus aristas: quitar una arista de un ciclo no desconecta el grafo y cada paso elimina un ciclo. Cuando no quedan ciclos el grafo es conexo y acíclico, es decir, un árbol, y conserva todos los vértices.

Como el resultado tiene $n - 1$ aristas, si $G$ tiene $m$ aristas se quitan exactamente $m - (n - 1)$.

![Grafo simple de siete vértices](adjuntos/Grafo%20simple%20de%20siete%20v%C3%A9rtices.png)

> [!example]- Transcripción de la imagen
> Grafo $G$ con vértices $a, \dots, g$ y nueve aristas: $ab$, $ae$, $bf$, $cf$, $cd$, $cg$, $ef$, $fg$ y $eg$ (esta última dibujada como arco curvo bajo $f$). Es conexo pero tiene ciclos, por ejemplo $a, b, f, e, a$.

Aquí $n = 7$ y $m = 9$, así que hay que quitar $9 - 6 = 3$ aristas. Se eligen $ae$, $ef$ y $cg$:

![Árbol generador del grafo](adjuntos/%C3%81rbol%20generador%20del%20grafo.png)

> [!example]- Transcripción de la imagen
> Los mismos siete vértices con seis aristas: $ab$, $bf$, $cf$, $cd$, $fg$ y $eg$. Es conexo y sin ciclos: $a$-$b$-$f$-$c$-$d$ forma una cadena, y $f$-$g$-$e$ cuelga de $f$. Es un árbol generador de $G$.

Hay muchas elecciones posibles: este grafo tiene $29$ árboles generadores distintos (se recomputa enumerando los subconjuntos de $6$ aristas que conectan los $7$ vértices).

## Bosques

Un **bosque** es un grafo en que dos vértices tienen a lo más un camino entre ellos; sus componentes conexas son árboles. Dos consecuencias útiles:

- Un bosque con $n$ vértices y $c$ componentes tiene $n - c$ aristas.
- **Todo bosque es bipartito**: se colorea cada árbol por separado (por paridad de la distancia a una raíz elegida en él) y los colores de componentes distintas no interactúan.

> [!warning] Árbol generador no es único ni mínimo en peso
> "Generador" solo exige conectar todos los vértices sin ciclos. Si las aristas tienen pesos y se quiere el de menor costo, es el problema de los árboles de cobertura mínima (ver [[01 - Árboles de cobertura mínima y cortes]]).

## Preguntas de repaso

> [!question]- ¿Por qué quitar una arista de un ciclo no desconecta el grafo?
> Porque el resto del ciclo da un camino alternativo entre los extremos de la arista quitada.

> [!question]- ¿Cuántas aristas se deben quitar de un grafo conexo con $12$ vértices y $20$ aristas para obtener un árbol generador?
> $20 - 11 = 9$.

> [!question]- ¿Puede un grafo desconexo tener árbol generador?
> No: un árbol es conexo y contiene todos los vértices, así que el grafo original debería serlo. Sí tiene un **bosque generador**.

> [!question]- ¿Por qué un bosque es bipartito aunque sea desconexo?
> Cada componente es un árbol (bipartito) y se pueden unir las clases de color de todas las componentes: no hay aristas entre componentes que impidan hacerlo.
