---
ramo: "Estructuras de Datos"
tema: "Árboles balanceados"
tags:
  - edd
  - avl
  - balance
  - abb
  - origen/complemento
prerrequisitos:
  - "[[03 - Eliminación en un ABB]]"
---

# Árboles AVL y propiedad de balance

Un [[01 - Diccionarios y árboles binarios de búsqueda|ABB]] garantiza **orden**, y sus operaciones cuestan $O(\log n)$ en promedio, pero $O(n)$ en el peor caso, cuando degenera en lista. Para garantizar el logaritmo hay que **controlar la altura**. Los **árboles AVL** lo hacen rebalanceando después de cada modificación, con un costo extra pequeño.

![ABB colapsado sobre una recta](adjuntos/ABB%20colapsado%20sobre%20una%20recta.png)

> [!example]- Transcripción de la imagen
> El ABB con raíz 6, hijos 3 y 8 y nietos 1, 4, 7 y 9. "Y la gracia es que si colapsamos los nodos…" quedan en orden sobre una recta: 1, 3, 4, 6, 7, 8, 9. El in-order de un ABB es la secuencia ordenada.

![Propiedad de balance](adjuntos/Propiedad%20de%20balance.png)

> [!example]- Transcripción de la imagen
> La *propiedad de balance* debe cumplir dos condiciones: 1. asegurar que la altura de un árbol con $n$ nodos sea $\mathcal{O}(\log n)$; 2. ser fácil de mantener. Este último punto es limitante: el (re)balanceo después de las operaciones debe costar **no más** que $\mathcal{O}(\log n)$, para que las operaciones sigan siendo $\mathcal{O}(\log n)$.

## La definición

> [!tip] Árbol AVL
> Un ABB está **AVL-balanceado** si (1) las alturas de los subárboles izquierdo y derecho de la raíz **difieren a lo más en 1** y (2) cada hijo también está AVL-balanceado, recursivamente.

![Subárboles de alturas distintas](adjuntos/Sub%C3%A1rboles%20de%20alturas%20distintas.png)

> [!example]- Transcripción de la imagen
> Un nodo $X$ con dos subárboles $T_1$ y $T_2$ de alturas distintas, marcadas con líneas punteadas por nivel: $T_2$ llega un nivel más abajo que $T_1$. Mientras la diferencia sea a lo más 1, $X$ está balanceado.

Se define el **balance** de un nodo como $h(\text{derecho}) - h(\text{izquierdo})$. En un AVL todos los nodos tienen balance $-1$, $0$ o $+1$. Un $\pm 2$ indica desbalance: negativo si sobra a la izquierda y positivo si sobra a la derecha.

## Las inserciones desbalancean

![Árbol antes de insertar B](adjuntos/%C3%81rbol%20antes%20de%20insertar%20B.png)

> [!example]- Transcripción de la imagen
> AVL con raíz T; hijos K e Y; K tiene hijos F y N; Y tiene hijo V; F tiene hijos E y H.

![Inserción de B desbalancea T y K](adjuntos/Inserci%C3%B3n%20de%20B%20desbalancea%20T%20y%20K.png)

> [!example]- Transcripción de la imagen
> "Ahora hay desbalance en los nodos T y K": se insertó B como hijo izquierdo de E (en verde), y T y K quedaron marcados en rojo.

La clave es que **basta con arreglar el primer nodo desbalanceado** al subir desde la inserción. Antes de insertar, el árbol estaba balanceado; si se corrige ese desbalance puntual de modo que el subárbol recupere su altura anterior, todos los ancestros vuelven a estar balanceados. La corrección es una **rotación**, que solo reasigna punteros: $O(1)$.

## Altura de un AVL: $O(\log n)$

¿Cuál es el AVL **más alto** posible con $n$ nodos? Equivale a preguntar por el AVL de altura $h$ con la **menor** cantidad de nodos $N(h)$: una raíz con un subárbol mínimo de altura $h-1$ y otro de altura $h-2$, que es el máximo desbalance permitido.

$$N(h) = N(h-1) + N(h-2) + 1, \qquad N(0) = 0,\ N(1) = 1$$

Es una recurrencia tipo **Fibonacci**: 0, 1, 2, 4, 7, 12, 20, 33, 54, … y crece exponencialmente en $h$. Por lo tanto $h \in O(\log n)$: incluso el AVL más desbalanceado posible tiene altura logarítmica (a lo más unas $1{,}44 \log_2 n$).

| Operación | Costo |
|---|---|
| Buscar | $O(h) = O(\log n)$ |
| Insertar (buscar + subir revisando balances + a lo más una rotación) | $O(h + h + 1) = O(\log n)$ |
| Rotar | $O(1)$ |

## Preguntas de repaso

> [!question]- ¿Qué dos condiciones debe cumplir una buena propiedad de balance?
> Que garantice altura $O(\log n)$ y que sea barata de mantener: el rebalanceo no puede costar más que $O(\log n)$ por operación.

> [!question]- ¿Por qué basta con corregir el primer nodo desbalanceado desde la inserción hacia arriba?
> Porque el árbol estaba balanceado antes de insertar. La rotación deja ese subárbol con la misma altura que tenía antes de la inserción, y para los ancestros nada cambió.

> [!question]- ¿Por qué la altura de un AVL es $O(\log n)$?
> Porque el mínimo número de nodos de un AVL de altura $h$ cumple $N(h) = N(h-1) + N(h-2) + 1$, que crece como Fibonacci, es decir, exponencialmente. Despejando, $h$ es logarítmico en $n$.

> [!question]- ¿Qué valores puede tomar el balance de un nodo en un AVL?
> $-1$, $0$ o $+1$. Un $\pm 2$ aparece solo transitoriamente después de una inserción o eliminación, y se corrige con rotaciones.
