---
ramo: "Testing"
tema: "Ejecución simbólica y fuzzing concólico"
tags:
  - testing/ejecucion-simbolica-y-fuzzing-concolico
  - origen/complemento
prerrequisitos:
  - "[[Testing/11-Ejecución simbólica y fuzzing concólico/02 - Fuzzing simbólico manual construcción de caminos y ramas inalcanzables|Fuzzing simbólico manual construcción de caminos y ramas inalcanzables]]"
---

# El problema de la reasignación de variables en ejecución simbólica y forma SSA

## ¿Por qué `a = a + b` vuelve loco a un *SMT Solver* ingenuo?

En la nota anterior vimos que una asignación como `final = total - 5` se traduce en Z3 como la igualdad matemática `final == total - 5`. Eso funciona de maravilla cuando cada variable del programa se asigna **una sola vez**.

Pero, ¿qué ocurre cuando un programa **reasigna (modifica) una variable usando su propio valor anterior**, como hacemos todos los días en programación imperativa? Analicemos la **Pregunta 22 de la Clase 17 (Preparación Interrogación 2)**:

```python
def process_values(a: int, b: int) -> int:
    a = a + b        # Línea 1: reasigna 'a'
    b = a - 2        # Línea 2: reasigna 'b' usando el NUEVO 'a'
    if a > 10:       # Línea 3
        if b < 5:    # Línea 4
            return 1 # <-- Queremos alcanzar este return 1
    return 0
```

### El error de traducir `=` directamente como `==` sin renombrar

Imagina qué pasa si un *fuzzer* simbólico ingenuo (como `SimpleSymbolicFuzzer` básico) crea solo dos variables simbólicas `a = z3.Int('a')` y `b = z3.Int('b')` y traduce línea por línea el camino hacia `return 1`:
1. Línea 1 (`a = a + b`) $\xrightarrow{\text{mal}}$ agrega la ecuación $a == a + b$.
2. Línea 2 (`b = a - 2`) $\xrightarrow{\text{mal}}$ agrega la ecuación $b == a - 2$.
3. Líneas 3 y 4 $\xrightarrow{}$ agrega $a > 10$ y $b < 5$.

¡Mira lo que acaba de pasar en el sistema de ecuaciones!
* En álgebra, la ecuación $a = a + b$ **obliga matemáticamente a que $b = 0$** (restando $a$ a ambos lados).
* Si $b = 0$, entonces la segunda ecuación $b = a - 2$ se convierte en $0 = a - 2 \implies a = 2$.
* Y si $a = 2$, ¡es imposible cumplir $a > 10$! Z3 responderá erróneamente **`unsat` (`no solution`)**, haciéndonos creer que `return 1` es inalcanzable cuando en realidad sí es perfectamente alcanzable.

¿Por qué ocurrió este desastre? Porque en programación el signo `=` **no es una igualdad simétrica eterna**, sino una actualización de estado a lo largo del tiempo: el `a` a la izquierda de `a = a + b` es el **nuevo estado de `a` después de la línea 1**, mientras que el `a` a la derecha era el **valor antiguo de `a` antes de la línea 1**.

---

## La solución paso a paso: versionado de variables (Forma SSA)

Para que la ejecución simbólica funcione ante reasignaciones, debemos aplicar una transformación clásica de compiladores llamada **Forma de Asignación Única Estática (*Static Single Assignment* o SSA)**: **cada vez que una variable recibe una nueva asignación, creamos una variable simbólica nueva con un subíndice de versión incrementado ($a_0 \to a_1$, $b_0 \to b_1$)**.

Resolvamos paso a paso el ejercicio de interrogación `process_values(a, b)` usando versionado SSA:

### Paso 1: Asignar versiones a las entradas y a cada reasignación

* **Entradas originales al entrar a la función:** llamémoslas **$a_0$** y **$b_0$**.
* **Línea 1 (`a = a + b`):** nace una nueva versión **$a_1$** definida por:
  $$a_1 == a_0 + b_0$$
* **Línea 2 (`b = a - 2`):** nace una nueva versión **$b_1$** que usa la versión vigente de `a` ($a_1$):
  $$b_1 == a_1 - 2$$
