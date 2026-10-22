---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/listas-ligadas
  - programacion/iterables
  - origen/complemento
prerrequisitos:
  - "[[06 - Listas ligadas: nodos y operaciones fundamentales]]"
  - "[[05 - Generadores y la palabra clave yield]]"
---

# Listas ligadas iterables: integrando __iter__ y generadores

Si para recorrer una lista ligada de mil elementos utilizamos un bucle tradicional llamando a `obtener(i)` en cada vuelta, el tiempo total se degrada a un ineficiente orden cuadrático $O(N^2)$, pues en cada iteración la búsqueda vuelve a empezar desde la cabeza.

## El problema del recorrido ingenuo

```python
# Ineficiente O(N^2): cada llamada a obtener(i) recorre desde el inicio
# for i in range(len(lista)):
#     print(lista.obtener(i))
```

Para recorrer la lista en tiempo lineal $O(N)$ y con la sintaxis natural `for elemento in lista:`, debemos dotar a nuestra estructura del **protocolo de iteración**.

## Implementación con generadores y yield

La forma más elegante y pythónica de hacer que una lista ligada sea iterable es implementar el método dunder **`__iter__()`** como una **función generadora** utilizando **`yield`**.

Al hacer esto, Python se encarga automáticamente de crear el objeto iterador, gestionar el avance y levantar `StopIteration` al llegar al final:

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaLigadaIterable:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def __iter__(self):
        """Generador que entrega los valores de los nodos uno a uno."""
        actual = self.cabeza
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def __repr__(self) -> str:
        """Representación gráfica de la lista ligada."""
        elementos = [str(v) for v in self]
        return " -> ".join(elementos) + " -> None"
```

## Beneficios inmediatos del protocolo de iteración

Al definir `__iter__()`, nuestra clase adquiere de forma gratuita compatibilidad con todas las herramientas nativas de Python que operan sobre iterables:

```python
lista = ListaLigadaIterable()
lista.agregar("Santiago")
lista.agregar("Valparaíso")
lista.agregar("Concepción")

# 1. Impresión estética gracias a __repr__ y __iter__
print(lista)

# 2. Recorrido natural con bucle for en tiempo lineal O(N)
print("Ciudades en la lista:")
for ciudad in lista:
    print(f"  * {ciudad}")

# 3. Comprobación de pertenencia con 'in'
print(f"¿Está Valparaíso?: {'Valparaíso' in lista}")

# 4. Conversión inmediata a listas o conjuntos de Python
ciudades_lista = list(lista)
print(f"Convertida a list: {ciudades_lista}")
```

```
Santiago -> Valparaíso -> Concepción -> None
Ciudades en la lista:
  * Santiago
  * Valparaíso
  * Concepción
¿Está Valparaíso?: True
Convertida a list: ['Santiago', 'Valparaíso', 'Concepción']
```

> [!tip] La magia de yield dentro de __iter__
> No es obligatorio crear una clase separada con `__next__()` para hacer que un objeto sea iterable. Usar `yield` dentro de `__iter__()` convierte al método en un generador, reduciendo decenas de líneas de código a un simple bucle `while`.

## Preguntas de repaso

> [!question]- ¿Por qué recorrer una lista ligada mediante un bucle de índices `obtener(i)` es mucho más lento que recorrerla con `for elemento in lista:`?
> Porque `obtener(i)` reinicia la búsqueda desde la cabeza en cada índice, realizando $1 + 2 + \dots + N$ pasos en total ($O(N^2)$); mientras que un iterador conserva el puntero actual y avanza un solo paso por elemento, completando el recorrido en tiempo $O(N)$.

> [!question]- ¿Qué ventaja ofrece implementar `__iter__` con `yield` en lugar de crear una clase iteradora externa con `__next__`?
> Simplifica drásticamente el diseño: elimina la necesidad de escribir una clase secundaria completa, gestionar manualmente el estado y levantar explícitamente `StopIteration`.

> [!question]- ¿Por qué el operador `in` (`"Valparaíso" in lista`) funciona automáticamente sin haber definido el método `__contains__`?
> Porque si una clase no implementa `__contains__`, Python utiliza su método `__iter__` para realizar una búsqueda secuencial recorriendo los elementos hasta encontrar una coincidencia o agotar la secuencia.

> [!question]- ¿Puede una lista ligada iterable ser convertida directamente a una lista común con `list(mi_lista_ligada)`?
> Sí, porque el constructor `list()` acepta cualquier objeto que implemente el protocolo de iteración (`__iter__`), consumiendo sus elementos hasta que la secuencia finaliza.
