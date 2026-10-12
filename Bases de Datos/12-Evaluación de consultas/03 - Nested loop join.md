---
ramo: Bases de Datos
tema: Evaluación de consultas
tags: [bd/evaluacion, bd/joins, origen/complemento]
prerrequisitos: ["[[01 - Algoritmos en un DBMS e iteradores|Algoritmos en un DBMS e iteradores]]", "[[10 - INNER JOIN|INNER JOIN]]"]
---
# Nested loop join

El algoritmo de join más simple: por cada tupla de R se recorre **toda** S, comparando cada par. Es correcto, pero carísimo: lee S una vez **por cada tupla** de R.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 10: Evaluación de consultas")
> El join es una operación **muy costosa**. Se suponen solo restricciones de igualdad (por ejemplo, R.a = S.a).
>
> **Algoritmo** ($R \bowtie_p S$):
> ```
> open():  R.open(); S.open(); r := R.next()
> next():  while r != null do
>              s := S.next()
>              if s == null then        // se acabó S: avanzar R y reiniciar S
>                  S.close(); r := R.next(); S.open()
>              else if (r, s) satisfacen p then
>                  return (r, s)
>          return null
> close(): R.close(); S.close()
> ```
> **Costo en I/O:**
> $$Costo(R) + Tuplas(R) \cdot Costo(S)$$
> Hay que leer R entera una vez y, por cada tupla de R, leer S entera.

> [!example] Ejemplo extra — cuánto demora (slides "Clase 10")
> R y S de 16 MB, páginas de 8 KB, tuplas de 300 bytes:
> - Cada relación tiene $16\text{ MB}/8\text{ KB} = 2048$ páginas y ≈ 55.000 tuplas.
> - I/O = $2048 + 55.000 \cdot 2048 \approx 112{,}6$ millones.
> - Con 0,1 ms por I/O: $\approx 11.264$ s ≈ **3,1 horas**.
>
> Mejoras inmediatas: poner como relación externa la más pequeña, y cargar **bloques** de R en vez de tuplas → [[04 - Block nested loop join|Block nested loop join]].

## Preguntas de repaso

1. Describe el nested loop join.
> [!question]- Respuesta
> Para cada tupla r de R se recorre toda S, y se devuelve cada par (r, s) que cumple el predicado.

2. ¿Cuál es su costo en I/O?
> [!question]- Respuesta
> Costo(R) + Tuplas(R) · Costo(S): R se lee una vez y S una vez por cada tupla de R.

3. ¿Por qué tarda 3,1 horas en el ejemplo de la clase?
> [!question]- Respuesta
> Porque S (2048 páginas) se lee ≈ 55.000 veces: ≈ 112 millones de I/O, a 0,1 ms cada uno.
