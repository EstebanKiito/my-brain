---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/io
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Estructura de sistemas operativos/05 - Llamadas al sistema\|05 - Llamadas al sistema]]"
---

# Capas de abstracción de entrada-salida y mecanismos de buffering

El sistema operativo proporciona capas de abstracción para independizar a las aplicaciones del hardware subyacente y gestiona la transferencia de datos mediante diferentes esquemas de buffering.

## Capas de abstracción y buffering de E/S (mis apuntes)

- Clase 10
- 30/09/24
- ARCHIVOS
- S.O nos abstrae del hardware
- Implementa capas de abstraccion
- La primera → Device Driver
- La segunda → Generic Block Layer
- La tercera → File System
- la Cuarta → Application
- open
- read
- write
- close, etc
- Este nos permite ejecutar funciones
- El sistema operativo nos brinda un SISTEMA DE ARCHIVOS
- Como nos comunicamos con dispositivos I/O
- 4 Tipos de forma de transferir datos entre dispositivos (I/O)
- Lectura Directa → Comunicacion Unbuffered → Bloquea la cpu hasta que termine de leer (LENTO)
- Buffer en el espacio de USUARIO → Esto permite CEDER en la CPU (pagina puede ser swapped out), ——> Al terminar tendremos en el buffer la memoria
- Buffer en el espacio KERNELL → Las paginas Nunca seran Swapeadas, siempre estaran disponibles para leer
- Double-Buffer → Version para escribir en varios buffers, ej: pantallas → Generan imagenes

> [!warning] Posible error
> En los apuntes dice `KERNELL` con doble 'L'; el término correcto es *kernel* space.

> [!tip] Complemento: Arquitectura de E/S y estrategias de Buffering
> 1. **Objetivo de independencia de dispositivo (*Device Independence*):**
>    - **Device Driver:** código específico para cada controlador de hardware (representa más del 70% del código fuente de Linux).
>    - **Generic Block Layer:** abstracción uniforme para dispositivos orientados a bloques (sectores fijos, colas de peticiones y scheduling de I/O).
>    - **File System:** mapea nombres de archivos y estructuras jerárquicas a bloques lógicos de disco.
>    - **Application:** invoca llamadas al sistema estándar POSIX (`open`, `read`, `write`, `close`).
> 2. **Comparación de esquemas de transferencia:**
>    - **Lectura directa (Unbuffered):** la CPU o el proceso se bloquea activamente durante la transferencia. Cero sobrecarga de copia en memoria, pero nula concurrencia.
>    - **Buffer en espacio de usuario:** el proceso cede la CPU, pero la página que alberga el buffer puede sufrir *page out* hacia el swap mientras el dispositivo opera, complicando el acceso por DMA.
>    - **Buffer en espacio de kernel:** las páginas de kernel están fijadas (*pinned*) en RAM y nunca se swapean. Una vez completada la transferencia por DMA, el kernel copia los datos al buffer del proceso de usuario.
>    - **Double Buffering:** desacopla al productor y al consumidor. El dispositivo llena el búfer $A$ mientras el proceso procesa el búfer $B$; al terminar, los roles se intercambian instantáneamente.

## Preguntas de repaso

> [!question]- ¿Por qué el buffering en espacio de kernel es preferible para transferencias DMA frente al buffering exclusivo en espacio de usuario?
> Porque los buffers del kernel pueden fijarse (*pinned*) en marcos de memoria física contigua sin riesgo de sufrir *swap-out* o reubicación de marcos por el paginador mientras el controlador de hardware DMA transfiere los datos.

> [!question]- ¿Cuál es la función de la capa de bloques genéricos (Generic Block Layer) entre el sistema de archivos y el device driver?
> Proporciona una interfaz y cola de peticiones uniforme para todos los dispositivos de bloques, permitiendo aplicar algoritmos de ordenación y combinación de peticiones (I/O scheduling) independientemente del hardware específico.

> [!question]- ¿Cómo mejora el rendimiento el doble buffering (double buffering) en operaciones de entrada/salida?
> Permite solapar en el tiempo el procesamiento en CPU con la transferencia de hardware: mientras el hardware llena o vacía un búfer, el procesador trabaja simultáneamente sobre el segundo búfer sin esperar inactivo.

