---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, origen/apuntes]
prerrequisitos: ["[[02 - Propiedades ACID|Propiedades ACID]]"]
---
# Problemas de concurrencia

Cuando dos transacciones leen y escriben **el mismo dato al mismo tiempo**, sus operaciones se pueden intercalar de forma que el resultado sea incorrecto, por ejemplo perdiendo dinero.

## Problemas de concurrencia (mis apuntes)
Problemas de Concurrencia (Acceder al mismo atributo simultaneamente):

![Transferencia doble - acceso concurrente opción 1](adjuntos/Transferencia%20doble%20-%20acceso%20concurrente%20opción%201.png)

![Transferencia doble - acceso concurrente opción 2](adjuntos/Transferencia%20doble%20-%20acceso%20concurrente%20opción%202.png)

> [!note]- Transcripción de las imágenes
> **Transacciones — Transferencia doble. Pero el acceso es CONCURRENTE, opción 1:**
> | Proceso Alice | Proceso Bob | Saldo cuenta A & B | Saldo cuenta C |
> |---|---|---|---|
> | READ(saldoAB, x) | | 1000 | 1000 |
> | WRITE(saldoAB, x - 100) | | 900 | |
> | | READ(saldoAB, y) | 900 | |
> | | WRITE(saldoAB, y - 200) | 700 | |
> | | READ(saldoC, y) | | 1000 |
> | | WRITE(saldoC, y + 200) | | 1200 |
> | READ(saldoC, x) | | | 1200 |
> | WRITE(saldoC, x + 100) | | | 1300 |
>
> **Opción 2:**
> | Proceso Alice | Proceso Bob | Saldo cuenta A & B | Saldo cuenta C |
> |---|---|---|---|
> | READ(saldoAB, x) | | 1000 | 1000 |
> | WRITE(saldoAB, x - 100) | | 900 | |
> | READ(saldoC, x) | | | x = 1000 |
> | | READ(saldoAB, y) | 900 | |
> | | WRITE(saldoAB, y - 200) | 700 | |
> | | READ(saldoC, y) | | 1000 |
> | | WRITE(saldoC, y + 200) | | 1200 |
> | WRITE(saldoC, x + 100) | | | **1100** |
>
> **¡Se perdieron 200!**

> [!tip] Complemento — el contexto (slides "Clase 11")
> Alice y Bob están casados y tienen una **cuenta común AB** con 1000. Alice quiere transferirle 100 a su amigo Charles (cuenta C, con 1000) y Bob quiere transferirle 200.
> - **Resultado correcto** (en cualquier orden serial): AB = 700 y C = 1300.
> - **Opción 1:** las operaciones se intercalan, pero ninguna lee un valor "viejo": el resultado es correcto.
> - **Opción 2:** Alice lee C = 1000 **antes** de que Bob escriba 1200, y luego escribe 1000 + 100 = 1100, **pisando** la escritura de Bob. Es una **actualización perdida** (ver [[04 - Lecturas sucias, no repetibles y actualización perdida|conflictos]]).
> - **Otra falla posible:** Alice descuenta 100 de AB y el sistema cae antes de depositar a C. AB queda en 900 y C en 1000: se pierde dinero si no hay **atomicidad**.

## Preguntas de repaso

1. En la opción 2, ¿por qué C termina en 1100 y no en 1300?
> [!question]- Respuesta
> Porque Alice leyó C = 1000 antes de que Bob escribiera 1200, y después escribió 1000 + 100 = 1100, sobrescribiendo la escritura de Bob.

2. ¿Por qué la opción 1 da el resultado correcto aunque se intercale?
> [!question]- Respuesta
> Porque cada transacción lee el valor actualizado por la otra antes de escribir. El efecto es equivalente a ejecutarlas en serie.

3. ¿Qué propiedad ACID se viola en la opción 2?
> [!question]- Respuesta
> El aislamiento: el resultado no es igual a ejecutar ambas transferencias una después de la otra.
