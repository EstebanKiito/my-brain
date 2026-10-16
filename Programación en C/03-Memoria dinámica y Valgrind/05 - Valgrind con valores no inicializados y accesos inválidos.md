---
ramo: "Programación en C"
tema: "Memoria dinámica y Valgrind"
tags:
  - c
  - valgrind
  - memcheck
  - depuracion
  - origen/complemento
prerrequisitos:
  - "[[04 - Valgrind y detección de memory leaks]]"
---

# Valgrind con valores no inicializados y accesos inválidos

Los leaks no cambian lo que hace un programa, pero los **errores de memoria** sí. Son los más difíciles de depurar sin herramientas, porque el programa casi nunca se cae en la línea culpable. Memcheck reporta tres tipos frecuentes, y en cada uno dice **qué** pasó, **en qué línea** y **qué bloque** estaba involucrado.

## Valor no inicializado

```c
#include <stdlib.h>
#include <stdio.h>

int main()
{
    int* E = malloc(sizeof(int));   // línea 6: basura
    if (*E > 10)                    // línea 7: decide con basura
    {
        printf("Hi there!\n");
    }
    free(E);
    return 0;
}
```

![Código bad_val](adjuntos/C%C3%B3digo%20bad_val%20con%20valor%20no%20inicializado.png)

> [!example]- Transcripción de la imagen
> Archivo `bad_val.c`, con 13 líneas numeradas que muestran exactamente el código de arriba.

El programa no se cae: a veces imprime y a veces no. Valgrind lo detecta:

![Salto condicional con valor no inicializado](adjuntos/Valgrind%20-%20salto%20condicional%20con%20valor%20no%20inicializado.png)

> [!example]- Transcripción de la imagen
> "Conditional jump or move depends on uninitialised value(s) at main (bad_val.c:7)". HEAP SUMMARY: "in use at exit: 0 bytes in 0 blocks; total heap usage: 1 allocs, 1 frees, 4 bytes allocated. All heap blocks were freed -- no leaks are possible". Al lado, el código con la línea 7 (`if (*E > 10)`) resaltada.

![Sugerencia de track-origins](adjuntos/Valgrind%20-%20sugerencia%20de%20track-origins.png)

> [!example]- Transcripción de la imagen
> "Use --track-origins=yes to see where uninitialised values come from. For lists of detected and suppressed errors, rerun with: -s".

`--track-origins=yes` dice **dónde se creó** el valor sin inicializar, que suele estar lejos de donde se usa:

![Origen del valor no inicializado](adjuntos/Valgrind%20-%20origen%20del%20valor%20no%20inicializado.png)

> [!example]- Transcripción de la imagen
> "Uninitialised value was created by a heap allocation, at malloc, by main (bad_val.c:6)", con la línea 6 (`int* E = malloc(sizeof(int));`) resaltada en el código.

## Escritura inválida

```c
int* F = calloc(10, sizeof(int));     // línea 6: 40 bytes
for (int i = 0; i <= 10; i += 1)      // <= : la última vuelta usa F[10]
    F[i] = i * i;                     // escribe 4 bytes fuera del bloque
```

![Código bad_write](adjuntos/C%C3%B3digo%20bad_write%20con%20escritura%20fuera%20del%20arreglo.png)

> [!example]- Transcripción de la imagen
> Archivo `bad_write.c`: `int* F = calloc(10, sizeof(int));` en la línea 6, el ciclo `for(int i = 0; i <= 10; i+=1)` en la línea 7, `F[i] = i * i;` adentro, y después `free(F); return 0;`.

![Escritura inválida después del bloque](adjuntos/Valgrind%20-%20escritura%20inv%C3%A1lida%20despu%C3%A9s%20del%20bloque.png)

> [!example]- Transcripción de la imagen
> "Address 0x4a47068 is 0 bytes after a block of size 40 alloc'd, at calloc, by main (bad_write.c:6)".

En el reporte completo, esa línea va precedida de *Invalid write of size 4* (en la lectura, *Invalid read of size 4*). Se lee así: *Invalid write of size 4* indica que se escribió un `int` donde no se debía. *0 bytes after a block of size 40* indica que se escribió justo al final del arreglo de 10 enteros pedido en la línea 6.

## Lectura inválida

```c
int* G = malloc(10 * sizeof(int));
for (int i = 0; i < 10; i += 1)
    G[i] = i * i + G[i - 1];          // con i = 0 se lee G[-1]
```

![Lectura inválida antes del bloque](adjuntos/Valgrind%20-%20lectura%20inv%C3%A1lida%20antes%20del%20bloque.png)

> [!example]- Transcripción de la imagen
> "Address 0x4a4703c is 4 bytes before a block of size 40 alloc'd, at malloc, by main (bad_read.c:6)".

> [!tip] Cómo leer cualquier reporte de memcheck
> 1. La primera línea dice **qué** pasó (*Invalid read/write of size N*, *Conditional jump… uninitialised*, *definitely lost*).
> 2. Las líneas `at …` / `by …` son el **stack trace**: la línea exacta y la cadena de llamadas que llevó a ella.
> 3. *Address … is N bytes before/after a block of size M* ubica el error **respecto del bloque pedido**: "after" suele ser un `<=` de más y "before", un índice `-1`.
> 4. Conviene corregir primero el **primer** error reportado: los siguientes suelen ser consecuencia de él.

## Preguntas de repaso

> [!question]- ¿Por qué Valgrind reporta el uso de un valor no inicializado en el `if` y no en el `malloc`?
> Porque pedir memoria sin inicializar no es un error en sí. El problema aparece cuando una decisión del programa depende de esa basura. `--track-origins=yes` permite volver hasta el `malloc` que la creó.

> [!question]- ¿Qué indica "0 bytes after a block of size 40"?
> Que el acceso inválido fue justo después del final de un bloque de 40 bytes, es decir, al elemento 11 de un arreglo de 10 `int`. Es el típico error de usar `<=` en vez de `<`.

> [!question]- ¿Por qué estos errores son más graves que un memory leak?
> Porque cambian el comportamiento del programa: deciden con basura o corrompen memoria vecina. Un leak solo desperdicia memoria sin cambiar los resultados.

> [!question]- Si Valgrind reporta 20 errores, ¿por cuál conviene partir?
> Por el primero. Un error de memoria temprano suele provocar los siguientes en cascada, y al corregirlo muchos de los demás desaparecen.
