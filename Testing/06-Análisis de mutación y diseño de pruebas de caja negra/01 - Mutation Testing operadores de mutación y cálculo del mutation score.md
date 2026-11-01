---
ramo: "Testing"
tema: "Análisis de mutación y diseño de pruebas de caja negra"
tags:
  - testing/analisis-de-mutacion-y-diseno-de-pruebas-de-caja-negra
  - origen/complemento
prerrequisitos:
  - "[[Testing/03-Cobertura de código e instrumentación con settrace/04 - La clase Coverage diferencias de conjuntos y límites de la cobertura|La clase Coverage diferencias de conjuntos y límites de la cobertura]]"
---

# Mutation Testing, operadores de mutación y cálculo del mutation score

## ¿Quién prueba a las pruebas?

En el Tema 03 descubrimos el punto ciego de la cobertura: **ejecutar una línea no es lo mismo que verificar que hace lo correcto**. Veámoslo sobre la función `triangle(a, b, c)` (que devuelve `'Equilateral'`, `'Isosceles'` o `'Scalene'`) comparando dos suites de pruebas que ejercitan exactamente las mismas cinco entradas `(1,1,1)`, `(1,2,1)`, `(2,2,1)`, `(1,2,2)` y `(1,2,3)`:

```python
def strong_suite(fn):
    assert fn(1, 1, 1) == 'Equilateral'
    assert fn(1, 2, 1) == 'Isosceles'
    assert fn(2, 2, 1) == 'Isosceles'
    assert fn(1, 2, 2) == 'Isosceles'
    assert fn(1, 2, 3) == 'Scalene'

def weak_suite(fn):
    assert fn(1, 1, 1) == 'Equilateral'
    assert fn(1, 2, 1) != 'Equilateral'
    assert fn(2, 2, 1) != 'Equilateral'
    assert fn(1, 2, 2) != 'Equilateral'
    assert fn(1, 2, 3) != 'Equilateral'
```

Ambas suites pasan en verde y **ambas alcanzan el $100\%$ de cobertura de sentencias y ramas**. Sin embargo, `weak_suite` tiene un oráculo pobrísimo: solo verifica que los cuatro últimos casos «no sean equiláteros».