* **Línea 3 (`if a > 10:`):** evalúa la versión vigente de `a` ($a_1$):
  $$a_1 > 10$$
* **Línea 4 (`if b < 5:`):** evalúa la versión vigente de `b` ($b_1$):
  $$b_1 < 5$$

### Paso 2: Expresar las restricciones en función de las entradas originales $(a_0, b_0)$ o pasarlas a Z3

Podemos pasarle las cuatro fórmulas con $a_0, b_0, a_1, b_1$ directamente a Z3, o bien sustituir hacia atrás para dejar el *path constraint* expresado puramente en términos de los parámetros de entrada $(a_0, b_0)$:
1. Sustituyendo $a_1 = a_0 + b_0$ en $b_1 = a_1 - 2$, obtenemos:
   $$b_1 = (a_0 + b_0) - 2$$
2. Por lo tanto, las dos condiciones para entrar a `return 1` son:
   $$\begin{cases} a_0 + b_0 > 10 \\ (a_0 + b_0) - 2 < 5 \iff a_0 + b_0 < 7 \end{cases}$$

¡Detente a mirar ese resultado!
* La primera condición exige que la suma $a_0 + b_0$ sea **estrictamente mayor que $10$** ($a_0 + b_0 > 10$).
* La segunda condición exige que $(a_0 + b_0) - 2 < 5$, lo que equivale a que la suma $a_0 + b_0$ sea **estrictamente menor que $7$** ($a_0 + b_0 < 7$).
* ¡Ningún par de números enteros puede sumar más de $10$ y al mismo tiempo menos de $7$! Gracias al versionado SSA ($a_0, a_1, b_0, b_1$), demostramos **sin corromper el solver** por qué la condición real del camino es $(a_0 + b_0 > 10) \land (a_0 + b_0 - 2 < 5)$, y si la segunda condición hubiera sido `if b < 15:` ($a_0 + b_0 - 2 < 15 \iff a_0 + b_0 < 17$), Z3 nos entregaría inmediatamente una solución válida como $a_0 = 6, b_0 = 5$ (donde $a_1 = 11 > 10$ y $b_1 = 9 < 15$).

```python
import z3

a0, b0, a1, b1 = z3.Ints("a0 b0 a1 b1")
s = z3.Solver()
s.add(a1 == a0 + b0)
s.add(b1 == a1 - 2)
s.add(a1 > 10)
s.add(b1 < 5)   # Con b1 < 5 da unsat (10 < a0+b0 < 7); con b1 < 15 da sat (ej. a0=6, b0=5)
print(s.check())
```

---

## Preguntas de repaso

> [!question]- En `process_values(a, b)`, ¿qué error matemático comete un analizador simbólico si traduce la instrucción `a = a + b` como la restricción `a == a + b` usando la misma variable simbólica `a` en ambos lados?
> Trata una asignación imperativa (cambio de estado en el tiempo) como una igualdad algebraica instantánea. En los números enteros, la ecuación $a = a + b$ se simplifica restando $a$ en ambos miembros a $0 = b$, forzando artificialmente a que el parámetro `b` valga siempre `0` y descartando todas las ejecuciones reales donde $b \neq 0$.

> [!question]- ¿En qué consiste la transformación a forma SSA (*Static Single Assignment*) para resolver el problema de la reasignación de variables en ejecución simbólica?
> Consiste en crear una **nueva variable simbólica versionada** (por ejemplo, $a_0, a_1, a_2, \dots$) cada vez que una variable del programa es reasignada, y reemplazar toda lectura posterior de esa variable por su versión más reciente activa. De ese modo, ninguna variable simbólica aparece a la izquierda de dos asignaciones distintas y cada paso se traduce limpiamente en una ecuación sin contradicciones.

> [!question]- Aplica forma SSA al fragmento `x = x * 2; if x == 10: return 1` y escribe las restricciones exactas en Z3 que permiten hallar el valor inicial de `x`.
> Llamando `x0` al valor de entrada de `x` y `x1` al valor tras la reasignación:
> 1. `x1 == x0 * 2`
> 2. `x1 == 10`
> Al resolver `[x1 == x0 * 2, x1 == 10]`, Z3 sustituye `x0 * 2 == 10` y obtiene el valor inicial exacto de entrada: **`x0 = 5`**.

