---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/apuntes
prerrequisitos:
  - "[[01 - Qué es un sistema operativo]]"
  - "[[01 - Concepto de proceso y espacio de memoria]]"
---

# Memoria principal y el desafío de la multiprogramación

La memoria principal (RAM) es un recurso físico finito estructurado como un gran arreglo lineal de bytes direccionables. Cuando el sistema operativo soporta múltiples procesos en ejecución simultánea, el modelo simplista de asignación estática con direcciones absolutas resulta insostenible.

## Gestión de memoria y multiprogramación (mis apuntes)

> [!note] Apuntes de clase
> **CONTENIDO 6: MEMORIA**
> Veremos como el sistema operativo es capaz de adminisitrar la memoria principal del proceso que esta ejecución
>
> La memoria es un arreglo de bytes
>
> - 1 KB | 1024 B | 2**10 B
> - 1 MB | 2**20 B
> - 1 GB | 2**30 B
>
> Como guardamos los procesos? → Variables codigos etc:
> - Sin Multiprogramacion → Muy facil: Solo tenemos que cargar el espacio completo.
> - Con Multiprogramacion se complica mas:
>   - Si el SO, no se encarga de avisarme donde esta, voy a entrar a una direccion de memoria que no es propia.
>   - Por lo tanto: DIRECCIONES ABSOLUTAS EN MULTIPGROMACION → NO SIRVE.
>
> Compilador + Sistema Operativo:
> Debe encargarse de utilizar no direccions absolutas, si no relativas dentro de la memoria principal. No buscar la direccion absoluta, si no la actual → (Se va actualiuzando).

> [!warning] Posible error
> En los apuntes figura la errata tipográfica "DIRECCIONES ABSOLUTAS EN MULTIPGROMACION" por multiprogramación.

![Memoria como arreglo lineal de bytes sin multiprogramación](adjuntos/Memoria%20como%20arreglo%20lineal%20de%20bytes%20sin%20multiprogramaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Representación de la memoria sin multiprogramación:
> - Un único proceso de usuario reside en memoria física.
> - El espacio de direcciones del sistema operativo ocupa la parte baja o alta (por ejemplo, direcciones $0$ a $k$), y el resto pertenece enteramente al proceso en ejecución.
> - El compilador puede generar direcciones absolutas fijas porque el programa siempre se ubica en la misma posición base.

![Memoria física compartida con multiprogramación](adjuntos/Memoria%20f%C3%ADsica%20compartida%20con%20multiprogramaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Memoria física compartida en un entorno con multiprogramación:
> - La memoria RAM alberga de forma concurrente el código y datos del Sistema Operativo junto a múltiples procesos independientes (Proceso A, Proceso B, Proceso C).
> - Cada proceso ocupa una porción arbitraria y dinámica de memoria según el orden de llegada y la disponibilidad de espacio libre.

![Problemas de relocalización y protección con multiprogramación](adjuntos/Problemas%20de%20relocalizaci%C3%B3n%20y%20protecci%C3%B3n%20con%20multiprogramaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Esquema de desafíos que surgen al compartir la memoria física:
> - **Incertidumbre de carga:** Un proceso no sabe de antemano en qué rango de direcciones físicas será cargado en cada ejecución.
> - **Riesgo de colisión:** Si los programas usaran direcciones absolutas codificadas por el compilador, dos procesos sobreescribirían las mismas posiciones de memoria.
> - **Necesidad de abstracción:** Se requiere disociar las direcciones lógicas utilizadas por el procesador durante la ejecución de las direcciones físicas reales del hardware.

> [!tip] Complemento: Direcciones absolutas vs. relativas
> En los sistemas primitivos monoprogramados, el compilador generaba código máquina con direcciones absolutas (físicas directas). Con la multiprogramación, un programa puede cargarse en cualquier ubicación física arbitraria. Por esta razón, el compilador y el enlazador (*linker*) generan direcciones relativas (lógicas), y el sistema operativo colabora con el hardware para traducir dinámicamente cada referencia en tiempo de ejecución.

## Preguntas de repaso

> [!question]- ¿Por qué no es viable utilizar direcciones de memoria absolutas en un sistema multiprogramado?
> Porque al compilar un programa no se puede predecir qué posición física de la RAM estará libre al momento de su ejecución. Si dos programas compilaran usando la misma dirección absoluta fija, entrarían en colisión inmediata, sobreescribiéndose mutuamente el código y los datos.

> [!question]- ¿Cuál es la equivalencia exacta en bytes de 1 Kilobyte (KB) y 1 Megabyte (MB) en arquitectura de computadores?
> En el sistema binario estándar de computadores, $1\text{ KB} = 2^{10}\text{ bytes} = 1024\text{ bytes}$, y $1\text{ MB} = 2^{20}\text{ bytes} = 1\,048\,576\text{ bytes}$.

> [!question]- ¿Qué rol cumplen el compilador y el enlazador respecto a las direcciones de memoria de un programa?
> En lugar de emitir direcciones físicas reales de la RAM, el compilador y el enlazador estructuran las referencias del programa de forma relativa a un origen lógico base ($0$), permitiendo que el binario pueda relocalizarse en cualquier zona de la memoria física.
