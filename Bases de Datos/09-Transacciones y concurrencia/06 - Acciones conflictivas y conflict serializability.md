---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, origen/apuntes]
prerrequisitos: ["[[05 - Schedules serial y serializable|Schedules serial y serializable]]"]
---
# Acciones conflictivas y conflict serializability

Dos operaciones de transacciones distintas **conflictúan** si usan el mismo dato y al menos una escribe. Las no conflictivas se pueden intercambiar. Un schedule es **conflict serializable** si, intercambiándolas, se puede llevar a uno serial.

## Transacciones no conflictivas (mis apuntes)
- Transaccion i ejecuta Read(X,t) → Ri(x)
- Transaccion i ejecuta Write(X,t) → Wi(x)

![Acciones no conflictivas](adjuntos/Acciones%20no%20conflictivas.png)

![Permutaciones permitidas - antes](adjuntos/Permutaciones%20permitidas%20-%20antes.png)

![Permutaciones permitidas - después](adjuntos/Permutaciones%20permitidas%20-%20después.png)

> [!note]- Transcripción de las imágenes
> **Acciones no conflictivas.** Las siguientes acciones son NO conflictivas para dos transacciones distintas i, j: $R_i(X), R_j(Y)$ · $R_i(X), W_j(Y)$ con X ≠ Y · $W_i(X), R_j(Y)$ con X ≠ Y · $W_i(X), W_j(Y)$ con X ≠ Y. ¡Podemos cambiarlas de orden en un **schedule**!
>
> **Permutaciones permitidas, antes:** T1 READ(A) · T2 READ(A) · T2 READ(C) · T1 READ(B) · T1 WRITE(A) · T2 WRITE(C) · T1 READ(D).
> **Después** (colores = pares intercambiados): T2 READ(A) · T1 READ(A) · T1 READ(C) · T1 WRITE(A) · T2 READ(B) · T1 READ(D) · T2 WRITE(C).

## Acciones conflictivas

![Acciones conflictivas](adjuntos/Acciones%20conflictivas.png)

![Permutaciones no permitidas](adjuntos/Permutaciones%20no%20permitidas.png)

> [!note]- Transcripción de las imágenes
> **Acciones conflictivas** para dos transacciones distintas i, j: **Lectura-Escritura** ($R_i(X), W_j(X)$): i lee X y j escribe X. **Escritura-Lectura** ($W_i(X), R_j(X)$): i escribe X y j lee X. **Escritura-Escritura** ($W_i(X), W_j(X)$): ambas escriben en X. ¡No podemos cambiar su orden en un **schedule** a la ligera!
>
> **Permutaciones no permitidas:** T2 WRITE(A) · T1 READ(A) (marcado con ✗: no se pueden intercambiar) · T2 WRITE(C) · T1 WRITE(C) · T1 WRITE(A) · T2 READ(A) · T1 READ(D).

## Se pueden permutar operaciones consecutivas
1. Par de operaciones que NO USEN EL MISMO RECURSO
2. Par de operaciones que USAN EL MISMO RECURSO PERO AMBAS DE LECTURA

Schedule es “CONFLICT SERIALIZABLE” → Si se puede transformar en uno serial usando permutaciones.

> [!tip] Complemento (slides "Clase 11")
> - Las operaciones **de una misma transacción** tampoco se pueden reordenar: $P_i(X), Q_i(Y)$ es conflictivo para P, Q en {R, W}.
> - **Conflict serializable ⇒ serializable**, pero hay schedules serializables que no son conflict serializables. Permutar preserva el orden de todos los conflictos.
>
> **Ejemplo de la clase: "Permutando a serial".**
> `R2(A) R1(B) W2(A) R3(A) W1(B) W3(A) R2(B) W2(B)`
> Intercambiando pares no conflictivos se llega a
> `R1(B) W1(B) | R2(A) W2(A) R2(B) W2(B) | R3(A) W3(A)`
> que es el serial **T1; T2; T3**: es conflict serializable.
>
> Probar todas las permutaciones es exponencial. Para decidirlo rápido está el [[07 - Grafo de precedencia|grafo de precedencia]].

## Preguntas de repaso

1. ¿Cuándo dos operaciones de transacciones distintas son conflictivas?
> [!question]- Respuesta
> Cuando acceden al mismo dato y al menos una es escritura: R-W, W-R o W-W sobre el mismo X.

2. ¿Se pueden intercambiar $R_1(A)$ y $R_2(A)$? ¿Y $R_1(A)$ y $W_2(A)$?
> [!question]- Respuesta
> $R_1(A)$ y $R_2(A)$ sí, porque ambas son lecturas. $R_1(A)$ y $W_2(A)$ no, porque es un conflicto lectura-escritura sobre A.

3. ¿Qué significa que un schedule sea conflict serializable?
> [!question]- Respuesta
> Que se puede transformar en un schedule serial intercambiando solo pares consecutivos de operaciones no conflictivas.

4. ¿Todo schedule serializable es conflict serializable?
> [!question]- Respuesta
> No. Conflict serializable implica serializable, pero existen schedules serializables que no son conflict serializables.
