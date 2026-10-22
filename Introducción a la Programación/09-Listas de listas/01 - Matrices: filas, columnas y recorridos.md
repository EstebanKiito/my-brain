---
ramo: "Introducción a la Programación"
tema: "Listas de listas"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[03 - Mutabilidad y listas como parámetro]]"
---

# Matrices: filas, columnas y recorridos

Una lista puede contener cualquier cosa… incluso **otras listas**. Así se representan datos con forma de **tabla**: un tablero de juego, una planilla de notas, un mapa. A una lista de listas con todas sus filas del mismo largo se le llama **matriz**.

## Del dato suelto a la tabla

Los datos de un amigo caben en una lista:

```python
amigo = ["Inigo Montoya", "inigo@gmail.com", "03/10/1995"]
```

Pero no se tiene un solo amigo. Para guardarlos todos, se hace una lista donde **cada elemento es la lista de un amigo**:

```python
M = [["Inigo Montoya", "inigo@gmail.com", "03/10/1995"],
     ["Lucy van Pelt", "lucy@gmail.com", "10/06/1997"],
     ["Ada Lovelace", "ada@gmail.com", "18/09/1996"]]
print(M[1])        # ['Lucy van Pelt', 'lucy@gmail.com', '10/06/1997']
print(M[1][1])     # lucy@gmail.com
```

`M[1]` es una fila completa (una lista) y `M[1][1]` es un dato de esa fila: primero se elige la **fila**, después la **columna**.

## Filas, columnas y tamaño

|  | col 0 | col 1 | col 2 | col 3 |
|---|---|---|---|---|
| **fila 0** | `M[0][0]` | `M[0][1]` | `M[0][2]` | `M[0][3]` |
| **fila 1** | `M[1][0]` | `M[1][1]` | `M[1][2]` | `M[1][3]` |
| **fila 2** | `M[2][0]` | `M[2][1]` | `M[2][2]` | `M[2][3]` |

- `M[i][j]`: elemento de la fila `i`, columna `j`.
- `len(M)`: número de **filas**.
- `len(M[0])`: número de **columnas** (el largo de una fila).

```python
M = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
M[0][3] = 10
print(len(M), len(M[0]))   # 3 4
print(M[0])                # [0, 0, 0, 10]
```

## Crear una matriz de un tamaño dado

Con dos ciclos, agregando filas nuevas:

```python
filas, cols = 3, 4
M = []
for i in range(filas):
    M.append([0] * cols)     # cada vuelta crea una fila NUEVA
print(M)
```

O en una línea, con una **lista por comprensión** (*list comprehension*):

```python
M = [[0 for j in range(4)] for i in range(3)]
```

Una lista por comprensión construye una lista a partir de un recorrido: `[expresión for x in secuencia if condición]`. Por ejemplo, `[x for x in dias if x[0] == "m"]` filtra los días que empiezan con "m".

> [!warning] La trampa de `[[0] * 4] * 3`
> Parece crear 3 filas, pero crea **una sola fila repetida 3 veces** (tres alias de la misma lista). Al cambiar `M[0][0]`, cambian las tres filas. Hay que crear cada fila por separado, como arriba.

```python
malo = [[0] * 2] * 3
malo[0][0] = 9
print(malo)        # [[9, 0], [9, 0], [9, 0]]
```

## Recorrer una matriz: doble `for`

Para visitar cada casilla se anida un ciclo de columnas dentro de uno de filas:

```python
L = [[2, 5, 7],
     [1, 4, 6],
     [8, 0, 3]]
for i in range(len(L)):            # cada fila
    for j in range(len(L[0])):     # cada columna de esa fila
        print(L[i][j], end=" ")
    print()                        # salto de línea al terminar la fila
```

```
2 5 7
1 4 6
8 0 3
```

También se puede recorrer por elemento: `for fila in L:` y adentro `for x in fila:`, cuando no hacen falta las posiciones.

## Buscar en una matriz

```python
L = [[2, 5, 7], [1, 4, 6], [8, 5, 3]]
buscado = 5
for i in range(len(L)):
    for j in range(len(L[0])):
        if L[i][j] == buscado:
            print("Encontrado en fila", i, "columna", j)
```

```
Encontrado en fila 0 columna 1
Encontrado en fila 2 columna 1
```

## Los vecinos de una casilla

En juegos de tablero (buscaminas, gato, el juego de la vida) importa qué hay **alrededor** de una casilla `(i, j)`:

|  | `j - 1` | `j` | `j + 1` |
|---|---|---|---|
| **`i - 1`** | arriba-izquierda | arriba | arriba-derecha |
| **`i`** | izquierda | **casilla** | derecha |
| **`i + 1`** | abajo-izquierda | abajo | abajo-derecha |

> [!warning] Los bordes
> En la fila 0 no existe `i - 1`. Ojo: `M[-1]` **no** da error, sino que entrega la **última** fila, lo que produce resultados equivocados sin aviso. Siempre hay que revisar que `0 <= i < len(M)` y `0 <= j < len(M[0])` antes de mirar un vecino.

## Preguntas de repaso

> [!question]- En una matriz de 5 filas y 3 columnas, ¿cuánto valen `len(M)` y `len(M[0])`?
> `len(M)` es 5 (filas) y `len(M[0])` es 3 (columnas).

> [!question]- ¿Por qué `[[0] * 3] * 4` no sirve para crear una matriz?
> Porque repite cuatro veces la misma lista interna (alias). Modificar una casilla cambia esa columna en todas las filas.

> [!question]- En el doble `for`, ¿para qué sirve el `print()` vacío después del ciclo interno?
> Para hacer un salto de línea al terminar cada fila; dentro del ciclo interno se usa `end=" "` para dejar los números de una fila en la misma línea.
