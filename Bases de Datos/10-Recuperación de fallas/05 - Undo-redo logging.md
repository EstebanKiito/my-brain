---
ramo: Bases de Datos
tema: Recuperación de fallas
tags: [bd/recuperacion, origen/complemento]
prerrequisitos: ["[[03 - Undo logging|Undo logging]]", "[[04 - Redo logging|Redo logging]]"]
---
# Undo/redo logging

Undo/redo logging guarda **el valor antiguo y el nuevo** de cada cambio. Así el DBMS puede escribir los datos a disco cuando le convenga, antes o después del commit, y al recuperar deshace lo no confirmado y rehace lo confirmado. Es lo que usan los DBMS reales.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 11: Transacciones y Recuperación de Fallas")
> - Es la solución que mezcla las dos estrategias anteriores para obtener **mayor rendimiento**.
> - Usa `<T, X, v_antiguo, v_nuevo>` con *write-ahead logging*: el registro va a disco antes que el dato.
> - `<COMMIT T>` puede ir a disco de forma **arbitraria**, antes o después de los datos.
> - **Recuperación:**
>   - **Undo** de las transacciones **sin COMMIT** (de atrás hacia adelante).
>   - **Redo** de las transacciones **con COMMIT**, que podrían no estar en disco (de adelante hacia atrás).

> [!tip] Complemento — comparación de técnicas (slides "Clase 11")
> | | Undo | Redo | Undo/Redo |
> |---|---|---|---|
> | Transacciones incompletas | cancelarlas (undo) | ignorarlas | undo |
> | Transacciones confirmadas | ignorarlas | repetirlas (redo) | redo |
> | Escribir COMMIT | **después** de guardar los datos en disco | **antes** de guardar los datos en disco | en cualquier momento |
> | Registro de UPDATE | valores antiguos | valores nuevos | ambos |
> | Problema | commits lentos | congestión de escritura a disco | logs más grandes |
>
> ```mermaid
> flowchart TD
>   F[Falla del sistema] --> L[Leer log desde el último checkpoint]
>   L --> Q{¿La transacción hizo COMMIT?}
>   Q -->|no| U["UNDO: restaurar valores antiguos"]
>   Q -->|sí| R["REDO: reescribir valores nuevos"]
> ```
>
> En la práctica, PostgreSQL usa un WAL de tipo redo, y el algoritmo industrial de undo/redo es **ARIES** (IBM, 1992).

## Preguntas de repaso

1. ¿Qué guarda cada registro de update en undo/redo logging?
> [!question]- Respuesta
> El valor antiguo y el valor nuevo del dato: `<T, X, v_antiguo, v_nuevo>`.

2. ¿Qué ventaja tiene sobre undo y sobre redo por separado?
> [!question]- Respuesta
> Da libertad para escribir los datos a disco antes o después del commit. Así no hace esperar el commit (problema del undo) ni retiene todos los cambios en memoria (problema del redo).

3. ¿Qué se hace con cada tipo de transacción al recuperar?
> [!question]- Respuesta
> Undo de las que no hicieron commit y redo de las que sí lo hicieron.

4. En undo logging, ¿cuándo se escribe el COMMIT respecto de los datos? ¿Y en redo?
> [!question]- Respuesta
> En undo, después de que todos los datos están en disco. En redo, antes de escribir cualquier dato en disco.
