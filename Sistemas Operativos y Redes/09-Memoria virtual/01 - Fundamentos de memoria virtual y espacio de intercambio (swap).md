---
ramo: "Sistemas Operativos y Redes"
tema: "Memoria virtual"
tags:
  - so/memoria
  - so/memoria-virtual
  - origen/apuntes
prerrequisitos:
  - "[[07 - Introducción al intercambio por demanda y ciclo de fallos de página]]"
  - "[[04 - Swapping, fragmentación externa y algoritmos de asignación libre]]"
---

# Fundamentos de memoria virtual y espacio de intercambio (swap)

La memoria virtual es una técnica fundamental que desacopla la memoria lógica vista por las aplicaciones de la memoria física instalada en el computador. Mediante el uso estratégico del espacio de intercambio (*swap space*) en almacenamiento secundario, el sistema operativo provee la ilusión de disponer de un espacio de memoria mucho mayor que la RAM real.

## Espacio de intercambio y sobrecarga de acceso (mis apuntes)

> [!note] Apuntes de clase
> **Clase 9**
> 11/09/24
>
> Dentro de un espacio del Disco Duro (Swap Space) se van a guardar paginas, para simular que tenemos mas espacio del que realmente tenemos en la memoria principal.
> Esto es lento, y queremos que la mayoria de pag se encuentren en la mem principal.
> Y aquellos que no son tan utilizados (o estan en espera), se ecnuentren dentro del espacio swap.
> Para ello necesitamos ciertos algoritmos que reemplazen aquellas paginas al momento de necesitar espacio libre en la memoria principal, saquen aquellas que no vayamos a utilizar!!
>
> En esta clase se verán los algoritmos que permiten hacer REEMPLAZO DE PAGINA.

> [!warning] Posible error
> En los apuntes aparecen las erratas tipográficas "ecnuentren" por encuentren, y "reemplazen" por reemplacen.

> [!tip] Complemento: Disparidad de rendimiento entre RAM y Swap
> La memoria física principal (RAM) responde con latencias en el orden de los nanosegundos ($10 - 100\text{ ns}$), mientras que acceder a almacenamiento secundario (discos duros magnéticos o incluso unidades SSD NVMe) involucra latencias de microsegundos a milisegundos ($0.1 - 10\text{ ms}$). Esta diferencia de hasta $100\,000\times$ implica que cada acceso que deba resolverse desde el espacio swap penaliza drásticamente el rendimiento del sistema, haciendo que la precisión de las políticas de reemplazo de páginas sea decisiva.

## Estructura del espacio swap en sistemas operativos modernos

En sistemas UNIX y GNU/Linux, el espacio swap puede implementarse como una partición de disco dedicada (*swap partition*) o como un archivo dentro del sistema de archivos ordinario (*swapfile*). El kernel traslada a esta área únicamente las páginas anónimas inactivas (heap, stack y datos dinámicos), mientras que las páginas de código ejecutable no requieren copiarse al swap porque pueden descartarse y recargarse directamente desde sus archivos binarios de origen en disco.

## Preguntas de repaso

> [!question]- ¿Qué objetivo persigue el sistema operativo al implementar memoria virtual con espacio swap?
> Permitir la ejecución de programas cuyo espacio de direcciones excede la capacidad de la memoria RAM física disponible, incrementando el grado de multiprogramación y abstrayendo a los procesos de las restricciones del hardware.

> [!question]- ¿Por qué es prioritario que la gran mayoría de las páginas activas residan en la memoria RAM principal?
> Debido a la inmensa brecha de velocidad entre la RAM ($\sim 100\text{ ns}$) y el almacenamiento secundario ($\sim 1\text{ ms}$). Si un proceso sufre fallos de página frecuentes, su tiempo de ejecución se degrada exponencialmente al pasar la mayor parte de su ciclo bloqueado en operaciones de I/O de disco.

> [!question]- ¿Qué diferencia existe entre respaldar páginas anónimas y páginas de código en el espacio swap?
> Las páginas de código son de solo lectura y ya existen en el archivo binario del programa en disco, por lo que el kernel puede descartarlas de la RAM sin escribirlas a swap. Las páginas anónimas (heap y stack) contienen datos dinámicos generados en ejecución que no existen en ningún archivo, por lo que obligatoriamente deben escribirse al espacio swap para no perderse.

