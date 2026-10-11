---
ramo: Bases de Datos
tema: Recuperación de fallas
tags: [bd/recuperacion, origen/complemento]
prerrequisitos: ["[[01 - Tipos de fallas|Tipos de fallas]]", "[[01 - Transacciones|Transacciones]]"]
---
# Log manager y registros de log

El **log** es un archivo de solo agregar donde el DBMS anota cada acción de cada transacción (inicio, cambios, commit, abort). Después de una caída, leerlo permite dejar la base en un estado consistente.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 11: Transacciones y Recuperación de Fallas")
> **Log Manager:**
> - Registra todas las acciones de las transacciones.
> - Una página se va llenando **secuencialmente** con registros de log. Cuando se llena, se guarda en disco.
> - Todas las transacciones escriben en el log de manera concurrente.
>
> **Registros de log comunes:**
> | Registro | Significa |
> |---|---|
> | `<START T>` | la transacción T comenzó |
> | `<COMMIT T>` | T terminó con éxito |
> | `<ABORT T>` | T se abortó |
> | `<T UPDATE>` | T modificó un elemento; según la técnica guarda el valor antiguo, el nuevo o ambos |
>
> **¿Cómo los usamos?** Depende de la técnica de logging:
> | Técnica | Registro de update | Nota |
> |---|---|---|
> | Undo logging | `<T, X, t>` con t = valor **antiguo** | [[03 - Undo logging\|Undo logging]] |
> | Redo logging | `<T, X, v>` con v = valor **nuevo** | [[04 - Redo logging\|Redo logging]] |
> | Undo/redo | `<T, X, v_antiguo, v_nuevo>` | [[05 - Undo-redo logging\|Undo/redo logging]] |

> [!tip] Complemento — cómo detectar el estado de cada transacción en el log
> | En el log aparece… | Estado de T al momento de la falla |
> |---|---|
> | `<START T> … <COMMIT T>` | completa (confirmada) |
> | `<START T> … <ABORT T>` | abortada |
> | `<START T> …` sin COMMIT ni ABORT | **incompleta**: estaba corriendo cuando el sistema cayó |
>
> **Write-Ahead Logging (WAL):** el registro de log de un cambio se escribe en disco **antes** que el dato modificado. PostgreSQL implementa exactamente esto (su "WAL").
>
> **Checkpoints:** marcas en el log que evitan leerlo entero al recuperar. Se ven con cada técnica.
>
> Recurso recomendado por la clase: http://mlwiki.org/index.php/Database_Transaction_Log

## Preguntas de repaso

1. ¿Qué es el log y para qué sirve?
> [!question]- Respuesta
> Un registro secuencial, de solo agregar, con todas las acciones de las transacciones. Tras una falla se lee para deshacer o rehacer cambios y dejar la base consistente.

2. ¿Cómo se sabe desde el log que una transacción estaba incompleta al momento de la falla?
> [!question]- Respuesta
> Porque tiene `<START T>` pero ni `<COMMIT T>` ni `<ABORT T>`.

3. ¿Qué dice la regla de Write-Ahead Logging?
> [!question]- Respuesta
> Que el registro de log de una modificación debe llegar al disco antes que el dato modificado.
