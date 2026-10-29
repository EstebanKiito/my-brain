---
ramo: "Testing"
tema: "Ejecución simbólica y fuzzing concólico"
tags:
  - testing/ejecucion-simbolica-y-fuzzing-concolico
  - origen/complemento
prerrequisitos:
  - "[[Testing/04-Fuzzing aleatorio y fuzzing basado en mutación/01 - Fuzzing aleatorio y sus límites ante entradas estructuradas|Fuzzing aleatorio y sus límites ante entradas estructuradas]]"
  - "[[Testing/05-Fuzzing basado en búsqueda/03 - Distancia de ramas estilo EvoSuite y algoritmos genéticos|Distancia de ramas estilo EvoSuite y algoritmos genéticos]]"
---

# Variables simbólicas, predicados de camino y resolución con Z3

## Dejar de adivinar: el programa como un sistema de ecuaciones

En los Temas 04 y 05 vimos que el *fuzzing* aleatorio choca contra un muro cuando una rama exige una condición muy estrecha, como `if x == 2 * (y + 1) and y == 42:`. En lugar de lanzar millones de dados esperando acertar por casualidad (o escalar colinas paso a paso), ¿qué haría una persona si mira ese código en una pizarra? **Trataría a `x` e `y` como incógnitas de álgebra, plantearía el sistema de ecuaciones y lo despejaría de inmediato** ($y = 42 \implies x = 2 \cdot 43 = 86$).

Esa es exactamente la idea detrás de la **ejecución simbólica** y la **ejecución concólica**: reemplazar los valores concretos por **variables simbólicas** (marcadores algebraicos sin valor fijo), recolectar las condiciones de los `if` como ecuaciones o inecuaciones llamadas **restricciones de camino (*path constraints*)**, y pedirle a un resolvedor matemático automático que calcule valores concretos de entrada que satisfagan todas las ecuaciones a la vez.

---

## ¿Qué es un *SMT Solver* (y en qué supera a un *SAT Solver*)?

El motor matemático que resuelve estas restricciones se llama **SMT Solver** (*Satisfiability Modulo Theories*), y el estándar de la industria (desarrollado por Microsoft Research) es **Z3** (de Moura & Bjørner, 2008).

* **SAT Solver (*Boolean Satisfiability*):** solo entiende fórmulas de lógica proposicional con variables booleanas puras ($p, q \in \{\text{True}, \text{False}\}$), como $(p \lor q) \land (\neg p \lor \neg q)$, y decide si existe una asignación de verdad que haga verdadera la fórmula.
* **SMT Solver (*Satisfiability Modulo Theories*):** extiende un *SAT Solver* incorporando **teorías matemáticas de dominio** (aritmética entera y real, arreglos, vectores de bits y cadenas de texto). Por ejemplo, Z3 puede resolver directamente ecuaciones sobre enteros ($x + y == 10 \land x > y$) o sobre cadenas ($h + t == \text{"hello, world"}$) y entregarnos un ejemplo concreto (`model`).

---

## Uso práctico de Z3 en Python (`Int`, `Solver`, `sat`, `unsat` y `model`)

En la librería `z3-solver` de Python, nunca debes usar los operadores booleanos nativos de Python (`and`, `or`, `not`), porque Python intentaría evaluarlos inmediatamente a un booleano. En su lugar, se usan los constructores lógicos de Z3: **`z3.And(...)`**, **`z3.Or(...)`** y **`z3.Not(...)`** (o se agregan varias restricciones separadas por coma).

```python
import z3

# 1. Declaramos variables simbólicas enteras (incógnitas algebraicas)
x = z3.Int("x")
y = z3.Int("y")

# 2. Creamos el Solver y agregamos las restricciones (path constraints)
solver = z3.Solver()
solver.add(x + y == 10)
solver.add(x > y)
solver.add(y > 0)

# 3. Verificamos si el sistema tiene solución (z3.sat) o es imposible (z3.unsat)
if solver.check() == z3.sat:
    modelo = solver.model()
    print(f"Solución encontrada: x = {modelo[x]}, y = {modelo[y]}")  # ej. x = 6, y = 4
else:
    print("Sin solución: las restricciones se contradicen (unsat)")
```

Para pruebas rápidas en una sola línea, Z3 ofrece también el atajo **`z3.solve(r1, r2, ...)`**, que imprime directamente una solución por pantalla o `"no solution"` si es insatisfacible.

---

## Pregunta clásica de examen: ¿cómo pedirle a Z3 una solución *distinta*?

Cuando llamas a `solver.check()` sobre un camino como `qty >= 3` en `apply_coupon(total, qty)`, Z3 es determinista: siempre te devolverá la misma solución cómoda (por ejemplo, `qty = 3, total = 5`).

**¿Cómo obligamos al *SMT Solver* a que nos entregue un segundo y un tercer caso de prueba distinto para ese mismo camino?**
Agregando al conjunto de restricciones del camino **la negación de la solución anterior** (`qty != 3`):

```python
total = z3.Int("total")
qty = z3.Int("qty")

# Corrida 1: condición original del camino P1
z3.solve(qty >= 3, final == total - 5)
# -> [qty = 3, total = 5, final = 0]

# Corrida 2: agregamos qty != 3 para prohibir repetir la solución anterior
z3.solve(qty >= 3, final == total - 5, qty != 3)
# -> [qty = 4, total = 5, final = 0]

# Corrida 3: acumulamos también qty != 4
z3.solve(qty >= 3, final == total - 5, qty != 3, qty != 4)
# -> [qty = 5, total = 5, final = 0]
```

Si una función tiene varios parámetros `(a, b)`, para obtener un vector de entrada distinto basta con agregar `z3.Or(a != val_a, b != val_b)`.

---

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia fundamental entre un *SAT Solver* y un *SMT Solver* como Z3?
> Un *SAT Solver* solo resuelve fórmulas compuestas por variables booleanas puras (`True`/`False`). Un *SMT Solver* (*Satisfiability Modulo Theories*) extiende esa capacidad incorporando teorías formales sobre tipos de datos ricos —como aritmética de números enteros, números reales, listas y cadenas de caracteres—, permitiendo resolver ecuaciones como `x + y == 10` o `s1 + s2 == "hola"`.

> [!question]- ¿Por qué al escribir una condición compuesta para Z3 en Python no puedes escribir `solver.add(not (x > 5 and y < 3))` y debes escribir `solver.add(z3.Not(z3.And(x > 5, y < 3)))`?
> Porque en Python las palabras clave `and`, `or` y `not` no se pueden sobrecargar para devolver expresiones simbólicas: fuerzan la conversión inmediata del objeto a un `bool` concreto (`True` o `False`), lanzando un `Z3Exception` o evaluando incorrectamente la fórmula. Las funciones `z3.And`, `z3.Or` y `z3.Not` construyen nodos simbólicos en el árbol de fórmulas de Z3.

> [!question]- Si al resolver la ecuación cuadrática `2*x*x - 11*x + 5 == 0` con `z3.solve(eqn)` Z3 te entrega la solución `x = 5`, ¿qué instrucción exacta debes ejecutar para que Z3 encuentre la otra raíz sin repetir `5`?
> Debes añadir la restricción de desigualdad contra la solución ya conocida: **`z3.solve(eqn, x != 5)`**, con lo cual Z3 devolverá la segunda raíz (`x = 1/2` si `x = z3.Real('x')`).
