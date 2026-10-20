---
ramo: "Sistemas Distribuidos"
tema: "Control de concurrencia distribuido"
tags:
  - sd/concurrencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Transacciones distribuidas y sus desafíos]]"
---

# Conflictos por concurrencia

Con muchos usuarios a la vez, las transacciones compiten por los mismos datos. Dos operaciones están en **conflicto** cuando su efecto combinado **depende del orden** en que se ejecutan. Reconocer qué pares de operaciones chocan, y qué problemas producen, es el primer paso para controlarlos.

## Tipos de conflicto

| Par de operaciones | ¿Conflicto? | Por qué |
|---|---|---|
| **Lectura-escritura** (*read-write*) | Sí | Lo que lee la lectura depende de si la escritura ocurrió antes o después |
| **Escritura-escritura** (*write-write*) | Sí | El valor final depende de cuál de las dos escribe al último |
| **Lectura-lectura** (*read-read*) | No | Leer no cambia nada, así que el orden no importa |

Es la misma noción de [[06 - Acciones conflictivas y conflict serializability|acciones conflictivas]] de las bases de datos, ahora entre servidores.

## Actualización perdida (*lost update*)

![Problema de la actualización perdida](adjuntos/Problema%20de%20la%20actualizaci%C3%B3n%20perdida.png)

> [!example]- Transcripción de la imagen
> Conflicto tipo write-write: dos o más transacciones concurrentes trabajan sobre la misma variable, y una sobrescribe a la otra o no ve su actualización antes de escribir. Ejemplo: un producto cuesta 5000; T1 lo rebaja en 1000 y T2 le aplica un 50 % de descuento. El precio final puede ser 4000 (T1 sobrescribe a T2), 2500 (T2 sobrescribe a T1), 2000 (T2 se ejecuta después de T1) o 1500 (T1 se ejecuta después de T2).

Solo 2000 y 1500 corresponden a ejecutar ambas transacciones en algún orden serial. En 4000 y 2500 una actualización **se perdió**: ambas leyeron 5000 y la última en escribir borró el trabajo de la otra. Los cuatro valores se verificaron en Python.

## Lecturas inconsistentes (*inconsistent retrievals*)

![Problema de lecturas inconsistentes](adjuntos/Problema%20de%20lecturas%20inconsistentes.png)

> [!example]- Transcripción de la imagen
> Conflicto tipo read-write: T1 está modificando una variable y todavía no hace commit, y T2 lee esa misma variable. Si T1 consolida, T2 queda con un valor obsoleto. Ejemplo: se carga un producto para ver su precio (T1), pero mientras carga la página le aplican un 50 % de descuento (T2). El precio mostrado puede ser el original (T1 no vio lo que hizo T2) o el rebajado (T1 sí lo vio).

El usuario puede tomar decisiones con un precio que ya no existe.

> [!tip] Cómo se enfrentan
> - **Evitar** el conflicto: control [[02 - Control pesimista y optimista|pesimista u optimista]].
> - **Aceptarlo** y resolverlo después: [[03 - Resolución de conflictos concurrentes|políticas de resolución]].

## Preguntas de repaso

> [!question]- ¿Por qué dos lecturas concurrentes no son un conflicto?
> Porque ninguna modifica el dato: ambas leen lo mismo en cualquier orden, así que el resultado no depende de cómo se intercalen.

> [!question]- En el ejemplo del precio, ¿qué resultados indican una actualización perdida?
> 4000 y 2500: en ambos, una transacción escribió sin ver la escritura de la otra. 2000 y 1500 corresponden a ejecutar ambas en serie.

> [!question]- ¿Qué tipo de conflicto produce las lecturas inconsistentes?
> Uno de lectura-escritura: una transacción lee un dato mientras otra lo está modificando, y lo que lee depende de si la escritura ya se consolidó.
