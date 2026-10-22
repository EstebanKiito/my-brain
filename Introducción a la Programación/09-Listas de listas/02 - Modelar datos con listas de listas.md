---
ramo: "Introducción a la Programación"
tema: "Listas de listas"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[01 - Matrices: filas, columnas y recorridos]]"
  - "[[02 - Métodos de listas y conversión con strings]]"
---

# Modelar datos con listas de listas

Las listas de listas no son solo tableros de números: sirven para **representar información** del mundo real, como una libreta de contactos, un árbol genealógico o las rutas entre ciudades. La parte difícil no es el código, sino **decidir cómo organizar los datos** para que las preguntas sean fáciles de responder.

## Una libreta de contactos

Cada fila es una persona y cada columna un dato fijo: 0 = nombre, 1 = mail, 2 = cumpleaños (`dd/mm`).

```python
amigos = [["Inigo", "inigo@gmail.com", "03/10"],
          ["Lucy", "lucy@gmail.com", "10/06"],
          ["Ada", "ada@gmail.com", "18/09"]]

# ¿Quiénes cumplen años en el segundo semestre (meses 7 a 12)?
for amigo in amigos:
    mes = int(amigo[2].split("/")[1])
    if mes >= 7:
        print(amigo[0])

# ¿Cuál es el mail de Lucy?
for amigo in amigos:
    if amigo[0] == "Lucy":
        print(amigo[1])
```

```
Inigo
Ada
lucy@gmail.com
```

Cada pregunta es un recorrido por las filas mirando la columna adecuada. Combinar con métodos de strings (`split`) permite sacar partes de un dato, como el mes del cumpleaños.

> [!tip] Documentar el significado de las columnas
> En una lista, las columnas no tienen nombre: `amigo[2]` no dice "cumpleaños". Conviene dejar un comentario que explique qué es cada posición. (Las clases, más adelante, resuelven esto dando nombre a cada dato.)

## Un árbol genealógico

Ahora cada fila guarda un nombre y la **lista de posiciones de sus hijos**: una lista dentro de una lista dentro de una lista.

```python
arbol = [["Abraham", [1, 2]],     # 0
         ["Herb", []],            # 1
         ["Homero", [3, 4, 5]],   # 2
         ["Bart", []],            # 3
         ["Maggie", []],          # 4
         ["Lisa", []],            # 5
         ["Marge", [3, 4, 5]]]    # 6

def hijos(arbol, nombre):
    resultado = []
    for persona in arbol:
        if persona[0] == nombre:
            for i in persona[1]:
                resultado.append(arbol[i][0])
    return resultado

def padres(arbol, nombre):
    resultado = []
    for i in range(len(arbol)):
        if arbol[i][0] == nombre:          # i es la posición de la persona
            for persona in arbol:
                if i in persona[1]:        # ¿la tiene como hija?
                    resultado.append(persona[0])
    return resultado

print(hijos(arbol, "Marge"))
print(padres(arbol, "Lisa"))
```

```
['Bart', 'Maggie', 'Lisa']
['Homero', 'Marge']
```

Los hijos se guardan como **posiciones** (índices) en vez de nombres; así `arbol[i][0]` lleva directo a los datos de cada hijo.

## Rutas de vuelos: una matriz de "sí o no"

Para 4 ciudades, una matriz `t` de 4 × 4 donde `t[i][j]` es 1 si hay vuelo directo de la ciudad `i` a la `j`, y 0 si no:

```python
t = [[0, 1, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 1, 0]]

# Vuelos de ida sin vuelta: hay i -> j pero no j -> i
for i in range(len(t)):
    for j in range(len(t)):
        if t[i][j] == 1 and t[j][i] == 0:
            print(i, "->", j)
```

```
2 -> 0
3 -> 2
```

Esta forma de guardar conexiones se llama **matriz de adyacencia**. Con ella se pueden responder preguntas más difíciles: ¿se puede llegar de `i` a `j` con una escala? Sí, si existe una ciudad `k` con `t[i][k] == 1` y `t[k][j] == 1`. Y repitiendo ese cálculo (incluso recursivamente) hasta que el resultado ya no cambie, se obtiene a qué ciudades se puede llegar con **cualquier** número de escalas. Este tipo de problemas se estudia en profundidad como **grafos** en [[Estructuras de Datos/_Índice|Estructuras de Datos]].

## Cómo elegir la representación

| Si los datos son… | Representación |
|---|---|
| Una tabla con columnas fijas (contactos, notas por alumno) | Lista de filas, una columna por dato |
| Un tablero o una cuadrícula | Matriz `M[fila][columna]` |
| Relaciones entre elementos (familia, rutas) | Índices que apuntan a otras filas, o matriz de 0 y 1 |

## Preguntas de repaso

> [!question]- En la libreta, ¿por qué se usa `amigo[2].split("/")[1]` para obtener el mes?
> Porque `amigo[2]` es el texto `"dd/mm"`; `split("/")` lo separa en `["dd", "mm"]` y `[1]` toma el mes, que luego se convierte con `int`.

> [!question]- En el árbol, ¿qué ventaja tiene guardar los hijos como posiciones y no como nombres?
> Con la posición se llega directamente a la fila del hijo (`arbol[i]`) y a todos sus datos, sin tener que buscarlo por nombre.

> [!question]- En la matriz de vuelos, ¿qué significa que `t[i][j] == 1` y `t[j][i] == 0`?
> Que hay vuelo directo de la ciudad `i` a la `j`, pero no de vuelta de `j` a `i`.
