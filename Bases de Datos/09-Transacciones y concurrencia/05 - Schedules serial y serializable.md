---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, origen/apuntes]
prerrequisitos: ["[[04 - Lecturas sucias, no repetibles y actualización perdida|Lecturas sucias, no repetibles y actualización perdida]]"]
---
# Schedules serial y serializable

Un **schedule** es el orden en que el DBMS intercala las operaciones de varias transacciones. Es **serial** si no intercala nada y **serializable** si, aunque intercale, siempre da el mismo resultado que algún orden serial.

## Schedules
- Un schedule (programa de ejecución) es una secuencia de operaciones primitivas de una o más transacciones.
- Las operaciones pueden ser de lectura (R) o escritura (W).
- Un schedule es **serial** si no hay intercalación entre las acciones.

![Schedule serial - T1 y T2](adjuntos/Schedule%20serial%20-%20T1%20y%20T2.png)

- Un schedule S es **serializable** si existe algún schedule serial S' con las mismas transacciones, tal que el resultado de S y S' es el mismo para todo estado inicial de la BD.

![Schedule serializable - T1 y T2](adjuntos/Schedule%20serializable%20-%20T1%20y%20T2.png)

![Schedule no serializable - T1 y T2](adjuntos/Schedule%20no%20serializable%20-%20T1%20y%20T2.png)

> [!note]- Transcripción de las imágenes
> T1 = `READ(A,x); x:= x + 100; WRITE(A,x); READ(B,x); x:= x + 200; WRITE(B,x)` · T2 = `READ(A,y); y:= y * 2; WRITE(A,y); READ(B,y); y:= y * 3; WRITE(B,y)`.
> | Schedule | Orden |
> |---|---|
> | **Serial** | todo T1 (A y B) y luego todo T2 (A y B) |
> | **Serializable** | T1 sobre A → T2 sobre A → T1 sobre B → T2 sobre B. "Como las operaciones para A en x e y no afectan al orden de x e y de B, entonces SÍ es serializable." |
> | **No serializable** | T1 sobre A → T2 sobre A → T2 sobre B → T1 sobre B. "En T2, la transacción de WRITE(B, y) realiza cambios que afectan a READ(B,x), por lo que el orden sí cambia los resultados y por lo mismo el schedule No es serializable." |

## Ejemplos de schedules
- **Schedule serial:** todo T1 (A + 100, B + 200) y después todo T2 (A · 2, B · 3).

```sql
-- T1
READ(A,x)
x = x + 100
WRITE(A,x)
READ(B,x)
x = x + 200
WRITE(B,x)
-- T2
READ(A,y)
y = y * 2
WRITE(A,y)
READ(B,y)
y = y * 3
WRITE(B,y)
```

- **Schedule no serializable:** T1 hace A, T2 hace A, T2 hace B y recién después T1 hace B. En A, T1 va antes que T2; en B, T2 va antes que T1. Ningún orden serial produce ese resultado.

```sql
READ(A,x)    -- T1
x = x + 100
WRITE(A,x)
READ(A,y)    -- T2
y = y * 2
WRITE(A,y)
READ(B,y)    -- T2
y = y * 3
WRITE(B,y)
READ(B,x)    -- T1
x = x + 200
WRITE(B,x)
```

> [!tip] Complemento — por qué el último no es serializable (slides "Clase 11")
> Con $A = B = 100$ al inicio:
> | Orden | A final | B final |
> |---|---|---|
> | Serial T1;T2 | (100+100)·2 = 400 | (100+200)·3 = 900 |
> | Serial T2;T1 | 100·2+100 = 300 | 100·3+200 = 500 |
> | **No serializable** | (100+100)·2 = **400** (como T1;T2) | 100·3+200 = **500** (como T2;T1) |
>
> El resultado mezcla los dos órdenes, así que no es igual a ningún schedule serial. La tarea del **Transaction Manager** es permitir solo schedules serializables. ¿Cómo decidirlo rápido? Con [[06 - Acciones conflictivas y conflict serializability|conflict serializability]].
>
> Definición precisa de la clase: un schedule es una secuencia de operaciones de una o más transacciones tal que, **para cada transacción, sus acciones aparecen en el mismo orden que en su definición**.

## Preguntas de repaso

1. ¿Qué es un schedule serial?
> [!question]- Respuesta
> Uno en que las transacciones se ejecutan una después de la otra, sin intercalar sus acciones.

2. ¿Cuándo es serializable un schedule?
> [!question]- Respuesta
> Cuando existe algún schedule serial con las mismas transacciones que produce el mismo resultado para todo estado inicial de la base de datos.

3. ¿Por qué el schedule que hace "T1 sobre A, T2 sobre A, T1 sobre B, T2 sobre B" es serializable?
> [!question]- Respuesta
> Porque en A y en B se respeta el mismo orden, T1 antes que T2. Es equivalente al serial T1;T2.

4. Con A = B = 100, ¿qué resultado da el schedule no serializable y por qué prueba que no lo es?
> [!question]- Respuesta
> A = 400 y B = 500. A coincide con T1;T2 y B con T2;T1, así que no hay un orden serial que dé ambos.
