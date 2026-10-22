---
ramo: "Introducción a la Programación"
tema: "Ordenamiento"
tags:
  - programacion/ordenamiento
  - origen/complemento
prerrequisitos:
  - "[[02 - Métodos de listas y conversión con strings]]"
  - "[[02 - Métodos especiales: __str__ y operadores]]"
---

# Sort, sorted y criterios con key

Ordenar datos es una de las tareas más comunes: un ranking de puntajes, una lista de contactos en orden alfabético, productos del más barato al más caro. Python ya trae herramientas para ordenar; lo importante es saber **cómo decirle según qué criterio** ordenar.

## `sort` y `sorted`

| | `lista.sort()` | `sorted(lista)` |
|---|---|---|
| ¿Qué es? | Un método de las listas | Una función predefinida |
| ¿Modifica la lista original? | **Sí**, la ordena ahí mismo | No |
| ¿Qué retorna? | `None` | Una **lista nueva** ordenada |

```python
numeros = [3, 4, 1, 6, 8, 2, 4]
ordenada = sorted(numeros)
print(numeros, ordenada)     # la original no cambió
numeros.sort()
print(numeros)               # ahora sí está ordenada
numeros.sort(reverse=True)   # de mayor a menor
print(numeros)
```

```
[3, 4, 1, 6, 8, 2, 4] [1, 2, 3, 4, 4, 6, 8]
[1, 2, 3, 4, 4, 6, 8]
[8, 6, 4, 4, 3, 2, 1]
```

> [!warning] `lista = lista.sort()`
> Como `sort` retorna `None`, esa línea **pierde la lista**. O se usa `lista.sort()` sola, o `lista = sorted(lista)`.

Los números se ordenan de menor a mayor y los strings en orden alfabético, con la trampa ya conocida: las mayúsculas van antes que las minúsculas.

## Ordenar según un criterio: `key`

¿Y si se quiere ordenar palabras sin importar mayúsculas, o pares de números según su suma? Se le pasa a `sort` una **función criterio** con `key=`. Python llama a esa función con **cada elemento** y ordena según lo que ella retorne.

```python
def sin_mayusculas(palabra):
    return palabra.lower()

lista = ["casa", "arbol", "ELEFANTE", "DelFiN"]
lista.sort(key=sin_mayusculas)
print(lista)
```

```
['arbol', 'casa', 'DelFiN', 'ELEFANTE']
```

Los elementos no cambian (siguen con sus mayúsculas); solo se **comparan** usando lo que retorna el criterio.

> [!warning] Sin paréntesis
> Se escribe `key=sin_mayusculas`, **sin** `()`. Se le entrega la función misma para que `sort` la llame con cada elemento; con paréntesis se la llamaría una vez, sin argumento, y daría error.

Más ejemplos de criterios:

```python
def suma(par):
    return sum(par)

pares = [[4, 4], [0, 1], [1, 6], [9, 0]]
pares.sort(key=suma)
print(pares)            # [[0, 1], [1, 6], [4, 4], [9, 0]]

def espanol(fila):      # fila = [inglés, español]
    return fila[1]

diccionario = [["cat", "gato"], ["house", "casa"], ["tree", "arbol"]]
diccionario.sort(key=espanol)
print(diccionario)      # ordenado por la palabra en español
```

## Varios criterios a la vez

Si el criterio retorna **varios valores** separados por coma (una **tupla**), Python compara por el primero y, si hay empate, por el segundo. Para invertir el orden de un criterio numérico se le cambia el signo.

## Ordenar objetos

Los objetos no tienen un orden natural, así que con ellos el `key` es obligatorio. Ejemplo: gatos de **mayor a menor edad** y, a igual edad, **alfabéticamente por nombre**:

```python
class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad})"

def criterio(gato):
    return -gato.edad, gato.nombre    # edad descendente, luego nombre

gatos = [Gato("Tom", 15), Gato("Garfield", 10), Gato("Silvestre", 12),
         Gato("Botas", 10)]
gatos.sort(key=criterio)
print(gatos)
```

```
[Tom (15), Silvestre (12), Botas (10), Garfield (10)]
```

## Ejemplo: palabras más repetidas de un texto

Combinando listas, `count` y `sort` con `reverse`:

```python
palabras = "el gato y el perro y el pez".split()
conteo = []
for p in palabras:
    if [p, palabras.count(p)] not in conteo:
        conteo.append([p, palabras.count(p)])

def veces(par):
    return par[1]

conteo.sort(key=veces, reverse=True)
print(conteo[:2])        # [['el', 3], ['y', 2]]
```

> [!tip] Idea clave
> `key` recibe una función que, para cada elemento, dice "compárame usando este valor". Cualquier orden se puede expresar así: por largo, por un atributo, por una columna, o por varios criterios con una tupla.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre `l.sort()` y `sorted(l)`?
> `l.sort()` ordena la misma lista y retorna `None`; `sorted(l)` deja `l` igual y retorna una lista nueva ordenada.

> [!question]- ¿Cómo se ordena una lista de palabras de la más corta a la más larga?
> Con `palabras.sort(key=len)`: `len` ya es una función que, para cada palabra, entrega su largo.

> [!question]- ¿Por qué en el criterio de los gatos se retorna `-gato.edad`?
> Porque `sort` ordena de menor a mayor; con el signo cambiado, la edad más alta queda primero sin tener que invertir también el orden de los nombres.
