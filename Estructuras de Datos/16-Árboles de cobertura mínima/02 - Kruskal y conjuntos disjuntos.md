---
ramo: "Estructuras de Datos"
tema: "Árboles de cobertura mínima"
tags:
  - edd
  - mst
  - kruskal
  - union-find
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles de cobertura mínima y cortes]]"
---

# Kruskal y conjuntos disjuntos

El algoritmo de **Kruskal** parte con un **bosque** de $V$ árboles de un solo nodo y recorre las aristas de **menor a mayor costo**. Cada arista que no forma un ciclo se agrega y une dos árboles en uno. Cuando quedan $V - 1$ aristas, el bosque es un único árbol: el MST.

```
Kruskal(G):
    E ← E ordenada por costo, de menor a mayor
    T ← lista vacía
    for e ∈ E:
        if agregar e a T no forma ciclo:
            T ← T ∪ {e}
    return T
```

**Por qué es correcto.** Al revisar $(u, v)$, se toma el corte $V_1$ = nodos conectados con $u$ en $T$, $V_2$ = el resto. Si $u$ y $v$ ya están conectados, la arista no cruza ese corte y formaría ciclo. Si no lo están, la arista sí lo cruza, y como las aristas se recorren en orden de costo, es la **más barata** que lo cruza. Por la [[01 - Árboles de cobertura mínima y cortes|propiedad del corte]], pertenece a algún MST.

![Slide - MST obtenido por Kruskal](adjuntos/Slide%20-%20MST%20obtenido%20por%20Kruskal.png)

> [!example]- Transcripción de la imagen
> Slide "Algoritmo de Kruskal". El grafo de ejemplo con las aristas del árbol en rojo: 5–3 (18), 1–7 (21), 7–6 (25), 0–2 (29), 0–7 (31), 3–4 (34) y 7–4 (46). "En este punto, $|E| = |V| - 1$ y $T$ es un árbol".

## ¿Forma ciclo? Conjuntos disjuntos

La arista $(u, v)$ forma ciclo si y solo si $u$ y $v$ ya están **en el mismo árbol** del bosque. Los árboles del bosque son **conjuntos disjuntos**, y la estructura que los maneja (*union-find*) ofrece dos operaciones:

- **`Find(x)`**: el **representante** del conjunto de $x$. Dos elementos están en el mismo conjunto si y solo si tienen el mismo representante.
- **`Union(x, y)`**: une los conjuntos de $x$ y de $y$.

Se representa cada conjunto como un **árbol en que cada nodo apunta a su padre**, y la raíz (que se apunta a sí misma) es el representante. `Union` solo cambia el puntero de una raíz: $O(1)$. `Find` sube hasta la raíz, así que su costo depende de la altura.

![Slide - Union de conjuntos como árboles](adjuntos/Slide%20-%20Union%20de%20conjuntos%20como%20%C3%A1rboles.png)

> [!example]- Transcripción de la imagen
> "La operación Union corresponde a cambiar el autoloop del representante de un conjunto: $\mathcal{O}(1)$". Arriba se unen dos árboles: F (raíz, que se apunta a sí misma) con hijos D y B, y C (raíz) con hijo A. Abajo, los dos resultados posibles: a la izquierda, C cuelga de F, y queda F con hijos C, D y B, y A bajo C; a la derecha, F cuelga de C, y queda C con hijos A y F, y D y B bajo F. "¿Cuál de las dos opciones escogemos como resultado?".

> [!tip] Dos mejoras que hacen a Find casi $O(1)$
> - **Unir el árbol más bajo bajo el más alto**, para no aumentar la altura sin necesidad.
> - **Compresión de rutas:** al hacer `Find(x)`, todos los nodos del camino pasan a apuntar directamente a la raíz, así que la siguiente búsqueda es inmediata.
>
> Con ambas, `Find` cuesta $O(\alpha(n))$, donde $\alpha$ es una función que crece tan lento (vale 4 para $2048 \le n \le 16512$) que en la práctica se considera constante.

![Slide - conjuntos disjuntos en un arreglo de padres](adjuntos/Slide%20-%20conjuntos%20disjuntos%20en%20un%20arreglo%20de%20padres.png)

> [!example]- Transcripción de la imagen
> "Podemos almacenar los árboles en un único arreglo de referencias: $A[k]$ es el padre de $k$". A la izquierda, $A[1..6] = 3, 6, 0, 6, 0, 0$ (0 marca una raíz), con los árboles {3 ← 1}, {6 ← 4, 6 ← 2} y {5}. A la derecha, después de unir 5 al conjunto de 6, $A[5] = 4$ y 5 queda colgando de 4.

```python
padre, altura = list(range(8)), [0] * 8

def find(x):
    if padre[x] != x:
        padre[x] = find(padre[x])          # compresión de rutas
    return padre[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if altura[rx] < altura[ry]: rx, ry = ry, rx
    padre[ry] = rx                         # el más bajo cuelga del más alto
    if altura[rx] == altura[ry]: altura[rx] += 1

def kruskal(E):                            # E: lista de (costo, u, v)
    T = []
    for c, u, v in sorted(E):
        if find(u) != find(v):             # extremos en árboles distintos
            T.append((u, v, c)); union(u, v)
    return T
# con el grafo de ejemplo: costo total 204
```

## Complejidad

| Paso | Costo |
|---|---|
| Ordenar las aristas | $O(E \log E)$ |
| Crear $V$ conjuntos de un elemento | $O(V)$ |
| $V - 1$ uniones | $O(V)$ |
| $2E$ búsquedas | $O(E\,\alpha(V)) \approx O(E)$ |

Domina el ordenamiento: $O(E \log E)$. Como $E \le V^2$, $\log E \le 2 \log V$, así que **Kruskal es $O(E \log V)$**.

## Preguntas de repaso

> [!question]- ¿Cómo sabe Kruskal si una arista formaría un ciclo?
> Comparando los representantes de sus extremos con `Find`: si son iguales, ya están en el mismo árbol y la arista cerraría un ciclo.

> [!question]- ¿Por qué conviene colgar el árbol más bajo del más alto al unir?
> Para que la altura del resultado no crezca innecesariamente, ya que `Find` cuesta según la altura.

> [!question]- ¿Qué hace la compresión de rutas?
> En cada `Find`, hace que todos los nodos recorridos apunten directamente a la raíz, de modo que las búsquedas siguientes sobre ellos son inmediatas.

> [!question]- ¿Qué paso domina la complejidad de Kruskal?
> Ordenar las aristas, $O(E \log E) = O(E \log V)$. Las operaciones de union-find son prácticamente constantes.
