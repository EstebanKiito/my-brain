---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[03 - Familias clásicas de grafos]]"
  - "[[05 - Caminatas y conectividad]]"
---

# Grafos bipartitos y ciclos impares

Decidir si un grafo es bipartito parece requerir probar todas las particiones posibles. Hay una caracterización simple: un grafo conexo es bipartito exactamente cuando no contiene ciclos de largo impar. La demostración usa inducción (ver [[03 - Inducción fuerte]]) en un lema sobre caminatas cerradas y construye la partición explícitamente.

## Lema de la caminata cerrada impar

> [!tip] Lema
> En un grafo simple, toda caminata cerrada de largo impar contiene un ciclo de largo impar.

**Idea:** si una caminata cerrada no repite vértices, ya es un ciclo. Si repite un vértice $v$, se parte en dos caminatas cerradas que parten y terminan en $v$; sus largos suman un número impar, así que **una de las dos es impar** y es estrictamente más corta. Se aplica el mismo argumento a esa.

**Demostración** por inducción fuerte en el largo $\ell$ (impar) de la caminata cerrada $C$:

- **Caso base:** la caminata cerrada impar más corta tiene largo $3$ (un triángulo), que ya es un ciclo impar. Un largo $1$ requeriría un rulo, que no existe en un grafo simple.
- **Hipótesis:** toda caminata cerrada de largo impar menor que $\ell$ contiene un ciclo impar.
- **Paso:** si $C$ no repite vértices, es un ciclo impar. Si repite $v$, se parte en $C'$ y $C''$ cerradas en $v$ con $\lvert C' \rvert + \lvert C'' \rvert = \ell$. No pueden ser ambas pares; la impar tiene largo $< \ell$ y por hipótesis contiene un ciclo impar, que también está en $C$.

## Teorema de caracterización

> [!tip] Teorema
> Un grafo simple **conexo** $G$ es bipartito si y solo si no contiene ningún ciclo de largo impar.

($\Rightarrow$) Si $G$ tuviera un ciclo impar $(v_1, \dots, v_k, v_1)$ y fuera bipartito con $v_1 \in V_1$, las aristas obligarían a $v_2 \in V_2$, $v_3 \in V_1$, y así: $v_i \in V_1$ si $i$ es impar. Como $k$ es impar, $v_k \in V_1$, pero $v_k$ es adyacente a $v_1 \in V_1$, contradiciendo que no hay aristas dentro de una parte.

($\Leftarrow$) Sin ciclos impares, se fija un vértice $v$ y se define
$$V_1 = \{u \mid \exists \text{ camino de largo impar de } v \text{ a } u\}, \qquad V_2 = \{u \mid \exists \text{ camino de largo par de } v \text{ a } u\}.$$
Si hubiera una arista $\{u_1, u_2\}$ con ambos en $V_1$ (o ambos en $V_2$), los dos caminos desde $v$ más esa arista formarían una caminata cerrada de largo impar (impar + impar + $1$, o par + par + $1$), que por el lema contiene un ciclo impar: contradicción. Como $G$ es conexo, $V_1 \cup V_2 = V$ (todo vértice se alcanza por algún camino), y no hay aristas dentro de cada parte: $G$ es bipartito.

**Ejemplos.** $C_4$ es bipartito (partes $\{1,3\}$ y $\{2,4\}$), $C_5$ no, y $K_{n,m}$ nunca tiene ciclos impares. Un grafo con un triángulo no es bipartito.

![Grafo bipartito con partición](adjuntos/Grafo%20bipartito%20con%20partición.png)

> [!example]- Transcripción de la imagen
> El mismo grafo bipartito de la nota de familias: aristas $\{1,3\}, \{2,3\}, \{2,5\}$ y vértice $4$ aislado. Desde $v = 1$: el $3$ está a distancia $1$ (impar), el $2$ a distancia $2$ (par) y el $5$ a distancia $3$ (impar); así $V_1 = \{3, 5\}$ y $V_2 = \{1, 2\}$, con el vértice $4$ fuera por no ser alcanzable (el grafo no es conexo).

## Si el grafo no es conexo y el algoritmo

Si $G$ no es conexo, se aplica el criterio a cada componente: $G$ es bipartito si y solo si cada componente lo es (y las particiones se combinan). El vértice aislado del ejemplo se pone en cualquier parte.

Esto da un algoritmo para decidir si un grafo es bipartito y justificar la respuesta: se recorre cada componente por niveles desde un vértice, coloreando por paridad de la distancia. Si aparece una arista entre vértices del mismo color, el ciclo impar que esa arista cierra es la **muestra** de que no es bipartito; si no aparece ninguna, los colores dan la partición.

## Preguntas de repaso

> [!question]- ¿Por qué basta que una de las dos partes de la caminata cerrada sea impar?
> Porque la suma de dos números pares es par, así que si el total es impar al menos un sumando es impar. Esa parte es una caminata cerrada impar estrictamente más corta, a la que se aplica la hipótesis de inducción.

> [!question]- ¿Por qué el teorema pide $G$ conexo en la implicancia ($\Leftarrow$)?
> Porque los conjuntos $V_1$ y $V_2$ solo contienen vértices alcanzables desde $v$. Si $G$ no es conexo, los vértices de otras componentes quedarían fuera de la partición; se arregla aplicando el argumento componente a componente.

> [!question]- ¿Es bipartito un grafo con un ciclo de largo $6$ y uno de largo $5$?
> No: contiene un ciclo de largo impar ($5$), y por el teorema (en cada componente) eso basta para que no sea bipartito.
