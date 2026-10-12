# Estructura de sistemas operativos — índice

Fundamentos de sistemas operativos, abstracción del hardware, gestión de recursos, modos de operación privilegiados, llamadas al sistema, flujo de interrupciones, arquitecturas de kernel y secuencia de arranque.

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de las Clases 1 y 2 de los apuntes de Sistemas Operativos, complementadas con las diapositivas oficiales de `Contenido_1.pdf` y referencias clásicas de Tanenbaum (*Modern Operating Systems*) y Silberschatz (*Operating System Concepts*).

## Orden de estudio

1. [[01 - Qué es un sistema operativo|Qué es un sistema operativo]]: rol de gestor de recursos y máquina extendida, abstracción del hardware y daemons del sistema.
2. [[02 - Modos de operación y anillos de protección|Modos de operación y anillos de protección]]: soporte de hardware para dual-mode, modo usuario vs modo kernel, y anillos x86 (Ring 0 a Ring 3).
3. [[03 - Arquitecturas de kernel monolítico y microkernel|Arquitecturas de kernel monolítico y microkernel]]: comparación estructural, ventajas de velocidad vs modularidad y tolerancia a fallos.
4. [[04 - Interrupciones y excepciones|Interrupciones y excepciones]]: naturaleza conducida por eventos del SO, interrupciones de hardware, trampas de software y tabla de vectores (IDT).
5. [[05 - Llamadas al sistema|Llamadas al sistema]]: interfaz de programación con el kernel, wrappers de `libc`, comparación UNIX vs Win32 y traza de ejecución de `cp`.
6. [[06 - Arranque del sistema computacional|Arranque del sistema computacional]]: secuencia de bootstrapping desde firmware (BIOS vs UEFI), verificación POST, bootloaders (GRUB) e inicialización del kernel.
7. [[07 - Multitasking y fundamentos de multiprocesamiento|Multitasking y fundamentos de multiprocesamiento]]: tiempo compartido (*time-sharing*), concurrencia en 1 CPU vs paralelismo en múltiples núcleos.

