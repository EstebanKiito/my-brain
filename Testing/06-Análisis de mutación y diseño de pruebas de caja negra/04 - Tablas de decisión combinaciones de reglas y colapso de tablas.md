---
ramo: "Testing"
tema: "Análisis de mutación y diseño de pruebas de caja negra"
tags:
  - testing/analisis-de-mutacion-y-diseno-de-pruebas-de-caja-negra
  - origen/complemento
prerrequisitos:
  - "[[03 - Pruebas de caja negra partición de equivalencia y valores límite]]"
---

# Tablas de decisión, combinaciones de reglas y colapso de tablas

## ¿Cuándo necesitamos una Tabla de Decisión?

La partición de equivalencia y el análisis de valores límite analizan cada variable de entrada por separado. Sin embargo, en muchos sistemas reales el resultado depende de la **combinación lógica de múltiples condiciones simultáneas** (reglas del tipo *«si el cliente es nuevo, o si tiene tarjeta de fidelidad y además presenta un cupón...»*).

Una **Tabla de Decisión** (también llamada tabla de **causa-efecto**) es una matriz que enumera sistemáticamente todas las combinaciones posibles de condiciones de entrada y especifica qué acción o salida corresponde a cada columna (**regla**).

### Cómo construir una tabla de decisión paso a paso

1. Listar las **$n$ condiciones de entrada** (causas) en las filas superiores.
2. Si las $n$ condiciones son booleanas (`V`/`F` o `S`/`N`), generar las **$2^n$ columnas (reglas)** posibles. Para no olvidar ninguna combinación, se alterna `S, N, S, N...` en la última condición, `S, S, N, N...` de dos en dos en la penúltima, `S, S, S, S, N, N, N, N` de cuatro en cuatro en la anterior, y así sucesivamente.
3. Determinar en las filas inferiores la **acción o resultado esperado** para cada regla (o marcarla con **`X`** si la combinación es imposible o inválida por regla de negocio).
4. Derivar **un caso de prueba por cada columna** relevante. La cobertura se mide como:
   $$\text{Cobertura de tabla de decisión} = \frac{\text{Columnas probadas por al menos un test}}{\text{Total de columnas}} \times 100\%$$

---

## Colapso (reducción) de tablas y combinaciones imposibles (`X`)

Cuando el número de condiciones $n$ crece, la tabla completa crece exponencialmente ($n = 3 \implies 8$ reglas; $n = 10 \implies 1024$ reglas; $n = 15 \implies 32\,768$ reglas). Existen dos mecanismos para simplificar y analizar la tabla:

### 1. Colapso de reglas indiferentes (`—`) — Ejemplo de préstamos bancarios (Q12)

Considera un banco con $n = 3$ condiciones binarias:
* **C1:** Historial crediticio limpio (`S` / `N`).
* **C2:** Monto solicitado $< \$10\,000\,000$ (`S` / `N`).
* **C3:** Empleo estable (`S` / `N`).
* **Regla de negocio:** *Se aprueba el préstamo si `C1 = S` y al menos una de (`C2 = S` o `C3 = S`). En cualquier otro caso se rechaza.*

La **tabla de decisión completa** tiene $2^3 = \mathbf{8}\text{ columnas}$ (`R1` a `R8`):

| Condición / Acción | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1:** Historial limpio | S | S | S | S | N | N | N | N |
| **C2:** Monto $< \$10\text{M}$ | S | S | N | N | S | S | N | N |
| **C3:** Empleo estable | S | N | S | N | S | N | S | N |
| **Resultado: ¿Aprobado?** | **Sí** | **Sí** | **Sí** | **No** | **No** | **No** | **No** | **No** |

Observa las columnas `R5`, `R6`, `R7` y `R8`: en las cuatro se cumple `C1 = N` (historial sucio) y en las cuatro la acción es **No (rechazo)** sin importar cuánto valgan `C2` y `C3`. Podemos **fusionar (colapsar)** `R5`–`R8` en una única columna con `C1 = N`, `C2 = —` y `C3 = —`, obteniendo la **tabla reducida de $5$ reglas**:

| Condición / Acción | R1 | R2 | R3 | R4 | R5–R8 (colapsada) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **C1:** Historial limpio | S | S | S | S | **N** |
| **C2:** Monto $< \$10\text{M}$ | S | S | N | N | **—** |
| **C3:** Empleo estable | S | N | S | N | **—** |
| **Resultado: ¿Aprobado?** | **Sí** | **Sí** | **Sí** | **No** | **No** |

Ainsi, cubrir la tabla completa exige **$8$ casos de prueba**, mientras que cubrir la tabla reducida exige un mínimo de **$5$ casos de prueba**.

### 2. Reglas inválidas por negocio (`X`) — Ejemplo de descuentos

* **Reglas:** Cliente nuevo $\to 15\%$; Cliente antiguo con tarjeta de fidelidad $\to 10\%$; Cupón $\to 20\%$ (acumulable con fidelidad $\to 30\%$, pero **no combinable** con cliente nuevo $\to$ queda en $20\%$).
* En las reglas `R1` (`T, T, T`) y `R2` (`T, T, F`), el cliente aparece simultáneamente como «Nuevo» y con «Tarjeta de fidelidad de cliente antiguo». Esa combinación se marca con **`X`** (inválida por regla de negocio, colapsable como `T, T, —`).
* **¿Debemos probar `R1` y `R2`?** En las láminas se destaca un matiz práctico crucial: si la combinación es físicamente imposible en la interfaz no se puede probar, pero si un bug en la base de datos pudiera marcar ambas banderas en `True`, conviene incluir los tests (`6 válidos + 2 inválidos = 8 tests`) para verificar que el sistema rechace el estado inconsistente en vez de regalar un $45\%$ de descuento.

---

## Preguntas de repaso

> [!question]- Un formulario de subida de imágenes exige $3$ condiciones binarias: (1) formato JPG, (2) tamaño menor a $32\text{ KB}$ y (3) resolución exacta de $137 \times 177\text{ px}$. Si cualquiera falla, muestra un mensaje de error genérico. ¿Cuántas reglas tiene la tabla de decisión completa y cuántas de ellas cargan la foto con éxito?
> Como hay $n = 3$ condiciones binarias independientes y todas las combinaciones son físicamente posibles, la tabla completa tiene **$2^3 = 8$ reglas** ($8$ casos de prueba), de las cuales **solo $1$ (`T, T, T`)** carga la foto exitosamente y las otras $7$ producen error.

> [!question]- ¿Cuándo es válido colapsar dos o más columnas de una tabla de decisión en una sola columna con el símbolo `—` («no importa»)?
> Cuando las columnas tienen exactamente los mismos valores en un subconjunto de condiciones, cubren todas las combinaciones posibles (`V` y `F`) de las condiciones restantes, y **producen exactamente las mismas acciones o resultados de salida** (lo que demuestra que esas condiciones restantes no influyen en la decisión bajo ese escenario).

> [!question]- Además de diseñar casos de prueba, ¿por qué construir una tabla de decisión sirve como herramienta de verificación temprana (*shift-left*) sobre los requerimientos?
> Porque al enumerar sistemáticamente las $2^n$ columnas, obliga a preguntarse qué debe hacer el sistema en combinaciones que el autor de la especificación olvidó mencionar (como en el ejemplo de solicitud de préstamo donde nadie había definido qué ocurría en la Regla 4 cuando no se ingresaba ni monto ni plazo, o qué pasa cuando un cliente nuevo usa un cupón de $20\%$).

