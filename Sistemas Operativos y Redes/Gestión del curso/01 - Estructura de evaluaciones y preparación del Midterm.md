---
ramo: "Sistemas Operativos y Redes"
tema: "Gestión del curso"
tags:
  - sistemas-operativos
  - gestion-curso
  - midterm
  - evaluaciones
  - repaso
prerrequisitos:
  - "[[Capa de enlace y seguridad/_Índice|Capa de enlace y seguridad]]"
---

# Estructura de evaluaciones y preparación del Midterm

Esta nota consolida las pautas de evaluación, formato del examen parcial (**Midterm**) y recomendaciones estratégicas transmitidas en la sesión de repaso oficial del curso de Sistemas Operativos y Redes. El examen aborda los contenidos del curso de manera estructurada y cronológica, evaluando desde los fundamentos del núcleo hasta los subsistemas de concurrencia, memoria y almacenamiento secundario.

---

## Pautas y comentarios del examen (mis apuntes)

Comentarios de la profe
El midterm va a estar ordenado (del inicio de la materia hasta el fin)
S.O → Forma de administrar los recursos del computador / Nos brinda servicios para realizar nuestras tareas
Minimo: Cosas para administrar Hardware, Guardar archivos en memoria (sin un programa seria super dificil)
Controlador para detectar teclado, parlantes
Que el computador reconozca un puerto
Kernell: Provee de los servicios minimos:
Permite compartir recursos → ENTRE LOS PROCESOS
Tenemos Un disco duro, y tenemos varios procesos corriendo, por tanto tenemos que distribuir entre todos los recursos
Sistemas de archivos → El S.O permote Compartir la memoria (Generalmente esta en el KERNELL)
Proteccion Seguridad → En el KERNELL
Control I/O → Depende de la arquitectura
- New → ready → Corriendo → Ready → …. →
Procesos Intensivo de Input Output : Constantemente hace un accion y requiere de un input (esperan todo el rato que venga algo) → No usan tanta CPU, ejecuto algo que el usuario pidio , luego me salgo de la cpu, y espero a que el usuario haga algo para volver a entrar
Procesos de Computo: CPU Burst: No requieren de Input Output, por ejemplo programas de alto computo, correr una base de datos, es intensivo de computo, corre todo el rato en la CPU y cuando termine sale (no espera que el usuario haga algo)
Pregunta de prueba: Definir ventajas y desventajas de los Microkernell y monoliticos → Aprenderselas
Problema de monolitico: PIEDRA Como esta diseñado para trabajar todo junto, es bloqueante (-) (si falla algo), pero las llamadas son mas rapidas (+)
Microkernell: LEGO : Es modificable, mas tolerancia a fallas, es mas pequeño y modularizado, pero es mas lento, no esta diseñado para que funcione todo junto
Pregunta de prueba: Multitasking y multiprogramacion: (V o F)
simultaneamente entre comillas
Un core puede al mismo instante de tiempo puede correr mas de un proceso a la vez → NO
Lo que hacemos es mentir, y que va muy rapido
Este proceso se llama Multitasking
Kernell en 2 modos:
Modo kernell → Tiene toda las facultad de hacer todas las cosas
Modo usuario → El sistema op me provee de proteccion → No puedo borrar lo que yo quiera, no tengo todos los permisos
El usuario puede ser un super user (sudo), pero aun asi no tiene tantas facultades
Solo tiene las minimas para que el sistema funcione, y no interfiera
EJ: Suponga que tenemos que instalar denuevo un controlador, suponga que su mac esta instalando una nueva actualizacion, a pesar de que el usuario pida actualizar, el que tiene la facultad de hacerlo es el kernell
El sudo de linux, no te da acceso al anillo mas de adentro, sigue siendo un usuario
Solo el S.O puede meterse a hacer paginacion por ejemplo, moririamos si tuvieramos que hacer cosas asi
PREGUNTA SI O SI: V o F

> [!tip] Complemento de clase: Arquitectura de evaluación y tipos de preguntas del Midterm
> 1. **Estructura cronológica**: La prueba sigue fielmente el orden del curso:
>    - Módulo 1: Fundamentos de SO, Kernel, dual-mode y llamadas al sistema.
>    - Módulo 2: Procesos, ciclo de vida, PCBs, señales y planificación (schedulers).
>    - Módulo 3: Hilos y concurrencia (recursos compartidos vs privados).
>    - Módulo 4: Sincronización clásica (sección crítica, mutex, semáforos y monitores).
>    - Módulo 5: Gestión de memoria (relocalización, segmentación, paginación y TLB).
>    - Módulo 6: Sistemas de archivos (estructuras en disco, inodos y bloques).
> 2. **Preguntas Verdadero o Falso con justificación**: Se enfocan en mitos comunes, tales como:
>    - "¿Un core de CPU ejecuta físicamente más de un hilo/proceso a la vez?": Falso, se alternan rápidamente mediante time-slicing (multitasking).
>    - "¿El comando `sudo` ejecuta código en modo Kernel?": Falso, `sudo` otorga privilegios de superusuario (root) pero continúa ejecutándose estrictamente en espacio de usuario (Ring 3). Solo las llamadas al sistema cruzan al Ring 0.
>    - "¿El PCB almacena el estado de los bloques del disco duro?": Falso, almacena el estado del proceso y sus descriptores de archivos abiertos, pero la estructura del disco es global del SO.

---

## Preguntas de repaso

> [!question]- ¿Por qué la metáfora "Piedra vs Lego" describe adecuadamente los núcleos Monolíticos y Microkernels?
> Porque el núcleo monolítico es una sola pieza sólida ("piedra"): todo el código corre en el mismo espacio de direcciones privilegiado, siendo muy rápido pero vulnerable a que un fallo en cualquier driver bloquee todo el sistema. El microkernel está armado por piezas independientes ("lego"): solo las funciones mínimas están en el núcleo y los demás servicios corren en procesos de usuario comunicados por IPC, facilitando la modularidad y el aislamiento de fallos a costa de sobrecarga por cambios de contexto.

> [!question]- ¿En qué se diferencia un proceso intensivo en CPU (CPU-bound) de uno intensivo en I/O (I/O-bound)?
> Un proceso CPU-bound ejecuta ráfagas de cálculo largas y continuas sin ceder la CPU voluntariamente (ej. cómputo matricial o base de datos analítica). Un proceso I/O-bound pasa la mayor parte del tiempo bloqueado esperando entradas del usuario o del disco, ejecutando ráfagas cortas de CPU y cediendo el procesador de inmediato.

> [!question]- ¿Por qué un usuario con privilegios de root (`sudo`) no puede manipular directamente las tablas de páginas de la MMU?
> Porque la separación entre modo kernel y modo usuario es forzada por el hardware del procesador (anillos de protección). El proceso `sudo` opera en espacio de usuario; únicamente el código del kernel ejecutándose en modo privilegiado puede acceder a las instrucciones y registros del sistema (como `CR3` en x86) que configuran la MMU.
