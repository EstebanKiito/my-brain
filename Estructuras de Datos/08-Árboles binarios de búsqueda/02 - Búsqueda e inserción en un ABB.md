---
ramo: "Estructuras de Datos"
tema: "Árboles binarios de búsqueda"
tags:
  - edd
  - abb
  - busqueda
  - insercion
  - origen/complemento
prerrequisitos:
  - "[[01 - Diccionarios y árboles binarios de búsqueda]]"
---

# Búsqueda e inserción en un ABB

Buscar en un ABB es la [[04 - Búsqueda binaria y dividir para conquistar|búsqueda binaria]] sobre un árbol: se compara con la raíz y se baja por el lado que corresponde. Insertar empieza con una búsqueda. Si la llave ya está, se actualiza su valor, y si no está, la búsqueda termina justo en el **lugar vacío donde debería estar**, que es donde se inserta.

## Búsqueda

![Búsqueda de la llave 7](adjuntos/B%C3%BAsqueda%20de%20la%20llave%207%20en%20un%20ABB.png)

> [!example]- Transcripción de la imagen
> ABB con raíz 6, hijos 3 y 8; nietos 1 y 5 (de 3) y 7 y 9 (de 8). Buscando el 7: "7 > 6" baja a la derecha, a 8; "7 < 8" baja a la izquierda, a 7; "7 = 7", encontrado (el 7 está marcado en verde).

![Pseudocódigo de Search](adjuntos/Pseudoc%C3%B3digo%20de%20Search.png)

> [!example]- Transcripción de la imagen
> input: ABB $A$, llave buscada $k$; output: ABB, o $\varnothing$ si no se encuentra. `Search(A, k)`: 1. `if A = ∅ ∨ A.key = k: return A`; 3. `if k < A.key: return Search(A.left, k)`; 5. `return Search(A.right, k)`.

Si la llave no está, la búsqueda termina en un `∅`, y ese hueco es informativo:

![Búsqueda fallida de la llave 4](adjuntos/B%C3%BAsqueda%20fallida%20de%20la%20llave%204.png)

> [!example]- Transcripción de la imagen
> Buscando el 4: "4 < 6" a la izquierda, "4 > 3" a la derecha, "4 < 5" a la izquierda, donde hay $\varnothing$. "Este lugar vacío es el lugar en que debería haber estado el nodo con clave 4 si hubiera estado en el árbol".

## Inserción

Para colgar el nodo nuevo hace falta conocer a su **padre**. Por eso se modifica Search para que retorne también el padre del nodo encontrado (o del hueco):

![Search que retorna también el padre](adjuntos/Search%20que%20retorna%20tambi%C3%A9n%20el%20padre.png)

> [!example]- Transcripción de la imagen
> input: ABB $A$, ABB padre $p$, llave $k$; output: tupla con el ABB encontrado y su padre. `Search(A, p, k)`: `if A = ∅ ∨ A.key = k: return (A, p)`; `if k < A.key: return Search(A.left, A, k)`; `return Search(A.right, A, k)`.

![Pseudocódigo de Insert](adjuntos/Pseudoc%C3%B3digo%20de%20Insert.png)

> [!example]- Transcripción de la imagen
> input: ABB $A$, llave $k$, valor $v$. `Insert(A, k, v)`: 1. `(B, p) ← Search(A, ∅, k)` (versión que indica el padre); 2. `if B = ∅`: 3. `B ← nodo vacío`; 4. `B.key ← k`; 5. conectar $B$ al padre $p$ en la posición adecuada; 6. `B.value ← v`.

![Inserción de la llave 4](adjuntos/Inserci%C3%B3n%20de%20la%20llave%204.png)

> [!example]- Transcripción de la imagen
> El mismo árbol con el 4 insertado (en verde) como hijo izquierdo de 5, siguiendo el camino 4 < 6, 4 > 3, 4 < 5.

```python
class Nodo:
    def __init__(self, key, value=None, p=None):
        self.key, self.value, self.left, self.right, self.p = key, value, None, None, p

def search(A, k, p=None):
    """Retorna (nodo, padre). Si no está, nodo es None y padre es donde colgarlo."""
    if A is None or A.key == k:
        return A, p
    return search(A.left, k, A) if k < A.key else search(A.right, k, A)

def insert(raiz, k, v=None):
    B, p = search(raiz, k)
    if B is None:                        # no estaba: nodo nuevo colgado del padre
        B = Nodo(k, v, p)
        if p is None: return B           # árbol vacío
        if k < p.key: p.left = B
        else: p.right = B
    B.value = v                          # si ya estaba, solo se actualiza
    return raiz
```

> [!tip] Por qué se mantiene la propiedad de ABB
> El nodo nuevo queda exactamente donde la búsqueda lo habría ido a buscar: cada comparación del camino lo dejó del lado correcto de cada ancestro. Insertar siempre crea una **hoja** y nunca reordena nada.

Ambas operaciones cuestan $O(h)$: $O(\log n)$ si el árbol está balanceado y $O(n)$ si degeneró en lista.

## Preguntas de repaso

> [!question]- ¿Por qué la búsqueda fallida es útil para insertar?
> Porque termina en el lugar vacío que ocuparía la llave si estuviera. Ese es precisamente donde hay que insertarla para mantener la propiedad de ABB.

> [!question]- ¿Para qué se modifica Search para que retorne también el padre?
> Para poder colgar el nodo nuevo: hay que asignar `p.left` o `p.right`, y sin el padre se perdería la referencia al llegar al hueco vacío.

> [!question]- ¿Qué hace Insert si la llave ya existe?
> No crea un nodo nuevo: actualiza el valor asociado a esa llave, porque las llaves de un diccionario son únicas.

> [!question]- Insertar 5, 3, 8, 4 en un ABB vacío. ¿Dónde queda el 4?
> 5 es la raíz, 3 su hijo izquierdo y 8 su hijo derecho. El 4 es menor que 5 y mayor que 3, así que queda como hijo derecho de 3.
