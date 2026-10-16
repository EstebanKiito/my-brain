---
ramo: "Estructuras de Datos"
tema: "Árboles balanceados"
tags:
  - edd
  - avl
  - rotaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles AVL y propiedad de balance]]"
---

# Rotaciones simples y dobles en AVL

Al subir desde la inserción se etiquetan tres nodos: **X**, el **primer nodo desbalanceado**; **Y**, el hijo de X en la ruta de la inserción; y **Z**, el hijo de Y en esa ruta. Según si la ruta X → Y → Z **sigue la misma dirección** o **cambia de dirección**, se aplica una rotación **simple** o una **doble**. En ambos casos solo se **ajustan punteros**: $O(1)$.

## Caso 1: desbalance hacia el exterior → rotación simple

Si la inserción fue izquierda-izquierda (o derecha-derecha), el subárbol exterior quedó demasiado alto. Se **rota** X con Y: Y sube a ocupar el lugar de X y X pasa a ser hijo de Y. El subárbol del medio ($T_2$) cambia de padre.

![Desbalance hacia el exterior - nodos X e Y](adjuntos/Desbalance%20hacia%20el%20exterior%20-%20nodos%20X%20e%20Y.png)

> [!example]- Transcripción de la imagen
> X (en rojo) con hijo izquierdo Y y subárbol derecho $T_3$; Y tiene los subárboles $T_1$ (el más profundo) y $T_2$. $T_1$ baja un nivel más de lo permitido.

![Rotación simple](adjuntos/Rotaci%C3%B3n%20simple.png)

> [!example]- Transcripción de la imagen
> "Realizamos un intercambio que llamaremos rotación". A la izquierda, X arriba con Y como hijo izquierdo ($T_1$, $T_2$) y $T_3$. A la derecha, después de rotar, Y es la raíz con $T_1$ a la izquierda y X a la derecha; X queda con $T_2$ y $T_3$. Los tres subárboles quedan balanceados.

El orden se conserva: $T_1 < Y < T_2 < X < T_3$ antes y después. Por eso la rotación es válida en un ABB.

![antes](adjuntos/Rotaci%C3%B3n%20simple%20en%20K%20-%20antes.png)

> [!example]- Transcripción de la imagen
> K (balance $-2$, marcado como X) con hijo izquierdo F ($-1$, Y) e hijo derecho N (0). F tiene hijos E ($-1$) y H (0). E tiene el hijo B recién insertado (en verde).

![después](adjuntos/Rotaci%C3%B3n%20simple%20en%20K%20-%20despu%C3%A9s.png)

> [!example]- Transcripción de la imagen
> Después de rotar, F (Y) es la raíz del subárbol, con hijo izquierdo E (que tiene a B) e hijo derecho K (X), y K tiene hijos H y N.

## Caso 2: cambio de dirección → rotación doble

Si la ruta cambia de dirección (izquierda y luego derecha), la rotación simple **no basta**: el subárbol del medio ($T_2$) es el que creció, y rotar X con Y lo deja igual de profundo, ahora del otro lado.

![Inserción de G - cambio de dirección](adjuntos/Inserci%C3%B3n%20de%20G%20-%20cambio%20de%20direcci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> K ($-2$) con hijo izquierdo F ($+1$) y N (0). F tiene hijos E (0) y H ($-1$), y H tiene el hijo G recién insertado (en verde). La ruta K → F → H va a la izquierda y luego a la derecha.

![La rotación simple no basta](adjuntos/La%20rotaci%C3%B3n%20simple%20no%20basta.png)

> [!example]- Transcripción de la imagen
> A la izquierda, X con Y a la izquierda; el subárbol más profundo es $T_2$, el del medio. Después de una rotación simple (derecha), Y queda arriba y X abajo con $T_2$ y $T_3$, pero $T_2$ sigue un nivel por debajo de lo permitido.

![Subárbol T2 con raíz Z](adjuntos/Sub%C3%A1rbol%20T2%20con%20ra%C3%ADz%20Z.png)

> [!example]- Transcripción de la imagen
> Se mira dentro de $T_2$: su raíz es Z, con subárboles $T_2'$ y $T_2''$ (marcados con un óvalo rojo). "Recordemos que X es el primero desbalanceado; por lo tanto, sabemos que los sub-árboles de $T_2$ son AVL".

La solución es una **rotación doble**. Primero se rota Y con Z, lo que convierte el caso en uno exterior, y después se rota X con Z:

![primera rotación](adjuntos/Rotaci%C3%B3n%20doble%20-%20primera%20rotaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "El desbalance resultante (intermedio) es como una inserción por la izquierda en el subárbol con raíz Z": tras la "primera rotación" (Y con Z), Z queda como hijo izquierdo de X e Y como hijo izquierdo de Z, con $T_1$ y $T_2'$; $T_2''$ y $T_3$ quedan a la derecha.

![resultado](adjuntos/Rotaci%C3%B3n%20doble%20-%20resultado.png)

> [!example]- Transcripción de la imagen
> "Doble rotación": el resultado final tiene a Z como raíz, Y a la izquierda (con $T_1$ y $T_2'$) y X a la derecha (con $T_2''$ y $T_3$). Todo queda balanceado.

> [!tip] Regla práctica
> **Misma dirección** (izq-izq o der-der): una rotación de X con Y. **Cambio de dirección** (izq-der o der-izq): rotar Y con Z y después X con Z. Z termina como raíz del subárbol. Para implementarlo, se guarda en una **pila** el camino recorrido al insertar (izquierda, izquierda, derecha…) y así se sabe por dónde subir.

## Ejemplo completo: insertar M, D, H, B, A, C, S, K, I

| Inserta | Árbol resultante | Rotación |
|---|---|---|
| M, D | M(D, ·) | — |
| H | H(D, M) | doble en M (Y = D, Z = H) |
| B | H(D(B, ·), M) | — |
| A | H(B(A, D), M) | simple en D (Y = B) |
| C | D(B(A, C), H(·, M)) | doble en H (Y = B, Z = D) |
| S | D(B(A, C), M(H, S)) | simple en H (Y = M) |
| K | D(B(A, C), M(H(·, K), S)) | — |
| I | D(B(A, C), M(I(H, K), S)) | doble en H (Y = K, Z = I) |

La tabla se obtuvo con una implementación de AVL en Python. El árbol final tiene altura 4 con 9 nodos.

## Preguntas de repaso

> [!question]- ¿Cómo se identifican X, Y y Z después de una inserción?
> X es el primer nodo desbalanceado al subir desde la inserción, Y es su hijo en la ruta de la inserción y Z es el hijo de Y en esa misma ruta.

> [!question]- ¿Por qué una rotación simple no arregla un desbalance con cambio de dirección?
> Porque el subárbol que creció es el del medio ($T_2$), y la rotación simple lo cambia de lado sin subirlo. Hay que rotar primero Y con Z para llevarlo al exterior.

> [!question]- ¿Cuánto cuesta una rotación y por qué?
> $O(1)$: solo se reasignan unos pocos punteros entre X, Y, Z y sus subárboles, sin recorrer nada.

> [!question]- En el ejemplo, al insertar A, ¿cuál es el primer nodo desbalanceado y qué rotación se aplica?
> D, que tenía a B a la izquierda y ahora a B con A: la ruta D → B → A es izquierda-izquierda. Se rota D con B (simple) y B queda con hijos A y D.
