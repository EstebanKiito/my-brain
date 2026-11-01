---
ramo: "Testing"
tema: "Ejecución simbólica y fuzzing concólico"
tags:
  - testing/ejecucion-simbolica-y-fuzzing-concolico
  - origen/complemento
prerrequisitos:
  - "[[Testing/10-Análisis de flujo de información y taint analysis/02 - Implementación de strings contaminados con la clase tstr en Python|Implementación de strings contaminados con la clase tstr en Python]]"
  - "[[Testing/11-Ejecución simbólica y fuzzing concólico/01 - Variables simbólicas predicados de camino y resolución con Z3|Variables simbólicas predicados de camino y resolución con Z3]]"
---

# Ejecución concólica: ConcolicTracer y exploración negando restricciones

## ¿Qué significa *Concolic*? (**Conc**rete + Symb**olic**)

La ejecución simbólica pura intenta analizar estáticamente todos los caminos del código a la vez, pero sufre cuando el programa tiene bucles complejos o llama a librerías externas. La **ejecución concólica** (Larson & Austin, 2003; Sen et al., 2005 en CUTE) propone un camino híbrido muy ingenioso:

1. **Ejecución concreta:** arranca ejecutando la función de verdad con **una entrada concreta semilla (*seed*)**, por ejemplo `factorial(5)` o `triangle(1, 2, 3)`.
2. **Sombra simbólica en paralelo:** mientras el programa corre con esos números reales, cada argumento lleva adosada una **variable simbólica sombra** (usando objetos *proxy* como `zint`, `zbool`, `zstr`, idénticos en espíritu al `tstr` de *Taint Analysis*). Cada vez que la ejecución pasa por un `if`, el *proxy* anota en una lista `path` qué condición simbólica se cumplió (`cond` si entró al `if`, o `Not(cond)` si saltó al `else`).
3. **Negación sistemática para explorar vecinos:** al terminar la corrida, tomamos una de las condiciones registradas en `path`, **la invertimos (`z3.Not(...)`)** manteniendo intactas las anteriores, y le pedimos a Z3 una nueva entrada concreta que fuerce al programa a desviarse hacia la rama vecina no visitada.

---

## Ejemplo paso a paso: de `factorial(5)` a cubrir las ramas faltantes

Observa qué pasa al ejecutar `factorial(n)` con la semilla concreta `n = 5`:

```python
def factorial(n):
    if n < 0:      # Decisión 0: con n=5 es False -> registra Not(n < 0)
        return None
    if n == 0:     # Decisión 1: con n=5 es False -> registra Not(n == 0)
        return 1
    if n == 1:     # Decisión 2: con n=5 es False -> registra Not(n == 1)
        return 1
    v = 1
    while n != 0:
        v = v * n
        n = n - 1
    return v
```

Hasta antes del bucle `while`, la traza concólica de `factorial(5)` recolectó los tres predicados:
$$\text{predicates} = [\;\neg(n < 0),\; \neg(n == 0),\; \neg(n == 1)\;]$$

* **¿Cómo generamos una entrada que entre al tercer `if` (`if n == 1: return 1`)?**
  Mantenemos los dos primeros predicados (para no desviarnos antes) e **invertimos el último predicado**:
  ```python
  z3.solve(predicates[0:-1] + [z3.Not(predicates[-1])])
  # Resuelve: Not(n < 0) ∧ Not(n == 0) ∧ (n == 1)  -->  Entrega: [n = 1]
  ```
* **¿Cómo generamos una entrada que entre al primer `if` (`if n < 0: return None`)?**
  Invertimos el primer predicado (`index 0`): `z3.solve(zn < 0)` $\to$ entrega `[n = -1]`.

---

## Uso práctico de `ConcolicTracer` en `triangle` y `treasure_points`

En `fuzzingbook`, la clase `ConcolicTracer` automatiza los objetos *proxy* dentro de un bloque `with`:

```python
from fuzzingbook.ConcolicFuzzer import ConcolicTracer
import z3

def triangle(a, b, c):
    if a == b:
        if b == c: return "equilateral"
        else:      return "isosceles #1"
    else:
        if b == c: return "isosceles #2"
        elif a == c: return "isosceles #3"
        else:      return "scalene"

with ConcolicTracer() as _:
    print(_[triangle](1, 2, 3))  # Ejecuta con la semilla (1, 2, 3) -> 'scalene'
```

Al salir del bloque `with`, el objeto tracer `_` expone tres atributos y métodos fundamentales:
1. **`_.decls`:** diccionario con las variables simbólicas creadas para la función:
   `{'triangle_a_int_1': 'Int', 'triangle_b_int_2': 'Int', 'triangle_c_int_3': 'Int'}`.
