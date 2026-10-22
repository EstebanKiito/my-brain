---
ramo: "Introducción a la Programación"
tema: "Ordenamiento"
tags:
  - programacion/ordenamiento
  - origen/complemento
prerrequisitos:
  - "[[01 - Sort, sorted y criterios con key]]"
  - "[[02 - Modelar datos con listas de listas]]"
---

# Problema integrador: estaciones de combinación

Al final del curso, los problemas de evaluación mezclan casi todo lo aprendido: listas de listas para modelar datos, ciclos anidados para buscar, funciones para ordenar el código y `sort` para presentar el resultado. Esta nota resuelve uno paso a paso, mostrando cómo se piensa un problema así.

## El problema

Una red de metro se guarda como una lista de líneas; cada línea es `[nombre_linea, [estaciones]]`. Se pide una función `estaciones_comunes(metro)` que retorne las **estaciones de combinación** (las que están en más de una línea) junto con las líneas donde aparecen, **ordenadas alfabéticamente** por estación.

```python
metro = [["L1", ["San Pablo", "Los Heroes", "Baquedano", "Tobalaba"]],
         ["L2", ["Vespucio Norte", "Los Heroes", "Franklin"]],
         ["L5", ["Plaza de Maipu", "Baquedano", "Franklin"]]]
```

Resultado esperado:

```text
[['Baquedano', ['L1', 'L5']], ['Franklin', ['L2', 'L5']], ['Los Heroes', ['L1', 'L2']]]
```

## Paso 1: entender los datos

- `metro[i]` es una línea, por ejemplo `["L1", [...]]`.
- `metro[i][0]` es su nombre y `metro[i][1]` su lista de estaciones.
- El resultado es otra lista de listas: `[estacion, [lineas]]`.

Escribir un ejemplo chico a mano y el resultado esperado (como arriba) aclara qué hay que construir.

## Paso 2: el algoritmo en palabras

Para cada línea `i` y cada estación de esa línea:
1. Empezar una lista con el nombre de la línea `i`.
2. Revisar las líneas **siguientes** (`j > i`) y agregar las que también tienen esa estación.
3. Si la lista quedó con más de una línea y la estación no se había agregado antes, guardarla en el resultado.

Al final, ordenar el resultado por el nombre de la estación.

Revisar solo las líneas siguientes evita contar dos veces la misma combinación (Baquedano se detecta desde L1; al llegar a L5 ya está guardada).

## Paso 3: el código

```python
def nombre_estacion(item):
    return item[0]

def estaciones_comunes(metro):
    resultados = []
    ya_agregadas = []
    for i in range(len(metro)):
        nombre_linea, estaciones = metro[i]
        for estacion in estaciones:
            lineas = [nombre_linea]
            for j in range(i + 1, len(metro)):
                if estacion in metro[j][1]:
                    lineas.append(metro[j][0])
            if len(lineas) > 1 and estacion not in ya_agregadas:
                resultados.append([estacion, lineas])
                ya_agregadas.append(estacion)
    resultados.sort(key=nombre_estacion)
    return resultados

metro = [["L1", ["San Pablo", "Los Heroes", "Baquedano", "Tobalaba"]],
         ["L2", ["Vespucio Norte", "Los Heroes", "Franklin"]],
         ["L5", ["Plaza de Maipu", "Baquedano", "Franklin"]]]
for fila in estaciones_comunes(metro):
    print(fila)
```

```
['Baquedano', ['L1', 'L5']]
['Franklin', ['L2', 'L5']]
['Los Heroes', ['L1', 'L2']]
```

## Qué se usó de cada tema

| Herramienta | Tema |
|---|---|
| Lista de listas `[nombre, [estaciones]]` | Listas de listas |
| Tres ciclos anidados y `in` para buscar | Ciclos y listas |
| `ya_agregadas` para no repetir | Patrón de filtrar |
| `nombre_linea, estaciones = metro[i]` | Asignar varios valores a la vez |
| `sort(key=…)` | Ordenamiento |
| Funciones con `return` | Funciones |

> [!tip] Cómo enfrentar un problema largo
> 1. Entender la forma de los datos de entrada y salida, con un ejemplo a mano.
> 2. Escribir el algoritmo en palabras.
> 3. Programar por partes, probando cada una con `print`.
> 4. Revisar casos especiales: ¿y si no hay ninguna combinación? (la función retorna `[]`).

## Preguntas de repaso

> [!question]- ¿Por qué el ciclo de `j` empieza en `i + 1` y no en 0?
> Para comparar cada línea solo con las siguientes: así cada combinación se encuentra desde la primera línea que la contiene y no se revisan pares repetidos.

> [!question]- ¿Para qué sirve la lista `ya_agregadas`?
> Una estación que está en tres líneas se detectaría de nuevo al revisar la segunda línea; `ya_agregadas` evita guardarla dos veces.

> [!question]- ¿Qué retorna la función si ninguna estación se repite?
> Una lista vacía `[]`, porque nunca se cumple `len(lineas) > 1`.
