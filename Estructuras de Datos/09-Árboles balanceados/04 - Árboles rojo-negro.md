---
ramo: "Estructuras de Datos"
tema: "Árboles balanceados"
tags:
  - edd
  - rojo-negro
  - balance
  - arbol-2-4
  - origen/complemento
prerrequisitos:
  - "[[03 - Árboles 2-3]]"
  - "[[02 - Rotaciones simples y dobles en AVL]]"
---

# Árboles rojo-negro

Un [[03 - Árboles 2-3|árbol 2-3]] garantiza altura logarítmica, pero sus nodos de distintos tamaños son incómodos de programar. El **árbol rojo-negro** mezcla AVL y 2-3: es un **ABB común** (nodos con una llave y dos hijos) en el que un **color** por nodo codifica los nodos múltiples. Así se obtiene la eficiencia del 2-3 con la simplicidad de un árbol binario.

## Del 2-3 (o 2-4) al rojo-negro

![los 2-nodos se representan igual](adjuntos/Rojo-negro%20-%20los%202-nodos%20se%20representan%20igual.png)

> [!example]- Transcripción de la imagen
> "Los 2-nodos se representan igual": el nodo X con subárboles $< X$ y $> X$ pasa a ser un nodo binario X con los mismos dos subárboles.

![un 3-nodo como padre negro e hijo rojo](adjuntos/Rojo-negro%20-%20un%203-nodo%20como%20padre%20negro%20e%20hijo%20rojo.png)

> [!example]- Transcripción de la imagen
> "Reasignamos dos de los hijos a un nuevo nodo": el 3-nodo X Y (con Y en rojo) pasa a ser X con hijo derecho Y (rojo). X conserva el subárbol $< X$, e Y se queda con los subárboles $> X, < Y$ y $> Y$. Es como una rotación de AVL, con diferencia de altura 1 permitida.

Un 3-nodo se representa como un **padre negro con un hijo rojo**, y el enlace rojo "pega" ambos nodos en uno solo del 2-3. Un 4-nodo (de un árbol **2-4**, con 3 llaves y 4 hijos) es un padre negro con **dos** hijos rojos.

![árbol 2-3 convertido](adjuntos/Rojo-negro%20-%20%C3%A1rbol%202-3%20convertido.png)

> [!example]- Transcripción de la imagen
> A la izquierda, el árbol 2-3 M; E J y R; A C, H, L, P y S V (con J, C y V en rojo, las segundas llaves). A la derecha, su versión binaria: M; E y R; A, J, P y S; C (rojo, hijo de A), H y L (hijos de J, que es rojo), y V (rojo, hijo de S).

## Definición

> [!tip] Propiedades de un árbol rojo-negro
> 1. Cada nodo es **rojo o negro**.
> 2. La **raíz es negra**.
> 3. Si un nodo es **rojo**, sus hijos son **negros**: no hay dos rojos seguidos.
> 4. Desde cualquier nodo, todos los caminos hacia las hojas tienen la **misma cantidad de nodos negros**.
>
> Además, las hojas vacías (`∅`) se consideran negras.

La propiedad 4 es la que balancea. Los nodos negros corresponden a los nodos del 2-4, y en un 2-4 todas las hojas están al mismo nivel. La propiedad 3 impide que un camino tenga más del doble de nodos que otro, así que la altura es $O(\log n)$.

![equivalencia con un 2-4](adjuntos/Rojo-negro%20-%20equivalencia%20con%20un%202-4.png)

> [!example]- Transcripción de la imagen
> El árbol rojo-negro M; E y R rojos; A, J, P, S negros; C, H, L y V rojos. A su lado, el árbol 2-4 equivalente: la raíz E M R y las hojas A C, H J L, P y S V.

![árbol de ejemplo](adjuntos/Rojo-negro%20-%20%C3%A1rbol%20de%20ejemplo.png)

> [!example]- Transcripción de la imagen
> Árbol rojo-negro grande: raíz M (negra); E y R (rojos); A, J, P y S (negros); C, H, L y V (rojos).

![equivalencias de nodos 2, 3 y 4](adjuntos/Rojo-negro%20-%20equivalencias%20de%20nodos%202%2C%203%20y%204.png)

> [!example]- Transcripción de la imagen
> "Con este nuevo modelo, podemos tener árboles equivalentes según": un 2-nodo P equivale a un P negro; un 3-nodo P R equivale a R negro con P rojo a la izquierda, o a P negro con R rojo a la derecha; un 4-nodo P R S equivale a R negro con P y S rojos.

![árbol y su 2-4 equivalente](adjuntos/Rojo-negro%20-%20%C3%A1rbol%20y%20su%202-4%20equivalente.png)

> [!example]- Transcripción de la imagen
> El mismo árbol rojo-negro (M; E, R; A, J, P, S; C, H, L, V) junto a su 2-4: E M R; A C | H J L | P | S V.

> [!warning] Equivalencias
> Todo árbol 2-4 tiene un rojo-negro equivalente, y viceversa. Pero **no** todo rojo-negro tiene un 2-3 equivalente, porque un nodo negro con dos hijos rojos es un 4-nodo, que un 2-3 no admite.

## Inserción

- El nodo insertado es **siempre rojo**. Así no cambia la cantidad de negros en ningún camino y la propiedad 4 se mantiene sola.
- Si su padre es **negro**, no hay nada que hacer: en el 2-4, se agregó una llave a un nodo con espacio.
- Si su padre es **rojo**, hay dos rojos seguidos y se mira al **tío**:
  - **Tío rojo:** en el 2-4, el nodo estaba lleno (un 4-nodo que ahora sería un 5-nodo). Se resuelve con un **cambio de color**, que equivale al **split**: el padre y el tío pasan a negros, el abuelo a rojo, y se revisa hacia arriba.
  - **Tío negro:** se resuelve con **rotaciones** como las de AVL, más un recoloreo.

Gracias a los colores no hay que recorrer el árbol buscando desbalances: basta con mirar el color del tío.

## Preguntas de repaso

> [!question]- ¿Qué representa un nodo rojo en términos de un árbol 2-3 o 2-4?
> Una llave que en el 2-4 vive en el mismo nodo que su padre negro. El enlace rojo junta dos (o tres) nodos binarios en un solo nodo múltiple.

> [!question]- ¿Por qué el nodo insertado se pinta de rojo?
> Para no alterar la cantidad de nodos negros en ningún camino (propiedad 4). Lo único que puede romperse es "no hay dos rojos seguidos", que se arregla localmente.

> [!question]- ¿A qué operación del árbol 2-4 corresponde el cambio de color cuando el tío es rojo?
> Al split de un nodo lleno: la llave del medio (el abuelo, que pasa a rojo) sube a juntarse con su propio padre, y el padre y el tío quedan como nodos separados (negros).

> [!question]- Dado un árbol con un nodo rojo hijo de otro rojo, ¿es rojo-negro?
> No: viola la propiedad 3. Hay que corregirlo con recoloreo o rotaciones, según el color del tío.
