# Recuperación de fallas — índice

Qué puede fallar en una base de datos y cómo el log permite recuperar un estado consistente después de una caída: undo, redo, undo/redo y checkpoints.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Mis apuntes de la I2, «Tipos de Fallas en Transacciones y Soluciones», que quedaron inconclusos («Seguir escribiendo este resumen…»). Las notas 02 a 05 son complemento de las slides de la clase 11 (Transacciones y Recuperación de Fallas).

## Orden de estudio
1. [[01 - Tipos de fallas|Tipos de fallas]]: datos erróneos, almacenamiento, catástrofes, sistema.
2. [[02 - Log manager y registros de log|Log manager y registros de log]]: START, COMMIT, ABORT, UPDATE y WAL.
3. [[03 - Undo logging|Undo logging]]: valores antiguos, recuperación hacia atrás, checkpoints.
4. [[04 - Redo logging|Redo logging]]: valores nuevos, recuperación hacia adelante.
5. [[05 - Undo-redo logging|Undo/redo logging]]: lo mejor de ambos y la tabla comparativa.
