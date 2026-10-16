---
ramo: "Programación en C"
tema: "Módulos, compilación y depuración"
tags:
  - c
  - compilacion
  - linker
  - pragma-once
  - origen/complemento
prerrequisitos:
  - "[[01 - Archivos de cabecera, include y static]]"
---

# Compilación separada, enlazado y pragma once

Con varios módulos, compilar todo de una vez funciona, pero obliga a recompilar **todos** los `.c` aunque solo haya cambiado uno. Si un módulo es grande, se pierde mucho tiempo. La solución es separar la compilación en dos etapas: **compilar** cada `.c` por separado a un archivo objeto `.o` y después **enlazar** los `.o` en el ejecutable.

## De un paso a dos etapas

![Compilación de todo en un solo paso](adjuntos/Compilaci%C3%B3n%20de%20todo%20en%20un%20solo%20paso.png)

> [!example]- Transcripción de la imagen
> `modulo.h` se incluye en `modulo.c` y en `main.c`, y los dos `.c` entran juntos a `gcc -o`, que produce el ejecutable `main`. Comando: `gcc modulo.c main.c -o main`.

![Compilación separada a archivos objeto](adjuntos/Compilaci%C3%B3n%20separada%20a%20archivos%20objeto.png)

> [!example]- Transcripción de la imagen
> `modulo.c` y `main.c` pasan por `gcc -c` ("compiler") y producen `modulo.o` y `main.o`, archivos con código de máquina (1010 0101 1001). Comandos: `gcc modulo.c -c -o modulo.o` y `gcc main.c -c -o main.o`.

![Enlazado de archivos objeto](adjuntos/Enlazado%20de%20archivos%20objeto.png)

> [!example]- Transcripción de la imagen
> Solo `main.c` pasa de nuevo por `gcc -c` (compiler) para generar `main.o`. Después, `modulo.o` (que ya existía) y `main.o` entran a `gcc -o` ("linker") y producen `main`. Comandos: `gcc main.c -c -o main.o` y `gcc modulo.o main.o -o main`.

| Etapa | Comando | Entrada → salida | Qué revisa |
|---|---|---|---|
| **Compilar** | `gcc x.c -c -o x.o` | Un `.c` (con sus `#include`) → código de máquina `.o` | Sintaxis y tipos de ese archivo |
| **Enlazar** (*link*) | `gcc a.o b.o -o main` | Todos los `.o` → ejecutable | Que cada función usada esté definida exactamente una vez |

Si se modifica solo `main.c`, basta con recompilar `main.o` y volver a enlazar: `modulo.o` se reutiliza. Por eso los errores de "función no definida" o "definida dos veces" aparecen al **enlazar** y no al compilar.

## El problema de los includes repetidos

Los headers se incluyen unos a otros. En el ejemplo de los reptiles, `frog.h`, `snake.h` y `turtle.h` incluyen `reptil.h`, y `main.c` incluye a los tres:

![Inclusión repetida de reptil.h](adjuntos/Inclusi%C3%B3n%20repetida%20de%20reptil.h.png)

> [!example]- Transcripción de la imagen
> `reptil.h` se incluye en `reptil.c`, `frog.h`, `snake.h` y `turtle.h`. Cada header de animal se incluye en su `.c` y en `main.c`. Pregunta: "¿Cuántas veces se incluye reptil.h?" y la respuesta "¡7!", junto a un emoji asustado.

Como `#include` copia texto, `main.c` termina con **tres copias** de `reptil.h`, y si este define un `typedef struct`, el compilador reclama *redefinition*. Peor aún son los ciclos:

![Inclusión circular de headers](adjuntos/Inclusi%C3%B3n%20circular%20de%20headers.png)

> [!example]- Transcripción de la imagen
> `snake.h` incluye `fly.h`, `fly.h` incluye `frog.h` y `frog.h` incluye `snake.h`, formando un ciclo. `fly.h` además se incluye en `main.c`. Pregunta: "¿Cuántas veces se incluye snake.h?" y la respuesta "∞".

## La solución: `#pragma once`

> [!tip] Regla
> Todo header empieza con `#pragma once`, que le indica al preprocesador: "incluye este archivo **una sola vez** por cada `.c`, aunque aparezca en muchos `#include`". Eso resuelve tanto las copias repetidas como los ciclos.

```c
// contador.h
#pragma once

typedef struct contador { int valor; int pasos; } Contador;
Contador* contador_init(int inicio);
```

Sin esa línea, un `main.c` que incluye `contador.h` y `reporte.h` (que a su vez incluye `contador.h`) falla con *redefinition of 'contador'*. Con ella, compila. La alternativa clásica, equivalente, son los *include guards*: `#ifndef CONTADOR_H` / `#define CONTADOR_H` / … / `#endif`.

## Compilar todo a mano no escala

![Compilación manual de todos los módulos](adjuntos/Compilaci%C3%B3n%20manual%20de%20todos%20los%20m%C3%B3dulos.png)

> [!example]- Transcripción de la imagen
> Todos los archivos del ejemplo de reptiles marcados con un check. Los comandos: `gcc reptil.c -c -o reptil.o`, `gcc frog.c -c -o frog.o`, `gcc snake.c -c -o snake.o`, `gcc turtle.c -c -o turtle.o`, `gcc main.c -c -o main.o` y `gcc reptil.o frog.o snake.o turtle.o main.o -o main`, junto a un emoji agobiado.

Con cinco módulos ya son seis comandos, y además hay que recordar cuáles `.o` quedaron desactualizados después de cada cambio. Para eso existe [[03 - Make y Makefile|Make]].

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene compilar cada `.c` a un `.o` por separado?
> Que al modificar un archivo solo se recompila su `.o` y se vuelve a enlazar. Los demás `.o` se reutilizan, lo que ahorra mucho tiempo en proyectos grandes.

> [!question]- ¿En qué etapa aparece un error de "undefined symbol" y por qué?
> Al enlazar. El compilador acepta una llamada a una función solo con ver su declaración. Es el enlazador el que busca la definición en los `.o` y falla si no la encuentra.

> [!question]- ¿Por qué incluir dos veces un header con un `typedef struct` provoca error?
> Porque `#include` copia el texto, así que el mismo struct quedaría definido dos veces en el mismo `.c`. Las definiciones de tipos no se pueden repetir.

> [!question]- ¿Qué resuelve `#pragma once`?
> Que cada header se incluya una sola vez por archivo `.c`. Elimina las redefiniciones por inclusiones repetidas y corta los ciclos de inclusión infinita.
