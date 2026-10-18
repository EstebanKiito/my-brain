---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, bd/edd, origen/apuntes]
prerrequisitos: ["[[07 - Diccionarios|Diccionarios]]"]
---
# Tablas de hash

Una tabla de hash implementa un diccionario usando una **función de hash** $h$, que lleva cada llave a uno de $m$ casilleros (*buckets*). Buscar una llave es calcular $h(k)$ e ir directo a su casillero: en promedio $O(1)$.

## Tablas de hash
- Dado un espacio de llaves K y un natural m > 0, una función de hash se define como
    - `h ∶ K → {0, . . . , m − 1}`
- Dado $k \in K$, se llama **valor de hash** de $k$ a la evaluación $h(k)$. Hay que notar que:
    - una función de hash permite mapear un espacio de llaves a otro más pequeño (con $m$ razonable);
    - una función de hash no necesariamente es inyectiva: **dos llaves distintas pueden tener el mismo valor de hash** (una **colisión**), y la tabla tiene que manejarlas.

> [!tip] Complemento — cómo funciona (slides "Clase 9", "Repaso (o spoiler) de EDD")
> - Se inicia un número **fijo** de casilleros (*buckets*). Cada tupla va a parar a un casillero según su llave, usando la función de hash.
> - Ejemplo de la clase: `Actores(aid, nombre)` con 5 casilleros y $h(aid) = aid \bmod 5$.
>
> | Bucket | Contenido |
> |---|---|
> | 0 | (5, Bernini) |
> | 1 | (1, Leonardo), (11, Brunelleschi) |
> | 2 | (12, Botticelli) |
> | 3 | (8, Michelangelo) |
> | 4 | — |
>
> - **Buscar aid = 12:** $12 \bmod 5 = 2$ → en **1 paso** se llega al casillero correcto, en vez de recorrer una lista.
> - **Colisiones:** 1 y 11 caen en el mismo casillero ($1 \bmod 5 = 11 \bmod 5 = 1$). Se resuelven, por ejemplo, encadenando los elementos del casillero en una lista.
> - Se supone que la función de hash distribuye **uniformemente** y que hay suficientes casilleros para que la búsqueda tome 1 paso (o no mucho más).
> - En el ejemplo de los RUT: con $m \approx 25.000$ casilleros y $h(rut) = rut \bmod m$, 25.000 estudiantes caben en un arreglo de tamaño razonable.
>
> En bases de datos, los casilleros son **páginas de disco**: ver [[10 - Índice hash|Índice hash]].

## Preguntas de repaso

1. ¿Qué hace una función de hash?
> [!question]- Respuesta
> Lleva cada llave de un espacio grande K a un número entre 0 y m − 1, el casillero donde se guarda.

2. ¿Qué es una colisión y por qué ocurre?
> [!question]- Respuesta
> Dos llaves distintas con el mismo valor de hash. Ocurre porque la función de hash no es inyectiva: el espacio de llaves es mayor que el número de casilleros.

3. Con $h(k) = k \bmod 5$, ¿en qué casillero quedan 8 y 16?
> [!question]- Respuesta
> 8 en el 3 y 16 en el 1 (colisiona con 1 y 11).

4. ¿Cuál es el costo esperado de buscar en una tabla de hash?
> [!question]- Respuesta
> $O(1)$ en promedio, si la función distribuye uniformemente y hay suficientes casilleros. En el peor caso, con todo en un casillero, es $O(n)$.
