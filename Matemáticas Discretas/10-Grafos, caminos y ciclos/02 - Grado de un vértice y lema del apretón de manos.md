---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de grafo y tipos de aristas]]"
---

# Grado de un vértice y lema del apretón de manos

Contar cuántas aristas toca cada vértice es la primera medida cuantitativa de un grafo. Su propiedad más útil es una igualdad global: la suma de los grados está atada al número de aristas, lo que permite descartar grafos imposibles sin dibujarlos.

## Grado, vecindad y matrices

El **grado** $\delta_G(v)$ de un vértice es la cantidad de aristas que inciden en él. La **vecindad** de $v$ es el conjunto de sus vecinos, $N_G(v) = \{u \mid (v, u) \in E\}$. En un grafo simple, $\delta_G(v) = \lvert N_G(v) \rvert$.

Como $E$ es una relación binaria, un grafo se puede guardar en una matriz. Para el grafo de aristas $\{1,2\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$:

- La **matriz de adyacencia** $M_G$ tiene un $1$ en la posición $(i, j)$ si $(i, j) \in E$. Es simétrica si el grafo es no dirigido y tiene diagonal de ceros si es simple.
- La **matriz de incidencia** $A_G$ tiene una fila por vértice y una columna por arista (previamente etiquetada), con un $1$ si la arista incide en el vértice.

$$M_G = \begin{pmatrix} 0&1&0&1 \\ 1&0&1&1 \\ 0&1&0&1 \\ 1&1&1&0 \end{pmatrix}, \qquad A_G = \begin{pmatrix} 1&1&0&0&0 \\ 1&0&1&1&0 \\ 0&0&1&0&1 \\ 0&1&0&1&1 \end{pmatrix}$$

(columnas de $A_G$ en el orden $e_1 = \{1,2\}$, $e_2 = \{1,4\}$, $e_3 = \{2,3\}$, $e_4 = \{2,4\}$, $e_5 = \{3,4\}$). El grado de un vértice es la suma de su fila en cualquiera de las dos matrices: aquí $(2, 3, 2, 3)$.

## Lema del apretón de manos

> [!tip] Handshaking lemma
> En un grafo sin rulos, $\sum_{v \in V} \delta_G(v) = 2\lvert E \rvert$: la suma de los grados es el doble de la cantidad de aristas.

**Por qué:** en la matriz de incidencia, sumar una fila da el grado del vértice, así que la suma de todos los grados es la suma de todas las entradas. Pero cada columna (arista) tiene exactamente dos unos, porque una arista sin rulo toca dos vértices; sumando por columnas se obtiene $2\lvert E \rvert$. Ambas sumas son la misma, y de ahí la igualdad. Con el ejemplo: $2 + 3 + 2 + 3 = 10 = 2 \cdot 5$.

La imagen mental es que cada arista "aporta un extremo" a dos vértices: contar extremos por vértice o por arista da el mismo total.

## Consecuencia: los grados impares vienen de a pares

> [!tip] Corolario
> En un grafo sin rulos hay una cantidad par de vértices de grado impar.

Se separa $V$ en $V_I$ (grado impar) y $V_P$ (grado par). La suma de los grados de $V_P$ es par, y la suma total es par ($2\lvert E \rvert$), luego la suma de los grados de $V_I$ también es par. Una suma de números impares es par solo si hay una cantidad par de sumandos, así que $\lvert V_I \rvert$ es par.

**Aplicación:** en un departamento de $15$ personas, la secretaria y el jefe saludan a todos ($14$ saludos cada uno) y cada uno de los otros $13$ asegura saludarse con exactamente $3$ compañeros sin contar a la secretaria ni al jefe. Cada uno de esos $13$ tiene entonces grado $3 + 2 = 5$. La suma de grados es $14 + 14 + 13 \cdot 5 = 93$, que es impar: no puede ser el doble de un número, así que **es imposible**. Equivalentemente, habría $13$ vértices de grado impar, cantidad impar.

> [!warning] Los rulos rompen la fórmula estándar
> El lema supone que cada arista tiene dos extremos distintos. Un rulo aporta una sola arista pero toca un único vértice, así que el conteo por columnas ya no da $2$. Por eso el enunciado dice "sin rulos".

## Preguntas de repaso

> [!question]- ¿Por qué cada columna de la matriz de incidencia suma exactamente $2$?
> Porque una arista de un grafo sin rulos incide en exactamente dos vértices distintos, sus extremos. Con un rulo habría un único vértice, y la columna sumaría $1$ o $2$ según la convención.

> [!question]- ¿Existe un grafo simple con grados $3, 3, 3, 1$ (cuatro vértices)?
> No, aunque cumple el lema: la suma es $10 = 2 \cdot 5$ y hay cuatro vértices de grado impar. En un grafo simple de $4$ vértices, uno de grado $3$ está unido a todos los demás, así que el vértice de grado $1$ sería adyacente a los tres de grado $3$ y tendría grado $3$. El lema es una condición necesaria, no suficiente.

> [!question]- ¿Puede haber un grafo con exactamente $5$ vértices de grado impar?
> No. Por el corolario del apretón de manos la cantidad de vértices de grado impar es par.