2. **`_.path`:** lista de condiciones simbólicas Z3 que tomó exactamente la ejecución `(1, 2, 3)`:
   `[Not(triangle_a_int_1 == triangle_b_int_2), Not(triangle_b_int_2 == triangle_c_int_3), Not(triangle_a_int_1 == triangle_c_int_3)]`.
3. **`_.zeval()`:** llama a Z3 sobre `_.path` y devuelve otra tupla concreta que recorre ese mismo camino, por ejemplo `('sat', ({'a': 0, 'b': -2, 'c': -1}, ()))`.

### Cómo forzar sistemáticamente todos los caminos negando índices

Supongamos que a partir de la traza de `triangle(1, 2, 3)` (donde `_.path` tiene índice `0`: $a \neq b$, índice `1`: $b \neq c$, índice `2`: $a \neq c$) queremos cubrir todas las demás ramas:

* **Alcanzar `'isosceles #3'` ($a \neq b \land b \neq c \land a == c$):** negamos la condición del **índice 2**:
  ```python
  za, zb, zc = [z3.Int(s) for s in _.decls.keys()]
  _.zeval({2: za == zc})  # o bien: _.path[2] = z3.Not(_.path[2]); _.zeval()
  # -> ('sat', {'a': 1, 'b': 0, 'c': 1}) -> triangle(1, 0, 1) da 'isosceles #3'
  ```
* **Alcanzar `'isosceles #2'` ($a \neq b \land b == c$):** truncamos el camino hasta el índice 1 y negamos el **índice 1**:
  ```python
  _.zeval({1: zb == zc})
  # -> ('sat', {'a': 1, 'b': 0, 'c': 0}) -> triangle(1, 0, 0) da 'isosceles #2'
  ```
* **Alcanzar la mitad superior (`a == b`):** truncamos las decisiones posteriores (`_.path = _.path[0:-2]`) y negamos la raíz (**índice 0**, exigiendo $a == b$):
  ```python
  _.path = _.path[0:-2]
  _.path[0] = z3.Not(_.path[0])
  _.zeval()  # -> ('sat', {'a': 0, 'b': 0, 'c': 0}) -> entra a 'equilateral'
  ```
  Luego, trazando `triangle(0, 0, 0)` (cuyo `_.path` es `[a == b, b == c]`) y negando su nuevo índice `1` (`_.path[1] = z3.Not(_.path[1])`), obtenemos `(1, 1, 0)`, cubriendo `'isosceles #1'` y alcanzando el **$100\%$ de cobertura de arcos (`ArcCoverage`)**.

*(La clase `SimpleConcolicFuzzer` automatiza este ciclo manteniendo un árbol de trazas `scf.ct.root`, eligiendo en cada iteración `scf.fuzz()` un arco `"?"` aún no visitado para negarlo y agregando la nueva traza con `scf.add_trace(_, v)`).*

---

---

## Ejemplo práctico: un mini motor concólico con Z3

Sin depender de `fuzzingbook`, se puede reproducir la lógica: partimos de una traza conocida y **negamos una condición a la vez**, manteniendo las anteriores.

```python
import z3

def triangle(a, b, c):
    if a == b:
        if b == c: return "equilateral"
        else:      return "isosceles #1"
    else:
        if b == c: return "isosceles #2"
        elif a == c: return "isosceles #3"
        else:      return "scalene"

A, B, C = z3.Ints("a b c")
path = [A != B, B != C, A != C]          # traza de la semilla (1, 2, 3)
print("semilla:", triangle(1, 2, 3))     # scalene

for i in range(len(path)):
    restricciones = path[:i] + [z3.Not(path[i])]
    s = z3.Solver()
    s.add(*restricciones)
    if s.check() == z3.sat:
        m = s.model()
        v = tuple(m.eval(x, model_completion=True).as_long() for x in (A, B, C))
        print(i, v, "->", triangle(*v))
```

Una salida posible:

```
semilla: scalene
0 (0, 0, 0) -> equilateral
1 (1, 0, 0) -> isosceles #2
2 (1, 0, 1) -> isosceles #3
```

Cada iteración conserva las decisiones previas y **invierte solo la actual**:

| Negación | Restricciones enviadas a Z3 | Rama alcanzada |
| :---: | :--- | :--- |
| índice $0$ | $\neg(a \ne b)$ es decir $a = b$ | mitad `a == b` (aquí cayó en `equilateral`) |
| índice $1$ | $a \ne b \land b = c$ | `isosceles #2` |
| índice $2$ | $a \ne b \land b \ne c \land a = c$ | `isosceles #3` |

