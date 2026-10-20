---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[01 - Dependencias funcionales|Dependencias funcionales]]"]
---
# Primera forma normal

Una tabla está en **1NF** si cada celda tiene un valor **atómico** (no una lista ni un grupo de valores) y no hay filas repetidas. Es el requisito mínimo del modelo relacional.

## Primera forma normal (1NF)
Una relación está en 1NF si y solo si todos los atributos son atómicos (no divisibles) y cada registro es único.

Ejemplo de relación NO en 1NF:

| ID cliente | Cliente | Transacciones |
|---|---|---|
| 1 | Isaac | (1, 2003-10-14, 100.000), (2, 2003-10-15, 150.000) |

Para transformar a 1NF, se descompone en varias filas:

| ID cliente | Cliente | ID transacción | Fecha | Cantidad |
|---|---|---|---|---|
| 1 | Isaac | 1 | 2003-10-14 | 100.000 |
| 1 | Isaac | 2 | 2003-10-15 | 150.000 |

> [!tip] Complemento
> - La tabla en 1NF tiene llave **(ID cliente, ID transacción)**, pero sigue habiendo redundancia: "Isaac" se repite en cada transacción, porque ID cliente → Cliente es una **dependencia parcial**. Eso lo corrige la [[04 - Segunda forma normal|segunda forma normal]], separando `Clientes(ID cliente, Cliente)` y `Transacciones(ID cliente, ID transacción, Fecha, Cantidad)`.
> - "Atómico" depende del uso: una dirección como string único es atómica si nunca se consulta por comuna. Si se consulta por comuna, conviene separarla.
> - Columnas repetidas (`telefono1`, `telefono2`, `telefono3`) también son un síntoma de no estar en 1NF: van en una tabla aparte.

## Preguntas de repaso

1. ¿Qué exige la 1NF?
> [!question]- Respuesta
> Que todos los atributos sean atómicos (sin listas ni grupos de valores en una celda) y que cada registro sea único.

2. ¿Por qué la primera tabla de Isaac no está en 1NF y cómo se arregla?
> [!question]- Respuesta
> Porque la columna Transacciones guarda una lista de transacciones. Se arregla con una fila por transacción y columnas separadas para ID, fecha y cantidad.

3. ¿Qué redundancia queda tras pasar el ejemplo a 1NF?
> [!question]- Respuesta
> El nombre del cliente se repite en cada transacción (ID cliente → Cliente). Se resuelve en 2NF.
