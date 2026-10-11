# Transacciones y concurrencia — índice

Cómo garantiza un DBMS que muchas transacciones corran a la vez sin corromper los datos: ACID, conflictos, schedules, serializabilidad, Strict 2PL, deadlocks y niveles de aislamiento en SQL.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Mis apuntes de la I2, «4. ACID, Transacciones y Locks», con 20 imágenes de slides (todas transcritas). Complementos de las slides de la clase 11 (Transacciones y Recuperación de Fallas). La parte de recuperación está en «Recuperación de fallas».

## Orden de estudio
1. [[01 - Transacciones|Transacciones]]: qué son, ventajas y desventajas, START TRANSACTION/COMMIT.
2. [[02 - Propiedades ACID|Propiedades ACID]]: las cuatro garantías y quién asegura cada una.
3. [[03 - Problemas de concurrencia|Problemas de concurrencia]]: la transferencia doble de Alice y Bob.
4. [[04 - Lecturas sucias, no repetibles y actualización perdida|Lecturas sucias, no repetibles y actualización perdida]]: WR, RW y WW.
5. [[05 - Schedules serial y serializable|Schedules serial y serializable]]: qué orden es correcto.
6. [[06 - Acciones conflictivas y conflict serializability|Acciones conflictivas y conflict serializability]]: permutar hasta llegar a serial.
7. [[07 - Grafo de precedencia|Grafo de precedencia]]: acíclico ⇔ conflict serializable.
8. [[08 - Strict 2PL|Strict 2PL]]: locks compartidos y exclusivos.
9. [[09 - Deadlocks|Deadlocks]]: esperas circulares.
10. [[10 - COMMIT, ROLLBACK y SAVEPOINT|COMMIT, ROLLBACK y SAVEPOINT]]: controlar transacciones en SQL.
11. [[11 - Locks y registros fantasma|Locks y registros fantasma]]: granularidad y fantasmas.
12. [[12 - Niveles de aislamiento|Niveles de aislamiento]]: SERIALIZABLE … READ UNCOMMITTED.

Las imágenes de esta carpeta están en `adjuntos/`.
