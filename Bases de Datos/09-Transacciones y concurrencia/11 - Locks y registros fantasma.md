---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, bd/locks, origen/apuntes]
prerrequisitos: ["[[08 - Strict 2PL|Strict 2PL]]"]
---
# Locks y registros fantasma

Un lock puede tomar una tabla entera o solo algunas tuplas (**granularidad**). Si solo bloquea las tuplas existentes, otra transacción puede **insertar** una tupla nueva que cumpla la condición: un **fantasma**.

## 4. Locks en SQL (mis apuntes)

![Locks y registro fantasma - Sailors](adjuntos/Locks%20y%20registro%20fantasma%20-%20Sailors.png)

T2 :

![T2 espera a T1](adjuntos/T2%20espera%20a%20T1.png)

> [!note]- Transcripción de las imágenes
> **T1:** `SELECT S.rating, MIN(S.age) FROM Sailors AS S WHERE S.rating = 8;` toma un **shared lock** sobre las tuplas con rating 8: (2, 21, 8) y (3, 16, 8).
>
> | sid | age | rating |
> |---|---|---|
> | 1 | 34 | 9 |
> | 2 | 21 | 8 |
> | 3 | 16 | 8 |
> | 4 | 26 | 10 |
>
> **T2:** `INSERT INTO Sailors AS S VALUES (5,22,8);` agrega la tupla (5, 22, 8), que también tiene rating 8: es el **"fantasma"**, que el lock de T1 no cubría.
>
> Segunda imagen: flecha "**espera a T1**". Con un lock adecuado, el `INSERT` de T2 tiene que esperar a que T1 termine.

> [!tip] Complemento — granularidad (slides "Clase 11")
> Para la consulta de T1:
> - **Lock seguro:** toda la tabla `Sailors`. Nadie puede insertar, pero se bloquea demasiado.
> - **Lock razonable:** las tuplas de `Sailors` con rating = 8. Es más concurrente, pero deja pasar fantasmas: si T1 vuelve a ejecutar la consulta, ve una fila nueva y el `MIN(age)` podría cambiar.
>
> **Fantasma:** una fila que aparece (o desaparece) entre dos lecturas de la misma consulta, por un `INSERT`/`DELETE` de otra transacción. Es distinto de la lectura no repetible, donde cambia el valor de una fila ya leída.
>
> **Solución:** bloquear también el **predicado** o el rango (`rating = 8`), por ejemplo con locks sobre el índice o la tabla. Es lo que exige el nivel `SERIALIZABLE` (ver [[12 - Niveles de aislamiento|Niveles de aislamiento]]). Así, T2 espera a T1.

## Preguntas de repaso

1. ¿Qué es un registro fantasma?
> [!question]- Respuesta
> Una tupla insertada (o borrada) por otra transacción que cumple la condición de una consulta en curso. Si la consulta se repite, aparece una fila que antes no estaba.

2. ¿Por qué los locks por tupla no evitan los fantasmas?
> [!question]- Respuesta
> Porque bloquean solo las tuplas que ya existen; una tupla nueva que cumpla la condición no tiene lock y se puede insertar.

3. ¿Qué diferencia hay entre un lock "seguro" y uno "razonable" en el ejemplo?
> [!question]- Respuesta
> El seguro bloquea toda la tabla (sin fantasmas, pero con poca concurrencia). El razonable bloquea solo las tuplas con rating 8 (más concurrencia, pero permite fantasmas).

4. ¿En qué se diferencia un fantasma de una lectura no repetible?
> [!question]- Respuesta
> En la lectura no repetible cambia el valor de una fila ya leída. En el fantasma cambia el conjunto de filas que cumple la condición.
