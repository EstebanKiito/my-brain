---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/colas
  - origen/complemento
prerrequisitos:
  - "[[03 - Stacks: pilas LIFO e implementación]]"
---

# Colas FIFO y deques de doble extremo

Cuando varios procesos o usuarios solicitan atención a un recurso compartido —como una cola de impresión, un servidor web que despacha solicitudes o un sistema de venta de entradas—, el orden justo de procesamiento es atender primero a quien llegó primero.

## Principio FIFO y concepto de Cola

Una **cola** (*queue*) es una estructura de datos secuencial que sigue la disciplina **FIFO** (*First-In, First-Out*): el primer elemento en ingresar es el primer elemento en salir.

Su comportamiento es idéntico a una fila del mundo real: las personas nuevas ingresan por el final de la fila y la persona en la cabecera es la primera en ser atendida y salir.

![Operaciones en una cola FIFO](adjuntos/Operaciones%20en%20una%20cola%20FIFO.png)

> [!example]- Transcripción de la imagen
> - Diagrama horizontal de una cola con varios elementos alineados.
> - Operación **Enqueue**: inserta un nuevo elemento por la parte trasera (*tail* o final).
> - Operación **Dequeue**: extrae y procesa el elemento ubicado en el frente (*head* o cabecera).

## El cuello de botella de usar listas como colas

Si intentáramos modelar una cola utilizando una lista convencional de Python con `lista.append(x)` para encolar y `lista.pop(0)` para desencolar, nos encontraríamos con un grave problema de rendimiento:

- `append(x)` al final tarda tiempo constante $O(1)$.
- `pop(0)` al inicio obliga al intérprete a desplazar en memoria todos los elementos restantes una posición a la izquierda. Su costo es **lineal $O(N)$**.
- Procesar $N$ elementos de una lista mediante `pop(0)` requiere tiempo cuadrático $O(N^2)$, volviéndose impracticable para miles de datos.

## Colas de doble extremo: deque

Para resolver esta limitación, el módulo `collections` incluye **`deque`** (*double-ended queue*, pronunciado *dikiu*). Internamente está construida mediante bloques de memoria doblemente enlazados, lo que garantiza operaciones en **tiempo constante $O(1)$ en ambos extremos**:

```python
from collections import deque

# Creación de una cola
cola = deque()

# Enqueue (encolar por la derecha)
cola.append("Ticket #101")
cola.append("Ticket #102")
cola.append("Ticket #103")

# Peek (inspeccionar el primer elemento sin sacarlo)
print(f"Siguiente en ser atendido: {cola[0]}")

# Dequeue (desencolar por la izquierda)
atendido = cola.popleft()
print(f"Atendiendo a: {atendido}")
print(f"Cola restante: {cola}")
```

```
Siguiente en ser atendido: Ticket #101
Atendiendo a: Ticket #101
Cola restante: deque(['Ticket #102', 'Ticket #103'])
```

### Métodos principales de deque

`deque` es una estructura versátil que actúa como una generalización de pilas y colas:

| Operación | Extremo izquierdo (cabecera) | Extremo derecho (cola) | Costo temporal |
|---|---|---|---|
| **Inserción** | `cola.appendleft(x)` | `cola.append(x)` | $O(1)$ |
| **Extracción** | `cola.popleft()` | `cola.pop()` | $O(1)$ |
| **Inspección** | `cola[0]` | `cola[-1]` | $O(1)$ |

## Comparación de rendimiento: list vs deque

| Operación | `list` | `deque` | Explicación |
|---|---|---|---|
| Inserción/Extracción al final | $O(1)$ amortizado | $O(1)$ | Ambos son óptimos en el extremo derecho |
| Inserción/Extracción al inicio | $O(N)$ | $O(1)$ | `list` debe desplazar memoria; `deque` solo actualiza punteros de bloque |
| Acceso por índice en el medio | $O(1)$ | $O(N)$ | `list` es un arreglo contiguo; `deque` debe recorrer bloques |

> [!tip] La regla para elegir entre list y deque
> Si tu programa necesita extraer e insertar elementos con frecuencia por el inicio o por ambos extremos, usa **`deque`**. Si necesitas acceder o modificar elementos en posiciones intermedias aleatorias (`coleccion[i]`), usa **`list`**.

## Aplicación: verificación de palíndromos

Aprovechando que `deque` puede extraer simultáneamente por la izquierda y la derecha en $O(1)$, podemos verificar si una palabra es un palíndromo comparando sus extremos hacia el centro:

```python
from collections import deque

def es_palindromo(palabra: str) -> bool:
    cola = deque(palabra.lower().replace(" ", ""))
    while len(cola) > 1:
        if cola.popleft() != cola.pop():
            return False
    return True

print(es_palindromo("reconocer"))
print(es_palindromo("radar"))
print(es_palindromo("algoritmo"))
```

```
True
True
False
```

## Preguntas de repaso

> [!question]- ¿Por qué no debe usarse `lista.pop(0)` para implementar una cola de alto rendimiento en Python?
> Porque al remover el elemento en el índice 0, Python debe desplazar físicamente todos los $N-1$ elementos restantes a la izquierda, lo que toma tiempo lineal $O(N)$ por cada extracción y resulta ineficiente para grandes volúmenes de datos.

> [!question]- ¿Cómo logra `collections.deque` insertar y remover por el inicio en tiempo $O(1)$?
> Porque está implementada como una lista doblemente enlazada de bloques de memoria, lo que permite agregar o desacoplar nodos en las cabeceras simplemente reasignando punteros sin mover el resto de los elementos.

> [!question]- Si `deque` es tan rápida en sus extremos, ¿por qué no reemplaza a `list` en todos los casos?
> Porque el acceso aleatorio a posiciones intermedias (`d[5000]`) en un `deque` requiere recorrer los bloques desde el extremo más cercano, lo que tiene costo $O(N)$, mientras que una lista accede a cualquier índice en tiempo constante $O(1)$.

> [!question]- ¿Qué sucede si se llama a `cola.popleft()` sobre un `deque` que no tiene elementos?
> Levanta una excepción `IndexError: pop from an empty deque`. Para evitarlo debe comprobarse previamente si `cola` tiene elementos (`if cola:`).
