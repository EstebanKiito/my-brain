---
ramo: "Sistemas Operativos y Redes"
tema: "Gestión del curso"
tags:
  - sistemas-operativos
  - gestion-curso
  - sincronizacion
  - memoria-virtual
  - sistemas-archivos
  - inodos
prerrequisitos:
  - "[[Gestión del curso/02 - Síntesis de procesos, hilos y planificación para el Midterm|02 - Síntesis de procesos, hilos y planificación para el Midterm]]"
---

# Síntesis de sincronización, memoria y archivos para el Midterm

Esta nota consolida los contenidos de la segunda mitad del temario del Midterm: las garantías de la sección crítica, primitivas de sincronización atómicas (mutex, semáforos, variables de condición), administración de memoria física y virtual (paginación, TLB y algoritmos de reemplazo), y la arquitectura de almacenamiento y sistemas de archivos (HDD vs SSD, capas de bloques, inodos y tipos de enlaces).

---

## Sincronización, memoria y almacenamiento en pizarra (mis apuntes)

Sincronizacion
→ Solucion al problema de la sección critica
→ Exclusion Mutua
→ Tiempo Acotado (espera)
→ Progreso
¿Que es una instrucción atomica?
→ Solo ejecuta una al mismo tiempo
MutexLock:
- Bloquea seccion critica del codigo con AQUIRE
- Libera seccion critica con REALEASE
- Solo permite un Thread por Seccion Critica
Semaforos:
- Permite N procesos en Seccion Critica
- VL → Aumenta contador
- PL → Disminuye contador. Si el contador esta en 0, se bloquea
Variables de condición:
- Bloquea seccion Critica con Condicion Arbitraria
- wait(): esoera a Thread Libere Ejecución
- Signal(): Intento de Despertar un Thread
MEMORIA
Problemas :
- Relocalización
- Protección
Estrategias :
- Segmentacion
- Paginacion → IMPORTANTE !!! → Pregunta de prueba
- Segmentos Paginados
- Paginacion Multinivel
- Paginacion Invertida
TLB
Es una memoria CACHE que almacena traducciones de Paginas → Frames
TLB HIT: Traduccion encontrada
→ Requiere ir a la memoria a buscar la traduccion (tabla de traducciones)
TLB MISS: Traduccion no encontrada
Algoritmo de Reemplazo de Paginas :
- FIFO
- RANDOM
- LRU → Aproximaciones: CLOCK/ AGING / DIRTY BIT

![Pizarra de repaso 3: Sincronización clásica, memoria virtual y TLB](adjuntos/IMG_1085.heic)

> [!example]- Transcripción de la imagen
> Registro fotográfico del pizarrón de repaso (panel derecho - memoria y sincronización):
> - **Sección Crítica**: Requisitos de exclusión mutua, progreso y espera acotada. Primitivas atómicas por hardware (*Compare-and-Swap*).
> - **Mecanismos de sincronización**: Mutex locks (`acquire` y `release`), semáforos contadores de Dijkstra ($V$ incrementa, $P$ decrementa y bloquea), y variables de condición (`wait` libera la CPU, `signal` despierta).
> - **Gestión de memoria**: Desafíos de relocalización y protección. Estrategias: segmentación pura, paginación, esquemas combinados, tablas multinivel e invertidas.
> - **TLB y reemplazo**: Traducción virtual-física, TLB Hit (inmediato) vs TLB Miss (acceso a memoria principal). Algoritmos de reemplazo FIFO, Random, LRU (aproximaciones Clock, Aging y Dirty Bit).

ARCHIVOS
Disco Duro v/s SSD:
- SSD + Rapida
- SSD No tiene partes moviles
- Etc.
Tipos:
- Bloque de datos
- Bloque indice
- Bloque de indireccion simple/doble…
Capas de Bloques:
Estrategias:
- ASIGNACION CONTIGUA
- ASIGNACION ENLAZADA
- FAT
- Asignacion indexada
- Asignacion indexada multinivel
Estas ultimas 2 son importantes → Entraran si o si en la prueba

![Pizarra de repaso 4: Memoria, HDD vs SSD y asignación de bloques e inodos](adjuntos/IMG_1086.heic)

