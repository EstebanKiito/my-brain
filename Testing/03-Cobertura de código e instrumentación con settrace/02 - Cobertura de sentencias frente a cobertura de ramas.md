---
ramo: "Testing"
tema: "Cobertura de código e instrumentación con settrace"
tags:
  - testing/cobertura-de-codigo-e-instrumentacion-con-settrace
  - origen/complemento
prerrequisitos:
  - "[[01 - Pruebas de caja blanca y métricas de cobertura estructural]]"
---

# Cobertura de sentencias frente a cobertura de ramas

## ¿Por qué el $100\%$ de *Statement Coverage* puede engañarnos?

Uno de los errores más frecuentes al iniciarse en testing es pensar que si ejecutamos el $100\%$ de las líneas de una función (**Statement Coverage**), entonces ya probamos todas las decisiones lógicas del código (**Decision / Branch Coverage**). Veamos con un ejemplo mínimo por qué **la cobertura de decisiones o ramas es estrictamente más exigente que la cobertura de sentencias**.

Considera la función `aplicar_descuento(precio, es_socio)` (problema clásico de interrogación):

```python
def aplicar_descuento(precio, es_socio):
    if es_socio:               # Sentencia 1 (contiene 1 decisión con 2 ramas: True y False)
        precio = precio * 0.8  # Sentencia 2
    return precio              # Sentencia 3
```

¿Qué ocurre si nuestra suite de pruebas tiene **un único caso de prueba**: `aplicar_descuento(100, True)`?

1. **Cálculo de *Statement Coverage*:**
   * Se evalúa la línea `if es_socio:` ($\checkmark$).
   * Como `es_socio` es `True`, entra al bloque y ejecuta `precio = precio * 0.8` ($\checkmark$).
   * Finalmente ejecuta `return precio` ($\checkmark$).
   * Se ejecutaron las $3$ sentencias de un total de $3$:
     $$\text{Statement Coverage} = \frac{3}{3} \times 100\% = 100\%$$
2. **Cálculo de *Branch / Decision Coverage*:**
   * La condición `if es_socio:` tiene **$2$ resultados de decisión (ramas) posibles**: evaluar a `True` (entrar al `if`) y evaluar a `False` (saltarse el cuerpo del `if` e ir directo al `return`).
   * Con `aplicar_descuento(100, True)` solo tomamos la rama `True` ($1$ de $2$); jamás comprobamos qué hace la función cuando un cliente **no** es socio (`es_socio = False`).
     $$\text{Branch Coverage} = \frac{1}{2} \times 100\% = 50\%$$

> [!important] Cuándo diverge el Statement Coverage del Branch Coverage
> Cada vez que existe un `if` **sin bloque `else`** (un `if` implícito), un solo caso de prueba que haga verdadera la condición ejecuta las sentencias dentro del `if` y luego continúa hacia abajo, logrando $100\%$ de *Statement Coverage* pero dejando la rama `False` ($50\%$ de *Branch Coverage*) completamente sin probar. Para subir el *Branch Coverage* al $100\%$ necesitamos agregar un segundo caso: `aplicar_descuento(100, False)`.

---

## Ejercicio paso a paso: cálculo manual en condicionales anidados

Analicemos cómo se calculan ambas métricas sobre `clasificar_impuesto(edad, ingresos)`:

```python
def clasificar_impuesto(edad, ingresos):   # L1 (firma)
    if edad < 18:                          # L2 (Decisión D1: True / False)
        if ingresos < 50000:               # L3 (Decisión D2: True / False)
            impuesto = 0                   # L4
        else:
            impuesto = ingresos * 0.1      # L5
    else:
        if ingresos < 30000:               # L6 (Decisión D3: True / False)
            impuesto = ingresos * 0.05     # L7
        else:
            impuesto = ingresos * 0.15     # L8
    return impuesto                        # L9
```

Nota que en `unittest` y en las pautas del curso contamos únicamente las **sentencias ejecutables** dentro del cuerpo de la función (`L2` a `L9`, es decir, **$8$ sentencias ejecutables**; las palabras clave `else:` no se cuentan como sentencias separadas porque el salto lo decide el `if` respectivo). Además, hay **$3$ decisiones (`if`)**, lo que equivale a $3 \times 2 = \mathbf{6}\text{ ramas}$ en total.

