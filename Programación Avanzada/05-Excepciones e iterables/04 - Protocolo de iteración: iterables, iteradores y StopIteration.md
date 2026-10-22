---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/iterables
  - programacion/iteradores
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructuras de datos y tuplas]]"
  - "[[02 - Manejo de excepciones: bloques try, except, else y finally]]"
---

# Protocolo de iteración: iterables, iteradores y StopIteration

Al escribir `for elemento in coleccion:`, Python recorre listas, tuplas, conjuntos o diccionarios con la misma sintaxis elegante. Detrás de esta aparente simplicidad existe un contrato formal riguroso: el **protocolo de iteración**.

## Iterable vs Iterador: la distinción fundamental

Es muy habitual confundir estos dos conceptos, pero cumplen roles estrictamente separados:

- **Iterable (*iterable*):** es el contenedor que almacena o representa los datos. Posee el método dunder **`__iter__()`**, cuya única responsabilidad es **construir y retornar un nuevo iterador**. Ejemplos: listas, tuplas, strings y diccionarios.
- **Iterador (*iterator*):** es el objeto que lleva el estado del recorrido (en qué posición va) y entrega los elementos uno por uno. Posee el método dunder **`__next__()`**, que devuelve el siguiente valor de la secuencia, y también implementa `__iter__()` retornándose a sí mismo.

## Funciones integradas: iter() y next()

En lugar de invocar los métodos dunder directamente, Python provee las funciones integradas de alto nivel **`iter()`** y **`next()`**:

```python
lenguajes = ["Python", "Rust", "Go"]

# 1. Obtenemos el iterador a partir del iterable
iterador = iter(lenguajes)
print(f"Objeto iterador: {type(iterador).__name__}")

# 2. Solicitamos elementos secuencialmente con next()
print(next(iterador))
print(next(iterador))
print(next(iterador))

# 3. Al agotarse, levanta StopIteration
# print(next(iterador))  # StopIteration
```

```
Objeto iterador: list_iterator
Python
Rust
Go
```

## La excepción StopIteration y el funcionamiento del bucle for

¿Cómo sabe un bucle `for` cuándo detenerse? No consulta la longitud con `len()`. Simplemente pide elementos con `next()` hasta que el iterador levanta una excepción **`StopIteration`**.

El bucle `for` es azúcar sintáctico para el siguiente bucle `while`:

```python
# Equivalente exacto a: for fruta in frutas:
frutas = ["manzana", "pera"]
it = iter(frutas)

while True:
    try:
        fruta = next(it)
        print(f"Fruta: {fruta}")
    except StopIteration:
        break  # Fin de la iteración
```

```
Fruta: manzana
Fruta: pera
```

## Creación de un iterable e iterador personalizado

Podemos hacer que cualquier clase propia sea iterable implementando ambos métodos:

```python
class ContadorDescendente:
    """Iterable e iterador que cuenta desde un número hasta 1."""
    def __init__(self, inicio: int):
        self.actual = inicio

    def __iter__(self):
        # Todo iterador debe retornarse a sí mismo en __iter__
        return self

    def __next__(self) -> int:
        if self.actual <= 0:
            raise StopIteration
        valor = self.actual
        self.actual -= 1
        return valor


for n in ContadorDescendente(3):
    print(n)
```

```
3
2
1
```

> [!tip] Los iteradores se consumen una sola vez
> Un iterador tiene memoria de su posición. Una vez que agota sus elementos y lanza `StopIteration`, queda vacío. Si intentas iterar sobre él por segunda vez con un `for`, no producirá ningún elemento. Para reiniciar el recorrido debes solicitar un **nuevo iterador** desde el iterable original.

> [!warning] Iterables infinitos
> Si el método `__next__()` nunca levanta `StopIteration`, el iterador generará valores de forma indefinida, provocando un bucle infinito si se utiliza en un `for` sin una cláusula `break` explícita.

## Preguntas de repaso

> [!question]- ¿Qué método dunder identifica a un objeto como iterable en Python?
> El método `__iter__(self)`, el cual debe retornar obligatoriamente un objeto iterador capaz de suministrar elementos.

> [!question]- ¿Qué rol cumple la excepción `StopIteration` en el protocolo de iteración?
> Actúa como señal de parada que indica que el iterador ha agotado todos sus elementos disponibles, permitiendo que las estructuras como el bucle `for` finalicen de forma limpia sin errores.

> [!question]- ¿Por qué no se puede reiniciar un iterador que ya fue recorrido por completo?
> Porque los iteradores son estructuras de un solo uso que avanzan en una sola dirección; cuando su estado interno alcanza el final, no conservan referencias a los elementos pasados para retroceder.

> [!question]- ¿Qué diferencia a un iterador de un iterable en términos de métodos implementados?
> Un iterable solo requiere implementar `__iter__()`, mientras que un iterador debe implementar obligatoriamente tanto `__next__()` (para avanzar) como `__iter__()` (que se retorna a sí mismo).

