---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, origen/apuntes]
prerrequisitos: ["[[03 - Problemas de concurrencia|Problemas de concurrencia]]"]
---
# Lecturas sucias, no repetibles y actualización perdida

Los tres conflictos clásicos entre dos transacciones que usan el mismo dato. Se nombran por el par de operaciones en conflicto: Write-Read (lectura sucia), Read-Write (lectura no repetible) y Write-Write (actualización perdida).

## Ejemplos de conflictos (mis apuntes)
- **Lecturas Sucias (Write - Read):** Ocurren cuando una transacción accede a datos que han sido modificados por otra transacción que aún no se ha terminado.
- **Lecturas No Repetibles (Read - Write):** Ocurren cuando una fila es leída dos veces y el valor cambia entre ambas lecturas.
- **Actualización Perdida o Reescritura de Datos Temporales (Write - Write):** Ocurren cuando dos transacciones que intentan actualizar la misma fila son procesadas en un tiempo que permite que una de las actualizaciones sobrescriba a la otra.

![Actualización perdida WW - asiento 24](adjuntos/Actualización%20perdida%20WW%20-%20asiento%2024.png)

![Lectura sucia WR - asiento 24](adjuntos/Lectura%20sucia%20WR%20-%20asiento%2024.png)

![Lectura no repetible RW - asientos](adjuntos/Lectura%20no%20repetible%20RW%20-%20asientos.png)

> [!note]- Transcripción de las imágenes
> **Actualización perdida (WW)**, "una transacción sobreescribe los datos que otra tx ya había escrito": T2 R(X) "¿Está libre el asiento 24? Sí" → T1 R(X) "¿Está libre el asiento 24? Sí" → T1 W(X) "Reserve el 24" → T1 C → T2 W(X) "Reserve el 24 (¡pero estaba ocupado!)".
>
> **Lectura sucia (WR)**, "una tx. lee lo que otra tx escribió pero no se había confirmado aún": T2 W(X) "Reserve el 24" → T1 R(X) "¿Cuántos asientos hay? No hay más" → T1 W(X) "Reserve entonces en primera clase" → T1 C → T2 A "…¡pero sí habían!".
>
> **Lectura no repetible (RW)**, "una tx. sobreescribe un dato que otra ya había leído antes pero no había confirmado": T2 R(X) "¿Cuántos asientos hay? A ver…" → T1 W(X) "Reserve el 24" → T1 C → T2 R(X) "…ahora sí. ¿Cuáles asientos? (¡Menos!)".

## Ejemplos

```sql
--Lecturas Sucias:

READ(A,x)
WRITE(A,x)

--Lecturas No Repetibles:

READ(A,x)
WRITE(A,x)

--Actualización Perdida o Reescritura de Datos Temporales:

WRITE(A,x)
WRITE(A,x)
```

> [!warning] Posible error (registrado en `_meta/Bases de Datos/DUDAS.md`)
> Los ejemplos no indican **qué transacción** hace cada operación, y los dos primeros quedaron idénticos. Con la notación de la clase, tomando las imágenes:
> | Conflicto | Secuencia mínima | Problema |
> |---|---|---|
> | Lectura sucia (WR) | $W_2(X) \to R_1(X) \to A_2$ | T1 leyó un valor que nunca se confirmó |
> | Lectura no repetible (RW) | $R_2(X) \to W_1(X) \to C_1 \to R_2(X)$ | T2 lee dos valores distintos de X |
> | Actualización perdida (WW) | $R_2(X) \to R_1(X) \to W_1(X) \to C_1 \to W_2(X)$ | la escritura de T2 pisa la de T1 |

> [!tip] Complemento
> - El orden de las letras indica qué operación va **primero**: WR = una escribe y **después** otra lee.
> - Estos tres conflictos son los que determinan si se pueden reordenar operaciones ([[06 - Acciones conflictivas y conflict serializability|acciones conflictivas]]). Los **niveles de aislamiento** de SQL definen cuáles se toleran (ver [[12 - Niveles de aislamiento|Niveles de aislamiento]]), junto con un cuarto problema: los **fantasmas**.

## Preguntas de repaso

1. ¿Qué es una lectura sucia? ¿Qué par de operaciones la causa?
> [!question]- Respuesta
> Una transacción lee un dato escrito por otra que aún no ha hecho commit, y que podría abortar. Es un conflicto Write-Read.

2. ¿Qué es una lectura no repetible?
> [!question]- Respuesta
> Una transacción lee el mismo dato dos veces y obtiene valores distintos, porque otra transacción lo modificó entre ambas lecturas (Read-Write).

3. Explica la actualización perdida con el ejemplo del asiento 24.
> [!question]- Respuesta
> Ambas transacciones leen que el asiento 24 está libre. T1 lo reserva y confirma, y después T2 también escribe la reserva, sobrescribiendo la de T1 aunque el asiento ya estaba ocupado.

4. Escribe la lectura sucia con notación $R_i$/$W_i$.
> [!question]- Respuesta
> $W_2(X), R_1(X), \ldots, A_2$: T1 lee lo que T2 escribió y T2 después aborta.
