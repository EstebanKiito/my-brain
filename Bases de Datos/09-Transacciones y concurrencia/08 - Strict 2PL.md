---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, bd/locks, origen/apuntes]
prerrequisitos: ["[[06 - Acciones conflictivas y conflict serializability|Acciones conflictivas y conflict serializability]]"]
---
# Strict 2PL

**Strict Two-Phase Locking** es el protocolo de control de concurrencia más usado: antes de leer o escribir hay que pedir un lock (compartido o exclusivo), y los locks se liberan todos juntos **al terminar** la transacción. Así solo se generan schedules conflict serializables.

## Strict 2PL (protocolo de locks)
- **Regla 1:** si una transacción T quiere leer o modificar un objeto:
    - primero pide un *shared lock* (para leer) o un *exclusive lock* (para modificar) sobre el objeto;
    - la transacción se suspende hasta que consigue el lock;
    - si una transacción mantiene un exclusive lock sobre un objeto, ninguna otra puede tener un shared ni un exclusive lock sobre él;
    - para obtener el exclusive lock, no debe haber ningún otro lock sobre el objeto.
- **Regla 2:** cuando la transacción se completa, libera todos los locks que mantenía.

![Strict 2PL - fase de locks](adjuntos/Strict%202PL%20-%20fase%20de%20locks.png)

> [!note]- Transcripción de la imagen
> Gráfico "**Strict 2PL**": en el eje del tiempo, la cantidad de locks crece durante la **lock phase** (rampa), se mantiene constante mientras la transacción trabaja y cae a cero de golpe en **locks release**, cuando la transacción termina.

> [!tip] Complemento — compatibilidad de locks y ejemplo (slides "Clase 11")
> | ¿Se otorga? | otra tiene **shared** | otra tiene **exclusive** | nadie tiene lock |
> |---|---|---|---|
> | pido **shared** (para leer) | ✅ | ❌ espera | ✅ |
> | pido **exclusive** (para escribir) | ❌ espera | ❌ espera | ✅ |
>
> **Cómo funciona** con T1 = R(A), W(B) y T2 = W(A), W(B):
> 1. T1 hace R(A) → **shared lock (A)**.
> 2. T2 quiere W(A) → pide exclusive (A) → **espera a T1**.
> 3. T1 hace W(B) → **exclusive lock (B)**.
> 4. T1 termina ("listo con T1") → libera todos sus locks.
> 5. T2 obtiene **exclusive lock (A)** y sigue con W(B).
>
> El resultado es equivalente al serial T1; T2. **Las reglas aseguran solo schedules conflict serializables.**
>
> **"Strict"** = los locks se sueltan solo al final (commit o abort). Así nadie lee datos no confirmados, y se evitan las lecturas sucias y los aborts en cascada. El costo son esperas y posibles [[09 - Deadlocks|deadlocks]].

## Preguntas de repaso

1. ¿Qué lock pide una transacción para leer y cuál para escribir?
> [!question]- Respuesta
> Un shared lock para leer y un exclusive lock para escribir.

2. ¿Pueden dos transacciones tener shared lock sobre el mismo objeto? ¿Y una shared y otra exclusive?
> [!question]- Respuesta
> Dos shared, sí. Shared con exclusive, no: si alguien tiene un exclusive, nadie más puede tener ningún lock sobre ese objeto.

3. ¿Cuándo libera sus locks una transacción en Strict 2PL?
> [!question]- Respuesta
> Todos juntos, cuando la transacción se completa (commit o abort).

4. ¿Qué garantiza Strict 2PL y qué problema puede causar?
> [!question]- Respuesta
> Garantiza que solo se produzcan schedules conflict serializables. Puede causar esperas y deadlocks.
