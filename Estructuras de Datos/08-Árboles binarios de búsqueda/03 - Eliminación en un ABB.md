---
ramo: "Estructuras de Datos"
tema: "Árboles binarios de búsqueda"
tags:
  - edd
  - abb
  - eliminacion
  - sucesor
  - origen/complemento
prerrequisitos:
  - "[[02 - Búsqueda e inserción en un ABB]]"
---

# Eliminación en un ABB

Eliminar es la operación difícil de un ABB, porque puede dejar un **hueco en medio del árbol** que hay que tapar sin romper el orden. Todo depende de cuántos hijos tenga el nodo a eliminar. Eliminar una hoja es trivial; eliminar un nodo con dos hijos, como la raíz, es el caso complicado.

## Los tres casos

1. **Es hoja:** se quita y el padre apunta a `∅`.
2. **Tiene un solo hijo:** el hijo toma su lugar. El padre pasa a apuntar a él, y el orden se mantiene porque todo el subárbol estaba del mismo lado del padre.
3. **Tiene dos hijos:** se reemplaza su llave por la de su **sucesor**, el **mínimo del subárbol derecho**, y se elimina el sucesor, que tiene a lo más un hijo derecho. También sirve el antecesor, que es el máximo del subárbol izquierdo.

![ABB antes de eliminar la raíz](adjuntos/ABB%20antes%20de%20eliminar%20la%20ra%C3%ADz.png)

> [!example]- Transcripción de la imagen
> El ABB con raíz 6 (marcada en rojo, la que se quiere eliminar), hijos 3 y 8, nietos 1, 5, 7, 9 y el 4 como hijo izquierdo de 5. La raíz tiene dos hijos: es el caso difícil.

¿Por qué el sucesor? Es la llave **inmediatamente mayor**: queda por encima de todo el subárbol izquierdo y por debajo de todo el resto del derecho. Al ponerla en el lugar del nodo eliminado, la propiedad de ABB se mantiene. Además, como es el mínimo de su subárbol, **no tiene hijo izquierdo**, así que quitarlo cae en el caso 1 o 2.

![Mínimo y máximo de un ABB](adjuntos/M%C3%ADnimo%20y%20m%C3%A1ximo%20de%20un%20ABB.png)

> [!example]- Transcripción de la imagen
> "Nos interesa encontrar el sucesor/antecesor del nodo extraído". Árbol M; I y T; D, K, Q y Z; A y G, con flechas que bajan siempre a la izquierda o siempre a la derecha. `Min(A)`: `if A.left = ∅: return A`, si no, `return Min(A.left)`. `Max(A)`: `if A.right = ∅: return A`, si no, `return Max(A.right)`.

![Pseudocódigo de Delete](adjuntos/Pseudoc%C3%B3digo%20de%20Delete.png)

> [!example]- Transcripción de la imagen
> `Delete(A, k)`: 1. `(D, p) ← Search(A, ∅, k)` (permite saber el padre de $D$); 2. `if D ≠ ∅`: 3. si $D$ es hoja, `D ← ∅` y se elimina la referencia en $p$; 4. si $D$ tiene un solo hijo $H$, `D ← H` y se actualiza $p$; 5. si no: 6. `R ← Min(D.right)`; 7. `t ← R.right`; 8. `D.key ← R.key`; 9. `D.value ← R.value`; 10. `R ← t`.

```python
def minimo(A):
    return A if A.left is None else minimo(A.left)

def delete(raiz, k):
    D, p = search(raiz, k)
    if D is None: return raiz
    if D.left and D.right:               # dos hijos: copiar el sucesor y borrar al sucesor
        R = minimo(D.right)
        D.key, D.value = R.key, R.value
        D, p = R, R.p
    hijo = D.left or D.right             # ahora D tiene 0 o 1 hijo
    if hijo: hijo.p = p
    if p is None: return hijo            # se eliminó la raíz
    if p.left is D: p.left = hijo
    else: p.right = hijo
    return raiz

# árbol 6, 3, 8, 1, 5, 7, 9, 4:
# delete(6) -> la raíz pasa a ser 7          inorder: 1 3 4 5 7 8 9
# delete(3) -> 3 se reemplaza por 4           inorder: 1 4 5 7 8 9
```

## Recorrido in-order

Recorrer **izquierda, nodo, derecha** de forma recursiva visita las llaves **en orden creciente**. Es la forma de listar un diccionario ordenado en $O(n)$, algo que una tabla de hash no puede hacer.

```python
def inorder(A):
    return [] if A is None else inorder(A.left) + [A.key] + inorder(A.right)
```

> [!warning] Eliminar también desbalancea
> Insertar y eliminar en orden adverso puede dejar el árbol alargado. Ni la inserción ni la eliminación de un ABB simple corrigen la altura. Para eso están los árboles balanceados (AVL, 2-3, rojo-negro).

## Preguntas de repaso

> [!question]- ¿Por qué al eliminar un nodo con dos hijos se usa el sucesor (mínimo del subárbol derecho)?
> Porque es la llave inmediatamente mayor: sigue siendo mayor que todo el subárbol izquierdo y menor que el resto del derecho, así que puede ocupar el lugar del nodo sin romper el orden.

> [!question]- ¿Por qué el sucesor nunca tiene hijo izquierdo?
> Porque es el mínimo de su subárbol. Si tuviera hijo izquierdo, ese hijo sería menor y el mínimo sería otro.

> [!question]- ¿Qué entrega el recorrido in-order de un ABB y cuánto cuesta?
> Las llaves en orden creciente, porque visita el subárbol menor, luego el nodo y luego el mayor. Cuesta $O(n)$, porque visita cada nodo una vez.

> [!question]- Al eliminar un nodo con un solo hijo, ¿por qué el hijo puede tomar su lugar sin problemas?
> Porque todo el subárbol del hijo estaba del mismo lado respecto del padre del nodo eliminado, así que el orden con el padre se mantiene.
