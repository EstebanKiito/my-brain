---
ramo: "Introducción a la Programación"
tema: "Recursión"
tags:
  - programacion/recursion
  - origen/complemento
prerrequisitos:
  - "[[01 - Caso base y caso recursivo]]"
---

# Fibonacci, fractales y recursión versus ciclos

En el factorial cada llamada genera **una** llamada nueva. Hay problemas donde la solución depende de **dos o más** versiones más pequeñas, y ahí la recursión brilla: el código queda corto y se parece mucho a la definición del problema. Esta nota muestra dos de esos casos (los conejos de Fibonacci y un árbol dibujado con la tortuga) y discute cuándo conviene recursión y cuándo un ciclo.

## Los conejos de Fibonacci

Un problema clásico: una pareja de conejos recién nacidos tarda un mes en madurar, y desde entonces produce una pareja nueva cada mes. ¿Cuántas parejas hay cada mes?

![Árbol de parejas de conejos mes a mes](adjuntos/Conejos%20de%20Fibonacci%20mes%20a%20mes.png)

> [!example]- Transcripción de la imagen
> - Árbol de parejas de conejos (cada pareja dibujada como dos caras) que crece hacia abajo, un nivel por mes.
> - A la derecha, el número de parejas por mes: 1, 1, 2, 3, 5.
> - Cada pareja madura tiene una pareja hija al mes siguiente; las recién nacidas esperan un mes antes de reproducirse.

Las parejas de este mes son las del mes anterior (siguen vivas) más las que nacen, que son tantas como las parejas que había hace dos meses (todas ya maduras). Así aparece la **sucesión de Fibonacci**: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …, donde cada número es la suma de los dos anteriores.

```python
def fibonacci(mes):
    if mes == 1 or mes == 2:                       # dos casos base
        return 1
    return fibonacci(mes - 1) + fibonacci(mes - 2)  # dos llamadas recursivas

for i in range(1, 11):
    print(fibonacci(i), end=" ")
print()
```

```
1 1 2 3 5 8 13 21 34 55
```

(Otra convención común empieza en 0: `fibonacci(0) = 0`, `fibonacci(1) = 1`; la idea es la misma.)

> [!warning] Las llamadas se multiplican
> `fibonacci(5)` llama a `fibonacci(4)` y `fibonacci(3)`; `fibonacci(4)` vuelve a llamar a `fibonacci(3)`… El mismo valor se calcula muchas veces, y la cantidad de llamadas casi se duplica con cada mes. Por eso `fibonacci(40)` ya tarda varios segundos y `fibonacci(47)` puede tardar muchos minutos.

## Un árbol fractal con la tortuga

El módulo `turtle` de Python es la tortuga de Blockly, escrita en código (`forward`, `back`, `left`, `right`). Un **árbol** es un tronco con dos árboles más pequeños encima: una definición recursiva perfecta.

```text
from turtle import *

def dibujar_arbol(n, largo):
    if n == 0:                     # caso base: no dibuja nada
        return
    forward(largo)                 # tronco
    left(45)
    dibujar_arbol(n - 1, largo * 2 / 3)   # rama izquierda (un árbol más chico)
    right(90)
    dibujar_arbol(n - 1, largo * 2 / 3)   # rama derecha
    left(45)
    back(largo)                    # vuelve al punto de partida

dibujar_arbol(8, 100)
```

![Árbol fractal dibujado con recursión](adjuntos/%C3%81rbol%20fractal%20dibujado%20con%20recursi%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Un árbol que crece hacia la derecha: un tronco horizontal que se divide en dos ramas, cada una se divide otra vez en dos, y así varios niveles, con ramas cada vez más cortas.

El detalle clave es la última línea: cada llamada **deja a la tortuga donde la encontró** (mismo lugar y misma dirección). Así, después de dibujar la rama izquierda, la tortuga está otra vez en la punta del tronco y puede girar para dibujar la derecha. A un dibujo que repite su forma a escalas cada vez menores se le llama **fractal**.

## ¿Recursión o ciclo?

Casi todo lo que se hace con recursión se puede hacer con ciclos, y al revés.

| | Recursión | Ciclos |
|---|---|---|
| Código | Corto y parecido a la definición matemática | A veces más largo o enredado |
| Memoria | Cada llamada pendiente ocupa memoria | Usa unas pocas variables |
| Velocidad | Más lenta (muchas llamadas), sobre todo si repite cálculos | En general más rápida |
| Mejor para | Problemas que se dividen en subproblemas parecidos (árboles, fractales, búsquedas) | Repetir un paso un número conocido de veces |

Fibonacci con un ciclo, guardando solo los dos últimos valores, es instantáneo incluso para meses grandes:

```python
def fibonacci_ciclo(mes):
    a, b = 1, 1
    for i in range(mes - 2):
        a, b = b, a + b
    return b

print(fibonacci_ciclo(47))
```

```
2971215073
```

> [!tip] Idea clave
> La recursión es una forma de **pensar** un problema: si se puede describir en función de versiones más chicas de sí mismo, la solución recursiva suele ser la más fácil de escribir. Luego, si es muy lenta, se puede pasar a un ciclo. Este tema se profundiza en [[Estructuras de Datos/_Índice|Estructuras de Datos]].

## Preguntas de repaso

> [!question]- ¿Por qué Fibonacci necesita dos casos base y el factorial uno solo?
> Porque cada valor de Fibonacci depende de los **dos** anteriores. Con un solo caso base, `fibonacci(2)` llamaría a `fibonacci(0)`, que no está definido, y la recursión no se detendría.

> [!question]- ¿Por qué la versión recursiva de Fibonacci es tan lenta para meses grandes?
> Porque recalcula los mismos valores una y otra vez: cada llamada abre dos llamadas más, y la cantidad total crece casi al doble con cada mes.

> [!question]- En `dibujar_arbol`, ¿para qué sirven `left(45)` y `back(largo)` al final?
> Dejan a la tortuga en la misma posición y dirección en que empezó esa llamada. Sin eso, la siguiente rama se dibujaría desde un lugar equivocado.