Con la semilla y estas tres entradas se cubren $4$ de los $5$ retornos. Falta `isosceles #1` ($a = b$, $b \ne c$): para alcanzarlo hay que **iterar**, usando como nueva semilla alguna de las entradas generadas (por ejemplo `(0, 0, 0)`), cuya traza es `[a == b, b == c]`, y negar su último predicado: `a == b ∧ ¬(b == c)`. Es el ciclo completo del fuzzing concólico: ejecutar, registrar, negar, resolver, repetir.

### Qué pasa con una condición no simbolizable

Supón una rama `if hash(x) == 0xCAFE:`. En ejecución concólica, `hash(x)` se evalúa con el valor **concreto** de `x`; si no podemos traducir `hash` a Z3, se omite esa condición del `path` y seguimos con el resto. Se pierde completitud (no llegamos a esa rama), pero la ejecución sigue siendo válida y no se bloquea.

---

## Preguntas de repaso

> [!question]- ¿Por qué para desviar la ejecución hacia la rama verdadera de la decisión $k$-ésima de `_.path` debemos mantener iguales las restricciones $0, 1, \dots, k-1$, invertir únicamente la restricción $k$ (`z3.Not(_.path[k])`) y descartar las restricciones posteriores $k+1, \dots$?
> * **Mantener $0 \dots k-1$:** garantiza que la nueva ejecución llegue exactamente hasta el mismo `if` número $k$ sin desviarse antes por otra rama superior.
> * **Invertir $k$:** fuerza a que en el `if` número $k$ se tome la rama opuesta a la de la semilla original.
> * **Descartar $k+1 \dots$:** las condiciones posteriores pertenecían al subárbol antiguo que ya no se ejecutará tras doblar hacia la nueva rama en $k$; conservarlas agregaría restricciones irrelevantes o contradictorias.

> [!question]- En la función `treasure_points(gold, traps)`, si la primera condición es `if traps == 0:` (con `if gold > 5:` adentro) y el `else` tiene `if traps > 3:`, ¿qué guarda `_.path` al trazar `_[treasure_points](0, 6)` y cómo obtienes con `_.zeval()` una entrada para la rama `traps != 0 and traps <= 3`?
> Con `gold = 0, traps = 6`, la primera condición `traps == 0` es falsa y la segunda `traps > 3` es verdadera, por lo que `_.path` guarda `[Not(traps == 0), traps > 3]`. Para alcanzar la rama `traps != 0 and traps <= 3`, basta con negar el índice `1` (`_.path[1] = z3.Not(_.path[1])`) y llamar a `_.zeval()`, lo que resuelve `Not(traps == 0) ∧ Not(traps > 3)` y entrega p. ej. `gold = 0, traps = 1`.

> [!question]- ¿Cómo logra `ConcolicTracer` interceptar las comparaciones (`==`, `<`, `>`) dentro de una función normal de Python sin reescribir su AST?
> Al invocar `_[funcion](arg1, arg2)`, `ConcolicTracer` envuelve cada argumento concreto (`int`, `str`, `bool`) en un objeto *proxy* subclase (`zint`, `zstr`, `zbool`) que sobrecarga los métodos mágicos de comparación (`__eq__`, `__lt__`, `__gt__`, etc.) y el método `__bool__`: cuando el `if` de Python consulta el valor de verdad de la comparación, el *proxy* devuelve el booleano concreto real y simultáneamente registra la fórmula simbólica Z3 en `self.path`.

> [!question]- ¿Por qué se descartan las decisiones posteriores al índice negado (`path[:i] + [Not(path[i])]`) y no se mantienen?
> Porque tras invertir la decisión $i$ el programa toma otra rama y las decisiones posteriores de la traza original ya no se evalúan (no pertenecen al nuevo camino). Mantenerlas agregaría restricciones sobre condiciones que ni siquiera se ejecutan, y podría volver `unsat` un camino alcanzable.

> [!question]- Dada la traza de `factorial(5)` con predicados $[\neg(n<0),\ \neg(n=0),\ \neg(n=1)]$, ¿qué restricciones envías a Z3 para llegar a `return 1` por la rama `n == 0`?
> Mantienes el primer predicado y niegas el segundo: $[\neg(n<0),\ n=0]$. Z3 entrega $n = 0$, y `factorial(0)` devuelve `1` por esa rama, que no se había cubierto con la semilla $n = 5$.
