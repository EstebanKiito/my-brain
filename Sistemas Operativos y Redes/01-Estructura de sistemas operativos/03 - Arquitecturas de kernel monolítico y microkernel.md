---
ramo: Sistemas Operativos y Redes
tema: Estructura de sistemas operativos
tags: [so/estructura-so, origen/complemento]
prerrequisitos: ["[[02 - Modos de operación y anillos de protección|Modos de operación y anillos de protección]]"]
---
# Arquitecturas de kernel monolítico y microkernel

Al diseñar un kernel hay que decidir **qué servicios corren en modo kernel** y cuáles como procesos normales en modo usuario. La decisión es un compromiso: todo lo que está en el kernel es rápido pero peligroso, porque una falla ahí lo bota todo; lo que está afuera es seguro pero paga *overhead* cada vez que debe pedirle algo al kernel.

## Kernel monolítico: todo adentro

Un **kernel monolítico** junta todo dentro de un solo programa grande: administración de procesos, memoria, sistemas de archivos, drivers e IPC corren en *kernel space*.

- **Más rápido:** los servicios se llaman entre sí como funciones dentro del mismo espacio, sin pedir permisos ni cambiar de modo.
- **Más peligroso:** poca tolerancia a fallos. Si falla un servicio, por ejemplo un driver, se cae todo el kernel.
- **Difícil de extender**, aunque puede usar **módulos**. Linux, por ejemplo, carga y descarga drivers en tiempo de ejecución como *loadable kernel modules* (LKM), sin recompilar el kernel.

Ejemplos: Linux, BSD (OpenBSD, NetBSD, FreeBSD), Solaris, DOS, OpenVMS.

## Microkernel: lo mínimo adentro

Un **microkernel** mantiene en el kernel solo los servicios básicos. Las demás funcionalidades corren como procesos servidores (*servers*) en *user space* y se comunican mediante **paso de mensajes** (IPC).

- **Más seguro:** un error en un servicio queda aislado. El servidor que falla se reinicia o se reemplaza sin botar el sistema.
- **Más modular:** el kernel y los servidores se desarrollan por separado, y el kernel queda sencillo, pequeño (poco *footprint*) y fácil de portar.
- **Más lento:** cualquier programa que no se considere mínimo vive afuera y paga *overhead*. Por ejemplo, para escribir en disco una aplicación manda un mensaje al servidor del sistema de archivos, este le manda otro al driver, y cada mensaje implica cambios de modo y de contexto.

Ejemplos: Mach (UNIX con microkernel, de CMU), GNU/Hurd (inspirado en Mach), L4, seL4 y MINIX 3 (de Andrew S. Tanenbaum).

## Comparación

| | Monolítico | Microkernel |
|---|---|---|
| Tamaño del kernel | Grande y complejo | Pequeño y simple |
| Servicios en *kernel space* | Todos | Solo los mínimos |
| Falla de un servicio | Afecta a todo el kernel | Queda aislada |
| Velocidad | Más rápida | *Overhead* por comunicación |
| Extensión | Difícil (salvo módulos) | Fácil |

![Comparación de kernel monolítico y microkernel](adjuntos/Comparación%20de%20kernel%20monolítico%20y%20microkernel.png)

> [!example]- Transcripción de la imagen
> - **Monolítico:** *kernel* de mayor tamaño y complejo; todos los servicios en *kernel space*; una falla en un servicio afecta a todo el *kernel*; ejecución más rápida; difícil de extender, pero puede usar módulos.
> - **Microkernel:** *kernel* pequeño y simple; servicios mínimos en *kernel space* y la mayoría en *user space*; una falla en un servicio queda aislada; ejecución con *overhead* por comunicación; fácil de extender.
>
> Abajo hay tres diagramas con las mismas aplicaciones arriba (navegador, editor, reproductor, compilador, mensajería) y el hardware abajo. Una línea separa *user space* de *kernel space*. En el monolítico, todos los subsistemas (interfaz, syscalls, IPC, scheduling, memoria, archivos ntfs/ext4, drivers de printer, mouse y usb) quedan bajo la línea. En los otros dos, la línea baja y deja en *user space* parte de los servicios, como los sistemas de archivos ntfs/ext4/fat, la tarjeta de red, el mouse y la impresora. Los componentes se conectan por IPC.

## Conclusión: híbridos

Hoy en día **casi todos los sistemas son híbridos**: mantienen la organización modular de un microkernel, pero dejan dentro del kernel los componentes críticos para el rendimiento. Windows NT y macOS (XNU) se citan como ejemplos típicos.

> [!tip] Para recordar
> Más cosas en el kernel significa más poder y más velocidad, pero también más peligro. Menos cosas en el kernel significa más seguridad, a cambio de más *overhead*.

## Preguntas de repaso

> [!question]- ¿Por qué un kernel monolítico es más rápido que un microkernel?
> Porque todos sus servicios comparten el espacio de kernel y se invocan como funciones, sin paso de mensajes ni cambios de modo entre servidores.

> [!question]- ¿Cómo logra un microkernel tolerar fallas de un driver?
> El driver corre como proceso en *user space*. Si falla, solo cae ese proceso, y el kernel puede reiniciarlo o reemplazarlo sin afectar al resto del sistema.

> [!question]- ¿Qué problema de los monolíticos resuelven los módulos cargables y cuál no resuelven?
> Resuelven la dificultad de extender el kernel, porque se agregan drivers sin recompilar. No resuelven la tolerancia a fallos: el módulo corre en modo kernel y un error suyo puede botar todo.

> [!question]- ¿Por qué la mayoría de los SO actuales son híbridos?
> Porque buscan lo mejor de ambos enfoques: la modularidad y el aislamiento del microkernel, sin pagar su *overhead* en los componentes críticos, que se dejan dentro del kernel.
