---
ramo: "Estructuras de Datos"
tema: "Grafos y DFS"
tags:
  - edd
  - grafos
  - dfs
  - tipos-de-aristas
  - origen/complemento
prerrequisitos:
  - "[[02 - Detección de ciclos y búsqueda en profundidad]]"
---

# Tiempos de DFS y tipos de aristas

Además de colorear, DFS puede registrar **cuándo** ocurre cada cambio: un **tiempo de inicio** (*start*), cuando el nodo se descubre y se pinta gris, y un **tiempo de término** (*end*), cuando se termina y se pinta negro. Ambos se numeran con un contador correlativo 1, 2, 3… Con esos tiempos se pueden clasificar las aristas y construir el orden topológico.

```
Dfs(G):                                    DfsVisit(G, u, t):
    t ← 1                                      u.start ← t;  t ← t + 1
    for u ∈ V(G): u.start ← 0; u.end ← 0       for v ∈ N_G(u):
    for u ∈ V(G):                                  if v.start = 0:
        if u.start = 0:                                t ← DfsVisit(G, v, t)
            t ← DfsVisit(G, u, t)              u.end ← t;  t ← t + 1
                                               return t
```

![Slide - DFS con tiempos de inicio y término](adjuntos/Slide%20-%20DFS%20con%20tiempos%20de%20inicio%20y%20t%C3%A9rmino.png)

> [!example]- Transcripción de la imagen
> "Desde $u = 0$ no quedan más nodos por descubrir y terminamos". Grafo de 7 nodos con su intervalo [inicio, término]: 4 [1, 6], 6 [2, 5], 5 [3, 4], 0 [7, 14], 1 [8, 13], 3 [9, 12], 2 [10, 11]. El recorrido empezó en 4 (que llegó a 6 y a 5) y después siguió desde 0 por 0 → 1 → 3 → 2. Las aristas del árbol DFS están en rojo; la arista 2 → 0 (verde) apunta a un nodo gris y detecta un ciclo. "¿Qué diferencia la arista (0, 3) de la (3, 6)?".

DFS puede generar **varios árboles** (un bosque), uno por cada llamado desde `Dfs`. En la figura hay dos: el que parte en 4 y el que parte en 0.

## Intervalos anidados

> [!tip] Propiedad del paréntesis
> Sean $I_u = [u.start, u.end]$ e $I_v = [v.start, v.end]$. Siempre se cumple exactamente una de estas condiciones:
> - $I_u \cap I_v = \varnothing$: $u$ y $v$ no están en el mismo árbol DFS (o ninguno desciende del otro).
> - $I_u \subset I_v$: $u$ es **descendiente** de $v$, porque se descubrió después de $v$ y terminó antes.
> - $I_v \subset I_u$: $v$ es descendiente de $u$.

## Tipos de aristas

Después de `Dfs(G)`, cada arista $(u, v)$ es de uno de estos tipos:

| Tipo | Condición | En la figura |
|---|---|---|
| **De árbol** | $v$ se descubrió al transitar $(u, v)$ | 0 → 1, 1 → 3, 3 → 2 (rojas) |
| **Hacia atrás** | $u$ es descendiente de $v$ ($v$ estaba gris) | 2 → 0 (verde) |
| **Hacia adelante** | No es de árbol y $v$ es descendiente de $u$ | 0 → 3: $[9,12] \subset [7,14]$ (azul) |
| **Cruzada** | En otro caso ($v$ ya terminado en otra rama o en otro árbol) | 3 → 6: $[2,5]$ es disjunto de $[9,12]$ |

Esa es la respuesta a la pregunta de la slide: (0, 3) va hacia adelante, a un descendiente, mientras que (3, 6) cruza a un nodo de otro árbol que ya terminó.

> [!tip] Ciclos y aristas hacia atrás
> Un grafo es **acíclico si y solo si** DFS no produce aristas **hacia atrás**. Esto no depende del orden en que se elijan los nodos: si hay un ciclo, cualquier DFS encuentra al menos una arista hacia atrás.

```python
G = {0: [1, 3], 1: [3, 4], 2: [5], 3: [2, 4, 5, 6], 4: [6], 5: [], 6: [5]}
# DFS lanzado en el orden 4, 0, 1, …
# {4: [1, 6], 6: [2, 5], 5: [3, 4], 0: [7, 14], 1: [8, 13], 3: [9, 12], 2: [10, 11]}  (como en la figura)
```

## Preguntas de repaso

> [!question]- ¿Qué indican el tiempo de inicio y el de término de un nodo?
> El de inicio, cuándo DFS lo descubrió (lo pintó gris). El de término, cuándo terminó de explorar todos sus descendientes (lo pintó negro).

> [!question]- Si $I_u \subset I_v$, ¿qué relación hay entre $u$ y $v$?
> $u$ es descendiente de $v$ en el árbol DFS: se descubrió después que $v$ y terminó antes.

> [!question]- ¿Qué tipo de arista prueba que un grafo tiene un ciclo?
> Una arista hacia atrás, que va desde un nodo hacia uno de sus ancestros (que todavía está gris). Un grafo es acíclico si y solo si DFS no encuentra ninguna.

> [!question]- En la figura, ¿por qué (3, 6) es cruzada y no hacia adelante?
> Porque 6 no es descendiente de 3: su intervalo $[2, 5]$ es disjunto de $[9, 12]$. 6 pertenece al árbol que partió en 4 y ya había terminado.
