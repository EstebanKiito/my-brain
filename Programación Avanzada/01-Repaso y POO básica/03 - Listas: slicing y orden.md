---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[02 - Listas: creación y comprensión]]"
---

# Listas: slicing y orden

Una vez creada la lista, interesa sacar trozos de ella (*slicing*), ordenarla y recorrerla. Esta nota repasa los tres usos y las trampas más comunes.

## Slicing: sacar un trozo

El **slicing** entrega una parte de la lista con la forma `secuencia[inicio:término:paso]`. El `término` **no se incluye**, y el paso por defecto es 1. Conviene pensar que los índices apuntan a las **líneas entre** los elementos, no a los elementos mismos.

![Índices del slicing apuntan a los bordes entre elementos](adjuntos/Índices%20para%20slicing%20de%20una%20lista.png)

> [!example]- Transcripción de la imagen
> - Una fila de 8 casillas con los valores 400, 20, 1, 4, 10, 11, 12 y 500.
> - Líneas rojas punteadas entre casillas (y en los extremos) numeradas de 0 a 8.
> - Título: «Índices para slicing». El trozo `[a:b]` va desde la línea `a` hasta la línea `b`.

| Expresión | Resultado |
|---|---|
| `a[start:end]` | Desde `start` hasta `end - 1` |
| `a[start:]` | Desde `start` hasta el final |
| `a[:end]` | Desde el inicio hasta `end - 1` |
| `a[:]` | Una copia (superficial) de toda la lista |
| `a[start:end:step]` | Saltando de a `step` |
| `a[-1]` | El último elemento |
| `a[-n:]` | Los últimos `n` elementos |
| `a[:-n]` | Todo menos los últimos `n` |

```python
numeros = [6, 7, 2, 4, 10, 20, 25]
print(numeros[2:6])
print(numeros[2:])
print(numeros[:5])
print(numeros[:5:2])
print(numeros[::-1])      # invierte la lista
```

```
[2, 4, 10, 20]
[2, 4, 10, 20, 25]
[6, 7, 2, 4, 10]
[6, 2, 10]
[25, 20, 10, 4, 2, 7, 6]
```

> [!warning] `a[:]` es una copia *superficial*
> La lista nueva está en otro lugar de la memoria, pero sus elementos siguen siendo los mismos objetos. Si los elementos son listas, modificar una lista interna se verá en ambas copias.

## Ordenar y recorrer

`sort()` ordena la lista **en el mismo lugar** (*in-place*) y no devuelve nada: su resultado es `None`.

```python
numeros = [6, 7, 2, 4, 10, 20, 25]
a = numeros.sort()
print(a)                    # None
print(numeros)

numeros.sort(reverse=True)  # de mayor a menor
print(numeros)
```

```
None
[2, 4, 6, 7, 10, 20, 25]
[25, 20, 10, 7, 6, 4, 2]
```

Con listas de listas, un `for` entrega cada sublista y se puede formatear la salida:

```python
piezas = [["Alfil", 2], ["Peón", 8], ["Rey", 1]]
for pieza in piezas:
    print(f'tipo de pieza: {pieza[0]:8} - cantidad: {pieza[1]}')
```

```
tipo de pieza: Alfil    - cantidad: 2
tipo de pieza: Peón     - cantidad: 8
tipo de pieza: Rey      - cantidad: 1
```

> [!warning] No hagas `numeros = numeros.sort()`
> Dejaría `numeros` en `None` y perderías la lista. Si necesitas una copia ordenada sin tocar la original, usa `sorted(numeros)`.

## Preguntas de repaso

> [!question]- ¿Por qué `numeros[2:6]` no incluye el elemento de la posición 6?
> Porque el término de un slice no se incluye: el trozo va desde la línea 2 hasta la línea 6, y los índices apuntan a los bordes entre elementos.

> [!question]- ¿Qué se imprime con `print(numeros.sort())` y por qué?
> `None`, porque `sort()` reordena la lista original y no devuelve ninguna lista nueva.

> [!question]- ¿Qué entrega `numeros[::-1]` y la lista original cambia?
> Entrega una lista nueva con los elementos en orden inverso. La original no cambia, porque el slicing siempre crea una lista nueva.
