---
ramo: "Programación en C"
tema: "Memoria dinámica y Valgrind"
tags:
  - c
  - memoria
  - memory-leak
  - segmentation-fault
  - origen/complemento
prerrequisitos:
  - "[[02 - malloc, calloc y free]]"
---

# Errores de memoria y memory leaks

Al manejar la memoria a mano, C no protege de los errores: no hay excepciones como `IndexError`, y muchos errores **no hacen caer el programa**, sino que producen resultados erróneos que aparecen lejos de la causa. Reconocer los cinco tipos clásicos es el primer paso para encontrarlos.

## Los cinco errores clásicos

**1. Acceso a memoria liberada** (*use after free*). Después del `free`, el puntero sigue guardando la dirección, pero ese bloque ya puede estar asignado a otra parte del programa.

```c
int* a = malloc(sizeof(int));
*a = 5;
free(a);
int b = 2 + *a;          // lee memoria que ya no es nuestra
```

**2. Acceso fuera del bloque.** Leer o escribir más allá de lo pedido: no siempre se cae, pero entrega o corrompe datos.

```c
int* a = malloc(2 * sizeof(int));
a[0] = 3; a[1] = 2;
int b = 2 + a[3];        // a[3] no pertenece al bloque
```

**3. Doble liberación.** Llamar dos veces a `free` sobre el mismo puntero corrompe las estructuras internas del administrador de memoria. Además, hay ataques que aprovechan este error.

```c
free(a);
free(a);                 // el bloque ya estaba libre
```

**4. Memoria no inicializada.** `malloc` entrega basura. Usarla sin asignarle un valor da resultados distintos en cada ejecución.

```c
int* a = malloc(sizeof(int));
int b = 2 + *a;          // *a nunca se inicializó
```

**5. Memory leak.** Se pierde la última referencia a un bloque sin haberlo liberado. Nadie puede usarlo ni devolverlo, y el bloque queda marcado como ocupado mientras el programa siga corriendo.

```c
int** A = calloc(2, sizeof(int*));
A[0] = calloc(3, sizeof(int));
A[1] = calloc(3, sizeof(int));
// ... se usa A ...
// faltan free(A[0]), free(A[1]) y free(A)
```

> [!warning] Por qué los leaks importan aunque el programa "funcione"
> Un leak no cambia el resultado, pero un programa que corre mucho tiempo o que pierde memoria dentro de un ciclo puede agotar la RAM disponible. En el curso, además, algunas tareas tienen límite de memoria o dan bonificación por no tener leaks.

## Cómo se manifiestan

| Síntoma | Causa típica |
|---|---|
| *Segmentation fault* | Desreferenciar `NULL`, usar memoria liberada, escribir en un literal (`char* s = "hola"; s[0] = 'H';`), un índice muy fuera de rango |
| *Stack overflow* | Recursión infinita o muy profunda, o arreglos enormes en el stack (`double x[1048576];`) |
| *Stack smashing detected* | Escribir fuera de un arreglo del stack |
| Resultados que cambian entre ejecuciones | Memoria no inicializada o lectura fuera de rango |
| El programa "funciona" pero usa cada vez más RAM | Memory leaks |

Un *segmentation fault* solo dice que el programa entró en un segmento de memoria que no le correspondía, no dónde ni por qué. Para encontrar la causa se usa [[04 - Valgrind y detección de memory leaks|Valgrind]].

> [!tip] Reglas que previenen casi todo
> Inicializar todo lo que se pide (o usar `calloc`), revisar que `malloc` no haya retornado `NULL`, hacer exactamente un `free` por cada `malloc`/`calloc` y, después del `free`, asignar `p = NULL;` para que un uso accidental falle de inmediato en vez de leer basura.

## Preguntas de repaso

> [!question]- ¿Por qué un *use after free* puede no hacer caer el programa?
> Porque `free` no borra el bloque ni invalida el puntero: solo lo marca como disponible. Leerlo suele "funcionar" y entregar el valor viejo o lo que otra parte escribió después. El error queda oculto.

> [!question]- ¿Qué diferencia a un memory leak de los otros cuatro errores?
> No corrompe datos ni cambia el resultado del programa: solo desperdicia memoria. Los otros cuatro afectan el comportamiento y pueden provocar resultados erróneos o caídas.

> [!question]- ¿Qué gana un programa al asignar `p = NULL` justo después de `free(p)`?
> Si después se usa `p` por error, desreferenciar `NULL` provoca un fallo inmediato y fácil de detectar, en vez de leer silenciosamente memoria liberada. Además, `free(NULL)` no hace nada, así que se evita la doble liberación.

> [!question]- ¿Qué error de memoria provoca `double x[1048576];` dentro de una función?
> Un *stack overflow*: son 8 MB en el stack, que normalmente es más pequeño. Un arreglo así debe pedirse al heap con `malloc` o `calloc`.
