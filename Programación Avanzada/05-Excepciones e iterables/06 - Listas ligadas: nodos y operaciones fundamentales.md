---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/estructuras-de-datos
  - programacion/listas-ligadas
  - origen/complemento
prerrequisitos:
  - "[[06 - Clases, objetos y variables de clase]]"
  - "[[04 - Colas FIFO y deques de doble extremo]]"
---

# Listas ligadas: nodos y operaciones fundamentales

Las listas estándar de Python son arreglos dinámicos contiguos en memoria: acceder por índice es inmediato ($O(1)$), pero insertar o eliminar elementos en posiciones intermedias exige desplazar miles de elementos en memoria con costo $O(N)$.

## El concepto de Lista Ligada

Una **lista ligada** (*linked list*) es una estructura de datos secuencial compuesta por elementos individuales dispersos en la memoria, conectados entre sí mediante referencias (punteros).

Para una visión formal de estas estructuras, consultar [[01 - Arreglos frente a listas ligadas]] de Estructuras de Datos.

### La unidad elemental: el Nodo

Cada celda de la lista se modela mediante un **Nodo** (`Node`), el cual almacena dos atributos:

1. **`valor`:** el dato real almacenado.
2. **`siguiente`:** la referencia al siguiente nodo en la cadena (o `None` si es el nodo final).

![Estructura de un nodo en lista ligada](adjuntos/Estructura%20de%20un%20nodo%20en%20lista%20ligada.png)

> [!example]- Transcripción de la imagen
> - Diagrama de un nodo individual dividido en dos partes:
>   - Compartimento izquierdo con el valor almacenado.
>   - Compartimento derecho con un puntero o referencia (`siguiente`) apuntando hacia el nodo contiguo.

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Apunta al siguiente nodo
```

### Estructura general de la Lista Ligada

La lista ligada completa solo necesita almacenar una referencia al nodo inicial, denominado **cabeza** (**`head`**):

![Estructura general de una lista ligada](adjuntos/Estructura%20general%20de%20una%20lista%20ligada.png)

> [!example]- Transcripción de la imagen
> - Secuencia de nodos conectados linealmente mediante flechas de referencia.
> - El puntero inicial `head` referencia al primer nodo de la lista.
> - El último nodo contiene una referencia nula (`None` o `null`) marcando el final de la cadena.

## Operaciones básicas e inserción

```python
class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        """Agrega un nuevo elemento al final de la lista."""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def obtener(self, posicion: int):
        """Recorre la lista hasta la posición deseada O(N)."""
        actual = self.cabeza
        for _ in range(posicion):
            if not actual:
                raise IndexError("Índice fuera de rango")
            actual = actual.siguiente
        if not actual:
            raise IndexError("Índice fuera de rango")
        return actual.valor
```

### Inserción en posición intermedia

Insertar un elemento en una lista ligada una vez localizado el punto de inserción no requiere desplazar elementos en memoria: solo reasignar dos referencias de puntero:

![Inserción de un nodo en lista ligada](adjuntos/Inserci%C3%B3n%20de%20un%20nodo%20en%20lista%20ligada.gif)

> [!example]- Transcripción de la imagen
> - Animación del proceso de inserción:
>   1. Se crea el nuevo nodo independiente.
>   2. El puntero `siguiente` del nuevo nodo se conecta al nodo posterior.
>   3. El puntero `siguiente` del nodo previo se reasigna para apuntar al nuevo nodo.

```python
lista = ListaLigada()
lista.agregar("A")
lista.agregar("B")
lista.agregar("C")

print(f"Elemento en índice 0: {lista.obtener(0)}")
print(f"Elemento en índice 2: {lista.obtener(2)}")
```

```
Elemento en índice 0: A
Elemento en índice 2: C
```

> [!tip] Acceso indexado vs Inserción
> En una lista convencional de Python (`list`), acceder por índice tarda $O(1)$ e insertar en el medio tarda $O(N)$. En una lista ligada simple, acceder por índice tarda $O(N)$ porque hay que saltar nodo por nodo desde la cabeza, pero acoplar un nodo nuevo toma tiempo $O(1)$ una vez posicionado el puntero.

## Preguntas de repaso

> [!question]- ¿Por qué acceder al elemento en la posición 100 de una lista ligada toma tiempo lineal $O(N)$?
> Porque los nodos están dispersos en distintas direcciones de memoria; para llegar a la posición 100 es imprescindible partir en la cabeza (`head`) y seguir secuencialmente los 100 punteros `siguiente` uno por uno.

> [!question]- ¿Qué ocurre si se pierde la referencia guardada en `self.cabeza` de una lista ligada?
> Toda la cadena de nodos queda inaccesible para el programa y el recolector de basura de Python liberará la memoria de todos los nodos al no haber ninguna referencia que apunte a ellos.

> [!question]- ¿Qué ventaja ofrece una lista ligada frente a un arreglo contiguo al momento de insertar un nodo al inicio?
> Insertar al inicio en una lista ligada toma tiempo constante $O(1)$ simplemente creando el nodo y apuntando su `siguiente` a la cabeza anterior, sin necesidad de desplazar en memoria el resto de los elementos.

> [!question]- ¿Cómo se detecta que se ha alcanzado el último nodo de una lista ligada simple?
> Cuando el atributo `siguiente` del nodo actual contiene el valor nulo `None`.