> [!example]- Transcripción de la imagen
> Registro fotográfico del pizarrón de repaso (panel extremo derecho - sistemas de archivos):
> - **Tecnologías de disco**: Discos mecánicos HDD (platos giratorios, cabezal/aguja física móvil, latencia rotacional y búsqueda) vs discos de estado sólido SSD (chips flash sin partes mecánicas móviles, mayor velocidad y resistencia a impactos).
> - **Organización en bloques**: Bloques de datos, bloques de índices e indirecciones simples/dobles/triples en esquemas tipo inodo UNIX.
> - **Estrategias de asignación de bloques**: Contigua, enlazada, tabla FAT, indexada simple e indexada multinivel (pregunta segura de examen).
> - **Enlaces de archivos**: Soft links (simbólicos, apuntan a una ruta/path) vs Hard links (apuntan directamente al número de inodo en el sistema de archivos).

Si o si pregunta de sincronización
Aprenderse las formas de resolver una sección critica
Siempre pensamos en 3 condiciones para sol
Exclusion mutua: Solo 1 thread y no mas de uno (max uno)
Tiempo acotado: No se queden infinitamente (algunos nunca entraran y mueren de hambre) (tiempo infinito)
Progreso: Asegura que siempre hay uno corriendo (todos) (almenos uno)
Instruccion atomicas → Compare and swap → Sabemos que estas insstruccciones solo se ejecuta esa al mismo tiempo
- Semaforo
- Lock (aquire y realesa) —> Por debajo usa instrucciones atomicas
Una forma de proteger seccion criticas es:
Mutex: Bloquea seccion de codigo
Libera SC con realease
Solo permiten 1 thread
Semaforos_
Paginacion es lo mas importante
→ Frame Fisico
→ Pagina → Virtual
Siempre se pregunta que es un hit y un miss → CACHE
Algoritmos de reemplazo de paginas → No va a ir tan cargado
Puede que vaya mas cargado
Un Disco duro no tiene aguja
Un harddrive si tiene
Las agujas son mas lentas, los ssd son mas rápida
El que se echa a perder es el de aguja si se cae al suelo
Asignaciones aprenderse
Los lonks aprenderse el simbolico y el hard
FOTOS PIZARRA

> [!tip] Complemento de clase: Síntesis de conceptos clave de examen
> 1. **Paginación y TLB**:
>    - Las direcciones virtuales se dividen en páginas lógicas; la memoria física RAM en marcos (*frames*).
>    - El TLB almacena las entradas más recientes de la tabla de páginas. En un **TLB Hit**, la dirección física se obtiene en un ciclo de reloj. En un **TLB Miss**, el procesador o el SO debe recorrer la tabla de páginas en RAM (ocasionando accesos adicionales a memoria).
> 2. **Sistemas de archivos**:
>    - **Hard Link**: Entrada de directorio que apunta al mismo número de inodo. Si se elimina el archivo original, los datos persisten mientras el contador de enlaces (*link count*) sea mayor a cero.
>    - **Soft Link (Simbólico)**: Archivo independiente cuyo contenido es la ruta textual hacia otro archivo. Si el archivo destino se mueve o borra, el enlace queda roto (*dangling link*).

---

## Preguntas de repaso

> [!question]- ¿Cuáles son las tres condiciones obligatorias que debe satisfacer cualquier solución válida al problema de la sección crítica?
> 1. **Exclusión Mutua**: Como máximo un hilo o proceso puede estar ejecutando dentro de la sección crítica al mismo tiempo.
> 2. **Progreso**: Si ningún hilo está en la sección crítica y hay hilos que desean entrar, la selección del siguiente no puede posponerse indefinidamente.
> 3. **Espera Acotada**: Debe existir un límite finito en la cantidad de veces que otros hilos pueden adelantarse a entrar después de que un hilo solicitó acceso, evitando inanición (*starvation*).

> [!question]- ¿Por qué la asignación indexada multinivel (como la de inodos en UNIX) es superior a la asignación contigua y a la asignación enlazada?
> Porque soporta acceso directo rápido a cualquier bloque del archivo (a diferencia de la enlazada que requiere recorrido secuencial), permite crecimiento dinámico sin fragmentación externa (a diferencia de la contigua) y puede direccionar archivos gigantescos mediante punteros indirectos simples, dobles y triples sin desperdiciar espacio en archivos pequeños.

> [!question]- ¿Qué ocurre a nivel físico y de inodos cuando se elimina un archivo que posee un Hard Link adicional?
> La llamada `unlink()` elimina la entrada del directorio y decrementa en uno el campo `i_links_count` del inodo. Dado que el contador sigue siendo mayor a cero ($1$), el inodo y los bloques de datos asociados en el disco no se liberan y el archivo sigue siendo plenamente accesible a través del hard link restante.
