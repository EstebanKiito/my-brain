---
ramo: "Programación en C"
tema: "Punteros, arreglos y strings"
tags:
  - c
  - punteros
  - memoria
  - hexadecimal
  - origen/complemento
prerrequisitos:
  - "[[04 - Funciones y stack de llamadas]]"
---

# Direcciones de memoria y punteros

C es de bajo nivel porque deja trabajar **directamente con direcciones de memoria**. Un **puntero** es una variable cuyo valor es la dirección de otra variable. Con punteros, una función puede modificar datos que no son suyos, se recorren arreglos y se construyen estructuras enlazadas como las listas ligadas.

## La memoria como tabla de direcciones

La RAM se puede pensar como una tabla gigante que asocia una **dirección** a cada **byte**. Las direcciones se escriben en **hexadecimal** (dígitos 0–9 y A–F), porque son números muy grandes y en base 16 quedan mucho más cortos.

![Base hexadecimal](adjuntos/Base%20hexadecimal.png)

> [!example]- Transcripción de la imagen
> "Base Hexadecimal. La base 16 usa los dígitos A, B, C, D, E y F para valores sobre 9." Desglose de `0xC2AF3B`: B×16⁰ = 11, 3×16¹ = 48, F×16² = 3840, A×16³ = 40960, 2×16⁴ = 131072 y C×16⁵ = 12582912. La suma es 12758843. "Es muy útil para representar números extremadamente grandes."

![Memoria como tabla de direcciones](adjuntos/Memoria%20como%20tabla%20de%20direcciones%20y%20bytes.png)

> [!example]- Transcripción de la imagen
> Columna "Memoria" con las direcciones `0x7a58f8` a `0x7a5901`, cada una apuntando a un byte (01111010, 11111011, 00100110, 11010011, 00011101, 11000011, 01011000, 00011101, 11011000, 11101001). Un `int` ocuparía los 4 primeros bytes y su dirección sería la del primero, `0x7a58f8`.

La dirección de una variable es la de **su primer byte**. Un `int` en `0x7a58f8` ocupa hasta `0x7a58fb`, y un `char` en `0x7a58fc` ocupa solo ese byte.

## Los operadores `&` y `*`

| Expresión | Significado |
|---|---|
| `&x` | Dirección de `x`. Se imprime con `%p`. |
| `int* p` | Declara `p` como **puntero a `int`**: guarda direcciones de `int`. |
| `*p` | **Desreferenciar**: el valor que está en la dirección guardada en `p`. |

```c
#include <stdio.h>

int main(void)
{
    int c = 12;
    int* d = &c;              // d guarda la dirección de c
    printf("%p = %p\n", (void*) d, (void*) &c);   // la misma dirección dos veces

    *d += 1;                  // modifica c a través de d
    printf("c = %d\n", c);    // 13

    int** e = &d;             // un puntero también es una variable: puntero a puntero
    printf("%d %d %d\n", c, *d, **e);   // 13 13 13

    int* nulo = NULL;         // no apunta a nada; vale 0, o sea, falso
    if (!nulo) printf("nulo no apunta a nada\n");
    return 0;
}
```

![Puntero a int en el stack](adjuntos/Puntero%20a%20int%20en%20el%20stack.png)

> [!example]- Transcripción de la imagen
> "type* - puntero a type". Código `int c = 12; int* d = &c; printf("%p = %p\n", d, &c);` y su salida `0x9b85f8 = 0x9b85f8`. En el stack de `main`, `c = 12` está en `0x9b85f8` y `d = 0x9b85f8` está en `0x9b85fc`: el valor de `d` es la dirección de `c`.

El **tipo** del puntero importa porque dice cómo interpretar lo que hay en la dirección (cuántos bytes leer y como qué). La dirección en sí siempre ocupa lo mismo: **8 bytes** en un sistema de 64 bits.

> [!warning] Desreferenciar `NULL` hace caer el programa
> `int* d = NULL; printf("%d", *d);` provoca un *segmentation fault*: la dirección 0 está protegida y leerla está prohibido. Antes de usar un puntero que puede ser `NULL`, hay que revisarlo con `if (p)`.

> [!tip] Dos usos del `*`
> En una **declaración** (`int* p`), `*` es parte del tipo. En una **expresión** (`*p = 3`), significa "lo que está en la dirección". `int* p`, `int *p` e `int * p` son la misma declaración.

## Preguntas de repaso

> [!question]- ¿Qué guarda exactamente una variable de tipo `int*`?
> Una dirección de memoria: la del primer byte de un `int`. No guarda el entero; para obtenerlo hay que desreferenciar con `*`.

> [!question]- Si `int g = 27; int* h = &g; int** i = &h;`, ¿qué valen `*h`, `**i` y `*i`?
> `*h` y `**i` valen 27. `*i` es el valor de `h`, es decir, la dirección de `g`.

> [!question]- ¿Por qué un puntero necesita tipo si todas las direcciones miden lo mismo?
> Porque el tipo dice cuántos bytes leer en esa dirección y cómo interpretarlos. También determina cuánto avanza la aritmética de punteros.

> [!question]- ¿Por qué `if (!p)` sirve para saber si un puntero es `NULL`?
> Porque `NULL` es la dirección 0, y en C el 0 es falso. `!p` es verdadero justamente cuando `p` no apunta a nada.
