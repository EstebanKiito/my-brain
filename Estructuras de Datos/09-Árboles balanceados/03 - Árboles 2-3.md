---
ramo: "Estructuras de Datos"
tema: "Árboles balanceados"
tags:
  - edd
  - arbol-2-3
  - balance
  - split
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles AVL y propiedad de balance]]"
---

# Árboles 2-3

El AVL inserta, revisa si se desbalanceó y después arregla. El **árbol 2-3** sigue otra estrategia: permite nodos con **más de una llave**, de modo que al insertar **nunca** se pierde el balance. Todas las hojas quedan siempre al **mismo nivel**, y el árbol solo crece en altura desde la raíz.

## Nodos 2 y nodos 3

- **2-nodo:** una llave $k$; si no es hoja, tiene exactamente **2 hijos**.
- **3-nodo:** dos llaves ordenadas $k_1 < k_2$; si no es hoja, tiene exactamente **3 hijos**.

Un nodo tiene **todos** sus hijos o **ninguno**. Por eso no hay "ramas cortas": las hojas están todas a la misma profundidad.

![Orden de llaves en nodos 2 y 3](adjuntos/Orden%20de%20llaves%20en%20nodos%202%20y%203.png)

> [!example]- Transcripción de la imagen
> Si es 2-nodo con llave $k$: las llaves $k'$ del hijo izquierdo cumplen $k' < k$ y las $k''$ del derecho, $k < k''$. Si es 3-nodo con llaves $k_1 < k_2$: hijo izquierdo $k' < k_1$, hijo central $k_1 < k'' < k_2$, hijo derecho $k_2 < k'''$.

![Nodo 2](adjuntos/Nodo%202.png)

> [!example]- Transcripción de la imagen
> Un nodo con llave X y dos subárboles: a la izquierda las llaves $k' < X$ y a la derecha las $X < k''$.

![Nodo 3](adjuntos/Nodo%203.png)

> [!example]- Transcripción de la imagen
> Un nodo con llaves X e Y y tres subárboles: izquierdo $k' < X$; central $X < k''$ y $k'' < Y$; derecho "$X < k'''$".

![Ejemplo de árbol 2-3](adjuntos/Ejemplo%20de%20%C3%A1rbol%202-3.png)

> [!example]- Transcripción de la imagen
> "Un ejemplo de árbol 2-3 con llaves alfabéticas": raíz M (nodo 2); hijos E J (nodo 3) y R (nodo 2); hojas A C, H, L (hijos de E J) y P, S X (hijos de R). Flechas rojas señalan "nodos 3" y "nodos 2".

Sigue siendo un **árbol de búsqueda**: buscar es como en un ABB, pero en un 3-nodo hay tres caminos en vez de dos.

![Búsqueda de X en un árbol 2-3](adjuntos/B%C3%BAsqueda%20de%20X%20en%20un%20%C3%A1rbol%202-3.png)

> [!example]- Transcripción de la imagen
> "Buscamos la llave X": $X > M$ baja a la derecha, a R; $X > R$ baja a la derecha, a la hoja S X; allí $X > S$ y $X = X$, encontrada.

Lo mismo pasa con recorrer en orden: el in-order de un ABB se adapta con dos casos. Un 2-nodo recorre izquierdo, llave y derecho; un 3-nodo recorre izquierdo, $k_1$, central, $k_2$ y derecho.

## Inserción con split

![Estrategia de inserción en un árbol 2-3](adjuntos/Estrategia%20de%20inserci%C3%B3n%20en%20un%20%C3%A1rbol%202-3.png)

> [!example]- Transcripción de la imagen
> "Al insertar llaves seguiremos la siguiente estrategia": se inserta como llave múltiple en una hoja existente; si la hoja era 2-nodo, queda como 3-nodo y se termina; si era 3-nodo, queda como 4-nodo (con 3 llaves) por ahora; la llave central del 4-nodo sube como llave múltiple al padre (**split**); se repite recursivamente hacia la raíz. "El árbol solo crece en altura cuando la raíz se llena al recibir una llave desde un hijo".

Ejemplo: insertar D, A, C, E, N, F, H en un árbol vacío.

![D](adjuntos/Inserci%C3%B3n%202-3%20-%20D.png)

