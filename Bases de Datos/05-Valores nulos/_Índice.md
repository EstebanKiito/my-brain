# Valores nulos — índice

Cómo representa SQL la información faltante y qué comportamientos raros produce: la lógica de tres valores, la trampa del `NOT IN` y los agregados que ignoran nulos.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Las notas parten de los apuntes del ramo, sección «NULL». La restricción `NOT NULL` está en [[07 - Restricciones de integridad y NOT NULL|Restricciones de integridad y NOT NULL]]. Complementos de las slides de la clase 4 (SQL Avanzado).

## Orden de estudio
1. [[01 - NULL en SQL|NULL en SQL]]: significados, `IS NULL` / `IS NOT NULL`.
2. [[02 - Lógica de tres valores|Lógica de tres valores]]: TRUE, FALSE, UNKNOWN y aritmética con nulos.
3. [[03 - NOT IN con nulos|NOT IN con nulos]]: por qué el resultado queda vacío.
4. [[04 - Agregación con nulos|Agregación con nulos]]: COUNT(*) vs COUNT(col), SUM, AVG.
