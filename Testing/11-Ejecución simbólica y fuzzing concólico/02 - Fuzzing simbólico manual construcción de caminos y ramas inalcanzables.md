---
ramo: "Testing"
tema: "Ejecución simbólica y fuzzing concólico"
tags:
  - testing/ejecucion-simbolica-y-fuzzing-concolico
  - origen/complemento
prerrequisitos:
  - "[[Testing/11-Ejecución simbólica y fuzzing concólico/01 - Variables simbólicas predicados de camino y resolución con Z3|Variables simbólicas predicados de camino y resolución con Z3]]"
---

# Fuzzing simbólico manual: construcción de caminos y ramas inalcanzables

## ¿Cómo funciona el *Symbolic Fuzzing*? (Pauta oficial de Interrogación 2)

A diferencia del *fuzzing* aleatorio o concólico, la **ejecución simbólica pura (*Symbolic Fuzzing*)** (King, 1976) **no ejecuta la función con ninguna entrada previa ni necesita una semilla (*seed*)**. Su mecanismo se resume en cuatro pasos que debes saber explicar con precisión en cualquier prueba escrita:

1. **Variables simbólicas:** trata los parámetros de entrada del programa como símbolos algebraicos ($a, b, c$) desde el principio.
2. **Enumeración estática de caminos:** analiza el árbol de sintaxis abstracta (AST) y el grafo de flujo de control (CFG) de la función para enumerar cada ruta posible desde el inicio hasta un `return` (hasta una profundidad máxima `max_depth`).
3. **Extracción de *path conditions*:** para cada camino, traduce las decisiones de los `if`/`else` intermedios (tomadas como verdaderas `L` o falsas `Not(L)`) y las asignaciones en una conjunción lógica llamada **condición de camino (*path condition*)**.
4. **Resolución con SMT Solver:** envía la fórmula de cada camino a Z3 (`solve_path_constraint`); si el camino es satisfacible (`sat`), Z3 devuelve valores concretos de entrada que **garantizan** recorrer exactamente esa rama al ejecutar la función.

---

## Paso a paso: codificación manual de caminos en Z3 (`tarifa_envio`)

Veamos cómo traducimos a mano una función con condicionales anidados y variables locales a predicados de Z3:

```python
def tarifa_envio(peso, distancia):
    tarifa_base = 10 + 2 * peso          # L1
    if peso > 5:                         # L2
        if distancia > 100:              # L3
            tarifa = tarifa_base + 30    # L4 (Camino P1)
        else:
            tarifa = tarifa_base + 10    # L5 (Camino P2)
    else:
        tarifa = tarifa_base + distancia # L6 (Camino P3)
    return tarifa                        # L7
```

1. **Declaramos una variable simbólica `z3.Int` por cada parámetro y variable local:**
   ```python
   peso, distancia = z3.Int("peso"), z3.Int("distancia")
   tarifa_base, tarifa = z3.Int("tarifa_base"), z3.Int("tarifa")
   ```
2. **Convertimos cada línea relevante en un predicado matemático (nota que la asignación `=` se escribe como igualdad `==`):**
   ```python
   L1 = (tarifa_base == 10 + 2 * peso)
   L2 = (peso > 5)
   L3 = (distancia > 100)
   L4 = (tarifa == tarifa_base + 30)
   L5 = (tarifa == tarifa_base + 10)
   L6 = (tarifa == tarifa_base + distancia)
   ```
3. **Armamos la lista de restricciones de cada camino desde la raíz hasta cada hoja:**
   * **Camino `P1` (`L2` verdadera y `L3` verdadera):** `P1 = [L1, L2, L3, L4]` $\to$ Z3 entrega p. ej. `peso = 6, distancia = 101`.
   * **Camino `P2` (`L2` verdadera y `L3` falsa):** `P2 = [L1, L2, z3.Not(L3), L5]` $\to$ Z3 entrega p. ej. `peso = 6, distancia = 100`.
   * **Camino `P3` (`L2` falsa; el `if` interno `L3` no se evalúa):** `P3 = [L1, z3.Not(L2), L6]` $\to$ Z3 entrega p. ej. `peso = 5, distancia = 0`.

---

## El superpoder de la ejecución simbólica: demostrar que una rama es inalcanzable

Observa ahora la función `check_triangle(a, b, c)` analizada en el Capítulo 13 del libro del curso:

```python
def check_triangle(a, b, c):
    if a == b:
        if a == c:
            if b == c: return "Equilateral"  # P1: T, T, T
            else:      return "Isosceles"    # P2: T, T, F  <-- ¡Mira esta rama!
        else:          return "Isosceles"    # P3: T, F
    else:
        if b != c:
            if a == c: return "Isosceles"    # P4: F, T, T
            else:      return "Scalene"      # P5: F, T, F
        else:          return "Isosceles"    # P6: F, F
```