> [!example]- Transcripción de la imagen
> El árbol tiene una sola hoja con D.

![A](adjuntos/Inserci%C3%B3n%202-3%20-%20A.png)

> [!example]- Transcripción de la imagen
> Se inserta A en la misma hoja, que pasa a ser el 3-nodo A D.

![C forma un 4-nodo](adjuntos/Inserci%C3%B3n%202-3%20-%20C%20forma%20un%204-nodo.png)

> [!example]- Transcripción de la imagen
> Al insertar C, la hoja queda A C D (un 4-nodo inválido, marcado en rojo).

![split con C en la raíz](adjuntos/Inserci%C3%B3n%202-3%20-%20split%20con%20C%20en%20la%20ra%C3%ADz.png)

> [!example]- Transcripción de la imagen
> Split: la llave central C sube y forma una raíz nueva con hijos A y D. El árbol creció en altura.

![E](adjuntos/Inserci%C3%B3n%202-3%20-%20E.png)

> [!example]- Transcripción de la imagen
> Se inserta E en la hoja D, que queda como el 3-nodo D E.

![N forma un 4-nodo](adjuntos/Inserci%C3%B3n%202-3%20-%20N%20forma%20un%204-nodo.png)

> [!example]- Transcripción de la imagen
> Al insertar N, la hoja queda D E N (4-nodo, marcado en rojo).

![E sube a la raíz](adjuntos/Inserci%C3%B3n%202-3%20-%20E%20sube%20a%20la%20ra%C3%ADz.png)

> [!example]- Transcripción de la imagen
> Split: E sube a la raíz, que queda C E con hijos A, D y N.

![F y H forman un 4-nodo](adjuntos/Inserci%C3%B3n%202-3%20-%20F%20y%20H%20forman%20un%204-nodo.png)

> [!example]- Transcripción de la imagen
> Al insertar F y H en la hoja de N, queda F H N (4-nodo).

![la raíz se llena](adjuntos/Inserci%C3%B3n%202-3%20-%20la%20ra%C3%ADz%20se%20llena.png)

> [!example]- Transcripción de la imagen
> Split de F H N: H sube y la raíz queda C E H, ahora un 4-nodo, con hijos A, D, F y N.

![el árbol crece en altura](adjuntos/Inserci%C3%B3n%202-3%20-%20el%20%C3%A1rbol%20crece%20en%20altura.png)

> [!example]- Transcripción de la imagen
> Split de la raíz: E sube como nueva raíz, con hijos C (hijos A y D) y H (hijos F y N). "Hora de crecer": el árbol aumentó un nivel y todas las hojas siguen al mismo nivel.

> [!tip] Por qué la altura es $O(\log n)$
> El árbol solo crece cuando la **raíz** hace split, y en ese caso todas las hojas bajan un nivel a la vez. Así, todas siguen a la misma profundidad, y como cada nodo tiene al menos 2 hijos, la altura es a lo más $\log_2 n$.

En la práctica, los árboles 2-3 se usan poco tal cual, porque manejar nodos de distintos tamaños es engorroso. Su valor está en que explican los **árboles rojo-negro** y los **árboles B+** de las bases de datos.

## Preguntas de repaso

> [!question]- ¿Por qué en un árbol 2-3 todas las hojas están al mismo nivel?
> Porque nunca se agregan niveles abajo. Las inserciones llenan hojas existentes y los splits empujan llaves hacia arriba. El árbol solo crece cuando la raíz hace split, y eso baja todas las hojas a la vez.

> [!question]- ¿Qué es un split y cuándo ocurre?
> Cuando un nodo queda con 3 llaves (4-nodo), se separa en dos 2-nodos y la llave central sube al padre. Si el padre también se llena, se repite hacia arriba.

> [!question]- ¿Cómo cambia el recorrido in-order respecto de un ABB?
> En un 3-nodo se visita hijo izquierdo, primera llave, hijo central, segunda llave e hijo derecho. En un 2-nodo es igual que en un ABB.

> [!question]- ¿Cuándo aumenta la altura de un árbol 2-3?
> Solo cuando la raíz se llena al recibir una llave de un hijo y hace split: la llave central pasa a ser la nueva raíz.
