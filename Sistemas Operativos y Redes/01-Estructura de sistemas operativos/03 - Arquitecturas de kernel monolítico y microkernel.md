---
ramo: Sistemas Operativos y Redes
tema: Estructura de sistemas operativos
tags: [so/estructura-so, origen/apuntes]
prerrequisitos: ["[[02 - Modos de operación y anillos de protección|Modos de operación y anillos de protección]]"]
---
# Arquitecturas de kernel monolítico y microkernel

El diseño interno del núcleo define qué servicios residen dentro del espacio privilegiado de memoria y cuáles se ejecutan como procesos independientes de usuario, determinando el balance entre rendimiento y tolerancia a fallos.

## Tipos de arquitecturas (mis apuntes)
TIPOS DE ARQUITECTURAS
- Kernell Gigante → Mas espacio para mas poder (La mayoria de programas en el Kernell)
- Si falla una cosa, se cae todo el programa → Mas peligroso
- MONOLITICO: Falta todo → Linux (Mas rápido)
- Menos funcionalidades, menos privilegios → Mas Lento
- Programas no considerados minimos tienen OVERHEAD → Son mas Lentos
- Pero son mas SEGUROS, no se va a caer por un error
- MICROKERNELL: (Liviano, Overhead

RESUMEN

ARQUITECTURAS
- Todo dentro de un programa
- Todos los programas adentro se ejecutan en MODO KERNELL (+Rapido)
- Poca tolerancia a fallos (un programa se cae → se bloquea todo)
→ Monoliticos:
- Solo servicios basicos en el kernell
- Mejor tolerancia a fallos (No bloqueante)
- Desventaja: (+LENTO)
→ Microkernelll:
Conclusion: Hoy en día CASI TODOS los sistemas son HIBRIDOS

> [!warning] Posible error (registrado en `_meta/Sistemas Operativos y Redes/DUDAS.md`)
> En la frase "MONOLITICO: Falta todo → Linux (Mas rápido)", la expresión "Falta todo" corresponde a una errata evidente por "junta todo" o "tiene todo adentro". En un kernel monolítico todos los subsistemas (sistema de archivos, drivers de red, memoria, IPC) corren juntos dentro del espacio de kernel, lo cual maximiza la velocidad pero reduce el aislamiento de fallas.

![Comparación de kernel monolítico y microkernel](adjuntos/Comparación%20de%20kernel%20monolítico%20y%20microkernel.png)

> [!example]- Transcripción de la imagen
> Comparación arquitectural de kernels:
> - **Monolítico:** Kernel de mayor tamaño y complejidad. Todos los servicios (IPC, memoria, sistema de archivos, drivers, scheduling) residen en *kernel space*. Ejecución directa y rápida; si un driver o servicio falla, puede corromper todo el sistema. Difícil de extender, aunque se apoya en módulos dinámicos cargables (*LKM*).
> - **Microkernel:** Kernel pequeño y minimalista. Solo mantiene en *kernel space* lo indispensable (mecanismos de IPC básicos, memoria elemental y scheduling básico). La mayoría de los servicios (sistema de archivos, drivers, red) corren como procesos de servidor en *user space*. Una falla en un servicio queda contenida; la desventaja es el *overhead* de mensajes IPC y cambios de contexto constantes.
> - **Híbrido:** Estructura intermedia que combina la modularidad del microkernel con componentes críticos en espacio de kernel por rendimiento (modelo usado por Windows NT y macOS XNU).

> [!tip] Complemento (slides "Contenido 1: Arquitecturas de Kernel")
> - **Monolítico modular (Linux moderno):** Utiliza *Loadable Kernel Modules* (LKM). Permite cargar y descargar código de controladores en tiempo de ejecución sin recompilar el núcleo, manteniendo la ejecución en espacio de kernel sin penalización de IPC.
> - **Microkernel (MINIX, Mach, seL4):** Diseñado con el principio de mínimo privilegio. Para escribir un bloque en disco, una aplicación envía un mensaje IPC al servidor de sistema de archivos, el cual envía otro IPC al driver de disco. Esto incrementa la seguridad formal pero multiplica los cambios de contexto.
> - **Híbrido:** La mayoría de sistemas operativos comerciales modernos (Windows NT / 11, macOS Darwin/XNU) implementan arquitecturas híbridas.

## Preguntas de repaso

1. ¿Cuál es la principal ventaja y la principal desventaja de un kernel monolítico?
> [!question]- Respuesta
> Ventaja: alto rendimiento, ya que los subsistemas se comunican mediante llamadas directas a funciones en memoria sin sobrecarga de IPC. Desventaja: escasa tolerancia a fallos, pues un error crítico en cualquier componente (como un driver de terceros) puede congelar todo el sistema.

2. ¿Cómo logra un microkernel mayor estabilidad y tolerancia a fallos?
> [!question]- Respuesta
> Ejecutando los controladores y el sistema de archivos como procesos independientes en espacio de usuario (Ring 3). Si un driver falla, el proceso simplemente se reinicia sin provocar una caída del núcleo.

3. ¿Por qué los microkernels suelen presentar menor rendimiento que los kernels monolíticos?
> [!question]- Respuesta
> Debido al continuo intercambio de mensajes IPC y a los múltiples cambios de contexto y de modo entre espacio de usuario y kernel requeridos para completar operaciones cotidianas de entrada/salida.

4. ¿Qué es un kernel híbrido y qué sistemas operativos representativos lo utilizan?
> [!question]- Respuesta
> Es una arquitectura que adopta la organización modular de los microkernels pero ejecuta componentes críticos de alto rendimiento (como el subsistema gráfico o el gestor de red) dentro del espacio de kernel. Ejemplos clásicos son Windows NT y macOS (XNU).

