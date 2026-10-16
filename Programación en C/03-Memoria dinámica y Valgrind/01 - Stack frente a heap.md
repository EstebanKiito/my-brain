---
ramo: "Programación en C"
tema: "Memoria dinámica y Valgrind"
tags:
  - c
  - memoria
  - stack
  - heap
  - origen/complemento
prerrequisitos:
  - "[[04 - Funciones y stack de llamadas]]"
  - "[[03 - Aritmética de punteros y arreglos]]"
---

# Stack frente a heap

Hasta aquí todas las variables vivían en el **stack**, que es rápido y se administra solo, pero tiene dos limitaciones. Su **tamaño es fijo**: un arreglo enorme o una recursión muy profunda lo desbordan (*stack overflow*). Y lo que una función guarda en él **muere al retornar**. El **heap** resuelve ambos problemas: es memoria que el programa le **pide explícitamente al sistema operativo**, que dura hasta que el programa la **libera**.

> [!info] Video
> El curso explica stack, heap y memoria dinámica en este [video](https://www.loom.com/share/936b6177d19847a6af0b1e18899a6c0a).

## El problema: retornar un arreglo local

```c
int* seq(int from, int count)
{
    int S[count];                       // S vive en el marco de seq (stack)
    for (int i = 0; i < count; i++) S[i] = from + i;
    return S;                           // ERROR: S se libera al retornar
}
```

El puntero retornado apunta a un marco del stack que ya se liberó y que la próxima llamada va a sobrescribir: es **comportamiento indefinido**. `gcc` incluso advierte *"address of stack memory associated with local variable 'S' returned"*. La regla es tajante: **una función nunca debe retornar un puntero a su propio stack**.

## El heap

El heap es una colección de **bloques** que el programa pide durante la ejecución. Cada bloque es contiguo por dentro, pero dos bloques pedidos en momentos distintos no tienen por qué estar juntos. El SO entrega cada bloque en exclusiva al programa, y el programa es responsable de devolverlo.

![Bloques del heap en la RAM](adjuntos/Bloques%20del%20heap%20en%20la%20RAM.png)

> [!example]- Transcripción de la imagen
> RAM dividida en dos zonas. Arriba, "programa": "tipos, funciones, STACK, etc.". Abajo, separado por "...", el "HEAP", con "Bloque 1", "...", "Bloque n" en lugares no consecutivos de la memoria.

Cuando se pide un arreglo al heap, en el stack queda solo **el puntero** a ese bloque:

![Arreglo en el heap apuntado desde el stack](adjuntos/Arreglo%20en%20el%20heap%20apuntado%20desde%20el%20stack.png)

> [!example]- Transcripción de la imagen
> En el STACK, el marco `(main)` tiene `A = 0x22d040` en la dirección `0x01fd2b`. En el HEAP, desde `0x22d040`, están los valores 1, 4, 3. Por eso `A` y `&A[0]` valen `0x22d040` (heap), mientras que `&A` vale `0x01fd2b` (stack).

| | Stack | Heap |
|---|---|---|
| Quién lo administra | El compilador, automáticamente | El programador (`malloc`/`calloc`/`free`) |
| Vida de los datos | Hasta que termina el bloque `{ }` o la función | Hasta que se llama a `free` |
| Tamaño | Fijo y pequeño (se puede desbordar) | Limitado por la RAM disponible |
| Velocidad | Muy rápido (mover el SP) | Más lento (hay que pedírselo al SO) |
| Uso típico | Variables chicas y temporales | Arreglos grandes, listas ligadas, structs que deben sobrevivir |

> [!tip] Criterio práctico
> En el stack van las variables pequeñas y de vida corta. Los arreglos de tamaño variable o grande, las listas ligadas y todo lo que deba sobrevivir a la función que lo crea va en el heap.

## Preguntas de repaso

> [!question]- ¿Por qué retornar la dirección de un arreglo local es un error aunque "a veces funcione"?
> Porque ese arreglo vive en el marco de la función, que queda libre al retornar. Si justo después nadie sobrescribe esa zona, los datos siguen ahí por casualidad. Cualquier llamada posterior los pisa, y el resultado es indefinido.

> [!question]- Si `int* A` apunta a un arreglo en el heap, ¿por qué `A` y `&A` imprimen direcciones distintas?
> `A` es el valor del puntero, es decir, la dirección del bloque en el heap. `&A` es la dirección de la variable puntero, que vive en el stack de `main`.

> [!question]- Nombra dos limitaciones del stack que el heap resuelve.
> El tamaño fijo del stack, que se desborda con datos grandes, y la vida corta de los datos, que mueren al terminar la función. El heap crece según lo que se pida y sus bloques duran hasta el `free`.

> [!question]- ¿Qué costo tiene usar el heap en vez del stack?
> Es más lento, porque hay que pedirle memoria al sistema operativo, y obliga a liberar manualmente cada bloque. Si no se libera, hay *memory leaks*.
