# Dudas y posibles errores en los apuntes originales — Programación en C (material de IIC2133)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido y las discrepancias entre apuntes, material de clase y conocimiento general (la nota sigue al material de clase).

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Fundamentos del lenguaje
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Control de flujo y valores de verdad en C\|Control de flujo y valores de verdad en C]] | CheatSheet: "`<stdbool.h>` hace `typedef int bool`" | Desde C99, `bool` es una macro de `_Bool`, un tipo entero que solo guarda 0 o 1 (`(bool) 17` vale 1, mientras que `(int) 17` vale 17). La nota dice solo que `true` y `false` son 1 y 0. |
| ℹ️ | [[02 - Tipos de datos, printf y casting\|Tipos de datos, printf y casting]] | CheatSheet: `char var[] = '100'; int number = atof(var);` | Las comillas simples son para un solo `char`, así que el string es `"100"`. Además, `atof` retorna `double`, y guardarlo en un `int` trunca el valor. La nota usa la forma correcta. |

## Punteros, arreglos y strings
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Aritmética de punteros y arreglos\|Aritmética de punteros y arreglos]] | Cápsulas: `int* n = &l; *(n+1)` da el valor de la variable siguiente (13) | Funciona solo porque ese compilador dejó las variables contiguas. Hacer aritmética fuera de un arreglo es comportamiento indefinido. La nota lo presenta como advertencia, no como técnica. |
| ℹ️ | [[03 - Aritmética de punteros y arreglos\|Aritmética de punteros y arreglos]] | CheatSheet: `int A[3] = {1, -2, 3}; multiply_by(A, 5, 3);` | El arreglo tiene 3 elementos, pero se le pasa largo 5, así que escribe fuera del arreglo. La nota usa un arreglo de 5. |
| ℹ️ | [[03 - Aritmética de punteros y arreglos\|Aritmética de punteros y arreglos]] | "un arreglo no es nada más que un puntero" | Un arreglo **decae** a puntero en casi todas las expresiones, pero no es un puntero: `sizeof(A)` da el tamaño completo (24 bytes en `int A[6]`, verificado) y `&A` tiene otro tipo, aunque la misma dirección. La nota lo matiza. |

## Memoria dinámica y Valgrind
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Errores de memoria y memory leaks\|Errores de memoria y memory leaks]] | Cápsulas y CheatSheet: la memoria con leak "sigue marcada como ocupada" al terminar el programa y el SO "se puede demorar mucho en recuperarla" | En un SO moderno, toda la memoria de un proceso se recupera al terminar. El daño real de un leak ocurre **mientras** el programa corre (programas largos o leaks dentro de ciclos). La nota lo plantea así. |
| ℹ️ | [[02 - malloc, calloc y free\|malloc, calloc y free]] | Taller: "malloc… Aquí solo tiene nulls" y "Calloc me devuelve lo que ya había en el espacio" | Está al revés: `malloc` deja la basura que hubiera y `calloc` inicializa en 0. La nota usa la versión correcta, que coincide con las cápsulas y el CheatSheet. |
| ℹ️ | [[04 - Valgrind y detección de memory leaks\|Valgrind y detección de memory leaks]] | Captura del curso tras agregar `free(B)`: "total heap usage: 11 allocs, 0 frees" | Con el `free(B)` debería decir 1 free. Probablemente se reutilizó el encabezado de la captura anterior. La transcripción describe solo las líneas relevantes. |

## Structs
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Structs como objetos y tipos compuestos\|Structs como objetos y tipos compuestos]] | Cápsulas y CheatSheet: `List* list_append(List* list);` | Sin un parámetro con el valor a agregar, la función no sabe qué insertar. La nota usa `list_append(List* list, int value)`. |
| ℹ️ | [[03 - Structs anidados y structs recursivos\|Structs anidados y structs recursivos]] | Cápsulas: "No se puede usar typedef recursivo" | Lo que no se puede es usar el **alias** dentro de su propia definición (`Dog*` antes de que exista). `typedef struct dog { struct dog* friend; } Dog;` sí compila. La nota explica las dos salidas. |

## Módulos, compilación y depuración
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[02 - Compilación separada, enlazado y pragma once\|Compilación separada, enlazado y pragma once]] | CheatSheet: el ejemplo `reptil.c` termina con `void foo(...) {...};` y lleva `#pragma once` | `#pragma once` va en el `.h`, no en el `.c` (el `.c` no se incluye). La nota lo muestra en el header. |
| ℹ️ | (ramo completo) | CheatSheet: 5 imágenes (memoria, structs, módulos) | No vienen en el export de Notion porque enlazan a otra página. Las figuras equivalentes de las cápsulas sí están en las notas. |
