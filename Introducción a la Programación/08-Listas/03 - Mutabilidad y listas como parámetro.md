---
ramo: "Introducción a la Programación"
tema: "Listas"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[02 - Métodos de listas y conversión con strings]]"
  - "[[02 - Definir funciones propias: def y return]]"
---

# Mutabilidad y listas como parámetro

Que las listas se puedan modificar es muy cómodo, pero trae sorpresas: una función puede cambiar una lista "de afuera", y dos variables pueden estar mirando **la misma** lista. Entender esto evita muchos errores difíciles de encontrar.

## Una variable es una etiqueta, no una caja

Con números, asignar `b = a` y después cambiar `b` no afecta a `a`. Con listas, sí:

```python
a = [1, 2, 3]
b = a            # b NO es una copia: es otro nombre para la misma lista
b.append(4)
print(a)         # [1, 2, 3, 4]
```

La lista existe una sola vez en la memoria y `a` y `b` son dos **etiquetas** pegadas sobre ella. Esto se llama **alias**. Para tener una lista independiente hay que **copiarla**:

```python
a = [1, 2, 3]
b = a[:]         # o list(a): una copia nueva
b.append(4)
print(a, b)      # [1, 2, 3] [1, 2, 3, 4]
```

## Listas dentro de funciones

Una función recibe en su parámetro **la misma lista** que se le pasó, no una copia. Por eso puede modificarla:

```python
def agregar_diez(m):
    m.append(10)

x = [1, 5, 7]
agregar_diez(x)
print(x)         # [1, 5, 7, 10]
```

En cambio, con un número el cambio dentro de la función no se ve afuera:

```python
def cambiar(n):
    n = 100

x = 1
cambiar(x)
print(x)         # 1
```

Y ojo con este caso: **reasignar** el parámetro dentro de la función tampoco afecta a la lista original, porque solo despega la etiqueta local y la pega en una lista nueva.

```python
def reemplazar(m):
    m = [1, 23]   # m ahora apunta a otra lista; x no se entera

x = [1, 5, 7]
reemplazar(x)
print(x)         # [1, 5, 7]
```

| Dentro de la función | ¿Cambia la variable de afuera? |
|---|---|
| `n = 100` (con un `int`, `float` o `str`) | No |
| `m.append(10)`, `m[0] = 5`, `m.remove(x)` | **Sí** (se modifica el contenido) |
| `m = [1, 23]` (asignar una lista nueva) | No |

> [!tip] Regla
> Modificar el **contenido** de una lista (métodos, `m[i] = …`) se ve afuera de la función. **Reasignar** la variable (`m = …`) no.

## Ejemplo: insertar en una lista ordenada

Como la función puede modificar la lista recibida, ni siquiera necesita retornarla:

```python
def agregar_ordenado(lista, x):
    for i in range(len(lista)):
        if lista[i] > x:
            lista.insert(i, x)
            return            # ya se insertó: salir
    lista.append(x)          # x es mayor que todos

numeros = [23, 33, 34, 45, 100]
agregar_ordenado(numeros, 35)
print(numeros)
```

```
[23, 33, 34, 35, 45, 100]
```

## Trampa: modificar una lista mientras se recorre

Se quiere eliminar todos los números que aparecen más de una vez. La idea obvia falla:

```python
def eliminar_duplicados_malo(lista):
    for elem in lista:
        if lista.count(elem) > 1:
            while elem in lista:
                lista.remove(elem)

l = [1, 8, 1, 3, 8, 2, 4, 1, 3, 4, 5, 6, 3, 2, 4, 7]
eliminar_duplicados_malo(l)
print(l)         # [8, 8, 5, 6, 7]: ¡quedaron los 8!
```

El `for` avanza por posiciones. Al borrar elementos, los que estaban después **se corren hacia adelante** y el ciclo se salta algunos. La solución es separar las dos tareas: primero anotar qué borrar en una lista aparte, y después borrar.

```python
def eliminar_duplicados(lista):
    a_borrar = []
    for elem in lista:
        if lista.count(elem) > 1 and elem not in a_borrar:
            a_borrar.append(elem)
    for elem in a_borrar:
        while elem in lista:
            lista.remove(elem)

l = [1, 8, 1, 3, 8, 2, 4, 1, 3, 4, 5, 6, 3, 2, 4, 7]
eliminar_duplicados(l)
print(l)         # [5, 6, 7]
```

> [!warning] Nunca borrar de la lista que se está recorriendo
> Si hay que quitar elementos, recorrer una copia (`for elem in lista[:]`) o anotar lo que hay que borrar y hacerlo después.

## Preguntas de repaso

> [!question]- Después de `a = [1]`, `b = a` y `b.append(2)`, ¿qué vale `a`?
> `[1, 2]`, porque `a` y `b` son dos nombres para la misma lista.

> [!question]- ¿Por qué `agregar_ordenado` no necesita `return lista`?
> Porque modifica con `insert` y `append` la misma lista que recibió, que es la del programa principal; el cambio ya se ve afuera.

> [!question]- ¿Por qué falla la versión mala de eliminar duplicados?
> Porque al borrar elementos mientras el `for` recorre la lista, los siguientes se corren de posición y el ciclo salta algunos sin revisarlos.
