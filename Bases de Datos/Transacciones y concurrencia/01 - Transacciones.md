---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, origen/apuntes]
prerrequisitos: ["[[02 - UPDATE y DELETE|UPDATE y DELETE]]"]
---
# Transacciones

Una transacción es un grupo de operaciones sobre la base de datos que se trata **como una unidad**: o se aplican todas o ninguna, aunque haya fallas o accesos concurrentes. En SQL se delimita con `START TRANSACTION … COMMIT`.

## 4. ACID, transacciones y locks — Transacciones (mis apuntes)
- Una transacción es una secuencia de operaciones que modifican o consultan la base de datos.
- Su principal objetivo es garantizar la integridad de los datos y la consistencia del estado de la base de datos, incluso en presencia de fallos y errores.
- Las transacciones tienen varias ventajas, como:
    - la integridad de los datos
    - la consistencia
    - el aislamiento
    - la durabilidad.
- Sin embargo, también tienen desventajas, como:
    - la complejidad en el manejo,
    - el rendimiento
    - el uso de recursos.

![Transacciones - ventajas y desventajas](adjuntos/Transacciones%20-%20ventajas%20y%20desventajas.png)

> [!note]- Transcripción de la imagen
> **Transacciones**
> | Ventajas | Desventajas |
> |---|---|
> | **Integridad de los datos:** asegura que todos los cambios en la base de datos son correctos y se preserva la consistencia, incluso ante errores o fallos del sistema. | **Complejidad en el manejo:** requiere mecanismos sofisticados de control de concurrencia y recuperación, lo que puede complicar el diseño y el mantenimiento de la base de datos. |
> | **Consistencia:** garantiza que la base de datos siempre refleje un estado válido según las reglas definidas, gracias a la ejecución completa de las transacciones. | **Rendimiento:** las transacciones, especialmente cuando son grandes o complejas, pueden afectar el rendimiento debido al bloqueo de recursos y a la gestión del control de concurrencia. |
> | **Aislamiento:** permite que múltiples transacciones se ejecuten simultáneamente sin interferir entre ellas, manteniendo la exactitud de los datos. | **Uso de recursos:** puede requerir un uso intensivo de recursos, como memoria y procesador, para gestionar el estado y la sincronización de las transacciones. |
> | **Durabilidad:** una vez que una transacción se completa, sus efectos son permanentes, incluso en caso de fallo del sistema. | **Tiempo de espera:** los bloqueos necesarios para mantener el aislamiento pueden llevar a tiempos de espera o a deadlocks que deben ser gestionados cuidadosamente. |

## Transacciones en SQL

```sql
START TRANSACTION

UPDATE cuentas 
SET saldo = saldo - v 
WHERE cid = 1

UPDATE cuentas 
SET saldo = saldo + v 
WHERE cid = 2

COMMIT
```

Transacciones en SQL:
- START TRANSACTION y COMMIT nos permiten agrupar operaciones en una sola transacción

**Operaciones:**
1. **Read(x):** Lectura del elemento x
2. **Write(x):** Escritura del elemento x
3. **Abort:** Abortar Transacción
4. **Commit:** Finalizar Transacción

> [!tip] Complemento (slides "Clase 11: Transacciones y Recuperación de Fallas")
> - Una transacción es una secuencia de **1 o más** operaciones. Ejemplos: transferencias de dinero entre cuentas, una compra por internet, inscribir un curso…
> - El ejemplo es una **transferencia** de `v` pesos de la cuenta 1 a la 2. Si el sistema falla entre los dos `UPDATE`, el dinero desaparece. Agruparlos en una transacción garantiza que pasen ambos o ninguno.
> - Notación usada en el resto del tema: $R_i(X)$ y $W_i(X)$ son la lectura y escritura de X por la transacción $i$; **A** es abort y **C** es commit.
> - Es uno de los componentes fundamentales de un DBMS y le valió un Premio Turing a Jim Gray (1998).
> - En SQL real se terminan las sentencias con `;`. En PostgreSQL también sirve `BEGIN;` en vez de `START TRANSACTION;`.

## Preguntas de repaso

1. ¿Qué es una transacción y cuál es su objetivo?
> [!question]- Respuesta
> Una secuencia de operaciones que modifican o consultan la base de datos, tratada como unidad. Su objetivo es garantizar la integridad y consistencia de los datos incluso con fallos y accesos concurrentes.

2. ¿Por qué la transferencia entre cuentas debe ser una transacción?
> [!question]- Respuesta
> Porque son dos `UPDATE` que deben ocurrir juntos. Si falla entre ellos, se restaría de una cuenta sin sumar en la otra.

3. Nombra dos desventajas de las transacciones.
> [!question]- Respuesta
> Complejidad en el manejo (control de concurrencia y recuperación), menor rendimiento por los bloqueos, uso de recursos, y tiempos de espera o deadlocks.

4. ¿Cuáles son las cuatro operaciones básicas de una transacción?
> [!question]- Respuesta
> Read(x), Write(x), Abort y Commit.
