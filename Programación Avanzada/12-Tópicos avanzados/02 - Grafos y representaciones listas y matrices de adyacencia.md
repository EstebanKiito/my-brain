---
ramo: "Programación Avanzada"
tema: "Tópicos avanzados"
tags:
  - programacion/grafos
  - programacion/estructuras-de-datos
  - origen/complemento
prerrequisitos:
  - "[[05 - Diccionarios: llave-valor, hashing y métodos]]"
  - "[[06 - Clases, objetos y variables de clase]]"
---

# Grafos y representaciones listas y matrices de adyacencia

Mientras que las listas representan secuencias lineales y los árboles modelan jerarquías estrictas con un único camino hacia la raíz, muchas relaciones del mundo real son reticulares y multidireccionales: redes de transporte subterráneo, topologías de internet o redes de contactos sociales. La estructura matemática que modela estas relaciones es el **grafo**.

## Conceptos fundamentales de grafos

Formalmente, un grafo $G = (V, E)$ está compuesto por:

- **Vértices o Nodos ($V$):** representan las entidades u objetos del sistema (ciudades, usuarios, servidores).
- **Aristas o Arcos ($E$):** representan las conexiones o relaciones entre pares de vértices.

![Estructura de un grafo no dirigido](adjuntos/Estructura%20topol%C3%B3gica%20de%20un%20grafo%20no%20dirigido.png)

> [!example]- Transcripción de la imagen
> - Diagrama de grafo no dirigido:
>   - Conjunto de nodos identificados con números interconectados mediante líneas bidireccionales que permiten transitar en ambos sentidos.

### Clasificación de grafos

1. **No dirigido (*Undirected*):** las relaciones son simétricas y bidireccionales (ejemplo: amistad recíproca; si $A$ conecta con $B$, $B$ conecta con $A$).
2. **Dirigido o Dígrafo (*Directed*):** las aristas poseen dirección y sentido único (ejemplo: seguir a un usuario en una red social o enlaces entre páginas web).
3. **Ponderado (*Weighted*):** cada arista tiene asociado un valor numérico o peso (distancia física en kilómetros, costo de peaje o latencia de red).

![Grafo ponderado con pesos](adjuntos/Grafo%20ponderado%20con%20pesos%20en%20aristas%20y%20etiquetas.png)

> [!example]- Transcripción de la imagen
> - Grafo ponderado:
>   - Aristas rotuladas con valores numéricos que representan la distancia o el costo de traslado entre nodos vecinos.

## Representaciones de grafos en Python

Existen tres formas estándar de representar un grafo en código según los requisitos de memoria y velocidad de consulta:

```
+--------------------------+-----------------------+-----------------------+
| Criterio                 | Lista de Adyacencia   | Matriz de Adyacencia  |
+--------------------------+-----------------------+-----------------------+
| Complejidad espacial     | $O(|V| + |E|)$        | $O(|V|^2)$            |
| Consultar si (u, v) ∈ E  | $O(\text{grado}(u))$  | $O(1)$ inmediato      |
| Iterar sobre vecinos     | $O(\text{grado}(u))$  | $O(|V|)$              |
| Ideal para               | Grafos dispersos      | Grafos densos         |
+--------------------------+-----------------------+-----------------------+
```

### 1. Lista de Adyacencia (Diccionario de Python)
Es la representación más idiomática y eficiente en memoria para la inmensa mayoría de problemas en Python: cada nodo es una llave en un diccionario cuyo valor es la lista (o conjunto) de sus vecinos:

```python
# Grafo no dirigido ponderado: nodo -> lista de tuplas (vecino, peso)
grafo_rutas = {
    "Santiago": [("Valparaíso", 120), ("Rancagua", 85)],
    "Valparaíso": [("Santiago", 120)],
    "Rancagua": [("Santiago", 85), ("Talca", 170)],
    "Talca": [("Rancagua", 170)]
}

# Consultar vecinos de Santiago
for destino, distancia in grafo_rutas["Santiago"]:
    print(f"Ruta hacia {destino}: {distancia} km")
```

```
Ruta hacia Valparaíso: 120 km
Ruta hacia Rancagua: 85 km
```

### 2. Matriz de Adyacencia
Consiste en una matriz cuadrada de tamaño $|V| \times |V|$ donde la celda en la fila $u$ y columna $v$ almacena un 1 (o el peso de la arista) si existe conexión, y 0 si no existe. Aunque consultar una conexión es instantáneo ($O(1)$), desperdicia memoria cuando el grafo tiene pocas aristas.

> [!tip] Grafos dispersos vs densos
> Un grafo es **disperso** (*sparse*) cuando la cantidad de aristas es mucho menor que el máximo posible ($|E| \ll |V|^2$), como en carreteras o internet. En estos casos, usa siempre **listas de adyacencia** con diccionarios.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia estructural entre un grafo dirigido y un grafo no dirigido?
> En un grafo no dirigido las aristas son bidireccionales y no tienen orientación, mientras que en un grafo dirigido (*dígrafo*) cada arista tiene un origen y un destino unidireccional estricto.

> [!question]- ¿Por qué la lista de adyacencia suele ser preferible sobre la matriz de adyacencia en aplicaciones reales?
> Porque en la mayoría de las redes reales los grafos son dispersos; la lista de adyacencia solo ocupa memoria proporcional a las conexiones existentes ($O(V + E)$), mientras que la matriz reserva espacio cuadrático ($O(V^2)$) lleno de ceros.

> [!question]- ¿Cómo se representa un grafo no dirigido en un diccionario de listas de adyacencia?
> Al agregar una arista entre el nodo $A$ y el nodo $B$, se debe añadir $B$ a la lista de vecinos de $A$ y simultáneamente añadir $A$ a la lista de vecinos de $B$.

> [!question]- ¿Qué ventaja específica ofrece una matriz de adyacencia por sobre una lista de adyacencia?
> Permite verificar si existe una arista directa entre dos nodos cualesquiera en tiempo constante $O(1)$ accediendo directamente a la celda `M[u][v]`.
