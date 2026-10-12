---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/complemento
prerrequisitos:
  - "[[05 - Segmentación de memoria y prevención de segmentation fault]]"
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
---

# Aritmética de bits y máscara de segmento en traducción de direcciones

En [[05 - Segmentación de memoria y prevención de segmentation fault|segmentación]] se obtuvo el offset restando la dirección virtual de inicio del segmento. Funciona, pero la MMU traduce en **cada** acceso a memoria y necesita algo más rápido. La lógica de bits da la respuesta: si la dirección virtual se arma de la forma adecuada, el segmento y el offset ya están escritos en ella y basta con separarlos.

## Bits de segmento y bits de offset

Lo que se hizo con aritmética decimal se puede hacer con **lógica de bits**. La dirección virtual se divide en dos partes:

- **Bits de segmento** (los más significativos): dicen **en qué segmento** estamos.
- **Bits de offset** (el resto): dicen **qué tan desplazado** se está desde el **inicio** del segmento.

¿Cuántos bits hacen falta para identificar 3 segmentos (código, heap, stack)? **2**, porque con 2 bits hay $2^2 = 4$ combinaciones: `00`, `01`, `10`, `11`. En el ejemplo, la dirección virtual tiene 14 bits (16 KB): 2 de segmento y **12 de offset**, así que lo máximo que uno se puede desplazar dentro de un segmento es $2^{12} = 4096$ bytes (4 KB).

![Descomposición de dirección virtual en bits de segmento y offset](adjuntos/Descomposici%C3%B3n%20de%20direcci%C3%B3n%20virtual%20en%20bits%20de%20segmento%20y%20offset.png)

> [!example]- Transcripción de la imagen
> "¿Cómo conocer segmento y offset? Se pueden hacer restas… pero la lógica de bit es más rápida. Ejemplo: ¿cuántos bit necesitamos para identificar 3 segmentos? → 2". Una dirección de 14 bits (13 a 0) con el valor `0 1 | 0 0 0 0 0 1 1 0 1 0 0 0`: los bits 13-12 marcados *Segment* y los bits 11-0 *Offset*. "Dirección virtual: 4200 = 0b01000001101000 = 0x1068. Bits de segmento: 0b01 = 1 = 0x1. Bits de offset: 0b000001101000 = 104 = 0x068".

![Aplicación de máscara binaria y desplazamiento a la derecha](adjuntos/Aplicaci%C3%B3n%20de%20m%C3%A1scara%20binaria%20y%20desplazamiento%20a%20la%20derecha.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano sobre el espacio "Virtual" de 16 KB: el 100 en *Program Code* y el 4200 en *Heap*. Llaves rojas dividen el espacio en cuatro franjas de 4 KB, numeradas **0** (0-4 KB, código), **1** (4-8 KB, heap), **2** (8-12 KB, libre) y **3** (12-16 KB, la parte de abajo, donde está el stack).

Y aquí está la "magia": los bits de offset `0000 0110 1000` valen **104**, y el segmento 1 (heap) empieza en 4 KB = **4096**. $4096 + 104 = 4200$. No es magia, es lógica: los 2 bits altos valen exactamente "qué bloque de 4 KB", y los 12 bajos "cuánto dentro del bloque".

## Máscaras

Para extraer cada parte se usa una **máscara**, que se aplica a la dirección original con un AND bit a bit. La máscara tiene **1 en las posiciones que interesan y 0 en las demás**.

| Paso | Operación | Resultado con 4200 = `0b01000001101000` |
|---|---|---|
| Máscara de segmento | `v & 0x3000` (`0b11000000000000`) | `0b01000000000000` |
| Desplazar a la derecha 12 (el tamaño del offset) | `>> 12` | `0b01` = **1**, el heap |
| Máscara de offset (complementaria) | `v & 0xFFF` (`0b00111111111111`) | `0b00000001101000` = **104** |

Con el segmento se busca la base física en la tabla de segmentos y se le suma el offset.

```c
#include <stdio.h>

#define SEG_MASK    0x3000      /* 0b11 0000 0000 0000: los 2 bits de segmento */
#define SEG_SHIFT   12          /* el offset ocupa 12 bits */
#define OFFSET_MASK 0x0FFF      /* 0b00 1111 1111 1111: los 12 bits de offset */

int main(void) {
    unsigned int virtuales[] = { 100, 4200, 15000 };
    for (int k = 0; k < 3; k++) {
        unsigned int v = virtuales[k];
        unsigned int segmento = (v & SEG_MASK) >> SEG_SHIFT;
        unsigned int offset   =  v & OFFSET_MASK;
        printf("virtual %5u = 0x%04X -> segmento %u, offset %u\n", v, v, segmento, offset);
    }
    return 0;   /* 100 -> seg 0, off 100 · 4200 -> seg 1, off 104 · 15000 -> seg 3, off 2712 */
}
```

> [!tip] Por qué es más rápido
> Un AND y un desplazamiento son operaciones elementales. En hardware ni siquiera hace falta calcular: los 2 bits altos se conectan directamente a la selección de la entrada de la tabla de segmentos, y los 12 bajos al sumador con la base.

## Preguntas de repaso

> [!question]- ¿Cuántos bits de segmento se necesitan para 3 segmentos y cuántos segmentos permiten?
> 2 bits, que permiten $2^2 = 4$ segmentos (`00`, `01`, `10`, `11`). Con 1 bit solo habría 2.

> [!question]- Con 12 bits de offset, ¿cuál es el tamaño máximo de un segmento?
> $2^{12} = 4096$ bytes, es decir, 4 KB.

> [!question]- Obtén segmento y offset de la dirección virtual 4200 con máscaras.
> $4200 = $ `0x1068`. Segmento: `(0x1068 & 0x3000) >> 12 = 1` (heap). Offset: `0x1068 & 0xFFF = 0x068 = 104`.

> [!question]- Si una arquitectura usa 3 bits de segmento y 13 de offset, ¿cuántos segmentos admite y de qué tamaño máximo?
> $2^3 = 8$ segmentos de hasta $2^{13} = 8192$ bytes (8 KB) cada uno.
