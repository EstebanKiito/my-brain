---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/apuntes
prerrequisitos:
  - "[[05 - Segmentación de memoria y prevención de segmentation fault]]"
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
---

# Aritmética de bits y máscara de segmento en traducción de direcciones

A nivel de arquitectura de hardware, la extracción del identificador de segmento y del desplazamiento relativo no se realiza con lentas operaciones de división o resta decimal, sino mediante operaciones lógicas a nivel de bits sobre la palabra de dirección virtual.

## Descomposición binaria y máscaras (mis apuntes)

> [!note] Apuntes de clase
> **LOGICA DE BITS**
> Para hacer lo que hicimos con aritmetrica en decimales nuestros, podemos hacerlo con logica de BITS.
>
> - Los bits de segmento: Nos dice en que segmento nos encontramos.
> - Los bits de offset: Nos dice que tan desplazado estoy desde el INICIO del segmento.
>
> En este caso, tengo 12 bits para el offset, por lo tanto, lo maximo que me puedo desplazar es $2^{12}$ bytes.
> Si tengo 2 bits de segmento, puedo tener:
> - $2^2$ posibles segmentos: 4
>   - 00
>   - 01
>   - 10
>   - 11
>
> Notar que:
> - Bits de offset: 0000 0110 1000: 104
> - Y la direccion del segmento 1 aprox (heap): 4kb → 4096
> - 4096 + 104 = 4200 !!! → Magia? No → LOGICA!
> - Investigar → Mascara de segmento

> [!warning] Posible error
> En los apuntes aparece la errata tipográfica "aritmetrica" por aritmética.

![Descomposición de dirección virtual en bits de segmento y offset](adjuntos/Descomposici%C3%B3n%20de%20direcci%C3%B3n%20virtual%20en%20bits%20de%20segmento%20y%20offset.png)

> [!example]- Transcripción de la imagen
> Formato de dirección virtual de 14 bits:
> - **Bits 13-12 (2 bits más significativos):** Selector de segmento ($s$).
>   - `00`: Código
>   - `01`: Heap
>   - `10`: Stack
>   - `11`: Reservado / no asignado
> - **Bits 11-0 (12 bits menos significativos):** Desplazamiento u offset dentro del segmento ($d$), con capacidad de direccionamiento de hasta $2^{12} = 4096\text{ bytes} = 4\text{ KB}$.

![Aplicación de máscara binaria y desplazamiento a la derecha](adjuntos/Aplicaci%C3%B3n%20de%20m%C3%A1scara%20binaria%20y%20desplazamiento%20a%20la%20derecha.png)

> [!example]- Transcripción de la imagen
> Extracción del segmento mediante operaciones bit a bit en lenguaje C / Hardware:
> 1. Dirección virtual de ejemplo: `4200` en decimal = `0b01000001101000` (hexadecimal `0x1068`).
> 2. Se aplica la **Máscara de segmento** `0x3000` (`0b11000000000000`) con un operador bitwise AND (`&`):
>    $$\text{Segmento\_crudo} = 0\text{x}1068 \ \& \ 0\text{x}3000 = 0\text{b}01000000000000$$
> 3. Se desplaza a la derecha (*right shift*) en 12 posiciones (`>> 12`):
>    $$\text{Segmento} = \text{Segmento\_crudo} \gg 12 = 0\text{b}01 = 1 \text{ (Heap)}$$
> 4. Se extrae el offset con la **Máscara de offset** `0x0FFF` (`0b00111111111111`):
>    $$\text{Offset} = 0\text{x}1068 \ \& \ 0\text{x}0\text{FFF} = 0\text{b}000001101000 = 104\text{ decimal}$$

> [!tip] Complemento: Eficiencia de la lógica de bits en hardware
> Para la circuitería digital de la MMU, esta división no requiere siquiera ciclos de reloj de cómputo aritmético: basta con rutear físicamente los 2 cables de los pines superiores del registro de direcciones directamente a las líneas de decodificación de la tabla de segmentos, y los 12 cables inferiores al sumador de la base física.

## Preguntas de repaso

> [!question]- Si una arquitectura utiliza 3 bits para el número de segmento y 13 bits para el desplazamiento, ¿cuántos segmentos admite y cuál es el tamaño máximo de cada uno?
> Con 3 bits de segmento puede direccionar hasta $2^3 = 8$ segmentos independientes. Con 13 bits de offset, el tamaño máximo de cada segmento es de $2^{13} = 8192\text{ bytes} = 8\text{ KB}$.

> [!question]- ¿Qué operación lógica realiza la MMU para aislar el número de segmento a partir de una dirección virtual de 14 bits?
> Realiza un producto lógico bit a bit (*bitwise AND*) con la máscara `0x3000` (`11000000000000` en binario) para conservar únicamente los 2 bits más significativos, seguido de un desplazamiento hacia la derecha de 12 posiciones (`>> 12`).

> [!question]- ¿Cómo se obtiene el desplazamiento (*offset*) a partir del valor hexadecimal `0x1068` empleando una máscara binaria?
> Se aplica la operación `0x1068 & 0x0FFF`. Como `0x0FFF` contiene 1s en los 12 bits inferiores y 0s en los bits superiores, el resultado es `0x0068`, que corresponde exactamente a $104$ en decimal ($6 \times 16^1 + 8 \times 16^0 = 96 + 8 = 104$).

