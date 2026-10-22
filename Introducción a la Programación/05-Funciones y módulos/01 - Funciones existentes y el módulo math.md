---
ramo: "Introducción a la Programación"
tema: "Funciones y módulos"
tags:
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[04 - Funciones predefinidas, random y booleanos]]"
  - "[[02 - El ciclo for y range]]"
---

# Funciones existentes y el módulo math

Una **función** es un pedazo de programa que calcula algo de forma independiente del resto. Ya se usaron muchas (`print`, `int`, `random.randint`) sin saber cómo están hechas por dentro. Antes de aprender a escribir funciones propias, conviene entender bien sus partes y conocer otras que ya existen, como las del módulo `math`.

## Las tres partes de una función

Una función es como un **mini programa**, con entrada, proceso y salida:

| Parte | Qué es | En `int("42")` |
|---|---|---|
| **Parámetros** (o argumentos) | Los datos que recibe, entre paréntesis y separados por comas | `"42"` |
| **Código** | Las operaciones que hace por dentro | Convertir el texto en número |
| **Resultado** (valor de retorno) | Lo que entrega al terminar | `42` |

**Retornar** es responder: el resultado es lo que uno guardaría en una variable (`x = int("42")`). Algunas funciones no retornan nada útil y solo hacen una acción, como `print`.

La cantidad de parámetros depende de la función:
- `print` recibe cero o más: `print()`, `print("a", 3, True)`.
- `float` recibe exactamente uno: `float("3.5")`.
- `range` recibe uno, dos o tres: `range(5)`, `range(1, 5)`, `range(1, 10, 2)`.

## Tres tipos de funciones

| Tipo | De dónde viene | Cómo se usa |
|---|---|---|
| **Existentes** | Vienen con Python, sueltas o en módulos de su biblioteca (`math`, `random`) | Directo, o después de `import` |
| **Definidas por otros** | Archivos `.py` escritos por otra persona (o por uno mismo, antes) | `import nombre_del_archivo` |
| **Propias** | Las escribe quien programa, en el mismo archivo | Se definen con `def` |

## El módulo `math`

`math` reúne funciones y constantes matemáticas:

```python
import math

print(math.sqrt(16))       # raíz cuadrada: 4.0
print(math.pi)             # 3.141592653589793
print(math.floor(3.7))     # redondea hacia abajo: 3
print(math.ceil(3.2))      # redondea hacia arriba: 4
```

`sqrt` viene de *square root* (raíz cuadrada) y equivale a `x ** 0.5`. Además existen funciones predefinidas que no necesitan `import`, como `abs` (valor absoluto), `max`, `min` y `round`:

```python
print(abs(-7), max(3, 9, 4), min(3, 9, 4), round(2.567, 2))
```

```
7 9 3 2.57
```

## Ejemplo: raíces entre dos números

```python
import math

a = 1
b = 5
for n in range(a, b + 1):
    print(n, round(math.sqrt(n), 3))
```

```
1 1.0
2 1.414
3 1.732
4 2.0
5 2.236
```

Y combinando dos módulos, la raíz de 3 números al azar entre 1 y 100:

```python
import math
import random

for i in range(3):
    n = random.randint(1, 100)
    print(n, math.sqrt(n))
```

> [!tip] Idea clave
> Antes de programar un cálculo, vale la pena preguntarse si ya existe una función que lo haga. Usarla ahorra trabajo y errores. La documentación oficial de Python lista todas las funciones predefinidas y las de cada módulo.

> [!warning] El `import` va primero
> Si se usa `math.sqrt` sin haber escrito `import math`, Python responde `NameError: name 'math' is not defined`. Los `import` se escriben al comienzo del archivo.

## Preguntas de repaso

> [!question]- ¿Cuáles son los parámetros y el resultado de `max(3, 9, 4)`?
> Los parámetros son 3, 9 y 4; el resultado es 9, el mayor de ellos.

> [!question]- ¿Qué diferencia hay entre `math.floor(3.7)` y `round(3.7)`?
> `floor` siempre redondea hacia abajo (da 3), mientras que `round` redondea al entero más cercano (da 4).

> [!question]- ¿Por qué `print` se considera una función que no retorna un valor útil?
> Porque su trabajo es una acción (mostrar algo en pantalla); si se guarda su resultado en una variable, esta queda con `None`, que no sirve para calcular.
