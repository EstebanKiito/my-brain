---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, bd/edd, origen/apuntes]
prerrequisitos: ["[[02 - Disco duro y páginas|Disco duro y páginas]]"]
---
# Memoria RAM y punteros

La RAM es una gran matriz de bits a la que se accede por **direcciones**. Un **puntero** es una variable cuyo valor es la dirección de otra. Son la base de las estructuras de datos que usan los índices.

## Memoria RAM (mis apuntes)
- La memoria ram es una gran matriz donde se guardan 0 y 1 (Bits)
- Se pueden acceder a esos datos mediante direcciones
- Cada fila tiene una direccion unica

![Memoria RAM de 1 GB - direcciones](adjuntos/Memoria%20RAM%20de%201%20GB%20-%20direcciones.png)

> [!note]- Transcripción de la imagen
> **RAM de 1 GB**: una matriz de 32 columnas (bits) con direcciones 0, 4, 8, 12, 16, 20, 24, 28, …, 1073741816, 1073741820. Una fila es una **palabra de 32 bits o 4 bytes**; por ejemplo, la de la dirección 24 ocupa las direcciones 24, 25, 26 y 27. Cada bit solo puede valer 0 o 1.

## Puntero
- Es la variable cuyo valor es la DIRECCION de memoria de otra variable

![Puntero - celdas de memoria](adjuntos/Puntero%20-%20celdas%20de%20memoria.png)

> [!note]- Transcripción de la imagen
> Celdas de **Memoria** de un byte con sus direcciones en hexadecimal: 0x7a58f8 → 01111010, 0x7a58f9 → 11111011, 0x7a58fa → 00100110, 0x7a58fb → 11010011, 0x7a58fc → 00011101, 0x7a58fd → 11000011, 0x7a58fe → 01011000, 0x7a58ff → 00011101, 0x7a5900 → 11011000, 0x7a5901 → 11101001. Un puntero guarda un valor como `0x7a58f8` para apuntar a esa celda.

> [!tip] Complemento (curso de Estructuras de Datos, repasado en la clase 9)
> - Las direcciones avanzan de a 4 porque cada palabra mide 4 bytes y la memoria se direcciona **por byte**.
> - Con 32 bits de dirección se alcanzan $2^{32}$ bytes = 4 GB. Por eso hoy se usan direcciones de 64 bits.
> - En C: `int x = 5; int *p = &x;` — `p` guarda la dirección de `x`, y `*p` lee el valor 5.
> - En bases de datos, los "punteros" a disco son **identificadores de página** (y de posición dentro de la página), no direcciones de RAM. Un índice unclustered guarda ese tipo de puntero: ver [[12 - Índices clustered y unclustered|Índices clustered y unclustered]].

## Preguntas de repaso

1. ¿Cómo se accede a un dato en la RAM?
> [!question]- Respuesta
> Mediante su dirección: cada fila o celda de la memoria tiene una dirección única.

2. ¿Qué es un puntero?
> [!question]- Respuesta
> Una variable cuyo valor es la dirección de memoria de otra variable.

3. ¿Por qué en la imagen de la RAM las direcciones van de 4 en 4?
> [!question]- Respuesta
> Porque cada fila es una palabra de 32 bits = 4 bytes, y la memoria se direcciona por byte.
