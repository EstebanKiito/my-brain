---
ramo: Bases de Datos
tema: Recuperación de fallas
tags: [bd/recuperacion, origen/complemento]
prerrequisitos: ["[[03 - Undo logging|Undo logging]]"]
---
# Redo logging

En redo logging el log guarda el **valor nuevo** de cada dato, y nada se escribe en disco hasta que el COMMIT está en el log. Al recuperar, se **rehacen** las transacciones confirmadas y se ignoran las demás.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 11: Transacciones y Recuperación de Fallas")
> **Registros:** `<START T>`, `<COMMIT T>`, `<ABORT T>`, `<T, X, v>` donde **v es el valor nuevo** de X, y `<T, END>` (los datos de T ya están en disco).
>
> **Regla:** antes de modificar cualquier elemento X en disco, **todos** los registros de log de T deben estar en disco, **incluido el COMMIT**. Es al revés que en undo logging.
>
> **En resumen:** escribir `<T, X, v>` → escribir `<COMMIT T>` → hacer *flush* del log a disco → escribir los datos en disco → escribir `<T, END>` en el log.
>
> **Algoritmo de recuperación** (del principio al final):
> 1. Identificar las transacciones que hicieron COMMIT sin END (las que hicieron END están OK).
> 2. Recorrer el log desde el principio. Si leo `<T, X, v>`: si T no hizo COMMIT, no hago nada; si T hizo COMMIT, reescribo X := v.
> 3. Para cada transacción sin COMMIT, escribir `<ABORT T>`.

> [!tip] Complemento — checkpoints en redo logging (slides "Clase 11")
> - Escribir `<START CKPT (T1, …, Tn)>` con las transacciones activas **sin COMMIT**, y guardar el log en disco.
> - Guardar en disco todo lo que haya hecho COMMIT hasta ese punto (escribiendo su `END`).
> - Escribir `<END CKPT>`.
>
> **Recuperación:** revisar el log desde el final. Si se encuentra un `<END CKPT>`, se retrocede hasta su `<START CKPT (T1, …, Tn)>` y se hace redo desde la transacción más antigua entre T1…Tn. **No se rehacen** las que hicieron COMMIT antes del `<START CKPT>`, porque ya están en disco. Si se encuentra un `<START CKPT>` sin su `<END CKPT>`, se retrocede hasta un `<END CKPT>` más antiguo.

> [!example] Ejemplo extra — log de la clase
> `<START T1>` `<T1, a, 5>` `<START T2>` `<COMMIT T1>` `<T2, b, 10>` `<START CKPT (T2)>` `<T2, c, 15>` `<START T3>` `<T3, d, 20>` `<T1, END>` `<END CKPT>` `<COMMIT T2>` `<COMMIT T3>`
>
> - T1 hizo COMMIT y END **antes** del `<END CKPT>`, así que sus cambios ya están en disco y no se rehace.
> - El redo parte desde `<START T2>`, la más antigua del checkpoint: se rehacen **b := 10, c := 15** (T2) y **d := 20** (T3), porque ambas hicieron COMMIT.
>
> **Problema del redo logging:** no se pueden ir grabando los valores en disco antes de que la transacción termine, así que la escritura a disco se congestiona y se necesita mucha memoria para retener los cambios.

## Preguntas de repaso

1. ¿Qué valor guarda `<T, X, v>` en redo logging?
> [!question]- Respuesta
> El valor nuevo de X, para poder reescribirlo si T hizo commit pero sus cambios no alcanzaron a llegar al disco.

2. ¿Cuál es la regla principal del redo logging?
> [!question]- Respuesta
> Ningún dato de T se escribe en disco hasta que todos sus registros de log, incluido `<COMMIT T>`, estén en disco.

3. ¿Qué se hace al recuperar con las transacciones sin COMMIT?
> [!question]- Respuesta
> Nada: sus cambios nunca llegaron a disco. Solo se les agrega `<ABORT T>` al log.

4. Compara undo y redo logging en la dirección de lectura del log.
> [!question]- Respuesta
> Undo lee del final al principio para deshacer las transacciones incompletas. Redo lee del principio al final para rehacer las confirmadas.
