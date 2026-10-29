# Dudas y correcciones de contenido — Testing (IIC3745)

Estados: 🟡 abierta · ✅ resuelta · ℹ️ informativa.

## General

| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ informativa | `_Índice.md` | Portadas de `00_Presentacion.pdf` a `08_EqPartitioningBAnalaysis.pdf` dicen `IIC2143-Testing` | El código oficial del curso en el programa (`IIC3745_202602_Programa.pdf`), en `10_EjerciciosI1.pdf` y en las actividades `A1`–`A4` es **IIC3745** (`IIC2143` corresponde a Ingeniería de Software, prerrequisito del ramo). Se usa `IIC3745` en el vault. |

## Pruebas unitarias dobles de prueba y test smells

| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ informativa | `01 - Estado e invariante de objetos y estructura Arrange Act Assert.md` | `Clases 3b4...html`: *"Object Invariant: Invariante → Condicion por la que un objeto esta en un ESTADO INCONSISTENTE"* | En los apuntes rápidos de clase quedó redactado al revés: tal como explica la línea anterior de los mismos apuntes (*"La invariante va a ser la CONDICION: Balance >= 0"*), el **invariante de objeto** es la condición que debe cumplirse (`True`) siempre que el objeto esté en un estado **consistente**; cuando el invariante se evalúa a `False`, el objeto cayó en un estado inconsistente. Se explica con precisión en la nota. |

## Transformaciones de código con AST

| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ informativa | `03 - Transformadores de expresiones operadores llamadas y la trampa de RenameTransformer.md` | `17-EjerciciosI2.pdf` p. 13: *"Detecta si hay una suma de valores donde un operando es 0, reduce la expresión quitando la suma ya que es redudanten. Por ejemplo, x+2 , resulta en solo x."* | Errata tipográfica en el ejemplo final de la slide: donde dice `x+2 , resulta en solo x` quiso decir `x + 0 , resulta en solo x` (como indica la frase inmediatamente anterior sobre el operando `0`). Se corrige en la nota. |
