---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Multiplexores y demultiplexores"
tags:
  - algoritmos/alu
  - algoritmos/circuitos-logicos
  - origen/complemento
prerrequisitos:
  - "[[02 - Demultiplexor (DEMUX)|Demultiplexor (DEMUX)]]"
---

# Unidad de selección y ALU

Con multiplexores se puede elegir no solo un dato, sino también una **operación**. Esa idea es la base de la **ALU** (*Arithmetic Logic Unit*), el circuito que ejecuta las operaciones aritméticas y lógicas de un procesador.

## Seleccionar una operación

Un sumador-restador de 4 bits puede sumar o restar según una señal de control $S$:

- $S = 0$: suma ($A + B$).
- $S = 1$: resta ($A - B$).

El circuito calcula ambas operaciones y un multiplexor elige el resultado según $S$. Así, una sola señal decide qué hace el bloque.

## La ALU

La **ALU** recibe dos datos, $A$ y $B$, y un conjunto de bits de selección $S_2S_1S_0$. Según esa combinación, ejecuta una operación distinta:

| $S_2$ | $S_1$ | $S_0$ | Operación |
|---:|---:|---:|---|
| 0 | 0 | 0 | $A + B$ |
| 0 | 0 | 1 | $A - B$ |
| 0 | 1 | 0 | $A \land B$ |
| 0 | 1 | 1 | $A \lor B$ |
| 1 | 0 | 0 | $\neg A$ |
| 1 | 0 | 1 | $A \oplus B$ |
| 1 | 1 | 0 | Shift left de $A$ |
| 1 | 1 | 1 | Shift right de $A$ |

Las tres líneas de selección permiten $2^3 = 8$ operaciones. La ALU calcula el resultado y lo entrega a la salida $R$; luego una señal de carga decide si ese resultado se guarda en un registro.

> [!tip] La idea central
> Un multiplexor elige un dato; una ALU elige una operación. En ambos casos, unos pocos bits de control deciden qué camino toma la información.

## Del cálculo al programa

Con una ALU, registros y multiplexores ya se puede construir una calculadora que acumula resultados. El siguiente paso es agregar una **memoria de instrucciones**: una lista de operaciones que se ejecutan una tras otra sin que una persona las escriba cada vez. Eso es lo que convierte la calculadora en un computador programable, y es el tema siguiente.

> [!warning] La ALU no recuerda nada
> La ALU solo calcula: recibe datos, aplica la operación y entrega el resultado. Para que el resultado se conserve hace falta un **registro** con una señal de carga que lo almacene.

## Preguntas de repaso

> [!question]- ¿Cómo se elige la operación en una ALU?
> Con los bits de selección ($S_2S_1S_0$ en este ejemplo). Cada combinación activa una operación distinta.

> [!question]- ¿Cuántas operaciones puede seleccionar una ALU con 3 bits de control?
> $2^3 = 8$ operaciones.

> [!question]- ¿Qué diferencia hay entre un MUX que elige datos y una ALU que elige operaciones?
> El MUX selecciona cuál dato pasa; la ALU selecciona qué operación se aplica a los datos. La idea de selección es la misma.

> [!question]- ¿Por qué la ALU necesita registros para ser útil?
> Porque la ALU no almacena resultados. Los registros guardan los datos de entrada y el resultado para el siguiente ciclo.
