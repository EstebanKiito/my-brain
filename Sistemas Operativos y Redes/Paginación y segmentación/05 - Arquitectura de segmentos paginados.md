---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/segmentacion
  - so/paginacion
  - origen/apuntes
prerrequisitos:
  - "[[05 - Segmentación de memoria y prevención de segmentation fault]]"
  - "[[04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna]]"
---

# Arquitectura de segmentos paginados

Los esquemas híbridos de segmentos paginados combinan las fortalezas de la segmentación (reflejar la estructura lógica del programa y delimitar rangos útiles) con las de la paginación (eliminar la fragmentación externa dividiendo cada segmento en páginas de tamaño uniforme).

## Combinación de segmentación y paginación (mis apuntes)

> [!note] Apuntes de clase
> **Segmentos Paginados:**
> Seg:
> - Limite y base de segmento
> - LA direccion virtual (primeros dos bits: Indican 4 segmentos posibles)
>
> Dentro de cada segmento → Paginas:
> - (VPN)
>
> La idea es: Cada SEGMENTO tiene su propia TABLA DE PAGINAS!
> Los segmentos en teoria, tienen un tamaño fijo a diferencia del heap, por lo tanto no va a usar todas las paginas que tiene asociada a el!!
>
> ESPACIO VIRUTAL: 16 PAGINAS
> - Un Proceso utiliza (EFECTIVAMENTE): 4 Paginas
> - 12 entradas vacias (75%) en tabla de paginas
>
> Con esto en la tabla de pagina, bastaría con poner menos (solo las utilizadas).
> Con eso → Reduzco la gran cantidad de Entradas en paginas.

> [!warning] Posible error
> En los apuntes figura la errata tipográfica "ESPACIO VIRUTAL" por Espacio Virtual.

![Esquema de segmentos paginados con tablas independientes](adjuntos/Esquema%20de%20segmentos%20paginados%20con%20tablas%20independientes.png)

> [!example]- Transcripción de la imagen
> Traducción en arquitectura de segmentos paginados:
> 1. Dirección virtual dividida en: Bits de Segmento ($s$), Número de Página dentro del segmento ($VPN_{\text{seg}}$) y Desplazamiento ($Offset$).
> 2. Los bits de segmento indexan la Tabla de Segmentos para obtener la Base y Límite de la tabla de páginas de ese segmento específico.
> 3. Se verifica que $VPN_{\text{seg}} < \text{Límite}(s)$.
> 4. Se suma $\text{Base}(s) + VPN_{\text{seg}} \times \text{sizeof(PTE)}$ para leer la PTE y obtener el marco físico PFN.
> 5. Dirección física = $\text{PFN} + Offset$.

![Reducción de entradas vacías en segmentos paginados](adjuntos/Reducción%20de%20entradas%20vacías%20en%20segmentos%20paginados.png)

> [!example]- Transcripción de la imagen
> Ahorro de memoria en espacio de direcciones disperso:
> - En una tabla lineal continua, si un proceso define 16 páginas pero solo utiliza efectivamente 4 (por ejemplo, 1 de código, 1 de heap, 2 de stack), las 12 páginas restantes (75%) ocupan entradas no asignadas nulas que consumen memoria RAM.
> - Al asignar una tabla de páginas independiente por segmento, el registro Límite de cada segmento restringe la tabla para que cubra únicamente las páginas que el proceso realmente ha reservado.

> [!tip] Complemento: Limitación de los segmentos paginados
> Aunque este esquema resuelve el desperdicio de páginas intermedias no utilizadas entre el Heap y el Stack, aún requiere que cada tabla de páginas de segmento resida en un bloque de memoria física contiguo. Si un segmento crece considerablemente, su tabla de páginas asociada puede volver a sufrir de fragmentación externa, lo que motivó el desarrollo de la paginación puramente multinivel.

## Preguntas de repaso

> [!question]- ¿Cómo se descompone una dirección virtual bajo un esquema de segmentos paginados?
> Se divide en tres campos:
> 1. Bits de segmento ($S$): identifican el segmento lógico (Código, Heap, Stack).
> 2. Número de página virtual ($VPN$): indexa la tabla de páginas privada de ese segmento.
> 3. Desplazamiento ($Offset$): byte específico dentro de la página y el marco físico.

> [!question]- ¿Qué rol cumple el registro límite en la tabla de segmentos cuando estos están paginados?
> En lugar de indicar el límite en bytes, el registro límite indica la cantidad de páginas válidas que posee la tabla de páginas de ese segmento, evitando asignar entradas para páginas que no están en uso.

> [!question]- ¿Por qué un esquema de segmentos paginados reduce el espacio consumido por tablas de páginas frente a una tabla lineal?
> Porque los rangos vacíos no mapeados (como el espacio no utilizado entre el Heap y el Stack) no requieren entradas en la tabla de páginas. Solo los segmentos activos mantienen tablas asignadas proporcionales a su tamaño efectivo.