El **Mutation Testing** (o *Mutation Analysis*, desarrollado también sobre las bases de [The Fuzzing Book](https://www.fuzzingbook.org/html/Fuzzer.html)) resuelve este problema: **siembra pequeños defectos artificiales llamados mutantes en el código fuente y ejecuta la suite de pruebas contra cada mutante para ver si nuestros tests son capaces de detectarlos**.

![Mapa conceptual en pizarra que distingue cómo creamos entradas para Unit Test frente a cómo evaluamos su calidad con test smells, coverage y mutation testing](adjuntos/Pizarra%20de%20mutation%20testing%20en%20clase.png)

---

## Ciclo de vida de un mutante y cálculo del *Mutation Score*

Un **mutante** es una copia del programa original con un único cambio sintáctico válido (que compila y se ejecuta). Cuando corremos nuestra batería de pruebas contra un mutante $m$:

* **Mutante muerto (*killed*):** al menos un test de la batería **falla** (`AssertionError` o excepción inesperada). ¡Buenas noticias! Nuestra suite detectó el bug sembrado.
* **Mutante sobreviviente (*survived*):** todos los tests de la batería **siguen pasando en verde**. ¡Alerta! El cambio alteró el código pero ningún `assert` de nuestra suite se dio cuenta.

En `triangle`, si sembramos el mutante `triangle_m1` cambiando `return 'Isosceles'` por `return None` cuando `a == b and b != c`:
* `strong_suite(triangle_m1)` evalúa `None == 'Isosceles'`, lanza `AssertionError` y **mata al mutante** (*Mutation Score* $= 1.0$).
* `weak_suite(triangle_m1)` evalúa `None != 'Equilateral'`, que es verdadero: la prueba pasa y el mutante **sobrevive** (*Mutation Score* $= 0.25$ en la batería de $4$ mutantes de clase).

La métrica global es el **Mutation Score** (o puntaje de mutación ajustado, descontando mutantes inválidos que no compilan y mutantes equivalentes):

$$\text{Mutation Score} = \frac{\text{Mutantes muertos (killed)}}{\text{Total de mutantes} - \text{Inválidos} - \text{Equivalentes}} \times 100\%$$

---

## Operadores de mutación clásicos y caso de análisis (`distance`)

En lugar de inventar bugs a mano, herramientas como **Cosmic Ray** o `MuFunctionAnalyzer` aplican **operadores de mutación** sobre el AST:

1. **Operadores aritméticos (AOR):** cambiar `+` por `-`, `*` por `/` o `+` (ej. `a + b` $\to$ `a - b`).
2. **Operadores relacionales (ROR):** cambiar `>` por `>=`, `<` por `<=`, `==` por `!=` (modelan directamente errores *off-by-one* de borde, como cambiar `subtotal >= 100000` por `subtotal > 100000` en `precio_final`, que solo muere si probamos exactamente `subtotal = 100000`).
3. **Operadores lógicos (LOR):** cambiar `and` por `or`, o negar condiciones.
4. **Mutación de constantes y sentencias:** cambiar `0` por `1`, alterar literales de retorno o reemplazar una línea por `pass`.

### Ejercicio clásico de interrogación: ¿por qué sobrevivió el mutante en `distance(dx, dy)`?

```python
import math
def distance(dx, dy):
    return math.sqrt(dx * dx + dy * dy)
```

Un mutador cambia el primer `*` por `+`, produciendo el mutante `math.sqrt(dx + dx + dy * dy)`. El alumno tiene dos pruebas que cubren el $100\%$ del código: `assert distance(0, 2) == 2` y `assert round(distance(2, 3), 2) == 3.61`. **¿Por qué sobrevive el mutante?**

* Porque para $dx = 0$ se cumple $0 \cdot 0 = 0 + 0 = 0$, y para $dx = 2$ se cumple la coincidencia algebraica $2 \cdot 2 = 2 + 2 = 4$. En ambas entradas de la suite, $dx^2$ vale exactamente lo mismo que $2\cdot dx$.
* **¿Cómo lo matamos?** Agregando cualquier test donde $dx \notin \{0, 2\}$, por ejemplo `assert distance(3, 4) == 5.0` (donde el original da $\sqrt{9 + 16} = 5.0$ y el mutante devuelve $\sqrt{6 + 16} = \sqrt{22} \approx 4.69$, muriendo de inmediato).

---

---

## Ejemplo práctico: ejecutar la mutación a mano sobre `triangle`

Para ver mutation testing sin herramientas, escribimos el programa, un mutante y las dos suites de la nota:

```python
def triangle(a, b, c):
    if a == b:
        if b == c:
            return "Equilateral"
        return "Isosceles"
    if b == c or a == c:
        return "Isosceles"
    return "Scalene"

def triangle_m1(a, b, c):             # mutante: 'Isosceles' → None cuando a == b != c
    if a == b:
        if b == c:
            return "Equilateral"
        return None
    if b == c or a == c:
        return "Isosceles"
    return "Scalene"
```

Corremos cada suite contra el original y contra el mutante:

| Suite | Contra `triangle` | Contra `triangle_m1` | Conclusión |
| :--- | :---: | :---: | :--- |
| `strong_suite` | pasa | **falla** (`None == 'Isosceles'` es falso) | mutante **muerto** |
| `weak_suite` | pasa | pasa (`None != 'Equilateral'` es verdadero) | mutante **sobrevive** |

Ambas suites tienen el mismo $100\%$ de cobertura, y solo la que tiene un oráculo fuerte detecta el defecto. Esa es la utilidad de la técnica: medir la calidad de los *asserts*, no solo cuántas líneas se ejecutan.

### Mutantes típicos de `triangle` y quién los mata

| Mutante | Cambio | ¿Lo mata `strong_suite`? |
| :--- | :--- | :---: |
| M1 | `return "Isosceles"` → `return None` (rama `a == b`) | Sí, con `fn(2, 2, 1)` |
| M2 | `if a == b` → `if a != b` | Sí, con `fn(1, 1, 1)` |
| M3 | `b == c or a == c` → `b == c and a == c` | Sí, con `fn(1, 2, 1)` |
| M4 | `return "Scalene"` → `return "Isosceles"` | Sí, con `fn(1, 2, 3)` |

La suite fuerte mata los $4$: $\text{score} = 4/4 = 100\%$. Con `weak_suite` el score sería muy inferior, porque solo detecta mutantes que provoquen `'Equilateral'` donde no corresponde.

---

## Preguntas de repaso

> [!question]- ¿Qué propiedad fundamental de una batería de pruebas mide el *Mutation Score* que el *Statement* y el *Branch Coverage* ignoran por completo?
> Mide la **fuerza y sensibilidad de los oráculos (las aserciones `assert`)**: si las pruebas no solo ejecutan la línea defectuosa, sino si además propagan el estado alterado y lo verifican con una aserción capaz de distinguir el resultado correcto del mutado.

> [!question]- En la función `precio_final(subtotal, es_socio, cupon)`, el mutante `m1` reemplaza la línea `if subtotal >= 100000:` por `if subtotal > 100000:`. ¿Qué única entrada de `subtotal` permite matar a este mutante y por qué?
> Únicamente la entrada exacta en la frontera: **`subtotal = 100000`**. Para cualquier valor menor a $100\,000$ ambas versiones dan `False`, y para cualquier valor estrictamente mayor a $100\,000$ ambas dan `True`. Solo en $100\,000$ el programa original aplica el $20\%$ de descuento (`True`) mientras que el mutante cae al tramo inferior del $10\%$ (`False`).

> [!question]- Al ejecutar un experimento de *Mutation Testing*, ¿por qué es obligatorio verificar primero que la batería de pruebas original pasa al $100\%$ sobre el código sin mutar antes de evaluar los mutantes?
> Porque un mutante se clasifica como *killed* en cuanto **al menos un test falla**. Si la batería base ya tenía un test roto sobre el código original, ese test fallará también en todas las corridas mutadas, marcando artificialmente el $100\%$ de los mutantes como *killed* sin haber evaluado nada.

> [!question]- Dado `def es_par(n): return n % 2 == 0`, el mutante cambia `==` por `!=`. Escribe un test mínimo que lo mate y uno que lo deje sobrevivir.
> Lo mata cualquier test con oráculo sobre un valor concreto, por ejemplo `assertTrue(es_par(4))` (el mutante devuelve `False`). Lo deja sobrevivir un test como `es_par(4) is not None`, que pasa con ambos programas: eso ilustra un oráculo débil.

> [!question]- Un mutante cambia `x * 2` por `x + 2` en una función. ¿Con qué entradas sobrevive?
> Solo con $x = 2$, porque $2 \cdot 2 = 4 = 2 + 2$. Para cualquier otra entrada ($x = 3$ da $6$ frente a $5$) el resultado difiere. Es el mismo fenómeno de `distance(0, 2)`: una coincidencia aritmética que se resuelve añadiendo un caso distinto.
