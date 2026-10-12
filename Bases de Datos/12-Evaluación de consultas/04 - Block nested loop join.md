---
ramo: Bases de Datos
tema: Evaluación de consultas
tags: [bd/evaluacion, bd/joins, origen/complemento]
prerrequisitos: ["[[03 - Nested loop join|Nested loop join]]", "[[03 - Disco, RAM y buffer pool|Disco, RAM y buffer pool]]"]
---
# Block nested loop join

Mejora del nested loop join que aprovecha el buffer: llena la RAM con **muchas páginas de R** y recorre S **una vez por cada bloque**, no una vez por cada tupla.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 10: Evaluación de consultas")
> **Algoritmo** (idea):
> ```
> fillBuffer():  Buff = vacío
>                while r := R.next() != null do
>                    Buff = Buff ∪ {r}
>                    if Buff.isFull() then break
>                S.close(); S.open()          // reiniciar S para este bloque
>
> next():  while Buff != vacío do
>              while s != null do
>                  r := Buff.next()
>                  if r == null then          // se probó s con todo el bloque
>                      Buff.reset(); s := S.next()
>                  else if (r, s) satisfacen p then
>                      return (r, s)
>              fillBuffer()                   // siguiente bloque de R
>          return null
> ```
> **Costo en I/O:** con $M$ páginas de buffer para R,
> $$Costo(R) + \left\lceil \frac{Páginas(R)}{M} \right\rceil \cdot Costo(S)$$
> Por cada vez que se llena el buffer, se recorre S entera una vez.

> [!example] Ejemplo extra — mismo caso que el nested loop (slides "Clase 10")
> R y S de 16 MB (2048 páginas de 8 KB cada una) y un buffer de 1 MB, donde caben **128 páginas**:
> - Bloques de R: $2048/128 = 16$.
> - I/O = $2048 + 16 \cdot 2048 = 34.816$.
> - Con 0,1 ms por I/O: ≈ **3,4 segundos** (versus 3,1 horas).
>
> | Algoritmo | I/O | Tiempo |
> |---|---|---|
> | Nested loop join | ≈ 112.600.000 | 3,1 h |
> | Block nested loop join | 34.816 | 3,4 s |
>
> Hay algoritmos aún más eficientes, basados en **hashing** (hash join) o **sorting** (sort-merge join, que usa el [[05 - External merge sort|external merge sort]]), y que aprovechan índices como el árbol B+ (index nested loop join).

## Preguntas de repaso

1. ¿Qué mejora el block nested loop join respecto del nested loop join?
> [!question]- Respuesta
> En vez de recorrer S por cada tupla de R, la recorre una vez por cada bloque de páginas de R que cabe en el buffer.

2. ¿Cuál es su costo en I/O?
> [!question]- Respuesta
> Costo(R) + ⌈Páginas(R)/M⌉ · Costo(S), con M las páginas de buffer disponibles para R.

3. Con 2048 páginas en cada relación y 128 páginas de buffer, ¿cuántos I/O cuesta?
> [!question]- Respuesta
> 2048 + 16 · 2048 = 34.816 I/O.

4. ¿En qué otras ideas se basan los algoritmos de join más eficientes?
> [!question]- Respuesta
> En hashing (hash join), en sorting (sort-merge join) y en índices como el árbol B+.
