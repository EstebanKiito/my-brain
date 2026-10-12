---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/complemento]
prerrequisitos: ["[[01 - Qué es un sistema operativo|Qué es un sistema operativo]]", "[[02 - Modos de operación y anillos de protección|Modos de operación y anillos de protección]]"]
---
# Concepto de proceso y espacio de memoria

Un archivo ejecutable en disco no hace nada por sí solo. Cuando el sistema operativo lo carga y le asigna recursos, se convierte en un **proceso**, que es la unidad que el SO planifica, protege y administra. Entender cómo se organiza su memoria explica después fenómenos como el *stack overflow*, las fugas de memoria o el *segmentation fault*.

## Proceso = código + recursos

> [!tip] Definición
> Un **proceso** es un **programa en ejecución**: $\text{Proceso} = \text{Código (programa)} + \text{Recursos}$.

Los recursos son memoria y archivos, además de sockets, dispositivos de I/O y bibliotecas. La diferencia con un programa es que el **programa** es pasivo, un archivo en disco como `/bin/ls`, mientras que el **proceso** es activo: tiene un *program counter* (PC), registros y un espacio de memoria propio. Dos terminales corriendo `bash` son dos procesos distintos del mismo programa: pueden compartir el código (`.text`, de solo lectura), pero cada uno tiene sus propias copias de datos, heap y stack, aisladas del otro.

La **multiprogramación** permite mantener múltiples procesos en memoria, y los *schedulers* deciden en qué orden la CPU los atiende. Aun así, **en un mismo instante un núcleo atiende un solo proceso** (ver [[07 - Multitasking y fundamentos de multiprocesamiento|multitasking]]).

## Las cuatro zonas de la memoria de un proceso

| Zona | Qué guarda | Cuándo se define su tamaño |
|---|---|---|
| **Código** (`.text`) | Las instrucciones del programa; información estática | Al compilar |
| **Datos** (`.data`) | Variables globales | Al compilar |
| **Heap** | Memoria dinámica, pedida durante la ejecución (`malloc`, `free`) | Crece y decrece en ejecución |
| **Stack** | Un *call frame* por cada llamada a función activa | Crece y decrece en ejecución |

Cada elemento del **stack** representa un llamado a función (*call frame*) y contiene:

- los **parámetros** de la función;
- sus **variables locales**;
- el **lugar de retorno**, es decir, dónde estaba la ejecución antes de la llamada (el PC al que se vuelve);
- el **stack base pointer** (SBP), que marca el punto de inicio del stack;
- el **stack pointer** (SP), límite inferior del stack, desde donde se sacan y ponen direcciones.

Heap y stack quedan en extremos opuestos con espacio libre entre ellos, y crecen uno hacia el otro: así cualquiera de los dos puede usar el espacio sin que haya que fijar de antemano cuánto le toca a cada uno.

```c
#include <stdio.h>
#include <stdlib.h>

int limite = 10;                          /* .data: variable global */

int suma(int a, int b) {                  /* .text: código */
    int r = a + b;                        /* stack: local en el frame de suma */
    return r;
}

int main(void) {
    int *v = malloc(100 * sizeof(int));   /* heap: memoria dinámica */
    v[0] = suma(limite, 5);               /* nuevo frame: a, b, r y dirección de retorno */
    printf("%d\n", v[0]);
    free(v);
    return 0;
}
```

![Espacio de memoria de un proceso](adjuntos/Espacio%20de%20memoria%20de%20un%20proceso.png)

> [!example]- Transcripción de la imagen
> "Memoria proceso 1", desde 0x000 hasta 0x400:
> - **Program (.text)** de 0x000 a 0x080, con un `int main(...){ for (int i;...) ... return 0; }`. El **PC** apunta dentro de esta zona.
> - **.data** de 0x080 a 0x110, con `int m[100];`.
> - **heap** desde 0x110, con `brk()`, `malloc()`, `mmap()`, `free()`, `new()`. Su tope lo marca **brk**.
> - Espacio libre gris, con una flecha hacia arriba (crece el heap) y otra hacia abajo (crece el stack).
> - **stack** de 0x300 a 0x400, con "function calls, args, return addr". El **SP** apunta a 0x300 y el **SBP** a 0x400.
>
> A la derecha, la memoria física completa: el **Sistema Operativo** ocupa la parte baja (0x000-0x300), el **proceso 1** va de 0x300 a 0x700, y más arriba están el **proceso 2** y el **proceso 3**, separados por espacios libres.

## Preguntas de repaso

> [!question]- ¿Qué diferencia a un programa de un proceso?
> El programa es un archivo pasivo en disco. El proceso es ese programa en ejecución: tiene PC, registros, memoria propia y recursos asignados. Un mismo programa puede dar origen a varios procesos.

> [!question]- ¿Qué contiene un *call frame* y cuándo se crea?
> Se crea en el stack en cada llamada a función. Contiene los parámetros, las variables locales y la dirección de retorno, y se delimita con el SBP y el SP. Desaparece cuando la función retorna.

> [!question]- ¿Por qué el heap y el stack crecen en sentidos opuestos?
> Porque así comparten el mismo espacio libre central sin fijar de antemano cuánto le corresponde a cada uno. Solo hay problema si llegan a encontrarse.

> [!question]- ¿En qué zona queda cada elemento de `int *v = malloc(40);` dentro de una función?
> El puntero `v` es una variable local y vive en el stack. Los 40 bytes reservados viven en el heap y persisten hasta que se llame a `free`.
