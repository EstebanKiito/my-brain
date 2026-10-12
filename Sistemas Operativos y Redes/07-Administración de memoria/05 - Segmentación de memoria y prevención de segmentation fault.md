---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/apuntes
prerrequisitos:
  - "[[04 - Swapping, fragmentación externa y algoritmos de asignación libre]]"
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
---

# Segmentación de memoria y prevención de segmentation fault

La segmentación es un esquema de administración de memoria que divide el espacio de direcciones lógico de un proceso en bloques de tamaño variable llamados segmentos (código, datos, heap, stack), permitiendo ubicarlos de manera independiente y dispersa en la memoria física.

## Segmentación lógica y tabla de segmentos (mis apuntes)

> [!note] Apuntes de clase
> **ESTRATEGIAS → ELIMINAR POR COMPLETO PROBLEMA DE FRAGMENTACION**
> - SEGMENTACION →
> Ya mencionamos que a ciertas partes del codigo le damos interpretaciones:
> La idea es ya no guardar todo el bloque de codigo unico de un programa dentro de la memoria fisica → si no que guardar segmentos de manera INDEPENDIENTE.
> → al ser mas pequeños, mas probabilidad que caigan en un lugar mas pequeño.
>
> Para ello, la MMU debe ser capaz de TRADUCIR.
>
> **PROBLEMA → SEGMENTION FAULT**
> En este caso claro, la direccion virtual del heap por ej buscamos en 4.2kb, eso si se lo sumamos a la base de la direccion fisica, ira a buscar memoria que no pertenece al programa → SEGMENTION FAULT.
>
> **SOL:**
> - La manera mas simple de corregir esto, es teniendo la direccion virtual de donde empieza el heap, restarle la direccion (offset: 4200), y esto nos da el desplazamiento (virtual)
> - Este mismo, se le suma a la direccion del Heap (de nuestro programa en la memoria real), y asi no nos salimos.

> [!warning] Posible error
> En los apuntes figura repetida la errata tipográfica "SEGMENTION FAULT" en lugar del término formal *Segmentation Fault* (`SIGSEGV`).

![Partición del espacio de direcciones en segmentos independientes](adjuntos/Partici%C3%B3n%20del%20espacio%20de%20direcciones%20en%20segmentos%20independientes.png)

> [!example]- Transcripción de la imagen
> División lógica del espacio de direcciones en tres segmentos principales:
> - **Segmento 0 (Code):** Código del programa (instrucciones legibles y ejecutables, típicamente de solo lectura).
> - **Segmento 1 (Heap):** Memoria asignada dinámicamente que crece hacia direcciones crecientes.
> - **Segmento 2 (Stack):** Pila de llamadas y variables locales que crece en sentido decreciente.
> Cada segmento se aloja en una región contigua separada dentro de la RAM.

![Traducción con tabla de segmentos y MMU](adjuntos/Traducci%C3%B3n%20con%20tabla%20de%20segmentos%20y%20MMU.png)

> [!example]- Transcripción de la imagen
> Mecanismo de traducción con Tabla de Segmentos:
> - La dirección virtual especifica un número de segmento ($s$) y un desplazamiento u offset ($d$).
> - La MMU consulta la fila $s$ en la **Tabla de Segmentos** (*Segment Table*), obteniendo el par `[Base, Límite]`.
> - Dirección física = $\text{Base}(s) + d$.

![Verificación de límites en tabla de segmentos](adjuntos/Verificaci%C3%B3n%20de%20l%C3%ADmites%20en%20tabla%20de%20segmentos.png)

> [!example]- Transcripción de la imagen
> Validación de seguridad en la MMU:
> - Antes de calcular la dirección física, el hardware compara si $d < \text{Límite}(s)$.
> - Si $d \ge \text{Límite}(s)$, el acceso es ilegal y se dispara una trampa (*Trap*) al sistema operativo, abortando la instrucción.

![Causa de segmentation fault por desborde de segmento](adjuntos/Causa%20de%20segmentation%20fault%20por%20desborde%20de%20segmento.png)

> [!example]- Transcripción de la imagen
> Ejemplo de error de acceso en el Heap:
> - Si el proceso intenta leer en la dirección virtual 4200 (que corresponde al Heap, iniciado en 4096), y sumara 4200 directamente a la base física del Heap, se desviaría completamente fuera del segmento asignado invadiendo memoria ajena.

![Cálculo de desplazamiento relativo virtual en el heap](adjuntos/C%C3%A1lculo%20de%20desplazamiento%20relativo%20virtual%20en%20el%20heap.png)

> [!example]- Transcripción de la imagen
> Solución mediante resta de la base virtual:
> - Desplazamiento ($d$) = $\text{Dirección Virtual} - \text{Base Virtual del Segmento} = 4200 - 4096 = 104\text{ bytes}$.
> - Dirección física resultante = $\text{Base Física del Heap} + 104$.
> - La referencia cae de manera segura dentro de la región asignada al proceso.

> [!tip] Complemento: Ventajas y limitaciones de la segmentación pura
> La segmentación refleja la estructura lógica del programa (un módulo de código, una pila, una tabla de símbolos) y permite aplicar permisos de protección independientes por segmento (e.g. Código = Read/Execute, Heap/Stack = Read/Write). No obstante, como los segmentos tienen tamaños variables, la segmentación pura sigue sufriendo de fragmentación externa, lo que derivó en la creación de esquemas combinados como la segmentación paginada.

## Preguntas de repaso

> [!question]- ¿Qué información almacena cada entrada de la tabla de segmentos administrada por la MMU?
> Cada entrada contiene la dirección física de inicio del segmento en la RAM (**Base**) y la longitud máxima permitida de dicho segmento (**Límite** o tamaño), junto con los bits de permisos de acceso (lectura, escritura, ejecución).

> [!question]- ¿Por qué no se puede sumar directamente la dirección virtual completa a la base física de un segmento en memoria?
> Porque la dirección virtual incluye la base virtual del segmento en el espacio lógico. Si se sumara directamente sin extraer el desplazamiento relativo (*offset*), el resultado apuntaría a una dirección física inflada mucho más allá del final del segmento, violando el límite y generando un *Segmentation Fault*.

> [!question]- ¿Qué ventaja ofrece la segmentación frente a la asignación contigua monolítica para mitigar la fragmentación?
> Al dividir el proceso en múltiples bloques autónomos y más pequeños (código, heap, stack), el sistema operativo ya no necesita encontrar un único hueco gigantesco contiguo en la RAM; puede aprovechar huecos medianos y dispersos para cada segmento individual.