Supongamos que ejecutamos una suite con dos casos de prueba:

* **Caso 1: `clasificar_impuesto(15, 40000)`**
  * En `L2`, `15 < 18` es **True** $\to$ pasa a `L3`.
  * En `L3`, `40000 < 50000` es **True** $\to$ ejecuta `L4` (`impuesto = 0`) y salta a `L9` (`return impuesto`).
  * Líneas ejecutadas por el Caso 1: $\{\text{L2}, \text{L3}, \text{L4}, \text{L9}\}$.
* **Caso 2: `clasificar_impuesto(30, 25000)`**
  * En `L2`, `30 < 18` es **False** $\to$ salta a la rama `else` en `L6`.
  * En `L6`, `25000 < 30000` es **True** $\to$ ejecuta `L7` (`impuesto = ingresos * 0.05`) y llega a `L9`.
  * Líneas ejecutadas por el Caso 2: $\{\text{L2}, \text{L6}, \text{L7}, \text{L9}\}$.

### Unión de la suite y cálculo de porcentajes

* **Sentencias cubiertas (unión de ambos casos):**
  $$\{\text{L2}, \text{L3}, \text{L4}, \text{L9}\} \cup \{\text{L2}, \text{L6}, \text{L7}, \text{L9}\} = \{\text{L2}, \text{L3}, \text{L4}, \text{L6}, \text{L7}, \text{L9}\} \quad (6\text{ sentencias})$$
  Quedan sin ejecutar `L5` y `L8`. Por lo tanto:
  $$\text{Statement Coverage} = \frac{6}{8} \times 100\% = 75\%$$
* **Ramas (decisiones) cubiertas:**
  * Decisión `L2` (`edad < 18`): se evaluó `True` (Caso 1) y `False` (Caso 2) $\to 2/2$.
  * Decisión `L3` (`ingresos < 50000`): solo se evaluó `True` (Caso 1), nunca `False` $\to 1/2$.
  * Decisión `L6` (`ingresos < 30000`): solo se evaluó `True` (Caso 2), nunca `False` $\to 1/2$.
  $$\text{Decision / Branch Coverage} = \frac{2 + 1 + 1}{6} \times 100\% = \frac{4}{6} \times 100\% \approx 66.7\%$$

Para alcanzar el $100\%$ en ambas métricas bastaría añadir dos entradas que activen `L5` ($\text{edad} < 18 \land \text{ingresos} \ge 50000$, ej. `(16, 60000)`) y `L8` ($\text{edad} \ge 18 \land \text{ingresos} \ge 30000$, ej. `(25, 60000)`).

---

---

## Ejemplo práctico: la suite que engaña y cómo se completa

Escribimos tests para `aplicar_descuento` y miramos qué cubren:

```python
import unittest

class DescuentoCoberturaTest(unittest.TestCase):
    def test_socio_recibe_descuento(self):
        self.assertEqual(80, aplicar_descuento(100, True))
```

* **Statement Coverage:** $3/3 = 100\%$ (las tres sentencias se ejecutaron).
* **Branch Coverage:** $1/2 = 50\%$ (nunca se tomó la rama `es_socio = False`).

El defecto escondido sale a la luz con el test que falta:

```python
    def test_no_socio_paga_precio_completo(self):
        self.assertEqual(100, aplicar_descuento(100, False))
```

Con este test la rama `False` queda cubierta ($2/2 = 100\%$). Pensemos ahora en una versión defectuosa donde el programador olvidó que el `if` no tiene `else` y escribió el `return` dentro del bloque:

```python
def aplicar_descuento(precio, es_socio):
    if es_socio:
        precio = precio * 0.8
        return precio           # el return quedó dentro del if
```

Con solo `test_socio_recibe_descuento` el *Statement Coverage* seguiría en $100\%$ y el test en verde. Con `test_no_socio_paga_precio_completo` el programa devuelve `None` en vez de `100`: **solo el criterio de ramas obligó a escribir el test que destapa el bug**.

