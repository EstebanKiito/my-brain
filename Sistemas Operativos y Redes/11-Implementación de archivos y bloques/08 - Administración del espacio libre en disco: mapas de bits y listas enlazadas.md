---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/almacenamiento
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/07 - Asignación indexada y arquitectura de inodos multinivel en Unix\|07 - Asignación indexada y arquitectura de inodos multinivel en Unix]]"
---

# Administración del espacio libre en disco: mapas de bits y listas enlazadas

Para asignar nuevos bloques a archivos en crecimiento, el sistema operativo implementa estructuras dedicadas de administración del espacio libre mediante vectores de bits o esquemas de listas enlazadas y conteo.

## Gestión de espacio libre (mis apuntes)

- Memoria libre
- Como encontramos bloque libres → BITMAP de bloques libres
- Sencillo, eficiente, implementable en hardware
- - Problema: No escala tan bien
- Otra Estrategia, es que cada bloque libre, tiene un puntero al siguiente bloque libre
- Poco eficiente
- Mejora: Agrupar espacio contiguos

> [!tip] Complemento: Comparación de técnicas de administración de bloques libres
> 1. **Vector de bits (*Bitmap* o *Bit Vector*):**
>    ![Gestión de espacio libre con mapa de bits o bitmap](adjuntos/Gestión%20de%20espacio%20libre%20con%20mapa%20de%20bits%20o%20bitmap.png)
>    > [!example]- Transcripción de la imagen
>    > **Vector de bits (*Bitmap*):**
>    > - Se asocia exactamente 1 bit por cada bloque físico del disco:
>      $$\text{bit}[i] = \begin{cases} 0 & \text{si el bloque } i \text{ está ocupado} \\ 1 & \text{si el bloque } i \text{ está libre} \end{cases}$$
>    > - **Ventajas:** operaciones muy rápidas en CPU mediante instrucciones de conteo de bits iniciales en cero/uno (instrucciones a nivel de palabra); facilita encontrar secuencias de bloques contiguos.
>    > - **Sobrecarga de memoria:**
>    >   - Disco de $1.3\text{ GB}$ con bloques de $512\text{ B} \implies \frac{1.3 \times 10^9}{512 \times 8} \approx 332\text{ KB}$ de bitmap.
>    >   - Disco de $1\text{ TB}$ con bloques de $4\text{ KB} \implies \frac{10^{12}}{4096 \times 8} \approx 30.5\text{ MB}$ (o hasta $256\text{ MB}$ en sectores menores).
>
> 2. **Lista enlazada de bloques libres (*Free-Space List*):**
>    ![Gestión de espacio libre con lista enlazada de bloques](adjuntos/Gestión%20de%20espacio%20libre%20con%20lista%20enlazada%20de%20bloques.png)
>    > [!example]- Transcripción de la imagen
>    > **Lista enlazada de bloques libres:**
>    > - El superbloque mantiene un puntero a la cabeza de la lista (*free-space list head*).
>    > - Cada bloque libre utiliza su propio espacio interno para guardar el puntero al siguiente bloque libre.
>    > - Cero sobrecarga de espacio de disco o memoria RAM dedicada.
>    > - Desventaja: recorrer la lista requiere lecturas a disco continuas.
>    > - **Optimización por conteo (*Counting*):** en lugar de enlazar cada bloque individual, se almacena la dirección del primer bloque libre junto con un contador de cuántos bloques contiguos libres le siguen.

## Preguntas de repaso

> [!question]- ¿Por qué el mapa de bits (*bitmap*) permite encontrar bloques libres contiguos más rápidamente que una lista enlazada simple?
> Porque los bits están empaquetados en palabras de memoria contiguas en RAM, permitiendo al procesador escanear palabras completas (de 32 o 64 bits) usando operaciones a nivel de bit e instrucciones de hardware especializadas en un solo ciclo de reloj.

> [!question]- ¿Qué ventaja clave tiene la lista enlazada de espacio libre respecto al mapa de bits en términos de consumo de memoria?
> La lista enlazada almacena los punteros dentro de los mismos bloques de disco que están libres, sin requerir reservar memoria RAM fija ni sectores dedicados de disco para alojar un mapa de bits.

> [!question]- ¿En qué consiste la técnica de conteo (*counting*) en la gestión de espacio libre?
> Aprovecha que frecuentemente se liberan grupos de bloques físicamente adyacentes; en vez de registrar cada bloque por separado, guarda pares formados por la dirección del primer bloque libre y la cantidad de bloques contiguos disponibles a partir de él.

