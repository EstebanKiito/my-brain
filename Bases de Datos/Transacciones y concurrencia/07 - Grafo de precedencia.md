---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, origen/complemento]
prerrequisitos: ["[[06 - Acciones conflictivas y conflict serializability|Acciones conflictivas y conflict serializability]]"]
---
# Grafo de precedencia

El grafo de precedencia decide en tiempo polinomial si un schedule es **conflict serializable**: tiene una arista $T_i \to T_j$ por cada conflicto en que $T_i$ actúa primero. El schedule es conflict serializable **si y solo si el grafo no tiene ciclos**.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 11: Transacciones y Recuperación de Fallas")
> **Por qué hace falta:** probar permutaciones es exponencial ($n!$, con $n$ el número de operaciones), y decidir si un schedule es serializable en general es **NP-completo**.
>
> **Construcción:**
> - **Nodos:** las transacciones del schedule.
> - **Aristas:** hay una arista de T a T' si T ejecuta una operación op1 **antes** de una operación op2 de T', y op1 y op2 **no se pueden permutar** (son conflictivas: mismo dato y al menos una escritura).
>
> **Teorema:** un schedule es conflict serializable **si y solo si** su grafo de precedencia es **acíclico**. Un orden topológico del grafo da el schedule serial equivalente.

> [!example] Ejemplo extra — ejemplo de pizarra de la clase
> `R2(A) R1(B) W2(A) R2(B) R3(A) W1(B) W3(A) W2(B)`
> | Conflicto (en orden) | Arista |
> |---|---|
> | W2(A) antes que R3(A) y W3(A) | T2 → T3 |
> | R2(B) antes que W1(B) | T2 → T1 |
> | R1(B) antes que W2(B), y W1(B) antes que W2(B) | T1 → T2 |
>
> ```mermaid
> flowchart LR
>   T1 --> T2
>   T2 --> T1
>   T2 --> T3
> ```
> Hay un **ciclo** T1 → T2 → T1, así que **no es conflict serializable**.
>
> En cambio, en el ejemplo de [[06 - Acciones conflictivas y conflict serializability|Permutando a serial]] (`R2(A) R1(B) W2(A) R3(A) W1(B) W3(A) R2(B) W2(B)`) las aristas son T1 → T2 (W1(B) antes que R2(B)) y T2 → T3 (W2(A) antes que R3(A)). Es acíclico, con orden topológico **T1; T2; T3**.

## Preguntas de repaso

1. ¿Qué representan los nodos y las aristas del grafo de precedencia?
> [!question]- Respuesta
> Los nodos son las transacciones. Hay una arista de Ti a Tj si una operación de Ti va antes que una operación conflictiva de Tj.

2. ¿Cuándo es conflict serializable un schedule según su grafo?
> [!question]- Respuesta
> Si y solo si el grafo de precedencia es acíclico.

3. ¿Cómo obtienes el schedule serial equivalente a partir del grafo?
> [!question]- Respuesta
> Con un orden topológico de las transacciones del grafo acíclico.

4. En `R2(A) R1(B) W2(A) R2(B) R3(A) W1(B) W3(A) W2(B)`, ¿qué ciclo hay?
> [!question]- Respuesta
> T1 → T2 (R1(B) antes que W2(B)) y T2 → T1 (R2(B) antes que W1(B)). Por eso no es conflict serializable.