### Cómo elegir entradas para cubrir todas las ramas de `clasificar_impuesto`

Hay $3$ decisiones (`edad < 18`, `ingresos < 50000`, `ingresos < 30000`) y $4$ hojas. Una suite mínima que cubre las $6$ ramas y las $8$ sentencias:

| Caso | `(edad, ingresos)` | Hoja alcanzada |
| :--- | :--- | :--- |
| 1 | `(15, 40000)` | L4: `impuesto = 0` |
| 2 | `(16, 60000)` | L5: `impuesto = ingresos * 0.1` |
| 3 | `(30, 25000)` | L7: `impuesto = ingresos * 0.05` |
| 4 | `(25, 60000)` | L8: `impuesto = ingresos * 0.15` |

Hay una hoja por cada combinación de decisiones, así que con $4$ casos se logra $100\%$ de sentencias y $100\%$ de ramas.

---

## Preguntas de repaso

> [!question]- ¿Por qué lograr $100\%$ de *Branch / Decision Coverage* garantiza siempre $100\%$ de *Statement Coverage* (en código sin código muerto inalcanzable), pero el recíproco es falso?
> Porque toda sentencia ejecutable vive o bien en el flujo secuencial principal o bien dentro de alguna de las ramas (`True` o `False`) de una decisión. Si cubrimos el $100\%$ de las ramas de todas las decisiones, obligatoriamente habremos entrado a cada bloque y ejecutado todas sus sentencias. En cambio, como muestra un `if` sin `else`, podemos ejecutar todas las sentencias tomando solo la rama `True` sin haber probado jamás qué ocurre cuando la condición es `False`.

> [!question]- En `clasificar_impuesto`, si cambiamos el Caso 2 de `(30, 25000)` a `(25, 60000)` (manteniendo el Caso 1 en `(17, 40000)`), ¿cuántas sentencias y cuántas ramas cubre la batería?
> Con `(17, 40000)` se cubren $\{\text{L2}, \text{L3}, \text{L4}, \text{L9}\}$ y con `(25, 60000)` se cubren $\{\text{L2}, \text{L6}, \text{L8}, \text{L9}\}$ (tomando la rama `False` de `L6`). La unión sigue teniendo $6$ de $8$ sentencias ($\text{SC} = 75\%$, ahora faltan `L5` y `L7`) y $4$ de $6$ ramas ($\text{BC} \approx 66.7\%$).

> [!question]- Diseña una función breve de tres líneas ejecutables y un único caso de prueba que logre $100\%$ de *Statement Coverage* y $50\%$ de *Decision Coverage*.
> ```python
> def normalizar_nota(nota):
>     if nota > 7.0:
>         nota = 7.0
>     return nota
> ```
> El único caso `normalizar_nota(8.5)` ejecuta las $3$ sentencias ($100\%$ *Statement Coverage*), pero evalúa `nota > 7.0` únicamente como `True` ($1$ de $2$ ramas $= 50\%$ *Decision Coverage*).

> [!question]- Dada `def f(x): if x > 10: y = 1 \n else: y = 2 \n return y`, ¿puede un solo test lograr $100\%$ de branch coverage? ¿Y $100\%$ de statement coverage?
> No puede lograr $100\%$ de branch coverage con un solo test, porque la decisión `x > 10` necesita evaluarse `True` y `False` y un test solo toma una de las dos. Tampoco puede lograr $100\%$ de statement coverage, porque cada rama tiene su propia sentencia (`y = 1` y `y = 2`) y un test ejecuta solo una. Hacen falta al menos dos tests, por ejemplo `f(11)` y `f(5)`.

> [!question]- Una función tiene un `if a and b:` sin `else`. Con los tests `(a=True, b=True)` y `(a=False, b=False)`, ¿cuál es el branch coverage y qué le falta a la suite?
> La decisión `a and b` se evaluó `True` y `False`, así que el branch coverage es $100\%$ aunque la condición compuesta no se haya probado en todas sus combinaciones (falta, por ejemplo, `a=True, b=False`). Eso muestra el límite del criterio de ramas: para cubrir las condiciones individuales haría falta cobertura de condición/MC-DC.
