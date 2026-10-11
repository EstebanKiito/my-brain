---
ramo: Bases de Datos
tema: Recuperación de fallas
tags: [bd/recuperacion, origen/complemento]
prerrequisitos: ["[[02 - Log manager y registros de log|Log manager y registros de log]]"]
---
# Undo logging

En undo logging el log guarda el **valor antiguo** de cada dato modificado. Al recuperar, se **deshacen** los cambios de las transacciones que no alcanzaron a hacer commit, leyendo el log de atrás hacia adelante.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 11: Transacciones y Recuperación de Fallas")
> **Registros:** `<START T>`, `<COMMIT T>`, `<ABORT T>` y `<T, X, t>`, donde **t es el valor antiguo** de X.
>
> **Reglas:**
> 1. Si T modifica X, el log `<T, X, t>` debe escribirse **antes** que el nuevo valor de X llegue a disco (*write-ahead logging*).
> 2. Si T hace commit, `<COMMIT T>` se escribe **justo después** de que todos los datos modificados por T estén en disco.
>
> **En resumen**, para cada cambio: T cambia X (t = valor antiguo) → escribir `<T, X, t>` → escribir el valor nuevo de X en disco → (repetir) → escribir `<COMMIT T>`.
>
> **Algoritmo de recuperación** (del final al principio del log):
> - Si leo `<COMMIT T>` → marco T como realizada.
> - Si leo `<ABORT T>` → marco T como realizada.
> - Si leo `<T, X, t>` y T **no** fue realizada → restituyo `X := t` en disco.
> - Si leo `<START T>` → lo ignoro.
>
> Al final se puede escribir `<ABORT T>` para las transacciones deshechas.

> [!tip] Complemento — checkpoints (slides "Clase 11")
> ¿Hasta dónde leer el log? ¿Qué pasa si el sistema falla en plena recuperación? ¿Cómo se trunca el log? Con **checkpoints**:
> - **Checkpoint simple:** dejar de aceptar transacciones nuevas, esperar a que terminen las actuales, guardar el log, escribir `<CKPT>` y reanudar. La recuperación lee hasta el `<CKPT>`. Problema: es prácticamente necesario "apagar" el sistema.
> - **Nonquiescent checkpoint** (no detiene el sistema): escribir `<START CKPT (T1, …, Tn)>` con las transacciones activas, esperar a que T1…Tn terminen (sin bloquear las nuevas) y escribir `<END CKPT>`.
> - **Recuperación:** se avanza desde el final. Si se encuentra un `<END CKPT>`, basta deshacer lo que está después del `<START CKPT>` correspondiente. Si se encuentra un `<START CKPT (…)>` sin su `<END CKPT>`, hay que retroceder hasta el inicio de la transacción más antigua entre T1…Tn.

> [!example] Ejemplo extra — los dos logs de la clase
> | Log | Caso 1: falla después de `<END CKPT>` | Caso 2: falla antes de `<END CKPT>` |
> |---|---|---|
> | `<START T1>` `<T1, a, 5>` `<START T2>` `<T2, b, 10>` | se puede **truncar** | hay que revisarlo |
> | `<START CKPT (T1, T2)>` | | |
> | `<T2, c, 15>` `<START T3>` `<T1, d, 20>` `<COMMIT T1>` `<T3, e, 25>` | | (el log termina aquí) |
> | `<COMMIT T2>` `<END CKPT>` | | — |
>
> - **Caso 1:** T1 y T2 hicieron commit; solo T3 (que partió después del checkpoint) está incompleta. Se deshace **e := 25**.
> - **Caso 2:** el checkpoint no se completó. Hay que retroceder hasta `<START T2>` (la más antigua sin commit) y deshacer T2 y T3: **e := 25, c := 15, b := 10**. T1 hizo commit, así que no se toca.
>
> **Problema del undo logging:** no se puede hacer COMMIT antes de guardar los datos en disco, así que las transacciones tardan más en terminar.

## Preguntas de repaso

1. ¿Qué valor guarda `<T, X, t>` en undo logging y para qué?
> [!question]- Respuesta
> El valor antiguo de X, para poder restituirlo si T no alcanzó a hacer commit.

2. ¿En qué orden se escriben el log, los datos y el COMMIT?
> [!question]- Respuesta
> Primero `<T, X, t>`, luego el valor nuevo de X en disco y, cuando todos los datos de T están en disco, `<COMMIT T>`.

3. ¿En qué dirección se recorre el log al recuperar y qué se hace con cada transacción?
> [!question]- Respuesta
> Del final al principio. Las transacciones con COMMIT o ABORT se ignoran; las incompletas se deshacen, restituyendo los valores antiguos.

4. ¿Qué ventaja tiene un nonquiescent checkpoint?
> [!question]- Respuesta
> Que no obliga a detener el sistema: las transacciones nuevas siguen corriendo mientras terminan las que estaban activas al iniciar el checkpoint.
