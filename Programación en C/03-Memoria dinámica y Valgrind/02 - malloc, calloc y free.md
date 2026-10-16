---
ramo: "Programación en C"
tema: "Memoria dinámica y Valgrind"
tags:
  - c
  - malloc
  - calloc
  - free
  - heap
  - origen/complemento
prerrequisitos:
  - "[[01 - Stack frente a heap]]"
---

# malloc, calloc y free

La biblioteca `<stdlib.h>` trae las tres funciones para usar el [[01 - Stack frente a heap|heap]]: dos para **pedir** bloques y una para **devolverlos**. Todo bloque pedido debe liberarse exactamente una vez.

| Función | Recibe | Contenido del bloque |
|---|---|---|
| `malloc(bytes)` | Cantidad de **bytes** | **Basura**: lo que haya quedado en esa memoria |
| `calloc(n, tamaño)` | Cantidad de **elementos** y tamaño de cada uno | **Todo en 0** (o `NULL` si son punteros) |
| `free(p)` | Un puntero retornado por `malloc`/`calloc` | El bloque vuelve a quedar disponible |

Las dos primeras retornan un **puntero al inicio del bloque**, o `NULL` si el SO no pudo entregarlo.

```c
#include <stdio.h>
#include <stdlib.h>

int* seq(int from, int count)          // ahora el arreglo sobrevive a la función
{
    int* S = calloc(count, sizeof(int));
    if (!S) return NULL;               // el SO puede negarse
    for (int i = 0; i < count; i++) S[i] = from + i;
    return S;                          // quien llama queda a cargo del free
}

int main(void)
{
    int* a = malloc(sizeof(int));      // 4 bytes con basura...
    *a = 5;                            // ...que se llenan de inmediato
    int* s = seq(7, 3);
    printf("%d | %d %d %d\n", *a, s[0], s[1], s[2]);   // 5 | 7 8 9
    free(s);
    free(a);
    return 0;
}
```

> [!tip] calloc para arreglos
> Conviene usar `calloc` para arreglos: parten en 0 y no hay riesgo de leer basura antes de llenarlos. Un hábito útil es escribir el `free` correspondiente apenas se escribe el `calloc`, o al menos un comentario `// LIBERAR`.

## Matrices en el heap: arreglo de punteros a filas

Para una matriz dinámica se pide primero un arreglo de **punteros a filas** (`int**`, con `sizeof(int*)`) y después cada fila por separado. Así las filas pueden tener **largos distintos**, algo imposible en una matriz del stack.

```c
int** A = calloc(2, sizeof(int*));   // 2 punteros, ambos NULL
A[0] = calloc(3, sizeof(int));       // fila 0: 3 enteros en 0
A[1] = calloc(2, sizeof(int));       // fila 1: 2 enteros en 0
A[0][0] = 2; A[0][1] = 27; A[0][2] = 5; A[1][0] = 6; A[1][1] = 3;
for (int i = 0; i < 2; i++) free(A[i]);   // primero cada fila...
free(A);                                  // ...después el arreglo de punteros
```

![Arreglo de punteros a filas](adjuntos/Matriz%20en%20el%20heap%20-%20arreglo%20de%20punteros%20a%20filas.png)

> [!example]- Transcripción de la imagen
> "Arreglos de Arreglos". Con `int** A = calloc(2, sizeof(int*));` resaltado, el stack de `(main)` tiene `A = 0x12fd14`. En el heap, desde `0x12fd14`, hay dos celdas `0x000000 (NULL)`.

![Primera fila](adjuntos/Matriz%20en%20el%20heap%20-%20primera%20fila.png)

> [!example]- Transcripción de la imagen
> Con `A[0] = calloc(3, sizeof(int));` resaltado, la celda `0x12fd14` ahora vale `0x12ff12`, y desde `0x12ff12` hay un bloque con 0, 0, 0. La segunda celda sigue en `0x000000`.

![Segunda celda aún en NULL](adjuntos/Matriz%20en%20el%20heap%20-%20segunda%20celda%20a%C3%BAn%20en%20NULL.png)

> [!example]- Transcripción de la imagen
> Al pasar a `A[1] = calloc(3, sizeof(int));`, la celda `0x12fd1c` (8 bytes después de `0x12fd14`, porque cada puntero ocupa 8) todavía vale `0x000000`.

![Segunda fila reservada](adjuntos/Matriz%20en%20el%20heap%20-%20segunda%20fila%20reservada.png)

> [!example]- Transcripción de la imagen
> Se ejecuta el `calloc` de la segunda fila: aparece un bloque nuevo en `0x105dc0` con 0, 0, 0, pero la celda `0x12fd1c` todavía no se actualiza.

![Puntero a la segunda fila](adjuntos/Matriz%20en%20el%20heap%20-%20puntero%20a%20la%20segunda%20fila.png)

> [!example]- Transcripción de la imagen
> Al terminar la asignación, la celda `0x12fd1c` vale `0x105dc0`: `A[1]` apunta a la segunda fila.

![Escritura del primer elemento](adjuntos/Matriz%20en%20el%20heap%20-%20escritura%20del%20primer%20elemento.png)

> [!example]- Transcripción de la imagen
> Con `A[0][0] = 2;` resaltado, las flechas muestran el camino: `A` (en el stack, `0x12fd14`) lleva a la celda `A[0]` del heap, que vale `0x12ff12`, y de ahí a `A[0][0]`, que ahora vale 2.

## El heap tampoco es infinito

```c
int* enorme = malloc((size_t) 1 << 62);
if (!enorme) printf("No hay un bloque de ese tamaño\n");
```

Cada bloque debe ser **contiguo**. Si no hay suficiente memoria libre seguida, `malloc`/`calloc` retornan `NULL`. Por eso, en programas serios, el resultado se revisa siempre antes de usarlo.

## Preguntas de repaso

> [!question]- ¿Qué diferencia práctica hay entre `malloc(3 * sizeof(int))` y `calloc(3, sizeof(int))`?
> Las dos piden 12 bytes, pero `calloc` los deja en 0 y `malloc` los deja con la basura que hubiera. Con `malloc` hay que inicializar antes de leer.

> [!question]- En una matriz `int**` del heap, ¿por qué hay que liberar las filas antes que el arreglo de punteros?
> Porque las direcciones de las filas están guardadas en ese arreglo. Si se libera primero, se pierden las direcciones (o se leen de memoria ya liberada) y las filas quedan como memory leaks.

> [!question]- ¿Por qué en el arreglo de punteros las celdas están separadas por 8 bytes?
> Porque cada celda guarda un `int*`, y un puntero ocupa 8 bytes en un sistema de 64 bits. Por eso se pide con `sizeof(int*)`.

> [!question]- ¿Cuándo retorna `NULL` un `malloc`?
> Cuando el sistema operativo no puede entregar un bloque contiguo del tamaño pedido, por falta de memoria o por fragmentación.