Construyamos la tabla completa de los $6$ caminos sintácticos que existen en el árbol de `check_triangle`:

| Camino | Decisiones | *Path Condition* enviada a Z3 | Solución de Z3 | Resultado |
| :---: | :---: | :--- | :---: | :--- |
| **P1** | `T, T, T` | $a == b \;\land\; a == c \;\land\; b == c$ | `(1, 1, 1)` | `"Equilateral"` |
| **P2** | `T, T, F` | $a == b \;\land\; a == c \;\land\; b \neq c$ | **`unsat` (sin solución)** | **Inalcanzable (código muerto)** |
| **P3** | `T, F` | $a == b \;\land\; a \neq c$ | `(2, 2, 3)` | `"Isosceles"` |
| **P4** | `F, T, T` | $a \neq b \;\land\; b \neq c \;\land\; a == c$ | `(2, 1, 2)` | `"Isosceles"` |
| **P5** | `F, T, F` | $a \neq b \;\land\; b \neq c \;\land\; a \neq c$ | `(1, 2, 3)` | `"Scalene"` |
| **P6** | `F, F` | $a \neq b \;\land\; b == c$ | `(2, 1, 1)` | `"Isosceles"` |

Mira con atención el **Camino P2**: para llegar a ese `else`, la entrada debe cumplir simultáneamente $a == b$, $a == c$ y $\neg(b == c)$. Por transitividad de la igualdad, si $a = b$ y $a = c$, obligatoriamente $b = c$; exigir a la vez $b \neq c$ es una **contradicción lógica**.

Cuando ejecutamos `z3.solve(a == b, a == c, z3.Not(b == c))`, Z3 responde **`no solution` (`unsat`)**. Esto marca una diferencia abismal con el *fuzzing* aleatorio o basado en búsqueda: cuando un *fuzzer* aleatorio no logra cubrir una rama tras un millón de intentos, no sabes si tuviste mala suerte o si la rama es imposible. La ejecución simbólica **demuestra matemáticamente que la rama P2 es código muerto inalcanzable**.

*(En `fuzzingbook`, la clase `SimpleSymbolicFuzzer(fn)` automatiza esta tabla con sus tres métodos internos: `get_all_paths`, `extract_constraints` y `solve_path_constraint`).*

---

## Preguntas de repaso

> [!question]- Explica detalladamente cómo funciona la técnica de *Symbolic Fuzzing* para generar entradas de prueba sin ejecutar previamente el programa.
> 1. Representa los parámetros de entrada como **variables simbólicas** (incógnitas sin valor concreto).
> 2. Recorre estáticamente el AST/CFG de la función (`get_all_paths`) enumerando los posibles caminos de ejecución hasta cierta profundidad.
> 3. Para cada camino, recolecta la conjunción de condiciones de los condicionales atravesados (afirmadas en ramas `then` y negadas con `Not` en ramas `else`), formando la **restricción de camino (*path condition*)** (`extract_constraints`).
> 4. Envía cada *path condition* a un **SMT Solver (como Z3)** (`solve_path_constraint`), el cual resuelve el sistema de ecuaciones y entrega valores concretos de entrada para cada camino satisfacible.

> [!question]- En `tarifa_envio(peso, distancia)`, ¿por qué la condición de camino `P3` (`[L1, Not(L2), L6]`) NO incluye ni `L3` ni `Not(L3)` (`distancia > 100`)?
> Porque en el código fuente el condicional `if distancia > 100:` (`L3`) está **anidado únicamente dentro de la rama verdadera** de `if peso > 5:` (`L2`). Cuando `L2` es falsa (`Not(L2)`), el flujo salta directamente al bloque `else` (`L6`) sin evaluar jamás `distancia > 100`.

> [!question]- ¿Qué significa que para un camino de un programa el *SMT Solver* responda `unsat` (`no solution`), y por qué un *fuzzer* aleatorio jamás podría llegar a esa conclusión con certeza?
> Significa que las condiciones acumuladas a lo largo de ese camino son **mutuamente contradictorias**, demostrando formalmente que se trata de una **rama inalcanzable (código muerto)** para cualquier entrada posible. Un *fuzzer* aleatorio solo muestrea entradas concretas: aunque falle millones de veces en entrar a la rama, nunca puede distinguir entre una condición muy estrecha (como `x == 918273645`) y una condición lógicamente imposible.

